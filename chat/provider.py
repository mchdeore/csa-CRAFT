"""Chat provider backed by PydanticAI agent with Azure OpenAI.

Pipeline: route → get_response → _make_provider → create_agent → agent.run
Each step is logged with trace ID for codepath tracking.
"""

import asyncio
import logging
import os
from typing import Any

from openai import AsyncAzureOpenAI
from pydantic_ai.messages import ModelRequest, ModelResponse, TextPart, UserPromptPart
from pydantic_ai.providers.openai import OpenAIProvider

from app.core.config import build_system_prompt
from app.core.logging import log_function_call
from app.core.protocols import ChatResponse
from chat.agent import ChatDeps, create_agent

logger = logging.getLogger(__name__)


class DeepSeekChat:
    """Chat provider using PydanticAI agent with Azure OpenAI.

    Accepts username, workspace_id, role, flags, and query_tool so
    user context flows into every tool call. Data scoping happens
    automatically based on role.
    """

    def __init__(
        self,
        weather: Any,
        historical_weather: Any,
        news: Any,
        excel: Any,
        bar_chart: Any,
        pie_chart: Any,
        scatter_chart: Any,
        heatmap: Any,
        histogram: Any,
        line_chart: Any,
        boxplot: Any,
        doc_search: Any,
        text_analysis: Any,
        ingest_document: Any = None,
        query_tool: Any = None,
        user_context: dict | None = None,
        username: str = "",
        workspace_id: str = "",
        user_role: str = "base_user",
        user_flags: list[str] | None = None,
    ) -> None:
        self._weather = weather
        self._historical_weather = historical_weather
        self._news = news
        self._excel = excel
        self._bar_chart = bar_chart
        self._pie_chart = pie_chart
        self._scatter_chart = scatter_chart
        self._heatmap = heatmap
        self._histogram = histogram
        self._line_chart = line_chart
        self._boxplot = boxplot
        self._doc_search = doc_search
        self._text_analysis = text_analysis
        self._ingest_document = ingest_document
        self._query_tool = query_tool
        self._user_context = user_context
        self._username = username
        self._workspace_id = workspace_id
        self._user_role = user_role
        self._user_flags = user_flags or []

    def _make_provider(self) -> tuple[OpenAIProvider, str] | tuple[None, str]:
        log_function_call("chat.provider", "_make_provider", step="create_azure_client")
        endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
        api_key = os.environ.get("AZURE_OPENAI_API_KEY")
        if not endpoint or not api_key:
            log_function_call("chat.provider", "_make_provider", step="missing_credentials")
            return None, ""
        client = AsyncAzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-10-21"),
        )
        deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "CHE-DSV4P")
        log_function_call(
            "chat.provider",
            "_make_provider",
            step="provider_ready",
            deployment=deployment,
        )
        return OpenAIProvider(openai_client=client), deployment

    def get_response(self, messages: list[dict]) -> ChatResponse:
        log_function_call(
            "chat.provider",
            "get_response",
            step="start",
            message_count=len(messages),
        )

        provider, deployment = self._make_provider()
        if provider is None:
            return ChatResponse(
                text="Azure OpenAI not configured. "
                "Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY in .env"
            )

        if not messages:
            return ChatResponse(text="No messages provided.")

        current_prompt = ""
        if messages[-1]["role"] == "user" and isinstance(messages[-1]["content"], str):
            current_prompt = messages[-1]["content"]
            prior = messages[:-1]
        else:
            current_prompt = "Continue."
            prior = messages

        log_function_call(
            "chat.provider",
            "get_response",
            step="build_agent",
            deployment=deployment,
        )
        system_prompt = build_system_prompt(self._user_context)
        agent = create_agent(deployment, provider, system_prompt)

        deps = ChatDeps(
            username=self._username,
            workspace_id=self._workspace_id,
            user_role=self._user_role,
            user_flags=self._user_flags,
            weather=self._weather,
            historical_weather=self._historical_weather,
            news=self._news,
            excel=self._excel,
            bar_chart=self._bar_chart,
            pie_chart=self._pie_chart,
            scatter_chart=self._scatter_chart,
            heatmap=self._heatmap,
            histogram=self._histogram,
            line_chart=self._line_chart,
            boxplot=self._boxplot,
            doc_search=self._doc_search,
            text_analysis=self._text_analysis,
            ingest_document=self._ingest_document,
            query_tool=self._query_tool,
        )

        history = _build_history(prior)

        log_function_call(
            "chat.provider",
            "get_response",
            step="agent_run",
            prompt=current_prompt[:100],
        )

        try:
            loop = asyncio.new_event_loop()
            try:
                result = loop.run_until_complete(
                    agent.run(current_prompt, deps=deps, message_history=history)
                )
            finally:
                loop.close()
            log_function_call(
                "chat.provider",
                "get_response",
                step="complete",
                rich_count=len(deps.rich_contents),
                output_len=len(result.output),
            )
            return ChatResponse(text=result.output, rich_contents=deps.rich_contents)
        except Exception as e:
            log_function_call("chat.provider", "get_response", step="error", error=str(e)[:200])
            logger.exception("PydanticAI agent error")
            return ChatResponse(text="Sorry, something went wrong. Please try again.")


def _build_history(
    messages: list[dict],
) -> list[ModelRequest | ModelResponse]:
    """Convert stored chat messages to pydantic-ai message history."""
    history: list[ModelRequest | ModelResponse] = []
    for msg in messages:
        role = msg["role"]
        content = msg.get("content", "")
        if not isinstance(content, str):
            continue
        if role == "user":
            history.append(ModelRequest(parts=[UserPromptPart(content=content)]))
        elif role == "assistant":
            history.append(ModelResponse(parts=[TextPart(content=content)]))
    return history
