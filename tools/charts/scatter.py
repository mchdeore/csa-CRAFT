"""Scatter chart tool."""

from typing import Any

from app.core.logging import log_function_call
from tools.charts._shared import CHART_COLORS, error_msg, rich_chart, success_msg


class ScatterChartTool:
    """Build a scatter plot from data points."""

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draw_scatter_chart",
                "description": (
                    "Draw an interactive scatter plot. "
                    "Pass one or more series of x,y points. "
                    "Use for correlations, distributions, and clusters."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Chart title displayed at the top.",
                        },
                        "series": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "Label for this data series in the legend.",
                                    },
                                    "points": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "x": {
                                                    "type": "number",
                                                    "description": "X coordinate.",
                                                },
                                                "y": {
                                                    "type": "number",
                                                    "description": "Y coordinate.",
                                                },
                                                "label": {
                                                    "type": "string",
                                                    "description": "Optional hover label.",
                                                },
                                            },
                                            "required": ["x", "y"],
                                        },
                                        "description": "Array of {x, y} point objects.",
                                    },
                                },
                                "required": ["name", "points"],
                            },
                            "description": "One or more data series of scatter points.",
                        },
                        "x_label": {
                            "type": "string",
                            "description": "Optional X-axis label.",
                        },
                        "y_label": {
                            "type": "string",
                            "description": "Optional Y-axis label.",
                        },
                        "trendline": {
                            "type": "boolean",
                            "description": "Add a linear trendline.",
                        },
                        "size_by": {
                            "type": "string",
                            "description": "Size markers by 'x', 'y', or 'none'.",
                        },
                    },
                    "required": ["title", "series"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        title = args.get("title", "Scatter Plot")
        series = args.get("series", [])
        x_label = args.get("x_label", "")
        y_label = args.get("y_label", "")
        trendline = args.get("trendline", False)
        size_by = args.get("size_by", "none")
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.charts.scatter",
            "execute",
            title=title,
            series_count=len(series),
            source="agent_or_route",
        )

        if not series:
            return error_msg(tool_call_id, "No series provided for scatter plot."), None
        for s in series:
            if "name" not in s or "points" not in s:
                return error_msg(tool_call_id, "Each series must have 'name' and 'points'."), None
            if not s["points"]:
                return error_msg(tool_call_id, f"Series '{s['name']}' has no points."), None

        figure = _build_scatter_figure(title, series, x_label, y_label, trendline, size_by)
        total_points = sum(len(s["points"]) for s in series)
        log_function_call(
            "tools.charts.scatter",
            "execute",
            step="complete",
            title=title,
            total_points=total_points,
        )
        return success_msg(tool_call_id, title, total_points), rich_chart(title, figure)


def _build_scatter_figure(
    title: str,
    series: list[dict],
    x_label: str,
    y_label: str,
    trendline: bool,
    size_by: str,
) -> dict[str, Any]:
    import plotly.graph_objects as go

    fig = go.Figure()

    for i, ser in enumerate(series):
        color = CHART_COLORS[i % len(CHART_COLORS)]
        points = ser["points"]
        xs = [p["x"] for p in points]
        ys = [p["y"] for p in points]
        labels = [p.get("label", "") for p in points]

        marker_size = 10
        if size_by == "x":
            marker_size = [max(5, min(30, abs(v) * 2)) for v in xs]
        elif size_by == "y":
            marker_size = [max(5, min(30, abs(v) * 2)) for v in ys]

        fig.add_trace(
            go.Scatter(
                x=xs,
                y=ys,
                mode="markers",
                name=ser["name"],
                marker=dict(
                    color=color,
                    size=marker_size,
                    opacity=0.7,
                    line=dict(width=1, color="white"),
                ),
                text=labels or None,
                hovertemplate="%{text}<br>x: %{x:,}<br>y: %{y:,}<extra></extra>"
                if any(labels)
                else "x: %{x:,}<br>y: %{y:,}<extra></extra>",
            )
        )

        if trendline and len(xs) >= 2:
            _add_trendline(fig, xs, ys, ser["name"], color)

    fig.update_layout(
        title=title,
        xaxis_title=x_label or "X",
        yaxis_title=y_label or "Y",
        height=500,
        margin=dict(l=40, r=20, t=50, b=40),
        hovermode="closest",
    )
    return fig.to_dict()


def _add_trendline(
    fig: Any,
    xs: list[float],
    ys: list[float],
    name: str,
    color: str,
) -> None:
    import plotly.graph_objects as go

    n = len(xs)
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xy = sum(x * y for x, y in zip(xs, ys, strict=True))
    sum_x2 = sum(x * x for x in xs)

    denominator = n * sum_x2 - sum_x * sum_x
    if denominator == 0:
        return

    slope = (n * sum_xy - sum_x * sum_y) / denominator
    intercept = (sum_y - slope * sum_x) / n

    x_min, x_max = min(xs), max(xs)
    fig.add_trace(
        go.Scatter(
            x=[x_min, x_max],
            y=[slope * x_min + intercept, slope * x_max + intercept],
            mode="lines",
            name=f"{name} trend",
            line=dict(color=color, dash="dash", width=1.5),
            showlegend=True,
        )
    )
