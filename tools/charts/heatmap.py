"""Heatmap chart tool."""

import math
from typing import Any

from app.core.logging import log_function_call
from tools.charts._shared import CHART_COLORS, error_msg, rich_chart, success_msg


class HeatmapTool:
    """Build an interactive heatmap from a 2D grid of values."""

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draw_heatmap",
                "description": (
                    "Draw an interactive heatmap. "
                    "Pass row labels, column labels, and a 2D grid of values. "
                    "Use for correlation matrices, frequency grids, intensity maps."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Chart title displayed at the top.",
                        },
                        "rows": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Labels for each row (y-axis).",
                        },
                        "cols": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Labels for each column (x-axis).",
                        },
                        "values": {
                            "type": "array",
                            "items": {
                                "type": "array",
                                "items": {"type": "number"},
                            },
                            "description": (
                                "2D grid of numbers. values[row_index][col_index]. "
                                "Must have same number of rows as row labels, "
                                "and each row must match column count."
                            ),
                        },
                        "x_label": {
                            "type": "string",
                            "description": "Optional X-axis label.",
                        },
                        "y_label": {
                            "type": "string",
                            "description": "Optional Y-axis label.",
                        },
                        "colorscale": {
                            "type": "string",
                            "description": (
                                "Color scale name. Options: viridis, rdbu, blues, "
                                "greens, reds, ylorrd, plasma, grays. Default: viridis."
                            ),
                        },
                    },
                    "required": ["title", "rows", "cols", "values"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        title = args.get("title", "Heatmap")
        rows = args.get("rows", [])
        cols = args.get("cols", [])
        values = args.get("values", [])
        x_label = args.get("x_label", "")
        y_label = args.get("y_label", "")
        colorscale = args.get("colorscale", "viridis")
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.charts.heatmap",
            "execute",
            title=title,
            row_count=len(rows),
            col_count=len(cols),
            source="agent_or_route",
        )

        # Validate the 2D grid
        error = _validate_heatmap(rows, cols, values)
        if error:
            return error_msg(tool_call_id, error), None

        figure = _build_heatmap_figure(title, rows, cols, values, x_label, y_label, colorscale)
        cell_count = len(rows) * len(cols)
        log_function_call(
            "tools.charts.heatmap", "execute", step="complete", title=title, cells=cell_count,
        )
        return success_msg(tool_call_id, title, cell_count), rich_chart(title, figure)


def _validate_heatmap(
    rows: list[str],
    cols: list[str],
    values: list[list],
) -> str | None:
    """Check that the 2D values grid matches row and column counts."""
    if not rows:
        return "No row labels provided for heatmap."
    if not cols:
        return "No column labels provided for heatmap."
    if not values:
        return "No values provided for heatmap."
    if len(values) != len(rows):
        return (
            f"Heatmap has {len(rows)} row labels but {len(values)} rows of values. "
            "They must match."
        )
    for i, row_vals in enumerate(values):
        if len(row_vals) != len(cols):
            return (
                f"Row {i} ('{rows[i]}') has {len(row_vals)} values "
                f"but there are {len(cols)} columns. They must match."
            )
    return None


def _build_heatmap_figure(
    title: str,
    rows: list[str],
    cols: list[str],
    values: list[list],
    x_label: str,
    y_label: str,
    colorscale: str,
) -> dict[str, Any]:
    """Build a Plotly heatmap figure from a 2D grid."""
    import plotly.graph_objects as go

    # Validate colorscale name, default to viridis
    valid_scales = {
        "viridis", "rdbu", "blues", "greens", "reds",
        "ylorrd", "plasma", "grays", "ylgnbu", "picnic",
        "portland", "blackbody", "earth", "electric", "hot",
    }
    if colorscale not in valid_scales:
        colorscale = "viridis"

    fig = go.Figure(
        data=[
            go.Heatmap(
                z=values,
                x=cols,
                y=rows,
                colorscale=colorscale,
                hovertemplate=(
                    "row: %{y}<br>col: %{x}<br>value: %{z:,}<extra></extra>"
                ),
                colorbar=dict(title=""),
            )
        ]
    )

    fig.update_layout(
        title=title,
        xaxis_title=x_label or "",
        yaxis_title=y_label or "",
        height=max(400, len(rows) * 30 + 150),
        margin=dict(l=60, r=40, t=50, b=60),
    )

    return fig.to_dict()