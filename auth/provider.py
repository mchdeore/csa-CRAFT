"""In-memory authentication backed by flask-login.

Users are stored in memory at runtime and seeded into the SQLite database
so that role, flags, and profile fields are available to the data store layer
during tool execution and data scoping.
"""

from dataclasses import dataclass, field

from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.core.logging import log_function_call

# Default users when no config provided — base_user with no flags
DEFAULT_USERS: dict[str, str] = {"demo": "demo"}


# flask-login User model
@dataclass
class User(UserMixin):
    id: str
    password_hash: str
    division: str = ""
    region: str = ""
    role: str = "base_user"
    flags: list[str] = field(default_factory=list)


class InMemoryAuth:
    """Authentication backed by an in-memory dict of users with hashed passwords.

    Roles are escalated: base_user < power_user < admin.
    Flags are for experimental feature gates only — not permissions.
    """

    def __init__(self, users: dict[str, str | dict] | None = None) -> None:
        raw: dict[str, str | dict] = users if users is not None else dict(DEFAULT_USERS)
        self._users: dict[str, User] = {}
        for username, profile in raw.items():
            if isinstance(profile, dict):
                password = profile.get("password", "")
                division = profile.get("division", "")
                region = profile.get("region", "")
                role = profile.get("role", "base_user")
                flags = profile.get("flags", [])
            else:
                password = profile
                division = ""
                region = ""
                role = "base_user"
                flags = []
            self._users[username] = User(
                id=username,
                password_hash=generate_password_hash(password),
                division=str(division),
                region=str(region),
                role=str(role),
                flags=list(flags),
            )

    def init_app(self, flask_app: Flask) -> LoginManager:
        log_function_call("auth.provider", "init_app", user_count=len(self._users))
        manager = LoginManager()
        manager.init_app(flask_app)

        @manager.user_loader
        def load_user(user_id: str) -> User | None:
            return self._users.get(user_id)

        return manager

    def try_login(self, username: str, password: str) -> bool:
        log_function_call("auth.provider", "try_login", username=username)
        user = self._users.get(username)
        if user is None:
            log_function_call("auth.provider", "try_login", step="failed", reason="unknown_user")
            return False
        if not check_password_hash(user.password_hash, password):
            log_function_call("auth.provider", "try_login", step="failed", reason="bad_password")
            return False
        login_user(user)
        log_function_call("auth.provider", "try_login", step="success", username=username)
        return True

    def do_logout(self) -> None:
        log_function_call("auth.provider", "do_logout")
        logout_user()
