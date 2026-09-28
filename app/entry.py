"""Dash app entry point — server setup, layout, clientside callbacks."""

from dash import Input, Output

from app.core.dash_app import app
from app.core.logging import get_structured_logger, register_middleware
from app.core.routes import register_all
from app.core.services import auth
from app.templates import make_layout

server = app.server
server.secret_key = "cheddar-dev-secret-key-change-in-production"

# Initialize structured JSON logging before anything else touches the app
get_structured_logger()

auth.init_app(server)
register_all(server)
register_middleware(server)

app.layout = make_layout()

app.clientside_callback(
    """function(children) {
        var el = document.getElementById('chat-messages');
        if (el) setTimeout(function() { el.scrollTop = el.scrollHeight; }, 50);
        return '';
    }""",
    Output("scroll-trigger", "children"),
    Input("chat-messages", "children"),
)

import auth.callbacks  # noqa: E402, F401
import chat.callbacks  # noqa: E402, F401
import storage.callbacks  # noqa: E402, F401

if __name__ == "__main__":
    app.run(debug=True)
