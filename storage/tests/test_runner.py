"""Tests for storage/database/runner.py — migration discovery and idempotent apply."""

import sqlite3
from pathlib import Path

import pytest

from storage.database.connection import create_connection
from storage.database.runner import run_migrations


class TestMigrationDiscovery:
    """Tests for how run_migrations discovers and sorts .sql files."""

    def test_discovers_numbered_sql_files(self, tmp_path: Path) -> None:
        """Only .sql files whose names start with a digit are discovered."""
        migrations_dir = tmp_path / "migrations"
        migrations_dir.mkdir()

        (migrations_dir / "001_first.sql").write_text(
            "CREATE TABLE IF NOT EXISTS discovered (id INTEGER);"
        )
        (migrations_dir / "notes.txt").write_text("not a migration")
        (migrations_dir / "no_number.sql").write_text("CREATE TABLE ignored;")

        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)
        run_migrations(conn, migrations_dir)

        # Only the numbered .sql file should have been applied
        row = conn.execute(
            "SELECT version FROM schema_version ORDER BY version"
        ).fetchone()

        assert row is not None
        assert row["version"] == 1

        # Check the table from the migration was created
        conn.execute("SELECT id FROM discovered")

        conn.close()

    def test_files_sorted_by_number_prefix(self, tmp_path: Path) -> None:
        """Migration files are applied in numeric order, not alphabetical."""
        migrations_dir = tmp_path / "migrations"
        migrations_dir.mkdir()

        # Create files in a deliberately unsorted order
        (migrations_dir / "010_last.sql").write_text(
            "CREATE TABLE IF NOT EXISTS step_three (value TEXT);"
        )
        (migrations_dir / "001_first.sql").write_text(
            "CREATE TABLE IF NOT EXISTS step_one (value TEXT);"
        )
        (migrations_dir / "002_second.sql").write_text(
            "CREATE TABLE IF NOT EXISTS step_two (value TEXT);"
        )

        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)
        run_migrations(conn, migrations_dir)

        # All three versions should be recorded in order
        versions = conn.execute(
            "SELECT version FROM schema_version ORDER BY version"
        ).fetchall()

        assert [v["version"] for v in versions] == [1, 2, 10]

        # All tables exist
        conn.execute("SELECT value FROM step_one")
        conn.execute("SELECT value FROM step_two")
        conn.execute("SELECT value FROM step_three")

        conn.close()

    def test_ignores_non_sql_files_in_directory(self, tmp_path: Path) -> None:
        """Files without .sql extension are ignored even if they start with a digit."""
        migrations_dir = tmp_path / "migrations"
        migrations_dir.mkdir()

        (migrations_dir / "001_real.sql").write_text(
            "CREATE TABLE IF NOT EXISTS real_table (x INTEGER);"
        )
        (migrations_dir / "002_garbage.txt").write_text("DROP TABLE real_table; -- not sql")

        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)
        run_migrations(conn, migrations_dir)

        # Only one migration applied
        row = conn.execute(
            "SELECT MAX(version) as v FROM schema_version"
        ).fetchone()

        assert row["v"] == 1

        conn.close()


class TestMigrationApply:
    """Tests for the actual application of migrations."""

    def test_running_inserts_into_schema_version(self, tmp_path: Path) -> None:
        """After applying a migration, a row is inserted into schema_version."""
        migrations_dir = tmp_path / "migrations"
        migrations_dir.mkdir()
        (migrations_dir / "001_init.sql").write_text(
            "CREATE TABLE IF NOT EXISTS accounts (name TEXT);"
        )

        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)
        run_migrations(conn, migrations_dir)

        row = conn.execute(
            "SELECT version, applied_at FROM schema_version WHERE version = 1"
        ).fetchone()

        assert row is not None
        assert row["version"] == 1
        assert row["applied_at"] != ""

        conn.close()

    def test_rerun_is_idempotent(self, tmp_path: Path) -> None:
        """Running migrations twice on the same database applies nothing the second time."""
        migrations_dir = tmp_path / "migrations"
        migrations_dir.mkdir()
        (migrations_dir / "001_init.sql").write_text(
            "CREATE TABLE IF NOT EXISTS items (name TEXT);"
        )

        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)

        # First run
        run_migrations(conn, migrations_dir)

        # Capture the number of rows after first run
        count_before = conn.execute("SELECT COUNT(*) as c FROM schema_version").fetchone()["c"]

        # Second run should do nothing
        run_migrations(conn, migrations_dir)
        count_after = conn.execute("SELECT COUNT(*) as c FROM schema_version").fetchone()["c"]

        assert count_before == count_after

        conn.close()

    def test_schema_version_table_exists_after_first_run(self, tmp_path: Path) -> None:
        """After calling run_migrations once, schema_version table is present."""
        migrations_dir = tmp_path / "migrations"
        migrations_dir.mkdir()
        (migrations_dir / "001_init.sql").write_text(
            "CREATE TABLE IF NOT EXISTS widgets (id INTEGER);"
        )

        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)

        # Verify table does NOT exist before running
        row = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='schema_version'"
        ).fetchone()
        assert row is None

        run_migrations(conn, migrations_dir)

        # Now it should exist
        row = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='schema_version'"
        ).fetchone()
        assert row is not None

        conn.close()

    def test_empty_migrations_dir_does_nothing(self, tmp_path: Path) -> None:
        """An empty migrations directory creates only the schema_version table."""
        migrations_dir = tmp_path / "migrations"
        migrations_dir.mkdir()

        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)
        run_migrations(conn, migrations_dir)

        count = conn.execute("SELECT COUNT(*) as c FROM schema_version").fetchone()["c"]

        assert count == 0
        conn.close()

    def test_skips_already_applied_versions(self, tmp_path: Path) -> None:
        """Migrations with version <= current max are not re-applied."""
        migrations_dir = tmp_path / "migrations"
        migrations_dir.mkdir()

        (migrations_dir / "001_first.sql").write_text(
            "CREATE TABLE IF NOT EXISTS a (x INTEGER);"
        )
        (migrations_dir / "002_second.sql").write_text(
            "CREATE TABLE IF NOT EXISTS b (x INTEGER);"
        )

        db_path = tmp_path / "test.db"
        conn = create_connection(db_path)

        # Manually insert version 2 to simulate it already being applied
        conn.execute(
            "CREATE TABLE IF NOT EXISTS schema_version "
            "(version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL)"
        )
        conn.execute(
            "INSERT INTO schema_version (version, applied_at) VALUES (?, ?)",
            (2, "2024-01-01T00:00:00+00:00"),
        )
        conn.commit()

        # Running should skip both (001 <= 2 and 002 <= 2)
        run_migrations(conn, migrations_dir)

        count = conn.execute("SELECT COUNT(*) as c FROM schema_version").fetchone()["c"]

        assert count == 1

        # Table 'a' from 001 should NOT exist since we skipped it
        row = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='a'"
        ).fetchone()

        assert row is None

        conn.close()