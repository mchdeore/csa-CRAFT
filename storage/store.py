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
        """Seed default users from auth config into the database.

        Reads auth.DEFAULT_USERS and parses the dict format manually
        (avoids importing auth.provider.InMemoryAuth, which is internal).

        The DEFAULT_USERS dict uses either:
          - {"username": "password"}  (simple string)
          - {"username": {"password": ..., "role": ..., "division": ...,
              "region": ..., "flags": [...]}}  (dict)
        """
        from auth import DEFAULT_USERS

        now = datetime.now(timezone.utc).isoformat()
        with self._conn:
            for username, profile in DEFAULT_USERS.items():
                # Check if user already exists
                existing = self._conn.execute(
                    "SELECT username FROM users WHERE username=?",
                    (username,),
                ).fetchone()
                if existing:
                    # User exists — update role/flags if they were added later
                    if isinstance(profile, dict):
                        role = profile.get("role", "base_user")
                        division = profile.get("division", "")
                        region = profile.get("region", "")
                        flags_json = json.dumps(profile.get("flags", []))
                        self._conn.execute(
                            "UPDATE users SET role=?, division=?, region=?, flags=? "
                            "WHERE username=? AND role='base_user' AND flags='[]'",
                            (role, division, region, flags_json, username),
                        )
                    continue

                # New user — insert with all fields
                if isinstance(profile, dict):
                    from werkzeug.security import generate_password_hash

                    password = profile.get("password", "")
                    role = profile.get("role", "base_user")
                    division = profile.get("division", "")
                    region = profile.get("region", "")
                    flags_json = json.dumps(profile.get("flags", []))
                else:
                    from werkzeug.security import generate_password_hash

                    password = profile
                    role = "base_user"
                    division = ""
                    region = ""
                    flags_json = "[]"

                self._conn.execute(
                    "INSERT OR IGNORE INTO users "
                    "(username, password_hash, role, division, region, flags, created_at) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (
                        username,
                        generate_password_hash(password),
                        role,
                        division,
                        region,
                        flags_json,
                        now,
                    ),
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


# ---------------------------------------------------------------------------
# Role levels for escalated permission checks
# ---------------------------------------------------------------------------

_ROLE_LEVEL = {
    "base_user": 1,
    "power_user": 2,
    "admin": 3,
}


def _role_level(role: str) -> int:
    """Return the numeric level for a role string. Unknown roles get 0."""
    return _ROLE_LEVEL.get(role, 0)


# ---------------------------------------------------------------------------
# SqliteDataStore — unified data access with role-based scoping
# ---------------------------------------------------------------------------


class SqliteDataStore:
    """Unified query/store for user data, profile fields, and global datasets.

    Every method accepts username + workspace_id + user_role so the calling
    tool can pass the current user's context. Data is scoped automatically:

      - base_user sees own workspace data + public datasets
      - admin sees all workspaces, all users, all datasets

    The calling code (QueryTool) is responsible for passing the correct
    user context — this store trusts the caller to have already checked
    permissions at the route gate layer.
    """

    def __init__(self, db_path: Path | None = None) -> None:
        self.db_path = db_path or Path("app/database/cheddar.db")
        self._conn = create_connection(self.db_path)

    # -- Query --------------------------------------------------------------

    def query(
        self, username: str, workspace_id: str, key: str, user_role: str
    ) -> list[dict] | None:
        """Resolve a key against three namespaces, scoped by role.

        1. Workspace user_data — scoped to this username + workspace_id
        2. User profile metadata — scoped to this username (admin can cross-read)
        3. Global datasets — gated by min_role on the dataset

        Returns None if key not found or user lacks access. Never leaks
        what exists beyond the user's scope.
        """
        # 1. Workspace-scoped user data
        row = self._conn.execute(
            "SELECT value FROM user_data WHERE username=? AND workspace_id=? AND key=?",
            (username, workspace_id, key),
        ).fetchone()
        if row:
            return [json.loads(row["value"])]

        # 2. User profile metadata
        # Admin can query other users' profiles with key format "profile:<target_username>"
        if user_role == "admin" and key.startswith("profile:"):
            target = key.split(":", 1)[1]
            row = self._conn.execute(
                "SELECT metadata_json FROM user_profiles WHERE username=?",
                (target,),
            ).fetchone()
            if row:
                return json.loads(row["metadata_json"])
        else:
            row = self._conn.execute(
                "SELECT metadata_json FROM user_profiles WHERE username=?",
                (username,),
            ).fetchone()
            if row:
                metadata = json.loads(row["metadata_json"])
                if key in metadata:
                    return metadata[key]

        # 3. Global datasets — role-gated
        dataset = self._conn.execute(
            "SELECT id, min_role FROM global_datasets WHERE name=?",
            (key,),
        ).fetchone()
        if dataset:
            if _role_level(user_role) < _role_level(dataset["min_role"]):
                return None  # Silent deny — user doesn't know this dataset exists
            rows = self._conn.execute(
                "SELECT data_json FROM global_data_rows WHERE dataset_id=?",
                (dataset["id"],),
            ).fetchall()
            return [json.loads(r["data_json"]) for r in rows]

        return None

    # -- Store --------------------------------------------------------------

    def store(self, username: str, workspace_id: str, key: str, value: dict) -> None:
        """Upsert a key-value pair into the user's workspace-scoped data.

        Only writes to user_data table — global datasets are read-only
        through the tool. Caller must check role before invoking.
        """
        now = datetime.now(timezone.utc).isoformat()
        value_json = json.dumps(value)
        with self._conn:
            self._conn.execute(
                """INSERT INTO user_data
                   (username, workspace_id, key, value, created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ON CONFLICT(username, workspace_id, key) DO UPDATE SET
                   value=excluded.value, updated_at=excluded.updated_at""",
                (username, workspace_id, key, value_json, now, now),
            )

    # -- List keys -----------------------------------------------------------

    def list_keys(self, username: str, workspace_id: str, user_role: str) -> list[str]:
        """Return all keys accessible to this user.

        Includes: their own user_data keys + global dataset names their
        role can access.
        """
        keys: list[str] = []

        # User data keys
        rows = self._conn.execute(
            "SELECT key FROM user_data WHERE username=? AND workspace_id=?",
            (username, workspace_id),
        ).fetchall()
        keys.extend(r["key"] for r in rows)

        # Global dataset names the user's role can access
        role_num = _role_level(user_role)
        rows = self._conn.execute("SELECT name, min_role FROM global_datasets").fetchall()
        for r in rows:
            if role_num >= _role_level(r["min_role"]):
                keys.append(r["name"])

        return keys

    # -- Delete --------------------------------------------------------------

    def delete(self, username: str, workspace_id: str, key: str) -> None:
        """Remove a key from the user's workspace-scoped data.

        Only removes from user_data — global datasets and profiles are
        not user-deletable through this tool.
        """
        with self._conn:
            self._conn.execute(
                "DELETE FROM user_data WHERE username=? AND workspace_id=? AND key=?",
                (username, workspace_id, key),
            )

    # -- Admin: cross-workspace access ---------------------------------------

    def list_all_workspaces(self, username: str, user_role: str) -> list[dict]:
        """List workspaces — admin sees all, others see only their own."""
        if user_role == "admin":
            rows = self._conn.execute(
                "SELECT * FROM workspaces ORDER BY last_accessed DESC"
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT * FROM workspaces WHERE username=? ORDER BY last_accessed DESC",
                (username,),
            ).fetchall()
        return [dict(r) for r in rows]

    # -- User profile helpers ------------------------------------------------

    def get_user_role(self, username: str) -> str:
        """Read the role column from the users table."""
        row = self._conn.execute(
            "SELECT role FROM users WHERE username=?",
            (username,),
        ).fetchone()
        return row["role"] if row else "base_user"

    def get_user_flags(self, username: str) -> list[str]:
        """Read the flags column from the users table, parsed from JSON."""
        row = self._conn.execute(
            "SELECT flags FROM users WHERE username=?",
            (username,),
        ).fetchone()
        if row and row["flags"]:
            try:
                return json.loads(row["flags"])
            except json.JSONDecodeError:
                pass
        return []
