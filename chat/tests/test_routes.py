"""Tests for chat/routes.py — send_message, upload_file endpoints.

These are lightweight tests because the routes depend on the full
provider stack (Azure OpenAI, SQLite, tools). We test error handling.
"""

import pytest
from flask import Flask

from chat.routes import register_routes


# Fixture: bare Flask app with chat routes registered, no real backend
@pytest.fixture
def chat_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "test-secret"
    register_routes(app)
    return app


class TestSendMessage:
    def test_missing_username_returns_400(self, chat_app: Flask) -> None:
        with chat_app.test_client() as client:
            response = client.post(
                "/chat/send",
                json={
                    "workspace_id": "ws-1",
                    "message": "Hello",
                },
            )
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data
            assert "username" in data["error"]

    def test_missing_workspace_id_returns_400(self, chat_app: Flask) -> None:
        with chat_app.test_client() as client:
            response = client.post(
                "/chat/send",
                json={
                    "username": "alice",
                    "message": "Hello",
                },
            )
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data

    def test_missing_message_returns_400(self, chat_app: Flask) -> None:
        with chat_app.test_client() as client:
            response = client.post(
                "/chat/send",
                json={
                    "username": "alice",
                    "workspace_id": "ws-1",
                    "message": "",
                },
            )
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data

    def test_whitespace_only_message_returns_400(self, chat_app: Flask) -> None:
        with chat_app.test_client() as client:
            response = client.post(
                "/chat/send",
                json={
                    "username": "alice",
                    "workspace_id": "ws-1",
                    "message": "   ",
                },
            )
            assert response.status_code == 400

    def test_empty_body_returns_400(self, chat_app: Flask) -> None:
        with chat_app.test_client() as client:
            response = client.post("/chat/send", json={})
            assert response.status_code == 400


class TestUploadFile:
    def test_missing_file_id_returns_400(self, chat_app: Flask) -> None:
        with chat_app.test_client() as client:
            response = client.post(
                "/chat/upload",
                json={
                    "columns": ["A", "B"],
                    "rows": [[1, 2]],
                },
            )
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data
            assert "file_id" in data["error"]

    def test_empty_body_returns_400(self, chat_app: Flask) -> None:
        with chat_app.test_client() as client:
            response = client.post("/chat/upload", json={})
            assert response.status_code == 400