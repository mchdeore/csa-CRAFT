"""Tests for app entry point — server, layout, configuration."""

from types import ModuleType

import pytest
from dash import html
from flask import Flask


# Import the app entry module — this runs the full app setup
@pytest.fixture(scope="module")
def entry_module() -> ModuleType:
    """Import app.entry once per test module."""
    import app.entry as entry

    return entry


class TestServer:
    def test_server_is_flask_app(self, entry_module: ModuleType) -> None:
        assert isinstance(entry_module.server, Flask)

    def test_secret_key_is_set(self, entry_module: ModuleType) -> None:
        assert entry_module.server.secret_key is not None
        assert len(entry_module.server.secret_key) > 0


class TestLayout:
    def test_make_layout_returns_html_div(self, entry_module: ModuleType) -> None:
        layout = entry_module.make_layout()
        assert isinstance(layout, html.Div)

    def test_layout_has_session_store(self, entry_module: ModuleType) -> None:
        layout = entry_module.make_layout()
        children = layout.children

        # First child should be the session store
        from dash import dcc

        assert len(children) >= 1
        assert isinstance(children[0], dcc.Store)
        assert children[0].id == "session-store"

    def test_layout_has_page_content_div(self, entry_module: ModuleType) -> None:
        layout = entry_module.make_layout()
        children = layout.children

        # Should have a page-content div
        page_divs = [
            c
            for c in children
            if isinstance(c, html.Div) and getattr(c, "id", "") == "page-content"
        ]
        assert len(page_divs) == 1
