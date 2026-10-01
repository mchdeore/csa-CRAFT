"""Interfaces for swappable app components."""

from __future__ import annotations

from typing import Any, Protocol

from flask import Flask


class AuthProvider(Protocol):
    """Authentication provider — login, logout, flask wiring."""

    def init_app(self, flask_app: Flask) -> object: ...

    def try_login(self, username: str, password: str) -> bool: ...

    def do_logout(self) -> None: ...


class WorkspaceStore(Protocol):
    def list(self, username: str) -> list[dict]: ...

    def load(self, username: str, workspace_id: str) -> dict | None: ...

    def save(self, username: str, workspace: dict) -> None: ...

    def create(self, username: str, name: str) -> dict: ...

    def save_messages(self, username: str, workspace_id: str, messages: list[dict]) -> None: ...


class ChatResponse:
    """Result from ChatProvider.get_response.

    text: the final text reply to display. May be empty if response is a tool call chain.
    rich_contents: extra message objects appended to chat history (charts, news_cards, etc.).
    """

    def __init__(self, text: str = "", rich_contents: list[dict] | None = None) -> None:
        self.text = text
        self.rich_contents: list[dict] = rich_contents or []


class ChatProvider(Protocol):
    _user_context: dict[str, str] | None

    def get_response(self, messages: list[dict]) -> ChatResponse: ...


class Tool(Protocol):
    """A tool the chat model can invoke.

    definition() returns the OpenAI tool JSON schema.
    execute(args) runs the tool and returns (tool_message, rich_content_or_none).
    """

    def definition(self) -> dict[str, Any]: ...

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]: ...
