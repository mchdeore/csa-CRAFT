"""Cheddar Chat — entry point."""

from app.entry import *  # noqa: F401, F403

if __name__ == "__main__":
    from app.core.dash_app import app

    app.run(debug=True)
