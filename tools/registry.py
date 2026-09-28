"""Holds a list of Tool implementations and dispatches execution."""

from typing import Any

from app.core.protocols import Tool


class ToolRegistry:
    """Collection of tools the chat model can invoke."""

    def __init__(self, tools: list[Tool] | None = None) -> None:
        self._tools: dict[str, Tool] = {}
        for tool in tools or []:
            name = tool.definition()["function"]["name"]
            self._tools[name] = tool

    # Register a tool programmatically after init
    def register(self, tool: Tool) -> None:
        name = tool.definition()["function"]["name"]
        self._tools[name] = tool

    # All tool definitions for the OpenAI API tools parameter
    def definitions(self) -> list[dict[str, Any]]:
        return [t.definition() for t in self._tools.values()]

    # Execute a tool by name, return (tool_message, rich_content_or_none)
    def execute(
        self,
        name: str,
        args: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, Any] | None]:
        tool = self._tools.get(name)
        if tool is None:
            return {
                "role": "tool_result",
                "content": {
                    "tool_call_id": "",
                    "result": f"Unknown tool: {name}",
                },
            }, None
        return tool.execute(args)
