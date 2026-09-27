"""Dictionary-based authentication."""

from config import VALID_USERS


class DictAuth:
    def authenticate(self, username: str, password: str) -> bool:
        return VALID_USERS.get(username) == password
