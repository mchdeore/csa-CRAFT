"""Cheddar Chat — Dash app entry point."""

from dash import Input, Output, dcc, html

from dash_app import app

server = app.server

app.layout = html.Div([
    dcc.Store(id="session-store", storage_type="session", data={
        "logged_in": False, "username": "", "workspace_id": "", "messages": [],
    }),
    html.Div(id="page-content"),
])

app.clientside_callback(
    """function(children) {
        var el = document.getElementById('chat-messages');
        if (el) setTimeout(function() { el.scrollTop = el.scrollHeight; }, 50);
        return '';
    }""",
    Output("scroll-trigger", "children"),
    Input("chat-messages", "children"),
)

import callbacks  # noqa: E402, F401

if __name__ == "__main__":
    app.run(debug=True)
