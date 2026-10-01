# 13 — HITL approval queue + resume routes (skeleton)

**Status:** planned · depends on `03-agent-azure-sdk.md`, `04-audit-hash-chained.md`, `06-permissions-declarative.md`

## Why

Pitch §2 Internals Panel A shows the HITL interrupt branching off the tool-call node; §4 Design Decisions "HITL queue + memory" row names Postgres at end state with SQLite today; §5 Solving the Problems — Today maps UMR-021–026 and HITL-001–007 to "LangGraph `interrupt` → Postgres approval queue → Dash reviewer UI". The code today has no HITL at all. This plan builds the SQLite-backed persistence + resume layer behind Microsoft Agent Framework's native function-approval primitive (plan 03):

- Agent Framework pauses the agent run when a tool with `approval_mode="always_require"` is proposed, and returns a `user_input_requests` list on the response instead of invoking the tool.
- We drain `user_input_requests` into an `approvals` SQLite table and raise `AgentPaused` so the chat route returns a "pending review" message to the user.
- Admin-only resume routes read the row, surface the decision, feed approval back to Agent Framework, and re-run the turn.
- An audit emission (`kind="hitl_requested"` / `kind="hitl_decision"`) fires on every pause and every decision.

The reviewer UI (Dash page) is reserved; the routes return JSON for now. Postgres cutover is a one-class swap behind the same `⟨I⟩ ApprovalQueue` protocol.

## Scope

**In**
- `storage/approvals.py` — `ApprovalQueue` protocol + `SqliteApprovalQueue` concrete implementation. Same shape as the first iteration; the **trigger** is now Agent Framework's `user_input_requests`, not a bespoke `risky` check inside a hand-rolled ReAct loop.
- `AgentPaused` exception path from plan 03 wired to the queue (plan 03's `run_agent` already raises it when the framework response carries `user_input_requests`).
- `/admin/approvals` and `/admin/approvals/<trace_id>/<decision>` routes.
- Audit emission (`kind="hitl_decision"`) on every approve / deny.
- `permissions.json` already covers `/admin/*` admin-only (plan 06).
- `settings.ENABLE_HITL` gate — when off, our tool adapter in plan 03 registers risky tools **without** `approval_mode`, so Agent Framework invokes them directly (regression check).

**Out**
- The Dash reviewer UI (reserved).
- Postgres cutover (end-state swap).
- Risk taxonomy (pitch marks it blocked — stub taxonomy drives the reserved `ClassifierTool`).
- Timeouts / escalation (UMR-025) — reserved; the schema has a `created_at` column so a later plan can add TTL logic.

## Protocol

```python
# storage/approvals.py (sketch)
from typing import Protocol
from dataclasses import dataclass

@dataclass
class ApprovalRequest:
    trace_id: str
    step: int
    tool_name: str
    args: dict
    state_json: str          # the serialized `messages` list to resume from
    created_at: str
    created_by: str          # username whose chat triggered the approval

@dataclass
class ApprovalDecision:
    trace_id: str
    decision: str            # "approve" | "deny"
    decided_at: str
    decided_by: str          # admin username

class ApprovalQueue(Protocol):
    def enqueue(self, req: ApprovalRequest) -> None: ...
    def pending(self) -> list[ApprovalRequest]: ...
    def take(self, trace_id: str) -> ApprovalRequest | None: ...
    def record_decision(self, dec: ApprovalDecision) -> None: ...
```

## Schema

New migration under `storage/database/migrations/003_approvals.sql`:
```sql
CREATE TABLE approvals (
    trace_id    TEXT PRIMARY KEY,
    step        INTEGER NOT NULL,
    tool_name   TEXT NOT NULL,
    args        TEXT NOT NULL,          -- JSON
    state_json  TEXT NOT NULL,          -- JSON (serialized messages)
    created_at  TEXT NOT NULL,
    created_by  TEXT NOT NULL,
    status      TEXT NOT NULL DEFAULT 'pending',  -- 'pending' | 'approved' | 'denied'
    decided_at  TEXT,
    decided_by  TEXT
);
CREATE INDEX idx_approvals_status ON approvals(status);
```

## Routes

```
GET  /admin/approvals                                 → list pending (JSON)
POST /admin/approvals/<trace_id>/approve              → approve + resume
POST /admin/approvals/<trace_id>/deny                 → deny + emit audit, no resume
```

All three gated by `permissions.json`'s `/admin/*` admin-only rule from plan 06.

## Agent integration

Plan 03 defines:
```python
class AgentPaused(Exception):
    def __init__(self, trace_id: str, step: int): ...
```

Plan 03's `chat/tool_adapter.py` wraps every risky tool with `approval_mode="always_require"` when `settings.ENABLE_HITL` is on. When the model proposes a risky call, Agent Framework returns a response with `user_input_requests` populated instead of invoking the tool. Plan 03's `run_agent` drains that list:

```python
# chat/agent.py (plan 03), simplified
response = await agent.run(messages=messages)
pending = getattr(response, "user_input_requests", None) or []
if pending:
    enqueue_pending(deps.trace_id, response, pending, messages)
    agent_action_log.emit(AgentAction(kind="hitl_requested", trace_id=deps.trace_id, ...))
    raise AgentPaused(deps.trace_id, step=len(messages))
```

`enqueue_pending(...)` lives in `storage/approvals.py` (this plan). It serialises the framework-side pending state (`response` plus the `messages` list) so the resume route can hand it back to Agent Framework.

The **approve** route reads the row, deserialises the saved state, calls Agent Framework's resume API with the approvals granted (exact call shape — likely `agent.resume(approvals=[…])` or re-running `agent.run(messages=…, approvals=…)` — **TBD, verify against 1.12.x at execution time**), and emits `AgentAction(kind="hitl_decision", decision="approve")`.

The **deny** route marks the row denied, emits `AgentAction(kind="hitl_decision", decision="deny")`, and does **not** feed approval back to Agent Framework. The user sees an assistant message like "This request was denied by review."

### Backup path (if Agent Framework's approval primitive is unusable at adoption)

If the framework's approval API turns out to be unstable or missing a feature we need (e.g. no clean way to carry approvals across process restarts), we fall back to a pre-registration gate: our tool adapter in plan 03 *does not register* risky tools on the first `agent.run(...)` call. Instead, we inspect the model's proposed `tool_calls` on the response and raise `AgentPaused` ourselves if any match a known-risky name. The approve route then re-registers the tool and re-runs the turn. Same `⟨I⟩ ApprovalQueue` protocol, same routes, same audit — only the trigger moves from framework-managed to us-managed. Noted here so the implementer knows the shape of the backup is already baked into plan 03's adapter.

## Files touched

- **New**
  - `storage/approvals.py` — protocol + `SqliteApprovalQueue`.
  - `storage/database/migrations/003_approvals.sql`.
  - `storage/tests/test_approvals.py`.
  - `app/core/routes.py` (edit) — register `/admin/approvals*` routes when the feature is enabled or always (admin-gated regardless).
- **Edit**
  - `chat/agent.py` — `enqueue_pending(...)` import + call wired into the `AgentPaused` branch (plan 03 reserves the import stub).
  - `chat/tool_adapter.py` — `approval_mode="always_require"` branch depends on both `tool.risky` **and** `settings.ENABLE_HITL`; already present in plan 03's sketch.
  - `app/core/services.py` — construct and wire `approval_queue: ApprovalQueue = SqliteApprovalQueue()`.
  - `app/core/permissions.json` — already covers `/admin/*` from plan 06; no change required.

## Workflow

**Pre-check**
- Plans 03, 04, 06 shipped.
- `settings.ENABLE_HITL` present.
- Migration runner picks up the new SQL file.

**Do**
1. Write `storage/database/migrations/003_approvals.sql`.
2. Write `storage/approvals.py` with the protocol and `SqliteApprovalQueue`.
3. Wire the queue into `app/core/services.py` (`approval_queue = SqliteApprovalQueue(settings.DATABASE_URL)`).
4. Add the three routes under `app/core/routes.py` (or a new `storage/approval_routes.py` registered from `app/core/services.py`).
5. Edit `chat/agent.py` to call `approval_queue.enqueue(...)` + raise `AgentPaused` when `ENABLE_HITL` and `tool.risky`.
6. On the approve route: load the row, deserialise `messages`, mark `__approved_trace_ids`, call `run_agent` again, emit `AgentAction(kind="hitl_decision", decision="approve")`.
7. On the deny route: update row to `status=denied`, emit `AgentAction(kind="hitl_decision", decision="deny")`, return a canned "denied" assistant message to the chat view.
8. Write `storage/tests/test_approvals.py`: enqueue, pending, take, record_decision; approve path resumes the loop; deny path does not; non-admin → 403 on both routes.

**Verify**
- `ENABLE_HITL=0`: risky tool runs without interrupt (regression check).
- `ENABLE_HITL=1`: calling `classify_risk` (stub) from the chat UI results in no response for the triggering user; an admin hitting `GET /admin/approvals` sees the row; `POST /admin/approvals/<id>/approve` → the loop resumes, tool raises `NotImplementedError` (because stub), the resulting error message surfaces to the triggering user; audit log contains both `hitl_requested` and `hitl_decision` entries with matching trace id.
- `make audit-verify` chain intact after an HITL cycle.
- Non-admin trying `POST /admin/approvals/.../approve` → 403.

**Commit**
`feat(hitl): SQLite approval queue + resume routes (reviewer UI reserved)`

**Rollback**
`git restore -SW .; git checkout -- storage/database/migrations/003_approvals.sql`

## Verification checklist

- [ ] `storage/approvals.py` exports `ApprovalQueue` protocol + concrete class.
- [ ] Migration `003_approvals.sql` applies cleanly on a fresh DB.
- [ ] Risky-tool call with `ENABLE_HITL=1` writes a row and does not call the tool.
- [ ] Approve route resumes the loop with the saved `messages`.
- [ ] Deny route does not call the tool and emits a decision audit entry.
- [ ] Only admins can hit `/admin/approvals*`.
- [ ] Audit chain contains both request + decision entries, same trace id.

## Out of scope

- Dash reviewer UI (reserved).
- Postgres cutover.
- Escalation / TTL on pending approvals (UMR-025).
- Approval of specific args (not re-prompt the whole tool call).

---

## Reasoning / justification extracts

**Pitch commitments honoured:**
- "HITL (UMR-021–026/HITL-001–007) is a graph interrupt off tool_node, not middleware: the queue, timeout, reviewer UI, and decision log sit inside the same auth and audit perimeter as the agent." (§2 Internals footnote).
- "LangGraph interrupt → Postgres approval queue → Dash reviewer UI, same auth as routes; decisions logged immutably with reasoning chain, confidence, sources." (§5 HITL approvals row).
- "HITL queue + memory — Postgres (approval queue + 3-tier memory) end state; SQLite scratch; approval table staged" (§4 Design Decisions).

**Why use Agent Framework's native approval primitive:**
Microsoft Agent Framework (plan 03) exposes function-tool approval via `approval_mode="always_require"`. When the model proposes to call such a tool, the run returns `user_input_requests` instead of invoking it — exactly the "interrupt → queue → decision" shape the pitch wants. Reusing the framework's primitive keeps the Microsoft-native story end-to-end, and keeps the "if we drop Agent Framework, we fall back to our own gate" backup path in scope (sketched above). Either way the `⟨I⟩ ApprovalQueue` protocol and the `/admin/approvals*` routes stay identical, so the Postgres cutover at end state is still a one-class swap.

**Why mark `ClassifierTool` as risky:**
Pitch UC-E2 explicitly runs the risk classifier through HITL. Marking the reserved stub (plan 08) as `risky=True` lets the HITL loop be exercised end-to-end before the real classifier lands.

**Why the deny route emits a canned message:**
Pitch §5 HITL approvals row: "decisions logged immutably". The user needs to know their request was reviewed. A canned message says that without leaking the admin's reasoning.
