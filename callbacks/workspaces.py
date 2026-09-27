"""Workspace management callbacks."""

from dash import ALL, Input, Output, State, ctx, no_update

from dash_app import app
from services import store


@app.callback(
    Output("session-store", "data", allow_duplicate=True),
    Input("create-ws-btn", "n_clicks"),
    State("new-ws-name", "value"),
    State("session-store", "data"),
    prevent_initial_call=True,
)
def handle_create_workspace(
    n_clicks: int | None, name: str | None, session: dict,
) -> object:
    if not n_clicks or not name or not name.strip():
        return no_update
    workspace = store.create(session["username"], name.strip())
    session["workspace_id"] = workspace["id"]
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
    loaded = store.load(session["username"], triggered["index"])
    if loaded is None:
        return no_update
    session["workspace_id"] = loaded["id"]
    session["messages"] = loaded.get("messages", [])
    return session
