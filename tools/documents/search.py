"""Document search tool — search and list files from data sources."""

import json
from typing import Any

from app.core.logging import log_function_call
from connectors.protocols import DataSource


class DocumentSearchTool:
    """Let the agent search for and list files from configured data sources."""

    def __init__(self, sources: dict[str, DataSource]) -> None:
        self._sources = sources

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_documents",
                "description": (
                    "Search for files in available data sources. "
                    "Use 'list' as the query to see all files in a source."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search term. Use 'list' to show all files.",
                        },
                        "source_name": {
                            "type": "string",
                            "description": (
                                "Data source to search. Available sources are listed "
                                "in your context. If unsure, ask the user."
                            ),
                        },
                    },
                    "required": ["query", "source_name"],
                },
            },
        }

    def execute(
        self,
        args: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, Any] | None]:
        query = args.get("query", "")
        source_name = args.get("source_name", "")
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.documents.search",
            "execute",
            query=query,
            source_name=source_name,
            source="agent_or_route",
        )

        entries = self._fetch_entries(query, source_name)
        if entries is None:
            log_function_call(
                "tools.documents.search",
                "execute",
                step="error",
                error=f"Unknown source: {source_name}",
            )
            return self._build_error(tool_call_id, source_name), None

        log_function_call(
            "tools.documents.search",
            "execute",
            step="complete",
            result_count=len(entries),
        )
        return _build_result(entries, source_name, query, tool_call_id)

    def _fetch_entries(self, query: str, source_name: str) -> list | None:
        source = self._sources.get(source_name)
        if source is None:
            return None
        if query.lower() == "list":
            return source.list_files()
        return source.search(query)

    def _build_error(self, tool_call_id: str, source_name: str) -> dict[str, Any]:
        available = list(self._sources.keys())
        return {
            "role": "tool_result",
            "content": {
                "tool_call_id": tool_call_id,
                "result": json.dumps(
                    {
                        "error": (
                            f"Unknown data source '{source_name}'. "
                            f"Available sources: {', '.join(available)}"
                        ),
                    }
                ),
            },
        }


def _build_result(
    entries: list,
    source_name: str,
    query: str,
    tool_call_id: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    names = [{"name": e.name, "path": e.path, "size": e.size, "type": e.mime_type} for e in entries]
    capped = names[:20]

    tool_msg = {
        "role": "tool_result",
        "content": {
            "tool_call_id": tool_call_id,
            "result": json.dumps({"source": source_name, "count": len(names), "files": capped}),
        },
    }
    rich = {
        "role": "rich_content",
        "content": {"type": "file_listing", "source": source_name, "query": query, "files": names},
    }
    return tool_msg, rich
