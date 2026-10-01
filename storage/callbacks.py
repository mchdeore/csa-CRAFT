"""Workspace management callbacks."""

import os

from dash import ALL, Input, Output, State, ctx, no_update

from app.core.dash_app import app
from app.core.logging import log_function_call


def _internal_headers() -> dict[str, str]:
    return {
        "X-Internal-Secret": os.environ.get(
            "INTERNAL_API_SECRET", "cheddar-internal-dev"
        )
    }


@app.callback(
    Output("session-store", "data", allow_duplicate=True),
    Input("create-ws-btn", "n_clicks"),
    State("new-ws-name", "value"),
    State("session-store", "data"),
    prevent_initial_call=True,
)
def handle_create_workspace(
    n_clicks: int | None,
    name: str | None,
    session: dict,
) -> object:
    if not n_clicks or not name or not name.strip():
        return no_update

    log_function_call(
        "storage.callbacks",
        "handle_create_workspace",
        username=session.get("username", ""),
        name=name,
        cause="user_request",
    )
    client = app.server.test_client()
    resp = client.post(
        "/storage/create",
        json={"username": session["username"], "name": name.strip()},
        headers=_internal_headers(),
    )
    data = resp.get_json() or {}

    if "id" not in data:
        return no_update

    session["workspace_id"] = data["id"]
    session["messages"] = []
    return session


@app.callback(
    Output("session-store", "data", allow_duplicate=True),
    Input({"type": "ws-btn", "index": ALL}, "n_clicks"),
    State("session-store", "data"),
    prevent_initial_call=True,
)
def handle_select_workspace(n_clicks_list: list, session: dict) -> object:
    if not any(n_clicks_list):
        return no_update
    triggered = ctx.triggered_id
    if not triggered:
        return no_update

    log_function_call(
        "storage.callbacks",
        "handle_select_workspace",
        username=session.get("username", ""),
        workspace_id=triggered.get("index", ""),
        cause="user_request",
    )
    client = app.server.test_client()
    resp = client.get(
        f"/storage/load/{session['username']}/{triggered['index']}",
        headers=_internal_headers(),
    )
    data = resp.get_json() or {}

    if "id" not in data:
        return no_update

    session["workspace_id"] = data["id"]
    session["messages"] = data.get("messages", [])
    return session
