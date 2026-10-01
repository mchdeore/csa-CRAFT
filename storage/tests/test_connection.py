"""Tests for storage/database/connection.py — SQLite connection factory."""

import sqlite3
from pathlib import Path

import pytest

from storage.database.connection import create_connection


class TestCreateConnection:
    """Tests for create_connection() factory function."""

    def test_returns_sqlite_connection(self, tmp_path: Path) -> None:
        """Calling create_connection returns a sqlite3.Connection object."""
        db_path = tmp_path / "test.db"

        conn = create_connection(db_path)

        assert isinstance(conn, sqlite3.Connection)
        conn.close()

    def test_wal_mode_enabled(self, tmp_path: Path) -> None:
        """Connection PRAGMA journal_mode should return 'wal'."""
        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)

        row = conn.execute("PRAGMA journal_mode").fetchone()

        assert row[0] == "wal"
        conn.close()

    def test_foreign_keys_enabled(self, tmp_path: Path) -> None:
        """Connection PRAGMA foreign_keys should return 1 (ON)."""
        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)

        row = conn.execute("PRAGMA foreign_keys").fetchone()

        assert row[0] == 1
        conn.close()

    def test_creates_file_at_path(self, tmp_path: Path) -> None:
        """Given a db_path, the .db file is created on disk."""
        db_path = tmp_path / "mydata.db"

        assert not db_path.exists()

        conn = create_connection(db_path)
        conn.close()

        assert db_path.exists()

    def test_connection_is_reusable(self, tmp_path: Path) -> None:
        """Calling create_connection twice on the same path returns working connections."""
        db_path = tmp_path / "test.db"

        conn1 = create_connection(db_path)

        # Create a table through the first connection
        conn1.execute("CREATE TABLE fruits (name TEXT)")
        conn1.execute("INSERT INTO fruits VALUES ('apple')")
        conn1.commit()

        # Open a second connection to the same file
        conn2 = create_connection(db_path)
        row = conn2.execute("SELECT name FROM fruits").fetchone()

        assert row[0] == "apple"

        conn1.close()
        conn2.close()

    def test_custom_subdirectory(self, tmp_path: Path) -> None:
        """Path can include subdirectories that don't exist yet — SQLite creates them."""
        db_path = tmp_path / "nested" / "deep" / "store.db"

        conn = create_connection(db_path)
        conn.execute("CREATE TABLE t (x INTEGER)")
        conn.commit()
        conn.close()

        assert db_path.exists()