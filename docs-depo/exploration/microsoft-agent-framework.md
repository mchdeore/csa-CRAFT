# Microsoft Agent Framework — research notes

Notes on `agent-framework`, the Microsoft agent SDK CRAFT adopts as the primary agent runtime. Informs the pitch (`docs-depo/pitch/CRAFT-pitch.md`) and the refactor plans (`plans/03`, `plans/13` on branch `claude/nice-cori-nb1ong`).

Not read by code.

---

## What it is

- Successor to **Semantic Kernel**. Microsoft announced Agent Framework in October 2025, hit Release Candidate in February 2026, GA'd April 3 2026. The Semantic Kernel GitHub repository now points new deployments at Agent Framework.
- Microsoft's enterprise-ready, long-term-supported Python / C# / Java SDK for building AI agents on Azure OpenAI and Azure AI Foundry.
- First-class HITL (function-level approval + workflow-level `RequestPort`), bounded iteration, observability through OpenTelemetry, built-in Azure OpenAI client.

## Installation

```bash
pip install agent-framework          # umbrella (includes most sub-packages)
# or granular:
pip install agent-framework-core     # just the runtime
pip install agent-framework-openai   # Azure OpenAI chat client
pip install agent-framework-foundry  # Azure AI Foundry integration
```

Requires Python 3.10+. Current stable release is `1.12.x` as of July 2026.

## Imports we expect to use

```python
from agent_framework import ChatAgent, tool
from agent_framework.openai import AzureOpenAIChatClient
```

The pitch and plans reference these; exact kwarg names are listed under **TBDs** below.

## Agent construction (sketch)

```python
from agent_framework import ChatAgent, tool
from agent_framework.openai import AzureOpenAIChatClient
from typing import Annotated
from pydantic import Field  # transitive; not imported directly in our source

@tool(approval_mode="always_require")  # TBD: exact kwarg name
def classify_risk(
    excerpt: Annotated[str, Field(description="Text excerpt to classify.")]
) -> dict:
    """Score risk severity for a CADRe part."""
    # delegates to our existing ⟨I⟩ Tool.execute(args)
    ...

client = AzureOpenAIChatClient(
    endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_key=settings.AZURE_OPENAI_API_KEY,
    api_version=settings.AZURE_OPENAI_API_VERSION,
    deployment=settings.AZURE_OPENAI_DEPLOYMENT,
)

agent = ChatAgent(
    chat_client=client,
    tools=[classify_risk, ...],
    max_iterations=settings.AGENT_RECURSION_LIMIT,  # TBD: max_iterations vs max_turns
)
```

Our `MsAgentFrameworkChatProvider` (satisfies `⟨I⟩ ChatProvider`) wraps `agent.run()` and converts between our `messages: list[dict]` and whatever shape the framework expects.

## HITL — two modes

### Function-level (what we use for MVP)

Mark the tool `approval_mode="always_require"`. When the model proposes a call, `agent.run()` returns a response with a `user_input_requests` field instead of invoking the tool. We persist that request to the SQLite `approvals` table and raise through to the `/admin/approvals/<trace_id>/<decision>` route. On approve: resume via the framework's resume API (TBD: `agent.resume(approvals=…)` vs. passing approvals on a re-run).

### Workflow-level (`RequestPort`)

The framework also has a workflow-level HITL mechanism via `RequestPort`. Richer — gates whole segments, not single tool calls — but overkill for the single-primary-agent MVP. Reserved for the multi-agent follow-up.

## Pydantic — honest status

- `agent-framework` uses `typing.Annotated[..., pydantic.Field(description=...)]` for `@tool` parameter descriptions. Confirmed in multiple Microsoft Learn tutorial excerpts.
- `pydantic` becomes a hard transitive dep when `agent-framework` is installed.
- Our guardrail (plan 12 on `claude/nice-cori-nb1ong`): tolerate `pydantic` in the installed package set, but no direct `import pydantic` or `from pydantic ...` lines allowed in our source. Enforced by `app/tests/test_imports.py`.
- Trade-off accepted: smaller dep tree (Azure SDK direct, no framework) vs. Microsoft-blessed, long-term-supported, HITL-native framework. We chose the framework.

## TBD items (verify at execution)

The subagent that pivoted the plans to Agent Framework left these verification points in the plan files:

- Exact iteration-cap kwarg: `max_iterations` vs. `max_turns` on `ChatAgent`.
- Exact approval-mode kwarg name on `@tool` and acceptable values.
- Shape of `response.user_input_requests` (dict? list of dataclass? which fields?).
- Resume API shape — `agent.resume(approvals=…)` vs. re-running with an approvals arg.
- Presence of a public `agent_framework.testing` module for scripted-response fixtures.
- Umbrella install vs. narrower `core + openai + foundry` set. The umbrella pulls more; the narrow set is cleaner for a locked production environment.

These are small details, not architectural unknowns. Resolve during plan 03 execution; adjust the sketch in plan 03 accordingly.

## Why we didn't pick LangChain / LangGraph

- Third-party, not Azure-native.
- Adds `langchain-*` and `pydantic` dep trees (bigger surface than Agent Framework's).
- Capability overlap: Agent Framework now provides ReAct, HITL interrupt, graph-level orchestration, telemetry, Foundry integration — the LangGraph "worth adopting" triggers we tracked in `azure-openai-sdk-usage.md` are all covered by Agent Framework from day one.
- Microsoft Learn documentation and support story is cleaner for a Canadian federal (PBMM) deployment.

## Why we kept the hand-rolled SDK path documented

Access to Agent Framework may be subject to procurement or environment constraints. If it is blocked, the hand-rolled ReAct loop on `openai.AsyncAzureOpenAI` (described in `docs-depo/exploration/azure-openai-sdk-usage.md`) is a viable backstop — ~250 lines, same protocol, same tool shapes, same HITL via `AgentPaused` + SQLite queue. Protocol `⟨I⟩ ChatProvider` is the swap point.

## References

- Package on PyPI — https://pypi.org/project/agent-framework/
- GA announcement + relationship to Semantic Kernel — https://atlan.com/know/ai-agent/microsoft/semantic-kernel/
- Companion decision notes — `docs-depo/exploration/azure-openai-sdk-usage.md`, `docs-depo/exploration/dependency-strategy.md` (both live on branch `claude/nice-cori-nb1ong`).
- Pivoted plans — `plans/03-agent-azure-sdk.md`, `plans/00-refactor-overview.md`, `plans/12-test-guardrails.md`, `plans/13-hitl-skeleton.md` (same branch).
