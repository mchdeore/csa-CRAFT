"""Box plot chart tool."""

from typing import Any

from app.core.logging import log_function_call
from tools.charts._shared import CHART_COLORS, error_msg, rich_chart, success_msg


class BoxPlotTool:
    """Build an interactive box plot from grouped numeric values."""

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draw_box_plot",
                "description": (
                    "Draw an interactive box plot. "
                    "Pass groups with labels and value arrays. "
                    "Use for comparing distributions, identifying "
                    "medians, quartiles, and outliers."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Chart title displayed at the top.",
                        },
                        "groups": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "Group label for the legend and x-axis.",
                                    },
                                    "values": {
                                        "type": "array",
                                        "items": {"type": "number"},
                                        "description": "Numeric values for this group.",
                                    },
                                },
                                "required": ["name", "values"],
                            },
                            "description": (
                                "Array of groups. Each group has a name and "
                                "a list of numeric values."
                            ),
                        },
                        "y_label": {
                            "type": "string",
                            "description": "Optional Y-axis label.",
                        },
                        "show_points": {
                            "type": "boolean",
                            "description": (
                                "If true, overlay individual data points "
                                "as jittered dots on top of boxes."
                            ),
                        },
                        "horizontal": {
                            "type": "boolean",
                            "description": "If true, draw horizontal boxes instead of vertical.",
                        },
                    },
                    "required": ["title", "groups"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        title = args.get("title", "Box Plot")
        groups = args.get("groups", [])
        y_label = args.get("y_label", "")
        show_points = args.get("show_points", False)
        horizontal = args.get("horizontal", False)
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.charts.boxplot",
            "execute",
            title=title,
            group_count=len(groups),
            source="agent_or_route",
        )

        # Validation
        if not groups:
            return error_msg(tool_call_id, "No groups provided for box plot."), None
        for g in groups:
            if "name" not in g or "values" not in g:
                return error_msg(
                    tool_call_id, "Each group must have 'name' and 'values'."
                ), None
            if not g["values"]:
                return error_msg(
                    tool_call_id, f"Group '{g.get('name', '?')}' has no values."
                ), None

        figure = _build_boxplot_figure(title, groups, y_label, show_points, horizontal)
        total_values = sum(len(g["values"]) for g in groups)
        log_function_call(
            "tools.charts.boxplot", "execute", step="complete", title=title,
        )
        return success_msg(tool_call_id, title, total_values), rich_chart(title, figure)


def _build_boxplot_figure(
    title: str,
    groups: list[dict],
    y_label: str,
    show_points: bool,
    horizontal: bool,
) -> dict[str, Any]:
    """Build a Plotly box plot figure dict.

    Returns the figure as a dict via to_dict() for JSON serialization.

    >>> groups = [{"name": "Control", "values": [1, 2, 3, 4, 5]}, {"name": "Test", "values": [3, 4, 5, 6, 7]}]
    >>> fig = _build_boxplot_figure("Comparison", groups, "Value", False, False)
    >>> isinstance(fig, dict)
    True
    >>> "data" in fig
    True
    >>> fig["layout"]["title"]["text"]
    'Comparison'
    """
    import plotly.graph_objects as go

    fig = go.Figure()

    boxpoints_setting = "all" if show_points else False

    for i, group in enumerate(groups):
        color = CHART_COLORS[i % len(CHART_COLORS)]

        if horizontal:
            fig.add_trace(
                go.Box(
                    x=group["values"],
                    name=group["name"],
                    orientation="h",
                    marker_color=color,
                    boxpoints=boxpoints_setting,
                    jitter=0.3 if show_points else 0,
                    hovertemplate=(
                        "%{x}<br>Group: %{y}<extra></extra>"
                    ),
                )
            )
        else:
            fig.add_trace(
                go.Box(
                    y=group["values"],
                    name=group["name"],
                    marker_color=color,
                    boxpoints=boxpoints_setting,
                    jitter=0.3 if show_points else 0,
                    hovertemplate=(
                        "Group: %{x}<br>%{y}<extra></extra>"
                    ),
                )
            )

    if horizontal:
        fig.update_layout(
            title=title,
            xaxis_title=y_label or "Value",
            height=max(350, len(groups) * 60 + 150),
            margin=dict(l=40, r=20, t=50, b=40),
        )
    else:
        fig.update_layout(
            title=title,
            yaxis_title=y_label or "Value",
            height=450,
            margin=dict(l=40, r=20, t=50, b=40),
        )

    return fig.to_dict()