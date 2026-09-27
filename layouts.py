"""Dash UI builder functions."""

from dash import dcc, html


def build_login() -> html.Div:
    return html.Div(
        html.Div([
            html.H1("Cheddar Chat"),
            html.H3("Login"),
            dcc.Input(
                id="login-username", placeholder="Username", type="text",
                style={"width": "100%", "marginBottom": "10px", "padding": "8px"},
            ),
            dcc.Input(
                id="login-password", placeholder="Password", type="password",
                style={"width": "100%", "marginBottom": "10px", "padding": "8px"},
            ),
            html.Button("Log in", id="login-btn", style={"width": "100%", "padding": "8px"}),
            html.Div(id="login-error", style={"color": "red", "marginTop": "10px"}),
        ], style={
            "maxWidth": "350px", "margin": "80px auto",
            "padding": "30px", "border": "1px solid #ddd", "borderRadius": "8px",
        }),
    )


def build_message(role: str, content: str) -> html.Div:
    is_user = role == "user"
    return html.Div([
        html.Strong("You" if is_user else "Assistant"),
        html.P(content, style={"margin": "4px 0 0", "whiteSpace": "pre-wrap"}),
    ], style={
        "padding": "10px 14px", "margin": "6px 0", "borderRadius": "8px",
        "backgroundColor": "#e3f2fd" if is_user else "#f5f5f5",
        "maxWidth": "80%",
        "alignSelf": "flex-end" if is_user else "flex-start",
    })


def build_sidebar(username: str, workspaces: list[dict]) -> html.Div:
    ws_buttons = [
        html.Button(
            ws["name"], id={"type": "ws-btn", "index": ws["id"]},
            style={
                "display": "block", "width": "100%", "textAlign": "left",
                "padding": "8px", "margin": "4px 0", "cursor": "pointer",
                "border": "1px solid #ddd", "borderRadius": "4px", "backgroundColor": "#fff",
            },
        )
        for ws in workspaces
    ]
    return html.Div([
        html.H2("Cheddar Chat"),
        html.P(username, style={"color": "#666"}),
        html.Hr(),
        dcc.Input(
            id="new-ws-name", placeholder="New workspace name", type="text",
            style={"width": "100%", "marginBottom": "6px", "padding": "6px"},
        ),
        html.Button("Create", id="create-ws-btn", style={"width": "100%", "padding": "6px"}),
        html.Hr(),
        html.H4("Workspaces"),
        html.Div(ws_buttons, id="ws-list"),
        html.Hr(),
        html.Button("Logout", id="logout-btn", style={"width": "100%", "padding": "6px"}),
    ], style={
        "width": "280px", "padding": "20px",
        "borderRight": "1px solid #ddd", "overflowY": "auto", "flexShrink": "0",
    })


def build_chat_area(session: dict) -> html.Div:
    workspace_id = session.get("workspace_id", "")
    if not workspace_id:
        return html.Div(
            html.P("Select or create a workspace to start chatting.",
                   style={"color": "#999", "marginTop": "40px", "textAlign": "center"}),
            style={"flex": "1"},
        )
    messages = session.get("messages", [])
    msg_els = [build_message(m["role"], m["content"]) for m in messages]
    if not msg_els:
        msg_els = [html.P("No messages yet.", style={"color": "#999"})]
    return html.Div([
        build_chat_messages_panel(msg_els),
        build_chat_input_bar(),
        html.Div(id="scroll-trigger", style={"display": "none"}),
    ], style={"flex": "1", "display": "flex", "flexDirection": "column"})


def build_chat_messages_panel(msg_els: list) -> html.Div:
    return html.Div(
        msg_els, id="chat-messages",
        style={
            "flex": "1", "overflowY": "auto", "padding": "20px",
            "display": "flex", "flexDirection": "column",
        },
    )


def build_chat_input_bar() -> html.Div:
    return html.Div([
        dcc.Input(
            id="chat-input", placeholder="Type a message...", type="text",
            style={"flex": "1", "padding": "10px"}, debounce=False,
        ),
        html.Button("Send", id="send-btn", style={"padding": "10px 20px", "marginLeft": "8px"}),
    ], style={"display": "flex", "padding": "10px", "borderTop": "1px solid #ddd"})


def build_main(username: str, workspaces: list[dict], session: dict) -> html.Div:
    return html.Div([
        build_sidebar(username, workspaces),
        build_chat_area(session),
    ], style={"display": "flex", "height": "100vh"})
