"""Tests for SqliteStore — workspace CRUD, message persistence, edge cases."""

from collections.abc import Generator
from pathlib import Path

import pytest

from storage.store import SqliteStore


# Fixture: fresh SqliteStore on a temp database for every test
@pytest.fixture
def store(tmp_path: Path) -> Generator[SqliteStore, None, None]:
    db_path = tmp_path / "test.db"
    s = SqliteStore(db_path)
    # Create users so FK constraints pass
    now = "2024-01-01T00:00:00+00:00"
    s._conn.execute(
        "INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)",
        ("alice", "hash_alice", now),
    )
    s._conn.execute(
        "INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)",
        ("bob", "hash_bob", now),
    )
    s._conn.commit()
    yield s
    import os

    s._conn.close()
    # Remove WAL/SHM sidecars if they exist
    for suffix in ["", "-wal", "-shm"]:
        f = str(db_path) + suffix if suffix else str(db_path)
        if os.path.exists(f):
            os.remove(f)


class TestCreate:
    def test_create_workspace_has_required_fields(self, store: SqliteStore) -> None:
        ws = store.create("alice", "My Workspace")

        assert ws["id"] != ""
        assert ws["name"] == "My Workspace"
        assert ws["created_at"] != ""
        assert ws["last_accessed"] != ""
        assert ws["messages"] == []

    def test_create_then_load_returns_same_data(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Test Space")
        loaded = store.load("alice", ws["id"])

        assert loaded is not None
        assert loaded["id"] == ws["id"]
        assert loaded["name"] == ws["name"]
        assert loaded["created_at"] == ws["created_at"]
        assert loaded["messages"] == []

    def test_create_multiple_workspaces(self, store: SqliteStore) -> None:
        ws1 = store.create("alice", "First")
        ws2 = store.create("alice", "Second")

        assert ws1["id"] != ws2["id"]

    def test_create_worksapces_for_different_users(self, store: SqliteStore) -> None:
        ws1 = store.create("alice", "Alice's Space")
        ws2 = store.create("bob", "Bob's Space")

        # Each user can only see their own workspaces
        alice_spaces = store.list("alice")
        bob_spaces = store.list("bob")

        assert len(alice_spaces) == 1
        assert len(bob_spaces) == 1
        assert alice_spaces[0]["id"] == ws1["id"]
        assert bob_spaces[0]["id"] == ws2["id"]


class TestSaveMessages:
    def test_save_and_load_text_messages(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Chat")
        messages = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"},
        ]
        store.save_messages("alice", ws["id"], messages)

        loaded = store.load("alice", ws["id"])
        assert loaded is not None
        assert len(loaded["messages"]) == 2
        assert loaded["messages"][0] == messages[0]
        assert loaded["messages"][1] == messages[1]

    def test_save_and_load_dict_messages_roundtrip(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Charts")
        messages = [
            {"role": "user", "content": "Show me a chart"},
            {
                "role": "assistant",
                "content": {
                    "type": "chart",
                    "data": [{"x": 1, "y": 2}, {"x": 3, "y": 4}],
                    "layout": {"title": "My Chart"},
                },
            },
        ]
        store.save_messages("alice", ws["id"], messages)

        loaded = store.load("alice", ws["id"])
        assert loaded is not None
        assert len(loaded["messages"]) == 2
        assert loaded["messages"][0] == messages[0]
        # Dict content should round-trip through JSON serialization
        assert loaded["messages"][1] == messages[1]

    def test_save_messages_replaces_existing(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Chat")
        original = [{"role": "user", "content": "First message"}]
        store.save_messages("alice", ws["id"], original)

        # Replace with new messages
        replacement = [{"role": "user", "content": "Second message"}]
        store.save_messages("alice", ws["id"], replacement)

        loaded = store.load("alice", ws["id"])
        assert loaded is not None
        assert len(loaded["messages"]) == 1
        assert loaded["messages"][0] == replacement[0]

    def test_save_empty_messages_list(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Chat")
        store.save_messages(
            "alice",
            ws["id"],
            [
                {"role": "user", "content": "Something"},
            ],
        )
        # Overwrite with empty
        store.save_messages("alice", ws["id"], [])

        loaded = store.load("alice", ws["id"])
        assert loaded is not None
        assert loaded["messages"] == []


class TestList:
    def test_list_sorted_by_last_accessed_desc(self, store: SqliteStore) -> None:
        # Create in order A, B, C — then update B so it becomes most recent
        store.create("alice", "A")
        ws_b = store.create("alice", "B")
        store.create("alice", "C")

        # Touch B by saving a message, which bumps last_accessed
        store.save_messages("alice", ws_b["id"], [{"role": "user", "content": "ping"}])

        results = store.list("alice")
        ids = [ws["id"] for ws in results]

        assert ids[0] == ws_b["id"], "Most recently touched workspace should be first"

    def test_list_returns_empty_for_new_user(self, store: SqliteStore) -> None:
        results = store.list("nobody")
        assert results == []


class TestLoad:
    def test_load_nonexistent_workspace_returns_none(self, store: SqliteStore) -> None:
        result = store.load("alice", "nonexistent-id")
        assert result is None

    def test_load_wrong_user_returns_none(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Secret")
        # Bob tries to load Alice's workspace
        result = store.load("bob", ws["id"])
        assert result is None


class TestSave:
    def test_save_creates_then_updates(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Original Name")

        # Update name and re-save
        ws["name"] = "Updated Name"
        store.save("alice", ws)

        loaded = store.load("alice", ws["id"])
        assert loaded is not None
        assert loaded["name"] == "Updated Name"

    def test_save_preserves_messages(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Chat")
        store.save_messages(
            "alice",
            ws["id"],
            [
                {"role": "user", "content": "Hello"},
            ],
        )

        # Reload, modify name, save — messages should survive
        reloaded = store.load("alice", ws["id"])
        assert reloaded is not None
        reloaded["name"] = "Renamed"
        store.save("alice", reloaded)

        loaded = store.load("alice", reloaded["id"])
        assert loaded is not None
        assert loaded["name"] == "Renamed"
        assert len(loaded["messages"]) == 1
        assert loaded["messages"][0]["content"] == "Hello"

    def test_save_with_non_string_content(self, store: SqliteStore) -> None:
        ws = store.create("alice", "Numbers")
        ws["messages"] = [{"role": "user", "content": 42}]
        store.save("alice", ws)

        loaded = store.load("alice", ws["id"])
        assert loaded is not None
        assert loaded["messages"][0]["content"] == "42"
