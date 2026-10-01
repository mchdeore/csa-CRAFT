"""Tests for chat/agent.py — agent creation and ChatDeps dataclass."""

from unittest.mock import MagicMock

import pytest
from pydantic_ai import Agent
from pydantic_ai.providers.openai import OpenAIProvider

from chat.agent import ChatDeps, create_agent


# Fixture: a mock OpenAI provider so we don't need real Azure credentials
@pytest.fixture
def mock_provider() -> OpenAIProvider:
    """Build a provider pointing at a fake local endpoint.

    create_agent needs a real provider to instantiate OpenAIChatModel.
    We point it at a non-existent host. The model object is created but
    no actual HTTP calls happen during agent construction.
    """
    return OpenAIProvider(
        base_url="http://localhost:9999/v1",
        api_key="test-key",
    )


class TestCreateAgent:
    def test_returns_agent_object(self, mock_provider: OpenAIProvider) -> None:
        agent = create_agent(
            model_name="gpt-4o-mini",
            provider=mock_provider,
            system_prompt="You are a test assistant.",
        )
        assert agent is not None
        assert isinstance(agent, Agent)

    def test_agent_has_tools_registered(self, mock_provider: OpenAIProvider) -> None:
        agent = create_agent(
            model_name="gpt-4o-mini",
            provider=mock_provider,
            system_prompt="You are a test assistant.",
        )

        # The agent's tools are stored internally. After registration,
        # we check the agent has function tools.
        tools = agent._function_tools

        # There should be many tools registered (14+ from the 13 tool
        # registration calls plus query_data).
        assert len(tools) > 10, f"Expected >10 tools, got {len(tools)}"

    def test_agent_has_key_tools(self, mock_provider: OpenAIProvider) -> None:
        agent = create_agent(
            model_name="gpt-4o-mini",
            provider=mock_provider,
            system_prompt="You are a test assistant.",
        )

        # Collect tool names from the registered function tools
        tool_names = {tool.name for tool in agent._function_tools}

        # Spot-check a few known tools
        expected_tools = {
            "get_weather",
            "search_news",
            "draw_bar_chart",
            "query_data",
            "search_documents",
        }
        missing = expected_tools - tool_names
        assert not missing, f"Missing expected tools: {missing}"

    def test_default_model_name_is_accepted(self, mock_provider: OpenAIProvider) -> None:
        agent = create_agent(
            model_name="gpt-4o",
            provider=mock_provider,
            system_prompt="Test prompt.",
        )
        assert agent is not None

    def test_system_prompt_is_stored(self, mock_provider: OpenAIProvider) -> None:
        prompt = "You are a helpful space systems analyst."
        agent = create_agent(
            model_name="gpt-4o-mini",
            provider=mock_provider,
            system_prompt=prompt,
        )
        # The system prompt is used as the agent's instruction
        assert agent._system_prompt == prompt


class TestChatDeps:
    def test_can_instantiate_with_required_fields(self) -> None:
        deps = ChatDeps(
            username="testuser",
            workspace_id="ws-123",
        )
        assert deps.username == "testuser"
        assert deps.workspace_id == "ws-123"

    def test_default_values_are_sane(self) -> None:
        deps = ChatDeps()
        assert deps.username == ""
        assert deps.workspace_id == ""
        assert deps.user_role == "base_user"
        assert deps.user_flags == []
        assert deps.rich_contents == []

    def test_all_fields_are_settable(self) -> None:
        deps = ChatDeps(
            username="alice",
            workspace_id="ws-42",
            user_role="admin",
            user_flags=["beta"],
        )
        assert deps.username == "alice"
        assert deps.workspace_id == "ws-42"
        assert deps.user_role == "admin"
        assert deps.user_flags == ["beta"]

    def test_tool_fields_default_to_none(self) -> None:
        deps = ChatDeps()
        assert deps.weather is None
        assert deps.news is None
        assert deps.doc_search is None
        assert deps.query_tool is None

    def test_tool_fields_can_be_set(self) -> None:
        mock_weather = MagicMock()
        deps = ChatDeps(weather=mock_weather)
        assert deps.weather is mock_weather