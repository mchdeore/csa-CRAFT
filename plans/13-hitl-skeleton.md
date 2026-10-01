# 13 — HITL approval queue + resume routes (skeleton)

**Status:** planned · depends on `03-agent-azure-sdk.md`, `04-audit-hash-chained.md`, `06-permissions-declarative.md`

## Why

Pitch §2 Internals Panel A shows the HITL interrupt branching off the tool-call node; §4 Design Decisions "HITL queue + memory" row names Postgres at end state with SQLite today; §5 Solving the Problems — Today maps UMR-021–026 and HITL-001–007 to "LangGraph `interrupt` → Postgres approval queue → Dash reviewer UI". The code today has no HITL at all. This plan builds the SQLite-backed skeleton:

- an approval queue the agent writes to when a `risky=True` tool is about to run,
- resume routes (admin-only) that re-enter the loop with the saved state,
- an audit emission for every decision.

The reviewer UI (Dash page) is reserved; the routes return JSON for now. Postgres cutover is a one-class swap behind the same queue protocol.

## Scope

**In**
- `storage/approvals.py` — `ApprovalQueue` protocol + `SqliteApprovalQueue` concrete implementation.
- `AgentPaused` exception path from plan 03 wired to the queue.
- `/admin/approvals` and `/admin/approvals/<trace_id>/<decision>` routes.
- Audit emission (`kind="hitl_decision"`) on every approve / deny.
- `permissions.json` already covers `/admin/*` admin-only (plan 06).
- `settings.ENABLE_HITL` gate.

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

In the ReAct loop (`chat/agent.py`), before calling a tool with `risky=True`:
```python
if settings.ENABLE_HITL and getattr(tool, "risky", False):
    approval_queue.enqueue(ApprovalRequest(
        trace_id=deps.trace_id, step=step, tool_name=call.function.name,
        args=json.loads(call.function.arguments or "{}"),
        state_json=json.dumps(messages),
        created_at=now_iso(), created_by=deps.username,
    ))
    agent_action_log.emit(AgentAction(kind="hitl_requested", ...))
    raise AgentPaused(deps.trace_id, step)
```

The approve route reads the row, deserialises `state_json` back into `messages`, re-enters `run_agent` with the saved step — but this time with the tool invocation marked as approved (we add a transient `__approved_trace_ids: set[str]` on the loop's `deps` so the risky check does not fire again this turn).

The deny route emits `AgentAction(kind="hitl_denied", ...)` and does **not** re-enter the loop; the user sees an assistant message like "This request was denied by review."

## Files touched

- **New**
  - `storage/approvals.py` — protocol + `SqliteApprovalQueue`.
  - `storage/database/migrations/003_approvals.sql`.
  - `storage/tests/test_approvals.py`.
  - `app/core/routes.py` (edit) — register `/admin/approvals*` routes when the feature is enabled or always (admin-gated regardless).
- **Edit**
  - `chat/agent.py` — fill in the `_enqueue_approval` placeholder; raise `AgentPaused`; add the "already-approved" bypass flag on `deps`.
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

**Why implement HITL without LangGraph:**
LangGraph's `interrupt` primitive is useful but is a single construct that we re-create in ~60 lines (enqueue + raise + resume with saved state). The pitch's end-state Postgres cutover is a swap behind the same `ApprovalQueue` protocol, independent of whether the agent runtime is LangGraph or our ReAct loop. We get HITL in-pitch mechanics with zero LangChain dep.

**Why mark `ClassifierTool` as risky:**
Pitch UC-E2 explicitly runs the risk classifier through HITL. Marking the reserved stub (plan 08) as `risky=True` lets the HITL loop be exercised end-to-end before the real classifier lands.

**Why the deny route emits a canned message:**
Pitch §5 HITL approvals row: "decisions logged immutably". The user needs to know their request was reviewed. A canned message says that without leaking the admin's reasoning.
