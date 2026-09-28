# PydanticAI Agent Integration

## Overview

The chat backend uses [PydanticAI](https://ai.pydantic.dev/) as the agent framework to manage LLM tool-calling loops. PydanticAI replaces the previous hand-rolled tool loop with a structured, typed agent harness.

## Architecture

```
User message
    │
    ▼
chat/routes.py          ← Flask route receives message
    │
    ▼
chat/provider.py        ← DeepSeekChat.get_response()
    │  builds message history, creates agent
    ▼
chat/agent.py           ← PydanticAI Agent with registered tools
    │  runs tool-calling loop automatically
    ▼
tools/*.py              ← Existing tool implementations (weather, news, etc.)
    │  return (tool_msg, rich_content)
    ▼
ChatResponse            ← text + rich_contents (charts, news cards)
```

## Key Files

| File | Purpose |
|------|---------|
| `chat/agent.py` | Defines `ChatDeps` (dependency injection) and `create_agent()` which registers all tools |
| `chat/provider.py` | `DeepSeekChat` — creates the PydanticAI agent, converts message history, calls `run_sync()` |
| `tools/*.py` | Tool implementations unchanged — each has `definition()` and `execute()` methods |

## How It Works

1. **`ChatDeps`** is a dataclass injected into every tool call. It holds references to all tool instances and a `rich_contents` list that accumulates charts and news cards during the agent loop.

2. **Tool wrappers** are thin `@agent.tool` functions that call the existing tool's `.execute()` method. Each wrapper:
   - Calls the underlying tool with the arguments
   - Appends any rich content (charts, news cards) to `deps.rich_contents`
   - Returns the text result string back to the LLM

3. **Message history** is converted from the app's stored format (`{role, content}` dicts) to PydanticAI's `ModelRequest`/`ModelResponse` format. Only `user` and `assistant` text messages are converted; rich content messages (charts, news cards) are UI-only and skipped.

4. **`run_sync()`** drives the full tool-calling loop. PydanticAI handles:
   - Sending the prompt + history to the LLM
   - Parsing tool call requests from the LLM
   - Executing the matching tool wrapper
   - Feeding tool results back to the LLM
   - Repeating until the LLM produces a final text response

## Model Configuration

The agent uses Azure OpenAI via PydanticAI's `OpenAIProvider` (v2.51+):

```python
from openai import AsyncAzureOpenAI
from pydantic_ai.providers.openai import OpenAIProvider

client = AsyncAzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2024-10-21",
)
provider = OpenAIProvider(openai_client=client)
agent = Agent("CHE-DSV4P", provider=provider, system_prompt=...)
```

## Adding a New Tool

1. Create `tools/my_tool.py` implementing `definition()` and `execute()`
2. Add the tool instance to `ChatDeps` in `chat/agent.py`
3. Add a `_register_my_tool()` function with an `@agent.tool` wrapper
4. Call it from `create_agent()`
5. Wire the tool instance in `app/core/services.py`

## Demo Flow

1. Login as `user1` (password: `1`)
2. Create a workspace
3. Ask: "Tell me about today in Montreal"
4. Agent calls `get_weather("Montreal")` and `search_news("Montreal")` 
5. Interactive Plotly weather charts and news cards render inline
6. Logout → login as `user2` → separate workspace
7. Logout → login as `user1` → Montreal conversation persisted
