"""Main page layout."""

from dash import dcc, html


def make_layout() -> html.Div:
    return html.Div(
        [
            dcc.Store(
                id="session-store",
                storage_type="session",
                data={
                    "logged_in": False,
                    "username": "",
                    "workspace_id": "",
                    "messages": [],
                },
            ),
            html.Div(id="page-content"),
            html.Div(id="demo-page-content"),
        ]
    )
