"""Tests for QueryTool — role-gated execute, data scoping, action dispatch."""

import importlib.util
import json
from pathlib import Path
from types import ModuleType
from unittest.mock import MagicMock

import pytest

# Load query_tool.py directly as a standalone module to avoid importing
# storage/__init__.py, which pulls in pydantic_ai through the chat dependency chain.
_qt_path = Path(__file__).parent.parent / "query_tool.py"
_spec = importlib.util.spec_from_file_location("query_tool", _qt_path)
if _spec is None or _spec.loader is None:
    raise RuntimeError("Failed to load query_tool.py spec")
_query_tool_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_query_tool_module)

QueryTool = _query_tool_module.QueryTool
_ROLE_LEVEL = _query_tool_module._ROLE_LEVEL
_role_number = _query_tool_module._role_number


@pytest.fixture
def mock_store():
    """Mock store that returns canned data."""
    store = MagicMock()
    store.query.return_value = [{"label": "test"}]
    store.list_keys.return_value = ["k1", "k2", "public_stats"]
    return store


@pytest.fixture
def tool(mock_store):
    """QueryTool with mock store and base_user context."""
    qt = QueryTool(mock_store)
    qt.set_user("alice", "ws1", "base_user")
    return qt


class TestRoleGating:
    """QueryTool checks role before executing."""

    def test_base_user_can_query(self, tool, mock_store) -> None:
        tool_msg, rich = tool.execute({"action": "query", "key": "test_key"})
        result = tool_msg["content"]["result"]
        assert "test" in result
        mock_store.query.assert_called_once()

    def test_base_user_can_list(self, tool, mock_store) -> None:
        tool_msg, _ = tool.execute({"action": "list", "key": "any"})
        result = tool_msg["content"]["result"]
        assert "k1" in result
        assert "k2" in result

    def test_base_user_cannot_store(self, tool, mock_store) -> None:
        tool_msg, _ = tool.execute({
            "action": "store",
            "key": "my_data",
            "value": {"x": 1},
        })
        result = tool_msg["content"]["result"]
        assert "Unable to store" in result
        mock_store.store.assert_not_called()

    def test_base_user_cannot_delete(self, tool, mock_store) -> None:
        tool_msg, _ = tool.execute({"action": "delete", "key": "my_data"})
        result = tool_msg["content"]["result"]
        assert "Unable to delete" in result
        mock_store.delete.assert_not_called()

    def test_power_user_can_store(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        qt.set_user("bob", "ws1", "power_user")
        tool_msg, _ = qt.execute({
            "action": "store",
            "key": "my_data",
            "value": {"x": 1},
        })
        result = tool_msg["content"]["result"]
        assert "Stored" in result
        mock_store.store.assert_called_once()

    def test_power_user_can_delete(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        qt.set_user("bob", "ws1", "power_user")
        tool_msg, _ = qt.execute({"action": "delete", "key": "my_data"})
        result = tool_msg["content"]["result"]
        assert "Deleted" in result
        mock_store.delete.assert_called_once()

    def test_admin_can_store(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        qt.set_user("carol", "ws1", "admin")
        tool_msg, _ = qt.execute({
            "action": "store",
            "key": "my_data",
            "value": {"x": 1},
        })
        result = tool_msg["content"]["result"]
        assert "Stored" in result


class TestActionDispatch:
    """Correct action handler is dispatched."""

    def test_query_unknown_key(self, mock_store) -> None:
        mock_store.query.return_value = None
        qt = QueryTool(mock_store)
        qt.set_user("alice", "ws1", "base_user")
        tool_msg, _ = qt.execute({"action": "query", "key": "nope"})
        assert "No data found" in tool_msg["content"]["result"]

    def test_store_without_value(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        qt.set_user("bob", "ws1", "power_user")
        tool_msg, _ = qt.execute({"action": "store", "key": "my_data"})
        assert "required" in tool_msg["content"]["result"].lower()

    def test_list_empty(self, mock_store) -> None:
        mock_store.list_keys.return_value = []
        qt = QueryTool(mock_store)
        qt.set_user("alice", "ws1", "base_user")
        tool_msg, _ = qt.execute({"action": "list", "key": "any"})
        assert "No data keys" in tool_msg["content"]["result"]

    def test_unknown_action(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        qt.set_user("alice", "ws1", "base_user")
        tool_msg, _ = qt.execute({"action": "destroy", "key": "x"})
        assert "Unknown action" in tool_msg["content"]["result"]


class TestToolDefinition:
    """QueryTool exposes a valid OpenAI tool definition."""

    def test_definition_structure(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        defn = qt.definition()
        assert defn["type"] == "function"
        assert defn["function"]["name"] == "query_data"
        params = defn["function"]["parameters"]
        assert "key" in params["properties"]
        assert "action" in params["properties"]
        assert "value" in params["properties"]
        assert params["required"] == ["key", "action"]

    def test_action_enum(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        defn = qt.definition()
        enum = defn["function"]["parameters"]["properties"]["action"]["enum"]
        assert set(enum) == {"query", "store", "list", "delete"}


class TestSetUser:
    """User context is set correctly."""

    def test_set_user_basic(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        qt.set_user("alice", "ws1", "base_user", ["beta_feature"])
        assert qt._username == "alice"
        assert qt._workspace_id == "ws1"
        assert qt._user_role == "base_user"
        assert qt._user_flags == ["beta_feature"]

    def test_set_user_defaults(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        qt.set_user("bob", "ws2")
        assert qt._username == "bob"
        assert qt._user_role == "base_user"
        assert qt._user_flags == []


class TestDenyMessages:
    """Denial messages never leak what exists."""

    def test_deny_is_generic(self, mock_store) -> None:
        qt = QueryTool(mock_store)
        qt.set_user("alice", "ws1", "base_user")
        # Store denied — message says "Unable to store", not "Forbidden" or "Insufficient role"
        msg, _ = qt.execute({"action": "store", "key": "x", "value": {"a": 1}})
        result = msg["content"]["result"]
        assert "forbidden" not in result.lower()
        assert "insufficient" not in result.lower()
        assert "role" not in result.lower()


class TestRoleNumber:
    """Role number mapping."""

    def test_valid_roles(self) -> None:
        assert _role_number("base_user") == 1
        assert _role_number("power_user") == 2
        assert _role_number("admin") == 3

    def test_unknown_role(self) -> None:
        assert _role_number("garbage") == 0

    def test_empty_role(self) -> None:
        assert _role_number("") == 0