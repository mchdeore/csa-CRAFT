"""Chat message callback."""

from dash import Input, Output, State, no_update

from dash_app import app
from services import chat_provider, store


@app.callback(
    Output("session-store", "data", allow_duplicate=True),
    Output("chat-input", "value"),
    Input("send-btn", "n_clicks"),
    Input("chat-input", "n_submit"),
    State("chat-input", "value"),
    State("session-store", "data"),
    prevent_initial_call=True,
)
def handle_send(
    n_clicks: int | None, n_submit: int | None,
    message: str | None, session: dict,
) -> tuple:
    if not message or not message.strip():
        return no_update, no_update
    if not session.get("workspace_id"):
        return no_update, no_update
    session["messages"].append({"role": "user", "content": message.strip()})
    response = chat_provider.get_response(session["messages"])
    session["messages"].append({"role": "assistant", "content": response})
    store.save_messages(session["username"], session["workspace_id"], session["messages"])
    return session, ""
