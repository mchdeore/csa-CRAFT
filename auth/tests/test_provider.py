"""Tests for InMemoryAuth — login, logout, user management."""

from typing import Any

import pytest
from flask import Flask

from auth.provider import DEFAULT_USERS, InMemoryAuth


# Fixture: a fully-wired Flask app with InMemoryAuth and custom users
@pytest.fixture
def app_with_users() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "test-secret"
    auth = InMemoryAuth({"alice": "secret123", "bob": "bobpass"})
    auth.init_app(app)
    app.extensions["auth"] = auth  # type: ignore[index]
    return app


# Fixture: a fully-wired Flask app with default users
@pytest.fixture
def app_with_defaults() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "test-secret"
    auth = InMemoryAuth()
    auth.init_app(app)
    app.extensions["auth"] = auth  # type: ignore[index]
    return app


class TestInit:
    def test_init_with_custom_users(self, app_with_users: Flask) -> None:
        auth: Any = app_with_users.extensions["auth"]
        with app_with_users.test_request_context():
            assert auth.try_login("alice", "secret123") is True

    def test_init_with_no_users_uses_defaults(self, app_with_defaults: Flask) -> None:
        auth: Any = app_with_defaults.extensions["auth"]
        with app_with_defaults.test_request_context():
            assert auth.try_login("user1", "1") is True
            assert auth.try_login("user2", "1") is True
            assert auth.try_login("user3", "1") is True


class TestInitApp:
    def test_init_app_returns_login_manager(self) -> None:
        from flask_login import LoginManager

        auth = InMemoryAuth()
        assert isinstance(auth.init_app(Flask(__name__)), LoginManager)


class TestTryLogin:
    def test_valid_credentials_return_true(self, app_with_users: Flask) -> None:
        auth: Any = app_with_users.extensions["auth"]
        with app_with_users.test_request_context():
            result = auth.try_login("alice", "secret123")
            assert result is True

    def test_wrong_password_returns_false(self, app_with_users: Flask) -> None:
        auth: Any = app_with_users.extensions["auth"]
        with app_with_users.test_request_context():
            result = auth.try_login("alice", "wrongpassword")
            assert result is False

    def test_nonexistent_user_returns_false(self, app_with_users: Flask) -> None:
        auth: Any = app_with_users.extensions["auth"]
        with app_with_users.test_request_context():
            result = auth.try_login("nonexistent", "anything")
            assert result is False


class TestDoLogout:
    def test_do_logout_does_not_crash(self, app_with_users: Flask) -> None:
        auth: Any = app_with_users.extensions["auth"]
        with app_with_users.test_request_context():
            # Login first so logout has something to clear
            auth.try_login("alice", "secret123")
            auth.do_logout()


class TestDefaultUsers:
    def test_default_users_contains_expected(self) -> None:
        assert "user1" in DEFAULT_USERS
        assert "user2" in DEFAULT_USERS
        assert "user3" in DEFAULT_USERS
        assert len(DEFAULT_USERS) == 3
        assert DEFAULT_USERS["user1"] == "1"
        assert DEFAULT_USERS["user2"] == "1"
        assert DEFAULT_USERS["user3"] == "1"
