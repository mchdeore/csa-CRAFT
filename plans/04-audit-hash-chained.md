# 04 — Hash-chained AgentAction audit log

**Status:** planned · depends on `01-config-stdlib-dotenv.md`, `03-agent-azure-sdk.md`

## Why

Pitch promises **hash-chained append-only JSONL** today, forwardable to Azure Log Analytics at end state (pitch §4 Audit sink, §5 Immutable audit, §6 Requirements Traceability Audit + traceability). Current code writes plain structured JSONL — no chain, no tamper detection. Pitch also names `⟨I⟩ AgentActionLog` as one of the five protocols; it is not formalised in `app/core/protocols.py`.

This plan formalises the protocol, writes a hash-chained concrete implementation, and wires emissions from the agent loop and tool wrappers.

## Scope

**In**
- New `AgentAction` dataclass with the fields the pitch names.
- New `⟨I⟩ AgentActionLog` protocol in `app/core/protocols.py`.
- New concrete `HashChainedJsonlLog` in `app/core/audit.py`.
- CLI entry point `python -m app.core.audit verify`.
- `agent_action_log.emit(...)` call sites in `chat/agent.py` (LLM turns + tool calls) and in `/admin/approvals/*` (HITL decisions, plan 13).
- Daily log rotation kept; chain seed from `settings.AUDIT_HASH_SEED`.

**Out**
- Forwarding JSONL → Log Analytics (deploy-time config, pitch end-state).
- GUI for browsing audit log.

## Protocol

```python
# app/core/protocols.py (addition)
class AgentActionLog(Protocol):
    def emit(self, action: AgentAction) -> None: ...
    def verify(self, since: str | None = None) -> tuple[bool, str | None]: ...
    # returns (True, None) if chain intact; (False, first_bad_trace_id) otherwise
```

## Data shape

```python
# app/core/audit.py
from __future__ import annotations
import json, hashlib, threading, fcntl
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from app.core.config import settings

@dataclass
class AgentAction:
    trace_id: str
    agent_id: str
    step: int
    kind: str                        # "llm_turn" | "tool_call" | "hitl_decision"
    role: str                        # user role at the time (base_user / power_user / admin)
    username: str
    tool_name: str | None = None
    args_summary: str | None = None  # truncated / scrubbed
    result_summary: str | None = None
    confidence: float | None = None  # for grounded responses
    citations: list[dict] = field(default_factory=list)
    timestamp: str = ""              # ISO8601 UTC
    previous_hash: str = ""
    hash: str = ""                   # sha256(previous_hash + canonical_json(payload_without_hash))
```

## Hash chain

- `previous_hash = <last hash in file, or settings.AUDIT_HASH_SEED on empty file>`
- payload = `asdict(action)` minus the `hash` field, sorted keys, UTF-8 JSON, no spaces
- `action.hash = sha256((previous_hash + payload_json).encode()).hexdigest()`
- Append `json.dumps(asdict(action), sort_keys=True) + "\n"` under an `fcntl.flock` on the file.

Verification walks the file, recomputes each hash, bails at the first mismatch, returns the offending `trace_id`.

## Files touched

- **New**
  - `app/core/audit.py` — `AgentAction`, `HashChainedJsonlLog`, `verify()` function, CLI entry `python -m app.core.audit verify`.
  - `app/tests/test_audit.py`.
- **Edit**
  - `app/core/protocols.py` — add `AgentActionLog` protocol + import `AgentAction` type.
  - `app/core/services.py` — construct `agent_action_log: AgentActionLog = HashChainedJsonlLog(settings.LOG_DIR, settings.AUDIT_HASH_SEED)`.
  - `chat/agent.py` — call `agent_action_log.emit(...)` at `_emit_llm_turn` and `_emit_tool_call` placeholders from plan 03.
  - `app/core/logging.py` — keep structured request logging; audit is a separate sink.
  - `Makefile` — add `audit-verify: ## verify today's audit log hash chain` target (lands with plan 09).

## Workflow

**Pre-check**
- Plans 01 + 03 shipped.
- `settings.LOG_DIR` resolves to a writable directory on startup.

**Do**
1. Write `app/core/audit.py`.
2. Extend `app/core/protocols.py` with `AgentActionLog`.
3. Construct the sink in `app/core/services.py`.
4. Add emission call sites in `chat/agent.py` (replacing the `_emit_llm_turn` / `_emit_tool_call` stubs from plan 03).
5. Write `app/tests/test_audit.py` with: (a) chain monotonic across many writes, (b) tampering with one line → `verify` returns `(False, trace_id)`, (c) two threads emitting concurrently under file lock → chain still verifies, (d) seed override honoured.
6. Add `audit-verify` entry point in `app/core/audit.py` (`if __name__ == "__main__":` block parsing `verify`).

**Verify**
- `pytest app/tests/test_audit.py -q` passes.
- `make audit-verify` on today's log reports chain intact.
- Manual tamper: `sed -i 's/foo/bar/' <today-jsonl>` then `make audit-verify` → prints the first corrupted trace id and exits non-zero.
- `grep -rn "agent_action_log\.emit" --include='*.py'` shows the two call sites in `chat/agent.py` (and later `storage/approvals.py` in plan 13).

**Commit**
`feat(audit): hash-chained AgentAction log + AgentActionLog protocol`

**Rollback**
`git restore -SW app/core/ chat/agent.py app/tests/test_audit.py`

## Verification checklist

- [ ] `AgentActionLog` protocol exists in `app/core/protocols.py`.
- [ ] `HashChainedJsonlLog.emit` writes under a file lock.
- [ ] Chain seed comes from `settings.AUDIT_HASH_SEED`.
- [ ] `verify()` returns `(False, trace_id)` on tamper.
- [ ] Emissions on both LLM turns and tool calls carry the same `trace_id`.
- [ ] `make audit-verify` entry point works.

## Out of scope

- Forwarding to Azure Log Analytics (end-state; same envelope, deploy-time config).
- Rotating keys for the hash chain seed.
- UI for browsing audit log.

---

## Reasoning / justification extracts

**Pitch commitments honoured:**
- "AgentAction envelope · AgentActionLog · hash-chained JSONL → Log Analytics" (§6 Requirements Traceability).
- "AgentActionLog writes append-only JSONL with hash chain; daily rotation; covers every tool call and LLM turn" (§5 Immutable audit).
- "⟨I⟩ AgentActionLog" is one of the five pitch protocols (§4 Design Decisions, Protocol contracts).
- "Forward the same envelope to Log Analytics (immutability policy); KQL replaces grep" at end state — our JSONL emission is already the right shape; cutover is deploy-time, not code.

**Pitch requirements mapped (§6):**
- UMR-015 (audit of every agent step).
- UMR-027 (immutable audit trail).
- UMR-045 (traceability from user request → tool call → response).
- UMR-061 / 062 (chain of custody).
- UMR-093 (containment via audit).
- AAR-005.
- ASG-003.

**Why hash chain here (not database constraints):**
Append-only JSONL on disk is grep-friendly today and KQL-friendly at end state (pitch §5). Hash chain gives tamper detection without a DB. Log Analytics ingests the same lines; the chain is retained as a verifiable property across the forwarder.
