"""Unified data query tool for the chat agent.

One tool, one store, one interface. The model calls query_data(key, action, value?).
The store resolves the key against user_data, profile metadata, and global datasets
— all scoped by the user's role. The model never knows which namespace the data
came from, or what data exists beyond the user's scope.
"""

import json
from typing import Any

from app.core.logging import log_function_call

from app.core.protocols import Tool


class QueryTool:
    """Query/Store tool for workspace-scoped and global data.

    Role-gated:
      - base_user+ can query and list
      - power_user+ can store and delete
      - admin sees all workspaces and users

    The store (SqliteDataStore) handles data scoping. This tool handles
    role checks and returns generic denial messages — never leaks what
    exists beyond the user's scope.
    """

    def __init__(self, store: Any) -> None:
        """Create a QueryTool backed by a DataStore implementation.

        store must implement: query(), store(), list_keys(), delete()
        with signature: (username, workspace_id, key, user_role) for query
        """
        self._store = store
        self._username = ""
        self._workspace_id = ""
        self._user_role = "base_user"
        self._user_flags: list[str] = []

    # Set user context before each agent run.
    # Called from the agent tool closure before executing.
    def set_user(
        self,
        username: str,
        workspace_id: str,
        user_role: str = "base_user",
        user_flags: list[str] | None = None,
    ) -> None:
        """Set user context before each agent run. Called from agent tool closure."""
        self._username = username
        self._workspace_id = workspace_id
        self._user_role = user_role
        self._user_flags = user_flags or []

    # -- Tool protocol -------------------------------------------------------

    def definition(self) -> dict[str, Any]:
        """Return OpenAI tool definition schema."""
        log_function_call("storage.query_tool", "definition")
        return {
            "type": "function",
            "function": {
                "name": "query_data",
                "description": (
                    "Query, store, list, or delete structured data by key name. "
                    "Use action='query' to read data, action='store' to save data, "
                    "action='list' to see available keys, action='delete' to remove data."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string",
                            "description": "Data key to operate on, e.g. 'population_stats' or 'my_notes'",
                        },
                        "action": {
                            "type": "string",
                            "enum": ["query", "store", "list", "delete"],
                            "description": "What to do: query (read), store (write), list (show all keys), delete (remove)",
                        },
                        "value": {
                            "type": "object",
                            "description": "JSON value to store. Required when action='store'.",
                        },
                    },
                    "required": ["key", "action"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        """Run a query_data action. Role-gated — base_user+ for query, power_user+ for store."""
        action = args.get("action", "query")
        key = args.get("key", "")
        log_function_call(
            "storage.query_tool", "execute",
            action=action, key=key, role=self._user_role,
        )

        # Role gate — base_user and above can query/list
        role_level = _role_number(self._user_role)
        if role_level < _ROLE_LEVEL["base_user"]:
            return self._deny("No data available for this query.")

        if action == "query":
            return self._do_query(key)
        elif action == "store":
            return self._do_store(key, args.get("value"))
        elif action == "list":
            return self._do_list()
        elif action == "delete":
            return self._do_delete(key)
        else:
            return self._error(f"Unknown action: {action}")

    # -- Action handlers -----------------------------------------------------

    def _do_query(self, key: str) -> tuple[dict[str, Any], dict[str, Any] | None]:
        result = self._store.query(
            self._username, self._workspace_id, key, self._user_role
        )
        if result is None:
            return self._build_result(f"No data found for '{key}'.")
        return self._build_result(json.dumps(result, default=str))

    def _do_store(self, key: str, value: dict | None) -> tuple[dict[str, Any], dict[str, Any] | None]:
        if _role_number(self._user_role) < _ROLE_LEVEL["power_user"]:
            return self._deny("Unable to store data.")
        if not value:
            return self._error("value is required for store action")
        self._store.store(self._username, self._workspace_id, key, value)
        return self._build_result(f"Stored data under '{key}'.")

    def _do_list(self) -> tuple[dict[str, Any], dict[str, Any] | None]:
        keys = self._store.list_keys(
            self._username, self._workspace_id, self._user_role
        )
        if not keys:
            return self._build_result("No data keys available.")
        return self._build_result(f"Available keys: {', '.join(keys)}")

    def _do_delete(self, key: str) -> tuple[dict[str, Any], dict[str, Any] | None]:
        if _role_number(self._user_role) < _ROLE_LEVEL["power_user"]:
            return self._deny("Unable to delete data.")
        self._store.delete(self._username, self._workspace_id, key)
        return self._build_result(f"Deleted '{key}'.")

    # -- Response builders ---------------------------------------------------

    def _build_result(self, result: str) -> tuple[dict[str, Any], dict[str, Any] | None]:
        """Build a standard tool_result message. No rich content for data queries."""
        return {
            "role": "tool_result",
            "content": {"tool_call_id": "", "result": result},
        }, None

    def _error(self, message: str) -> tuple[dict[str, Any], dict[str, Any] | None]:
        """Build an error result message."""
        return {
            "role": "tool_result",
            "content": {"tool_call_id": "", "result": f"Error: {message}"},
        }, None

    def _deny(self, message: str) -> tuple[dict[str, Any], dict[str, Any] | None]:
        """Build a denial message. Never leaks what exists — just says unavailable."""
        return {
            "role": "tool_result",
            "content": {"tool_call_id": "", "result": message},
        }, None


# Role levels — kept in sync with storage.store._ROLE_LEVEL and logging._ROLE_LEVEL
_ROLE_LEVEL: dict[str, int] = {
    "base_user": 1,
    "power_user": 2,
    "admin": 3,
}


def _role_number(role: str) -> int:
    """Return the numeric level for a role string. Unknown roles get 0."""
    return _ROLE_LEVEL.get(role, 0)