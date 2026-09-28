"""SQLite-backed workspace storage with WAL mode and proper indexing."""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from app.core.logging import log_function_call
from storage.database.connection import create_connection
from storage.database.runner import run_migrations


class SqliteStore:
    def __init__(self, db_path: Path | None = None) -> None:
        self.db_path = db_path or Path("app/database/cheddar.db")
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = create_connection(self.db_path)
        run_migrations(self._conn)
        self._seed_users()

    def _seed_users(self) -> None:
        from werkzeug.security import generate_password_hash

        from auth import DEFAULT_USERS

        now = datetime.now(timezone.utc).isoformat()
        with self._conn:
            for username, password in DEFAULT_USERS.items():
                self._conn.execute(
                    "INSERT OR IGNORE INTO users (username, password_hash, created_at) "
                    "VALUES (?, ?, ?)",
                    (username, generate_password_hash(password), now),
                )

    def list(self, username: str) -> list[dict]:
        log_function_call("storage.store", "list", username=username)
        rows = self._conn.execute(
            "SELECT * FROM workspaces WHERE username = ? ORDER BY last_accessed DESC",
            (username,),
        ).fetchall()
        result = []
        for row in rows:
            ws = dict(row)
            msg_rows = self._conn.execute(
                "SELECT role, content, content_json FROM messages "
                "WHERE workspace_id = ? ORDER BY id",
                (ws["id"],),
            ).fetchall()
            ws["messages"] = []
            for r in msg_rows:
                msg = {"role": r["role"], "content": r["content"]}
                if r["content_json"]:
                    try:
                        msg["content"] = json.loads(r["content_json"])
                    except json.JSONDecodeError:
                        pass
                ws["messages"].append(msg)
            result.append(ws)
        return result

    def load(self, username: str, workspace_id: str) -> dict | None:
        row = self._conn.execute(
            "SELECT * FROM workspaces WHERE id = ? AND username = ?",
            (workspace_id, username),
        ).fetchone()
        if row is None:
            log_function_call(
                "storage.store", "load", username=username, workspace_id=workspace_id, found=False
            )
            return None
        ws = dict(row)
        msg_rows = self._conn.execute(
            "SELECT role, content, content_json FROM messages WHERE workspace_id = ? ORDER BY id",
            (ws["id"],),
        ).fetchall()
        ws["messages"] = []
        for r in msg_rows:
            msg = {"role": r["role"], "content": r["content"]}
            if r["content_json"]:
                try:
                    msg["content"] = json.loads(r["content_json"])
                except json.JSONDecodeError:
                    pass
            ws["messages"].append(msg)
        return ws

    def save(self, username: str, workspace: dict) -> None:
        now = datetime.now(timezone.utc).isoformat()

        log_function_call(
            "storage.store",
            "save",
            username=username,
            workspace_id=workspace.get("id", "unknown"),
            message_count=len(workspace.get("messages", [])),
        )

        with self._conn:
            self._conn.execute(
                """INSERT INTO workspaces (id, username, name, created_at, last_accessed)
                   VALUES (?, ?, ?, ?, ?)
                   ON CONFLICT(id) DO UPDATE SET
                   name=excluded.name, last_accessed=excluded.last_accessed""",
                (
                    workspace["id"],
                    username,
                    workspace["name"],
                    workspace.get("created_at", now),
                    now,
                ),
            )
            self._conn.execute("DELETE FROM messages WHERE workspace_id = ?", (workspace["id"],))
            for msg in workspace.get("messages", []):
                content = msg["content"]
                content_json = None
                if isinstance(content, dict):
                    content_json = json.dumps(content)
                    content = json.dumps(content)
                elif not isinstance(content, str):
                    content = str(content)
                self._conn.execute(
                    "INSERT INTO messages (workspace_id, role, content, content_json) "
                    "VALUES (?, ?, ?, ?)",
                    (workspace["id"], msg["role"], content, content_json),
                )

    def create(self, username: str, name: str) -> dict:
        log_function_call("storage.store", "create", username=username, name=name)
        now = datetime.now(timezone.utc).isoformat()
        workspace = {
            "id": str(uuid.uuid4()),
            "name": name,
            "created_at": now,
            "last_accessed": now,
            "messages": [],
        }
        self.save(username, workspace)
        return workspace

    def save_messages(self, username: str, workspace_id: str, messages: list[dict]) -> None:
        log_function_call(
            "storage.store",
            "save_messages",
            username=username,
            workspace_id=workspace_id,
            message_count=len(messages),
        )
        now = datetime.now(timezone.utc).isoformat()
        with self._conn:
            self._conn.execute(
                "UPDATE workspaces SET last_accessed = ? WHERE id = ? AND username = ?",
                (now, workspace_id, username),
            )
            self._conn.execute("DELETE FROM messages WHERE workspace_id = ?", (workspace_id,))
            for msg in messages:
                content = msg["content"]
                content_json = None
                if isinstance(content, dict):
                    content_json = json.dumps(content)
                    content = json.dumps(content)
                elif not isinstance(content, str):
                    content = str(content)
                self._conn.execute(
                    "INSERT INTO messages (workspace_id, role, content, content_json) "
                    "VALUES (?, ?, ?, ?)",
                    (workspace_id, msg["role"], content, content_json),
                )
