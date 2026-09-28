"""Authentication UI templates."""

from dash import dcc, html

_CARD_STYLE = {
    "maxWidth": "350px",
    "margin": "80px auto",
    "padding": "30px",
    "border": "1px solid #ddd",
    "borderRadius": "8px",
}


def _login_inputs() -> list:
    return [
        html.H1("Cheddar Chat"),
        html.H3("Login"),
        dcc.Input(
            id="login-username",
            placeholder="Username",
            type="text",
            style={"width": "100%", "marginBottom": "10px", "padding": "8px"},
        ),
        dcc.Input(
            id="login-password",
            placeholder="Password",
            type="password",
            style={"width": "100%", "marginBottom": "10px", "padding": "8px"},
        ),
        html.Button(
            "Log in",
            id="login-btn",
            style={"width": "100%", "padding": "8px"},
        ),
        html.Div(id="login-error", style={"color": "red", "marginTop": "10px"}),
    ]


def build_login() -> html.Div:
    return html.Div(html.Div(_login_inputs(), style=_CARD_STYLE))
