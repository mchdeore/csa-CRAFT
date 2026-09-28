"""Dash application instance."""

import logging
from pathlib import Path

from dash import Dash

app = Dash(__name__, suppress_callback_exceptions=True)

# Write server logs to file so errors survive terminal clears and restarts
LOGS_PATH = Path(__file__).parent.parent / "logs"
LOGS_PATH.mkdir(exist_ok=True)

file_handler = logging.FileHandler(LOGS_PATH / "server.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
file_handler.setLevel(logging.DEBUG)

logging.getLogger().addHandler(file_handler)
logging.getLogger().setLevel(logging.DEBUG)
