# 03 — ReAct agent on Azure OpenAI SDK (drop pydantic-ai)

**Status:** planned · depends on `01-config-stdlib-dotenv.md`, `02-app-factory.md`

## Why

The pitch names LangGraph for the agent runtime; current code uses `pydantic-ai`. Neither is what we want to ship for the MVP: LangChain pulls `pydantic` as a hard transitive dep and adds abstractions between us and the LLM transport we don't need at this scope (1 primary agent, ~10 tools). We drop `pydantic-ai` and write a ~250-line ReAct loop directly on `openai.AsyncAzureOpenAI`. The `⟨I⟩ ChatProvider` protocol stays stable — a different runtime (LangGraph or similar) slots in behind it later with no changes to routes / audit / data.

See `docs-depo/exploration/azure-openai-sdk-usage.md` for the full SDK-usage reference and the decision rule for revisiting LangChain adoption.

## Scope

**In**
- Delete `pydantic-ai` + `pydantic-ai[openai]` from deps.
- Rewrite `chat/agent.py` as a ReAct loop on `openai.AsyncAzureOpenAI`.
- Rename `chat/provider.DeepSeekChat` → `AzureChatProvider`; keep the `⟨I⟩ ChatProvider` protocol.
- Delete the silent echo fallback (`[echo — Azure OpenAI not configured]`). Construction raises when creds are missing.
- Reserved hook point in the tool wrapper for `settings.GUARDRAIL_HOOK` (no-op today).
- Reserved `AgentPaused` / HITL hook (full implementation in plan 13).

**Out**
- Content Safety wiring (plan 13 reserves the hook; actual wiring is a later cutover).
- LangGraph / LangChain. If multi-agent orchestration arrives, swap behind `⟨I⟩ ChatProvider`.
- Streaming to the UI (optional; our Dash chat appends whole messages).

## Protocols touched

```python
# app/core/protocols.py (unchanged interfaces, kept stable)
class ChatProvider(Protocol):
    def get_response(self, messages: list[dict]) -> ChatResponse: ...

class Tool(Protocol):
    def definition(self) -> dict[str, Any]: ...                                   # OpenAI tool schema
    def execute(self, args: dict[str, Any]) -> tuple[dict, dict | None]: ...      # (tool_message, rich_content_or_none)
```

Both already exist. No shape change.

## Files touched

- **New**: none at module level; `chat/agent.py` is rewritten in place.
- **Rewrite**
  - `chat/agent.py` — ReAct loop, `AgentPaused`, `AgentRecursionLimit`, `AzureChatProvider` deps container.
  - `chat/provider.py` — `AzureChatProvider` class; strict `_make_provider`; no echo fallback.
- **Edit**
  - `app/core/services.py` — build the provider via `{"azure": AzureChatProvider}` dispatch keyed by `settings.CHAT_PROVIDER`.
  - `chat/__init__.py` — export `AzureChatProvider`.
  - `app/requirements.txt` — remove `pydantic-ai` lines.
  - `pyproject.toml` — same (if present after plan 09).
- **Test rewrites**
  - `chat/tests/*` — replace pydantic-ai dependent tests with ones using a stub `AsyncAzureOpenAI`.

## Implementation sketch

```python
# chat/agent.py
from __future__ import annotations
import json
from dataclasses import dataclass, field
from typing import Any
from openai import AsyncAzureOpenAI
from app.core.config import settings

class AgentPaused(Exception):
    def __init__(self, trace_id: str, step: int): self.trace_id, self.step = trace_id, step

class AgentRecursionLimit(Exception):
    def __init__(self, limit: int): self.limit = limit

@dataclass
class ChatDeps:
    username: str = ""
    workspace_id: str = ""
    user_role: str = "base_user"
    trace_id: str = ""
    rich_contents: list[dict] = field(default_factory=list)

async def run_agent(client: AsyncAzureOpenAI, messages: list[dict], tools: list, deps: ChatDeps):
    for step in range(settings.AGENT_RECURSION_LIMIT):
        r = await client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
            tools=[t.definition() for t in tools],
        )
        msg = r.choices[0].message
        messages.append(_msg_to_dict(msg))
        _emit_llm_turn(deps, step, r)
        if not msg.tool_calls:
            return messages
        for call in msg.tool_calls:
            tool = _lookup(tools, call.function.name)
            if settings.ENABLE_HITL and getattr(tool, "risky", False):
                _enqueue_approval(deps.trace_id, step, messages)
                raise AgentPaused(deps.trace_id, step)
            args = json.loads(call.function.arguments or "{}")
            result, rich = tool.execute(args)
            deps.rich_contents.extend(rich or [])
            messages.append({"role":"tool","tool_call_id":call.id,"content":json.dumps(result)})
            _emit_tool_call(deps, step, call, result)
    raise AgentRecursionLimit(settings.AGENT_RECURSION_LIMIT)
```

```python
# chat/provider.py (sketch)
class AzureChatProvider:
    def __init__(self, tools: list, ...):
        self._tools = tools
        self._client = AsyncAzureOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version=settings.AZURE_OPENAI_API_VERSION,
        )  # settings loader has already enforced the required fields

    def get_response(self, messages: list[dict]) -> ChatResponse:
        deps = ChatDeps(..., trace_id=get_trace_id())
        loop = asyncio.new_event_loop()
        try:
            final = loop.run_until_complete(run_agent(self._client, messages, self._tools, deps))
        finally:
            loop.close()
        text = final[-1].get("content", "") if final else ""
        return ChatResponse(text=text, rich_contents=deps.rich_contents)
```

## Workflow

**Pre-check**
- Plans 01 + 02 shipped.
- `make check` green.
- `pip uninstall pydantic-ai pydantic-ai[openai]` succeeds in a scratch venv.

**Do**
1. Remove `pydantic-ai` + `pydantic-ai[openai]` from `app/requirements.txt` (and `pyproject.toml` once plan 09 lands).
2. Rewrite `chat/agent.py` as above.
3. Rewrite `chat/provider.py`: rename class, strict `_make_provider`, delete the echo fallback.
4. Edit `app/core/services.py`: build via `{"azure": AzureChatProvider}` dispatch keyed by `settings.CHAT_PROVIDER`.
5. Update `chat/__init__.py` export.
6. Rewrite `chat/tests/*` to use a stub `AsyncAzureOpenAI` (define a `FakeAzureClient` fixture that returns scripted `ChatCompletion` objects).

**Verify**
- `grep -rn "pydantic_ai\|pydantic-ai" --include='*.py'` returns zero.
- `grep -rE "^import pydantic\|^from pydantic " --include='*.py'` returns zero in our source.
- `pytest chat/tests -q` passes against the fake client, including a scripted multi-step tool-call sequence.
- Manual round-trip: with real Azure creds in `.env`, `curl -X POST /chat/send` returns an assistant message.
- Without creds and `CHAT_PROVIDER=azure`, startup raises per plan 01 — not a runtime echo.

**Commit**
`refactor(chat): ReAct loop on Azure OpenAI SDK, drop pydantic-ai`

**Rollback**
`git restore -SW chat/ app/core/services.py app/requirements.txt pyproject.toml`

## Verification checklist

- [ ] Zero `pydantic_ai` imports.
- [ ] Zero `import pydantic` in our source.
- [ ] Zero `[echo — Azure OpenAI not configured]` strings anywhere.
- [ ] Stub-client tests cover: final text with no tool calls, single tool call, recursion-limit guard, HITL pause.
- [ ] `AzureChatProvider` constructs cleanly when `settings.CHAT_PROVIDER=azure` and the three required Azure fields are set.
- [ ] `app/core/services.py` dispatches via a dict registry, not an `if/elif` chain.

## Out of scope

- Content Safety wiring on the guardrail hook (reserved).
- Streaming responses to the UI (optional; MVP uses whole-message appends).
- Multi-agent orchestration.
- Replacing `storage.store.save_messages` for state persistence — reuse it.

---

## Reasoning / justification extracts

**User instructions:**
- "if there's an azure solution we should try and use it to reduce dependency surface area and code simplicity".
- "ok why not use azure sdk now, what changes, still lang on top of azure sdk?".
- "ship with Azure SDK" (confirmed verdict).

**Pitch commitments honoured:**
- `⟨I⟩ ChatProvider` protocol stays stable (§4 Design Decisions, Protocol contracts row).
- Bounded recursion with `AGENT_RECURSION_LIMIT=25` (§6 Requirements Traceability, Primary agent).
- Tool calling validated against `⟨I⟩ Tool` (§2 Internals, Panel B).
- `AgentAction` audit emission per LLM turn and per tool call (§2 Internals, Panel A).
- Guardrail hook point in tool wrapper (§5 Guardrails + sandbox row — kept as no-op today, honoured by the `settings.GUARDRAIL_HOOK` check).

**Why not LangGraph at MVP scope:**
LangChain pulls `pydantic` as a hard transitive dep. At one primary agent + ten tools the framework is net overhead — upgrade churn, extra abstractions, no capability gain. See `docs-depo/exploration/azure-openai-sdk-usage.md` for the decision rule and the triggers that would make LangGraph worth adding later (multi-agent orchestration, dynamic tool composition, LangSmith tracing, retrieval-chain self-correction loops).

**Why strict construction instead of silent echo fallback:**
Silent fallback masked a config error during the demo pass. Fail-fast at import matches pitch §8 invariants and the user instruction "no hardcoding anything".
