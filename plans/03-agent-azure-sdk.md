# 03 — Microsoft Agent Framework for the primary agent

**Status:** planned · depends on `01-config-stdlib-dotenv.md`, `02-app-factory.md`

## Why

The pitch promises an *abstracted* agent runtime behind `⟨I⟩ ChatProvider` — the first iteration of this plan was going to hand-roll a ~250-line ReAct loop directly on `openai.AsyncAzureOpenAI`. That path is still viable (see `docs-depo/exploration/azure-openai-sdk-usage.md`, kept as the fallback reference). We are **pivoting to Microsoft Agent Framework** as the Azure-native agent runtime from day one.

Why the pivot:

- **Azure-native, blessed path.** Microsoft Agent Framework (`agent-framework`, GA April 2026, current `1.12.x` July 2026) is Microsoft's enterprise agent SDK and the stated successor to Semantic Kernel. It has first-class integrations for Azure OpenAI (`agent-framework-openai`) and Azure AI Foundry (`agent-framework-foundry`). For a project that lives inside Azure/PBMM, choosing the Microsoft framework over a hand roll aligns with the procurement/support story.
- **Replaces our ~250-line hand roll** with framework primitives (`ChatAgent`, function-tool registration, built-in HITL via function approvals, workflow `RequestPort`, telemetry).
- **Honest cost.** It adds `agent-framework` (plus `agent-framework-openai` and/or `agent-framework-foundry`) as a direct dep, and pulls `pydantic` back in as a transitive dep (the framework's function-tool decorator uses `typing.Annotated[..., pydantic.Field(...)]` for parameter descriptions). The "zero pydantic installed" rule from the first iteration softens to "no direct `import pydantic` in our source" (plan 12 enforces).
- **Protocol seams stay intact.** `⟨I⟩ ChatProvider` is unchanged; `AzureChatProvider` becomes `MsAgentFrameworkChatProvider` behind the same signature. If Microsoft Agent Framework access is ever blocked (preview access, licensing, air-gap), the SDK-direct fallback in `docs-depo/exploration/azure-openai-sdk-usage.md` is the drop-in alternate `⟨I⟩ ChatProvider` implementation.

## Scope

**In**
- Delete `pydantic-ai` + `pydantic-ai[openai]` from deps.
- Add `agent-framework` (umbrella install) **or** `agent-framework-core` + `agent-framework-openai` + `agent-framework-foundry` (narrower install) — TBD, pick at execution time based on footprint; the examples here import from `agent_framework` and `agent_framework.openai` which is covered by either shape.
- Rewrite `chat/agent.py` on top of Agent Framework's `ChatAgent` / `AzureOpenAIChatClient`.
- Rename `chat/provider.DeepSeekChat` → `MsAgentFrameworkChatProvider`; keep the `⟨I⟩ ChatProvider` protocol stable.
- Delete the silent echo fallback (`[echo — Azure OpenAI not configured]`). Construction raises when creds are missing.
- Register our tools (currently `⟨I⟩ Tool.definition()` + `.execute(args)`) through an adapter that exposes them as framework-compatible function tools.
- HITL via the framework's function-approval primitive (`approval_mode="always_require"` on risky tools), persisted through our existing `storage/approvals.py` (plan 13).
- Reserved hook point for `settings.GUARDRAIL_HOOK` (no-op today) — wired as a framework middleware if the API supports it, otherwise around our tool adapter.

**Out**
- Content Safety wiring (plan 13 reserves the hook; actual wiring is a later cutover).
- Streaming to the UI (optional; our Dash chat appends whole messages). Agent Framework exposes streaming; we don't light it up yet.
- Multi-agent orchestration via Agent Framework `Workflow` / planner graphs. The MVP is one `ChatAgent`.

## Protocols touched

```python
# app/core/protocols.py — unchanged interfaces, kept stable
class ChatProvider(Protocol):
    def get_response(self, messages: list[dict]) -> ChatResponse: ...

class Tool(Protocol):
    def definition(self) -> dict[str, Any]: ...                                   # OpenAI tool schema
    def execute(self, args: dict[str, Any]) -> tuple[dict, dict | None]: ...      # (tool_message, rich_content_or_none)
```

Both already exist. No shape change. The *implementation* of `ChatProvider` now wraps a `ChatAgent`; the implementation of `Tool` is adapted to a framework function tool at registration time (see `_as_framework_tool` below).

## Files touched

- **Rewrite**
  - `chat/agent.py` — thin wrapper that constructs the framework `ChatAgent`, runs a turn, and surfaces `AgentPaused` / `AgentRecursionLimit`.
  - `chat/provider.py` — `MsAgentFrameworkChatProvider` class; strict `_make_provider`; no echo fallback.
- **New**
  - `chat/tool_adapter.py` — `as_framework_tool(⟨I⟩ Tool) -> <framework function tool>`; translates our `definition()`/`execute()` into whatever shape Agent Framework consumes (decorator / registration call — TBD, verify at execution time).
- **Edit**
  - `app/core/services.py` — build the provider via `{"azure": MsAgentFrameworkChatProvider}` dispatch keyed by `settings.CHAT_PROVIDER`.
  - `chat/__init__.py` — export `MsAgentFrameworkChatProvider`.
  - `app/requirements.txt` — remove `pydantic-ai` lines; add `agent-framework` (and `agent-framework-foundry` if Foundry is in-scope at that execution step — TBD, keep `agent-framework-openai` at minimum).
  - `pyproject.toml` — same (after plan 09).
- **Test rewrites**
  - `chat/tests/*` — replace pydantic-ai dependent tests with ones using Agent Framework's test helpers if any (`agent_framework.testing` — **TBD, verify at execution time**); otherwise a stub `AzureOpenAIChatClient` that returns scripted responses.

## Implementation sketch

```python
# chat/agent.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
# Imports verified against agent-framework 1.12.x public surface. TBD if the
# exact submodule names shift before adoption; verify at execution time.
from agent_framework import ChatAgent, tool  # noqa: F401  — `tool` decorator used by the adapter
from agent_framework.openai import AzureOpenAIChatClient

from app.core.config import settings
from chat.tool_adapter import as_framework_tool


class AgentPaused(Exception):
    """Raised when a risky tool call needs HITL approval. Carries the trace id
    the approval row is keyed on and the step at which the pause happened."""
    def __init__(self, trace_id: str, step: int):
        self.trace_id, self.step = trace_id, step


class AgentRecursionLimit(Exception):
    def __init__(self, limit: int): self.limit = limit


@dataclass
class ChatDeps:
    username: str = ""
    workspace_id: str = ""
    user_role: str = "base_user"
    trace_id: str = ""
    rich_contents: list[dict] = field(default_factory=list)


def build_agent(tools: list, deps: ChatDeps) -> ChatAgent:
    client = AzureOpenAIChatClient(
        endpoint=settings.AZURE_OPENAI_ENDPOINT,
        api_key=settings.AZURE_OPENAI_API_KEY,
        api_version=settings.AZURE_OPENAI_API_VERSION,
        deployment=settings.AZURE_OPENAI_DEPLOYMENT,
    )  # settings loader has already enforced the required fields
    fw_tools = [as_framework_tool(t, deps=deps) for t in tools]
    return ChatAgent(
        chat_client=client,
        instructions=settings.SYSTEM_PROMPT,
        tools=fw_tools,
        # recursion / max-iteration limit — TBD, exact kwarg name on ChatAgent
        # may be `max_iterations` or `max_turns`; verify at execution time.
        max_iterations=settings.AGENT_RECURSION_LIMIT,
    )


async def run_agent(agent: ChatAgent, messages: list[dict], deps: ChatDeps):
    """Single turn. Returns the final messages list.

    Agent Framework surfaces an approval-required outcome through the
    response's `user_input_requests` field (shape: list of pending function
    calls awaiting approval). When one is present we persist via
    `storage.approvals.enqueue(...)` and raise AgentPaused so the route
    returns a 'pending review' message to the user. Plan 13 holds the
    persistence + resume route."""
    response = await agent.run(messages=messages)
    pending = getattr(response, "user_input_requests", None) or []
    if pending:
        from storage.approvals import enqueue_pending  # avoid import cycle
        enqueue_pending(deps.trace_id, response, pending, messages)
        raise AgentPaused(deps.trace_id, step=len(messages))
    deps.rich_contents.extend(_collect_rich(response))
    return response.messages
```

```python
# chat/tool_adapter.py (sketch)
from agent_framework import tool

def as_framework_tool(t, *, deps):
    """Wrap one of our ⟨I⟩ Tool objects as a framework function tool.

    Agent Framework prefers plain Python functions annotated with
    typing.Annotated[..., pydantic.Field(description=...)] and discovers the
    JSON schema from the signature. Our ⟨I⟩ Tool already carries a definition()
    dict in OpenAI tool-schema shape, so we synthesise a function with the
    right name / docstring and route the call through t.execute(args).

    Risky tools get `approval_mode="always_require"` so the framework pauses
    before invocation (HITL — plan 13 handles persistence and resume).
    """
    name = t.definition()["function"]["name"]
    doc = t.definition()["function"].get("description", "")
    approval_mode = "always_require" if getattr(t, "risky", False) else None

    @tool(name=name, description=doc, approval_mode=approval_mode)  # exact kwarg names TBD — verify
    def _call(**kwargs):
        result, rich = t.execute(kwargs)
        if rich:
            deps.rich_contents.extend(rich)
        return result

    return _call
```

```python
# chat/provider.py (sketch)
import asyncio
from app.core.protocols import ChatProvider, ChatResponse
from chat.agent import build_agent, run_agent, ChatDeps
from storage.audit import get_trace_id


class MsAgentFrameworkChatProvider:  # satisfies ⟨I⟩ ChatProvider
    def __init__(self, tools: list):
        self._tools = tools  # the framework client is constructed per-call so
                             # each turn uses a fresh ChatAgent bound to deps.

    def get_response(self, messages: list[dict]) -> ChatResponse:
        deps = ChatDeps(trace_id=get_trace_id())
        agent = build_agent(self._tools, deps)
        loop = asyncio.new_event_loop()
        try:
            final = loop.run_until_complete(run_agent(agent, messages, deps))
        finally:
            loop.close()
        text = final[-1].get("content", "") if final else ""
        return ChatResponse(text=text, rich_contents=deps.rich_contents)
```

### HITL mechanism

Agent Framework provides a built-in human-approval primitive for function tools (`approval_mode="always_require"`): when the model proposes to call such a tool, the agent run returns early with a `user_input_requests` list instead of invoking the tool. That is the primary mechanism.

Our side of HITL is persistence + resume (plan 13): we drain `user_input_requests` into `storage/approvals.py`, raise `AgentPaused`, and the `/admin/approvals/<trace_id>/approve` route reconstructs the pending state and feeds the approval back to the framework (concrete call shape — `agent.resume(approvals=...)` or similar — **TBD, verify against the 1.12.x API at execution time**).

For workflow-shaped HITL (multi-step pauses) the framework's `RequestPort` is available; the MVP does not need it.

Fallback if the framework's approval primitive turns out to be unstable at adoption time: keep the `AgentPaused` + resume-route pattern driven by our own `risky` check *before* the tool is passed to the framework (we never register the risky tool with the agent for the first turn; we re-register and resume on approval). This is noted in plan 13's "backup path".

## Workflow

**Pre-check**
- Plans 01 + 02 shipped.
- `make check` green.
- `pip install agent-framework agent-framework-openai` (and `agent-framework-foundry` if the Foundry layer is in-scope) succeeds in a scratch venv.
- Verify at scratch time: the exact import paths used above (`agent_framework.ChatAgent`, `agent_framework.openai.AzureOpenAIChatClient`, `agent_framework.tool`). If the 1.12.x surface differs, update the sketches and the adapter accordingly before touching source.

**Do**
1. Remove `pydantic-ai` + `pydantic-ai[openai]` from `app/requirements.txt` (and `pyproject.toml` after plan 09).
2. Add `agent-framework` (+ `agent-framework-foundry` if chosen) to the deps.
3. Write `chat/tool_adapter.py` with `as_framework_tool`.
4. Rewrite `chat/agent.py` as above.
5. Rewrite `chat/provider.py`: rename class to `MsAgentFrameworkChatProvider`, strict `_make_provider`, delete echo fallback.
6. Edit `app/core/services.py`: build via `{"azure": MsAgentFrameworkChatProvider}` dispatch keyed by `settings.CHAT_PROVIDER`.
7. Update `chat/__init__.py` export.
8. Rewrite `chat/tests/*` to use the framework's test helpers if available, otherwise a stub `AzureOpenAIChatClient` fixture that returns scripted agent-run responses.

**Verify**
- `grep -rn "pydantic_ai\|pydantic-ai" --include='*.py'` returns zero.
- `grep -rE "^import pydantic\|^from pydantic " --include='*.py'` returns zero *in our source* (transitive install is now allowed — plan 12).
- `pytest chat/tests -q` passes against the stub, including: tool-less reply, single-tool reply, risky-tool approval request (produces `user_input_requests`), approval resume, recursion-limit guard.
- Manual round-trip: with real Azure creds in `.env`, `curl -X POST /chat/send` returns an assistant message.
- Without creds and `CHAT_PROVIDER=azure`, startup raises per plan 01 — not a runtime echo.

**Commit**
`refactor(chat): Microsoft Agent Framework for the primary agent (drop pydantic-ai)`

**Rollback**
`git restore -SW chat/ app/core/services.py app/requirements.txt pyproject.toml`

## Verification checklist

- [ ] Zero `pydantic_ai` imports.
- [ ] Zero `import pydantic` in our source. (`pydantic` installed transitively via `agent-framework` is allowed — plan 12.)
- [ ] Zero `[echo — Azure OpenAI not configured]` strings anywhere.
- [ ] Stub-client tests cover: final text with no tool calls, single tool call, recursion-limit guard, HITL approval request + resume.
- [ ] `MsAgentFrameworkChatProvider` constructs cleanly when `settings.CHAT_PROVIDER=azure` and the three required Azure fields are set.
- [ ] `app/core/services.py` dispatches via a dict registry, not an `if/elif` chain.
- [ ] `chat/tool_adapter.py` wraps every registered `⟨I⟩ Tool` with the correct `approval_mode` based on `tool.risky`.

## Out of scope

- Content Safety wiring on the guardrail hook (reserved).
- Streaming responses to the UI (optional; MVP uses whole-message appends).
- Multi-agent orchestration via Agent Framework `Workflow` graphs.
- Replacing `storage.store.save_messages` for state persistence — reuse it.

## TBD items (verify at execution time)

- Exact distribution choice: single `agent-framework` umbrella vs narrower `agent-framework-core` + `agent-framework-openai` (+ `agent-framework-foundry`). Prefer narrower if the dep tree is noticeably smaller.
- Exact kwarg name for the recursion / iteration cap on `ChatAgent` (`max_iterations` vs `max_turns`).
- Exact kwarg name for `approval_mode` on `@tool` and the shape of `response.user_input_requests` on `agent.run(...)`.
- Resume API shape (`agent.resume(approvals=...)` or similar).
- Presence of a public `agent_framework.testing` module with a scripted-response client fixture; fall back to a hand-rolled stub if absent.

---

## Reasoning / justification extracts

**User instructions:**
- "no lets use azure explicitly ... modify plans as if we already have it or just need to install it" (the pivot that triggered this rewrite).
- "if there's an azure solution we should try and use it to reduce dependency surface area and code simplicity".
- "ok why not use azure sdk now, what changes, still lang on top of azure sdk?".
- "ship with Azure SDK" (earlier verdict — the Agent Framework pivot supersedes this for the primary runtime but keeps the SDK-direct implementation documented as the fallback).

**Research informing the imports / API shape:**
- Microsoft Learn — Agent Framework overview + tutorials: `pip install agent-framework` installs the umbrella; `agent-framework-openai` is the OpenAI/Azure OpenAI provider; `agent-framework-foundry` is the Microsoft Foundry integration layer.
- PyPI — `agent-framework` 1.12.x (July 2026), GA April 2026, Semantic Kernel successor.
- Function-tool shape — `@tool` decorator over plain Python functions with `typing.Annotated[..., Field(description=...)]` for parameter docs; `pydantic.Field` is used from `typing.Annotated` → `pydantic` is a hard transitive dep.
- HITL — Agent Framework exposes function-level approval via `approval_mode="always_require"`; the agent run returns `user_input_requests` instead of invoking the tool. Workflow-level HITL uses `RequestPort`. (Microsoft Learn `agent-framework/workflows/human-in-the-loop`.)

**Pitch commitments honoured:**
- `⟨I⟩ ChatProvider` protocol stays stable (§4 Design Decisions, Protocol contracts row).
- Bounded recursion with `AGENT_RECURSION_LIMIT=25` — now enforced by `ChatAgent`'s max-iterations kwarg (§6 Requirements Traceability, Primary agent).
- Tool calling validated against `⟨I⟩ Tool` (§2 Internals, Panel B) — our adapter preserves `definition()` + `execute(args)`.
- `AgentAction` audit emission per LLM turn and per tool call (§2 Internals, Panel A) — emitted around the `agent.run(...)` call and inside the tool adapter.
- Guardrail hook point in tool wrapper (§5 Guardrails + sandbox row) — kept as a no-op today inside `as_framework_tool`.

**Why Microsoft Agent Framework over the hand-rolled SDK path:**
Choosing Microsoft's blessed Azure agent SDK aligns with the Azure/PBMM end-state the pitch commits to, delivers HITL / orchestration primitives Microsoft maintains (vs. our 60-line resume-loop), and makes the "successor to Semantic Kernel" procurement story straightforward. The cost is `pydantic` back in the install tree and a thicker transitive-dep footprint — explicitly acknowledged in `docs-depo/exploration/dependency-strategy.md`.

**Why keep the SDK-direct path documented as a fallback:**
If Agent Framework access is blocked (preview access, licensing, air-gap), the SDK-direct implementation (`docs-depo/exploration/azure-openai-sdk-usage.md`) is a drop-in alternate `⟨I⟩ ChatProvider` behind the same protocol. One class swap in `app/core/services.py`, no changes to routes / audit / data.

**Why strict construction instead of silent echo fallback:**
Silent fallback masked a config error during the demo pass. Fail-fast at import matches pitch §8 invariants and the user instruction "no hardcoding anything".
