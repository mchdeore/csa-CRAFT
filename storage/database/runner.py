"""Migration runner — discovers and applies numbered .sql files."""

import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def run_migrations(conn: sqlite3.Connection, migrations_dir: Path | None = None) -> None:
    if migrations_dir is None:
        migrations_dir = Path(__file__).parent / "migrations"

    current = _current_version(conn)
    migration_files = sorted(f for f in migrations_dir.glob("*.sql") if f.name[0].isdigit())

    for sql_file in migration_files:
        version = int(sql_file.name.split("_")[0])
        if version <= current:
            continue
        sql = sql_file.read_text()
        conn.executescript(sql)
        conn.execute(
            "INSERT INTO schema_version (version, applied_at) VALUES (?, ?)",
            (version, datetime.now(timezone.utc).isoformat()),
        )
        conn.commit()


def _current_version(conn: sqlite3.Connection) -> int:
    conn.execute(
        "CREATE TABLE IF NOT EXISTS schema_version "
        "(version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL)"
    )
    row = conn.execute("SELECT MAX(version) as v FROM schema_version").fetchone()
    return row["v"] if row and row["v"] is not None else 0
