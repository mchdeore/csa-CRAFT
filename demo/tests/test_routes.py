"""Tests for demo/routes.py — Flask endpoints.

Routes tested: /demo/compare (distance engine), /demo/page (profile load).
The full Dash callbacks require the Dash app to be running; those are
skipped in this unit test file.
"""

import pytest
from flask import Flask

from demo.routes import register_routes


# Fixture: bare Flask app with demo routes registered
@pytest.fixture
def demo_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "test-secret"
    register_routes(app)
    return app


class TestDemoPageRoute:
    def test_get_returns_200(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.get("/demo")
            assert response.status_code == 200
            data = response.get_json()
            assert data["ok"] is True
            assert data["route"] == "/demo"

    def test_post_with_known_user_returns_profile(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post(
                "/demo/page",
                json={"username": "fredmoney"},
            )
            assert response.status_code == 200
            data = response.get_json()
            assert data["ok"] is True
            assert data["role"] == "finance"
            assert "display_name" in data
            assert "tools" in data
            assert isinstance(data["tools"], list)

    def test_post_with_unknown_user_falls_back_to_fredmoney(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post(
                "/demo/page",
                json={"username": "nobody"},
            )
            assert response.status_code == 200
            data = response.get_json()
            # Falls back to fredmoney profile
            assert data["role"] == "finance"

    def test_post_with_empty_body_falls_back_to_default(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post("/demo/page", json={})
            assert response.status_code == 200
            data = response.get_json()
            assert data["ok"] is True


class TestCompareRoute:
    def test_missing_extracted_fields_returns_400(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post(
                "/demo/compare",
                json={
                    "weight_order": ["mass_kg"],
                },
            )
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data

    def test_missing_weight_order_returns_400(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post(
                "/demo/compare",
                json={
                    "extracted_fields": {"mass_kg": 100},
                },
            )
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data

    def test_empty_body_returns_400(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post("/demo/compare", json={})
            assert response.status_code == 400


class TestComplianceRoute:
    def test_missing_extracted_fields_returns_400(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post("/demo/compliance", json={})
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data


class TestIngestRoute:
    def test_missing_contents_returns_400(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post(
                "/demo/ingest",
                json={"filename": "test.pdf"},
            )
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data

    def test_missing_filename_returns_400(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post(
                "/demo/ingest",
                json={"contents": "base64stuff"},
            )
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data


class TestRiskRegisterRoute:
    def test_missing_contents_returns_400(self, demo_app: Flask) -> None:
        with demo_app.test_client() as client:
            response = client.post("/demo/risk-register", json={})
            assert response.status_code == 400
            data = response.get_json()
            assert "error" in data