# Azure OpenAI SDK — usage reference for CRAFT

Reference notes for building CRAFT's agent on `openai.AsyncAzureOpenAI` directly, with no LangChain / LangGraph. Explains what the SDK gives us, how far it goes, and when LangChain would be worth adding back.

Not read by code. Informs plans `03-agent-azure-sdk.md`, `04-audit-hash-chained.md`, `13-hitl-skeleton.md`.

---

## What the SDK gives us

The `openai` Python package (used against Azure via `AsyncAzureOpenAI`) covers the entire LLM surface we need for CRAFT's primary agent:

### Chat completions
`client.chat.completions.create(model=…, messages=…, …)` — the baseline call. `messages` is a list of dicts (`{"role": "system|user|assistant|tool", "content": …}`). Response carries `choices[0].message.content` and optional `tool_calls`.

### Native tool calling
Pass `tools=[{"type":"function","function":{"name":…,"description":…,"parameters":<JSON Schema>}}]` on the request. If the model decides to call a tool, response has:
```python
response.choices[0].message.tool_calls == [ChatCompletionMessageToolCall(id=…, function=Function(name=…, arguments=<str JSON>))]
```
Appending a `{"role":"tool","tool_call_id":<id>,"content":<result str>}` and re-calling is the entire ReAct loop. No framework needed. Our existing `⟨I⟩ Tool.definition()` already returns the right dict shape — the SDK accepts it verbatim.

### Structured outputs (JSON mode / strict schema)
`response_format={"type":"json_object"}` for free-form JSON, or `{"type":"json_schema","json_schema":{…,"strict":True}}` to constrain to a specific schema. Lets a tool return a validated object without us hand-rolling a parse step.

### Streaming
`stream=True` returns an async iterator of `ChatCompletionChunk` objects. Yields partial `content` deltas and partial `tool_calls`. Needed only if we want token-by-token UI; our Dash chat appends whole messages, so streaming is optional.

### Embeddings
`client.embeddings.create(model=…, input=…)` — vectors on demand. Needed only when we build local hybrid retrieval before Azure AI Search is wired. The pitch defers this to AI Search end-state, so we don't need it today.

### Rate-limit headers
Every response includes `x-ratelimit-remaining-requests` and `-tokens` headers on the raw HTTP response. The async client exposes them via `response._raw_response.headers`. Lets us emit backoff warnings to the audit log without external tooling.

### Content Safety hook (reserved)
Azure OpenAI supports a `content_filter_results` field in responses when Content Safety is enabled on the deployment. Our tool-wrapper hook (`settings.GUARDRAIL_HOOK`) can read it and emit an `AgentAction` row with the category breakdown. No extra SDK needed — same `client.chat.completions.create` call.

### Function and arguments validation on our side
The model returns tool-call `arguments` as a JSON string. Our tools accept a dict. We `json.loads(arguments)` and the tool's own body validates the fields. No pydantic needed.

---

## What the SDK does *not* give us (we build these)

| Capability | Our implementation | ~Lines |
|---|---|---|
| ReAct loop (reason → call tool → reason → …) | `_react_loop()` in `chat/agent.py` | ~80 |
| Bounded recursion (pitch `recursion_limit=25`) | counter + `AgentRecursionLimit` exception | ~5 |
| Tool registry | plain `TOOLS: list[Tool]` + `_lookup(name)` | ~15 |
| State persistence between turns | existing `storage.store.save_messages` | 0 (reuse) |
| HITL interrupt | SQLite `approvals` table + `AgentPaused` + resume route | ~60 |
| Audit emission per tool call / LLM turn | `HashChainedJsonlLog.emit(AgentAction(…))` | ~5 at call sites |
| Rich-content side channel (charts, news_cards) | `deps.rich_contents.extend(rich)` after tool.execute | ~2 |
| Error / retry policy | `openai`'s built-in retry (`max_retries=2` on client) + our own on `AgentRecursionLimit` | ~5 |

Total ≈ 170 lines on top of the SDK for the full agent harness. Compare to the LangGraph wrapper which also pulls LangChain + pydantic.

---

## Minimum viable agent loop

Pattern for the one that lives in `chat/agent.py`:

```python
from openai import AsyncAzureOpenAI
from app.core.config import settings
from app.core.audit import agent_action_log, AgentAction

class AgentPaused(Exception): ...
class AgentRecursionLimit(Exception): ...

async def run_agent(client: AsyncAzureOpenAI, messages: list[dict], tools: list, deps):
    for step in range(settings.AGENT_RECURSION_LIMIT):
        r = await client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
            tools=[t.definition() for t in tools],
        )
        msg = r.choices[0].message
        messages.append(msg.to_dict())
        agent_action_log.emit(AgentAction(step=step, kind="llm_turn", trace_id=deps.trace_id, ...))
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
            messages.append({"role":"tool", "tool_call_id":call.id, "content":json.dumps(result)})
            agent_action_log.emit(AgentAction(step=step, kind="tool_call", tool_name=call.function.name, trace_id=deps.trace_id, ...))
    raise AgentRecursionLimit(settings.AGENT_RECURSION_LIMIT)
```

That's the whole thing. Everything else is tool implementation (`tools/*/`) or infrastructure (routes, storage, audit).

---

## When would LangChain / LangGraph earn its keep later

LangChain is overhead at this scope but genuinely buys things at larger scope. Honest table:

| Trigger | What LangChain / LangGraph adds | Rough extra deps |
|---|---|---|
| **Multi-agent orchestration** (planner → specialist agents, dynamic routing) | `langgraph.graph.StateGraph` with branching nodes; cleaner than hand-rolling | `langgraph`, `langchain-core`, `pydantic` |
| **Dynamic tool composition from user input** (tools built at runtime from a config file) | `langchain-core`'s `StructuredTool.from_function` and tool binding helpers | `langchain-core`, `pydantic` |
| **Hybrid retrieval chains with reranking and self-correction** (RAGAS-style grounding loops) | `langchain`'s retriever abstractions and `RetrievalQA`-style chains | `langchain`, `langchain-core`, `pydantic` |
| **Persistent long-running conversations with branch-and-merge history** | `langgraph.checkpoint.*` savers for durable graph state | `langgraph`, `pydantic` |
| **Streaming graph events to a UI** (per-node status, intermediate thoughts) | `graph.astream_events()` with typed event payloads | `langgraph` |
| **Observability through LangSmith** | LangSmith callbacks | `langsmith`, `langchain-core` |

**None of those are in the CRAFT pitch for the MVP.** All of them slot behind the `⟨I⟩ ChatProvider` protocol — the one we hold stable in `chat/provider.py`. The switch would be: write a new `LangGraphChatProvider(ChatProvider)` class, update one dict entry in `app/core/services.py`'s provider registry (`"azure"` → `"langgraph"`), and ship. Routes, audit, storage, data sources, tools — all untouched.

### Partial adoption (if we need just one piece)

- **Only the tool decorator** — not useful, our `⟨I⟩ Tool.definition()` is simpler and visible.
- **Only `langgraph.checkpoint.sqlite.SqliteSaver`** — we already persist messages via `storage.store`; the saver would duplicate.
- **Only `langchain-openai.AzureChatOpenAI`** — a thin wrapper around `AsyncAzureOpenAI`. No win.
- **Only `langgraph.types.interrupt`** — our `AgentPaused` + SQLite approval row is 60 lines and already pitch-aligned.

Verdict: there is no useful partial adoption at this scope. All-or-nothing is fine. Direct SDK until a trigger above becomes real.

---

## Decision rule for revisiting

Add LangGraph when any of these become true:

1. ≥ 3 specialist agents coordinating under a planner.
2. The audit / grounding / confidence loop grows past ~400 lines (current ceiling ≈ 170 + ~200 tools).
3. A requirement lands that needs `astream_events` style per-node UI updates in Dash.
4. LangSmith tracing is a procurement line.

Until then: Azure SDK direct keeps the dep tree small, the code visible, and the pitch's protocol seams honest.

---

## References

- Azure OpenAI Python SDK reference — https://learn.microsoft.com/azure/ai-services/openai/reference
- OpenAI Python SDK repo — https://github.com/openai/openai-python
- Function/tool calling guide (Azure) — https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling
- Structured outputs — https://learn.microsoft.com/azure/ai-services/openai/how-to/structured-outputs
- Content filtering — https://learn.microsoft.com/azure/ai-services/openai/concepts/content-filter
- LangGraph docs (for later reference) — https://langchain-ai.github.io/langgraph/
