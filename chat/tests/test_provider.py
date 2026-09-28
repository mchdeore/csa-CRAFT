"""Tests for DeepSeekChat — message building, fallback behavior, no actual API calls."""

from unittest.mock import MagicMock

import pytest

from chat.provider import DeepSeekChat, _build_history


def _make_mock_tools() -> dict:
    return {
        "weather": MagicMock(),
        "historical_weather": MagicMock(),
        "news": MagicMock(),
        "excel": MagicMock(),
        "doc_search": MagicMock(),
        "text_analysis": MagicMock(),
    }


@pytest.fixture
def chat(monkeypatch: pytest.MonkeyPatch) -> DeepSeekChat:
    monkeypatch.delenv("AZURE_OPENAI_ENDPOINT", raising=False)
    monkeypatch.delenv("AZURE_OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("AZURE_OPENAI_API_VERSION", raising=False)
    monkeypatch.delenv("AZURE_OPENAI_DEPLOYMENT", raising=False)
    return DeepSeekChat(**_make_mock_tools())


@pytest.fixture
def chat_with_env(monkeypatch: pytest.MonkeyPatch) -> DeepSeekChat:
    monkeypatch.setenv("AZURE_OPENAI_ENDPOINT", "https://example.openai.azure.com")
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "fake-key")
    monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "2024-10-21")
    return DeepSeekChat(**_make_mock_tools())


class TestGetProvider:
    def test_returns_none_when_env_vars_unset(self, chat: DeepSeekChat) -> None:
        provider = chat._get_provider()
        assert provider is None

    def test_returns_provider_when_env_vars_set(self, chat_with_env: DeepSeekChat) -> None:
        provider = chat_with_env._get_provider()
        assert provider is not None


class TestGetResponse:
    def test_fallback_when_no_provider(self, chat: DeepSeekChat) -> None:
        response = chat.get_response([])
        assert "Azure OpenAI not configured" in response.text
        assert response.rich_contents == []

    def test_fallback_with_messages_no_provider(self, chat: DeepSeekChat) -> None:
        response = chat.get_response(
            [
                {"role": "user", "content": "What is the weather?"},
            ]
        )
        assert "Azure OpenAI not configured" in response.text


class TestBuildHistory:
    def test_empty_list(self) -> None:
        assert _build_history([]) == []

    def test_user_and_assistant_messages(self) -> None:
        messages = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"},
            {"role": "user", "content": "How are you?"},
        ]
        result = _build_history(messages)
        assert len(result) == 3

    def test_skips_non_text_content(self) -> None:
        messages = [
            {"role": "user", "content": "Hello"},
            {"role": "chart", "content": {"type": "chart", "figure": {}}},
            {"role": "assistant", "content": "Here is your chart"},
        ]
        result = _build_history(messages)
        assert len(result) == 2

    def test_skips_non_user_assistant_roles(self) -> None:
        messages = [
            {"role": "user", "content": "Hello"},
            {"role": "news_cards", "content": {"articles": []}},
            {"role": "tool_call", "content": {"tool_calls": []}},
            {"role": "assistant", "content": "Done"},
        ]
        result = _build_history(messages)
        assert len(result) == 2
