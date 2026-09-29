"""
Demo Quick runner — starts the Dash app with demo routes registered.

Usage: python -m demo.runner
Or via alias: demo-run (from pyproject.toml [project.scripts])
"""

import os
import sys

# Add project root to path so imports work
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.dash_app import app
from app.core.routes import register_all
from app.templates import make_layout

# Register all routes (includes auth, chat, storage, tools, AND demo)
register_all(app.server)

# Set Dash layout
app.layout = make_layout()


def main():
    """Start the demo Dash server on port 8050."""
    print("=" * 60)
    print("  CSA Cheddar — Demo Quick")
    print("  Starting on http://localhost:8050")
    print("=" * 60)
    print()
    print("  Demo users:")
    print("    fredmoney / 1    — Finance (CADRe + Comparison)")
    print("    joemotochar / 1   — Engineer (Compliance + Diff)")
    print("    murphyslipz / 1   — Risk (Register + Correlation)")
    print()

    app.run(debug=True, host="0.0.0.0", port=8050)


if __name__ == "__main__":
    main()