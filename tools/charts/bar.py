"""Bar chart tool."""

from typing import Any

from app.core.logging import log_function_call
from tools.charts._shared import (
    CHART_COLORS,
    error_msg,
    rich_chart,
    success_msg,
    validate_categories_and_series,
)


class BarChartTool:
    """Build a bar chart from categories and values."""

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draw_bar_chart",
                "description": (
                    "Draw an interactive bar chart. "
                    "Pass categories (labels) and one or more value series. "
                    "Use for comparisons, rankings, frequency counts."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Chart title displayed at the top.",
                        },
                        "categories": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "X-axis labels, one per bar group.",
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
                                    "values": {
                                        "type": "array",
                                        "items": {"type": "number"},
                                        "description": "Numeric values, same length as categories.",
                                    },
                                },
                                "required": ["name", "values"],
                            },
                            "description": "One or more data series to plot as grouped bars.",
                        },
                        "x_label": {
                            "type": "string",
                            "description": "Optional X-axis label.",
                        },
                        "y_label": {
                            "type": "string",
                            "description": "Optional Y-axis label.",
                        },
                        "horizontal": {
                            "type": "boolean",
                            "description": "If true, draw horizontal bars instead of vertical.",
                        },
                    },
                    "required": ["title", "categories", "series"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        title = args.get("title", "Bar Chart")
        categories = args.get("categories", [])
        series = args.get("series", [])
        x_label = args.get("x_label", "")
        y_label = args.get("y_label", "")
        horizontal = args.get("horizontal", False)
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.charts.bar",
            "execute",
            title=title,
            cat_count=len(categories),
            source="agent_or_route",
        )

        err = validate_categories_and_series(categories, series, "bar")
        if err:
            return error_msg(tool_call_id, err), None

        figure = _build_bar_figure(title, categories, series, x_label, y_label, horizontal)
        log_function_call("tools.charts.bar", "execute", step="complete", title=title)
        return success_msg(tool_call_id, title, len(categories)), rich_chart(title, figure)


def _build_bar_figure(
    title: str,
    categories: list[str],
    series: list[dict],
    x_label: str,
    y_label: str,
    horizontal: bool,
) -> dict[str, Any]:
    import plotly.graph_objects as go

    fig = go.Figure()

    for i, ser in enumerate(series):
        color = CHART_COLORS[i % len(CHART_COLORS)]
        orientation = "h" if horizontal else "v"

        fig.add_trace(
            go.Bar(
                name=ser["name"],
                x=ser["values"] if horizontal else categories,
                y=categories if horizontal else ser["values"],
                orientation=orientation,
                marker_color=color,
                text=ser["values"],
                textposition="outside",
                texttemplate="%{text:,}",
            )
        )

    if horizontal:
        fig.update_layout(
            title=title,
            xaxis_title=y_label or "Value",
            yaxis_title=x_label or "Category",
            height=max(400, len(categories) * 40 + 150),
            margin=dict(l=40, r=20, t=50, b=40),
            barmode="group",
            hovermode="x unified",
        )
    else:
        fig.update_layout(
            title=title,
            xaxis_title=x_label or "Category",
            yaxis_title=y_label or "Value",
            height=450,
            margin=dict(l=40, r=20, t=50, b=40),
            barmode="group",
            hovermode="x unified",
        )

    return fig.to_dict()
