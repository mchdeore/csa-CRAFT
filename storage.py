"""JSON file workspace storage."""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from config import WORKSPACES_DIR


class JsonFileStore:
    def __init__(self) -> None:
        self.base_dir = WORKSPACES_DIR

    def _user_dir(self, username: str) -> Path:
        user_dir = self.base_dir / username
        user_dir.mkdir(parents=True, exist_ok=True)
        return user_dir

    def _workspace_path(self, username: str, workspace_id: str) -> Path:
        return self._user_dir(username) / f"{workspace_id}.json"

    def list(self, username: str) -> list[dict]:
        user_dir = self._user_dir(username)
        workspaces = []
        for ws_file in user_dir.glob("*.json"):
            workspaces.append(json.loads(ws_file.read_text()))
        workspaces.sort(key=lambda w: w.get("last_accessed", ""), reverse=True)
        return workspaces

    def load(self, username: str, workspace_id: str) -> dict | None:
        path = self._workspace_path(username, workspace_id)
        if not path.exists():
            return None
        return json.loads(path.read_text())

    def save(self, username: str, workspace: dict) -> None:
        path = self._workspace_path(username, workspace["id"])
        path.write_text(json.dumps(workspace, default=str))

    def create(self, username: str, name: str) -> dict:
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
        path = self._workspace_path(username, workspace_id)
        workspace = json.loads(path.read_text())
        workspace["messages"] = messages
        workspace["last_accessed"] = datetime.now(timezone.utc).isoformat()
        path.write_text(json.dumps(workspace, default=str))
