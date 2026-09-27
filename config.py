"""App settings and constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

WORKSPACES_DIR = Path(__file__).parent / "workspaces"
VALID_USERS: dict[str, str] = {"user1": "1", "user2": "1", "user3": "1"}
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")
SYSTEM_PROMPT = "You are a helpful assistant."
