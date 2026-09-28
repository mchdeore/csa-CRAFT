"""Authentication callbacks: login, logout, page rendering."""

from dash import Input, Output, State, html, no_update

from app.core.dash_app import app
from app.core.services import store
from auth.templates import build_login
from storage.templates import build_main


@app.callback(
    Output("page-content", "children"),
    Input("session-store", "data"),
)
def render_page(session: dict | None) -> html.Div:
    if not session or not session.get("logged_in"):
        return build_login()
    workspaces = store.list(session["username"])
    return build_main(session["username"], workspaces, session)


@app.callback(
    Output("session-store", "data", allow_duplicate=True),
    Output("login-error", "children"),
    Input("login-btn", "n_clicks"),
    Input("login-password", "n_submit"),
    State("login-username", "value"),
    State("login-password", "value"),
    State("session-store", "data"),
    prevent_initial_call=True,
)
def handle_login(
    n_clicks: int | None,
    n_submit: int | None,
    username: str | None,
    password: str | None,
    session: dict,
) -> tuple:
    if not n_clicks and not n_submit:
        return no_update, no_update

    # Call auth route
    client = app.server.test_client()
    resp = client.post(
        "/auth/login",
        json={"username": username or "", "password": password or ""},
    )
    data = resp.get_json() or {}

    if data.get("success"):
        session["logged_in"] = True
        session["username"] = username
        return session, ""
    return no_update, data.get("error", "Invalid username or password.")


@app.callback(
    Output("session-store", "data", allow_duplicate=True),
    Input("logout-btn", "n_clicks"),
    prevent_initial_call=True,
)
def handle_logout(n_clicks: int | None) -> object:
    if not n_clicks:
        return no_update

    client = app.server.test_client()
    client.post("/auth/logout")
    return {"logged_in": False, "username": "", "workspace_id": "", "messages": []}
