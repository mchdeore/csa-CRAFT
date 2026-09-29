"""Tests for SqliteDataStore — role-scoped query/store/list/delete."""

import importlib.util
import json
from pathlib import Path
from types import ModuleType

import pytest

# Load store.py directly to bypass storage/__init__.py which triggers
# the pydantic_ai dependency chain through chat provider imports.
_store_path = Path(__file__).parent.parent / "store.py"
_store_spec = importlib.util.spec_from_file_location("store", _store_path)
if _store_spec is None or _store_spec.loader is None:
    raise RuntimeError("Failed to load store.py spec")
_store_module = importlib.util.module_from_spec(_store_spec)
_store_spec.loader.exec_module(_store_module)

SqliteDataStore = _store_module.SqliteDataStore
_role_level = _store_module._role_level

# database package doesn't trigger storage/__init__.py — direct sub-package
from storage.database.connection import create_connection
from storage.database.runner import run_migrations


@pytest.fixture
def data_store(tmp_path):
    """Create a SqliteDataStore backed by a temp SQLite database.

    Uses a temp file so WAL mode works correctly. Seeds test users
    and global datasets for role-scoping tests.
    """
    db_path = tmp_path / "test_cheddar.db"
    conn = create_connection(db_path)
    run_migrations(conn)  # Uses default migrations dir

    # Seed test users directly
    conn.execute(
        "INSERT OR REPLACE INTO users (username, password_hash, role, division, region, flags, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        ("alice", "hash", "base_user", "Ops", "East", "[]", "2024-01-01"),
    )
    conn.execute(
        "INSERT OR REPLACE INTO users (username, password_hash, role, division, region, flags, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        ("bob", "hash", "power_user", "Finance", "West", "[]", "2024-01-01"),
    )
    conn.execute(
        "INSERT OR REPLACE INTO users (username, password_hash, role, division, region, flags, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        ("carol", "hash", "admin", "IT", "Global", "[]", "2024-01-01"),
    )
    conn.commit()

    # Seed global datasets
    conn.execute(
        "INSERT INTO global_datasets (name, description, min_role) VALUES (?, ?, ?)",
        ("public_stats", "Public stats anyone can see", "base_user"),
    )
    conn.execute(
        "INSERT INTO global_data_rows (dataset_id, data_json) VALUES (?, ?)",
        (1, json.dumps({"label": "Widgets", "value": 100})),
    )
    conn.execute(
        "INSERT INTO global_data_rows (dataset_id, data_json) VALUES (?, ?)",
        (1, json.dumps({"label": "Gadgets", "value": 200})),
    )

    conn.execute(
        "INSERT INTO global_datasets (name, description, min_role) VALUES (?, ?, ?)",
        ("internal_finance", "Finance only", "power_user"),
    )
    conn.execute(
        "INSERT INTO global_data_rows (dataset_id, data_json) VALUES (?, ?)",
        (2, json.dumps({"revenue": 5000})),
    )
    conn.commit()

    # Seed workspaces for admin cross-workspace tests
    conn.execute(
        "INSERT INTO workspaces (id, username, name, created_at, last_accessed) "
        "VALUES (?, ?, ?, ?, ?)",
        ("ws-alice", "alice", "Alice Workspace", "2024-01-01", "2024-01-01"),
    )
    conn.execute(
        "INSERT INTO workspaces (id, username, name, created_at, last_accessed) "
        "VALUES (?, ?, ?, ?, ?)",
        ("ws-bob", "bob", "Bob Workspace", "2024-01-01", "2024-01-01"),
    )
    conn.commit()

    store = SqliteDataStore(db_path)
    store._conn = conn
    return store


class TestUserDataCRUD:
    """Workspace-scoped user data store/query/delete."""

    def test_store_and_query(self, data_store) -> None:
        data_store.store("alice", "ws1", "my_notes", {"text": "hello"})
        result = data_store.query("alice", "ws1", "my_notes", "base_user")
        assert result == [{"text": "hello"}]

    def test_store_then_update(self, data_store) -> None:
        data_store.store("alice", "ws1", "counter", {"n": 1})
        data_store.store("alice", "ws1", "counter", {"n": 2})
        result = data_store.query("alice", "ws1", "counter", "base_user")
        assert result == [{"n": 2}]

    def test_query_unknown_key_returns_none(self, data_store) -> None:
        result = data_store.query("alice", "ws1", "no_such_key", "base_user")
        assert result is None

    def test_workspace_isolation(self, data_store) -> None:
        """Data in ws1 should not be visible in ws2."""
        data_store.store("alice", "ws1", "secret", {"value": "confidential"})
        result = data_store.query("alice", "ws2", "secret", "base_user")
        assert result is None

    def test_user_isolation(self, data_store) -> None:
        """Alice's data should not be visible to Bob."""
        data_store.store("alice", "ws1", "private", {"data": "alice_only"})
        result = data_store.query("bob", "ws1", "private", "power_user")
        assert result is None  # Different user

    def test_delete(self, data_store) -> None:
        data_store.store("alice", "ws1", "temp", {"x": 1})
        data_store.delete("alice", "ws1", "temp")
        result = data_store.query("alice", "ws1", "temp", "base_user")
        assert result is None

    def test_delete_only_own_data(self, data_store) -> None:
        """Delete should not affect other users' data."""
        data_store.store("alice", "ws1", "shared_key", {"owner": "alice"})
        data_store.store("bob", "ws1", "shared_key", {"owner": "bob"})
        data_store.delete("alice", "ws1", "shared_key")
        # Alice's is gone
        assert data_store.query("alice", "ws1", "shared_key", "base_user") is None
        # Bob's still exists
        assert data_store.query("bob", "ws1", "shared_key", "power_user") == [{"owner": "bob"}]


class TestListKeys:
    """list_keys returns scoped results."""

    def test_list_own_keys(self, data_store) -> None:
        data_store.store("alice", "ws1", "k1", {"v": 1})
        data_store.store("alice", "ws1", "k2", {"v": 2})
        keys = data_store.list_keys("alice", "ws1", "base_user")
        assert "k1" in keys
        assert "k2" in keys
        assert "public_stats" in keys  # Global dataset

    def test_list_keys_role_gated_global(self, data_store) -> None:
        """base_user should NOT see power_user-only datasets."""
        keys = data_store.list_keys("alice", "ws1", "base_user")
        assert "public_stats" in keys
        assert "internal_finance" not in keys  # Requires power_user

    def test_power_user_sees_elevated_datasets(self, data_store) -> None:
        """power_user should see their role-level datasets."""
        keys = data_store.list_keys("bob", "ws1", "power_user")
        assert "public_stats" in keys
        assert "internal_finance" in keys

    def test_admin_sees_all(self, data_store) -> None:
        """admin sees everything."""
        keys = data_store.list_keys("carol", "ws1", "admin")
        assert "public_stats" in keys
        assert "internal_finance" in keys


class TestGlobalDataAccess:
    """Global datasets are role-gated."""

    def test_base_user_queries_public_dataset(self, data_store) -> None:
        result = data_store.query("alice", "", "public_stats", "base_user")
        assert result is not None
        assert len(result) == 2
        assert result[0]["label"] == "Widgets"

    def test_base_user_cannot_query_power_dataset(self, data_store) -> None:
        result = data_store.query("alice", "", "internal_finance", "base_user")
        assert result is None  # Silent deny

    def test_power_user_can_query_elevated_dataset(self, data_store) -> None:
        result = data_store.query("bob", "", "internal_finance", "power_user")
        assert result is not None
        assert result[0]["revenue"] == 5000

    def test_admin_can_query_all(self, data_store) -> None:
        result = data_store.query("carol", "", "internal_finance", "admin")
        assert result is not None


class TestRoleHelpers:
    """Role utility functions."""

    def test_role_level_values(self) -> None:
        assert _role_level("base_user") == 1
        assert _role_level("power_user") == 2
        assert _role_level("admin") == 3
        assert _role_level("unknown") == 0

    def test_get_user_role(self, data_store) -> None:
        assert data_store.get_user_role("alice") == "base_user"
        assert data_store.get_user_role("bob") == "power_user"
        assert data_store.get_user_role("carol") == "admin"
        assert data_store.get_user_role("nobody") == "base_user"


class TestAllWorkspaces:
    """Admin cross-workspace access."""

    def test_base_user_sees_only_own_workspaces(self, data_store) -> None:
        workspaces = data_store.list_all_workspaces("alice", "base_user")
        assert len(workspaces) == 1
        assert workspaces[0]["id"] == "ws-alice"

    def test_admin_sees_all_workspaces(self, data_store) -> None:
        workspaces = data_store.list_all_workspaces("carol", "admin")
        assert len(workspaces) == 2