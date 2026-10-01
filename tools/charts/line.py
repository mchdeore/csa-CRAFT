"""Line chart tool."""

from typing import Any

from app.core.logging import log_function_call
from tools.charts._shared import CHART_COLORS, error_msg, rich_chart, success_msg


class LineChartTool:
    """Build an interactive line chart from ordered series."""

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draw_line_chart",
                "description": (
                    "Draw an interactive line chart. "
                    "Pass x values and one or more y-value series. "
                    "Use for time series, trends, cumulative curves."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Chart title displayed at the top.",
                        },
                        "x_values": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "X-axis values (labels, dates, or numbers).",
                        },
                        "series": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "Label for this series in the legend.",
                                    },
                                    "y_values": {
                                        "type": "array",
                                        "items": {"type": "number"},
                                        "description": "Y values, same length as x_values.",
                                    },
                                },
                                "required": ["name", "y_values"],
                            },
                            "description": "One or more data series to plot as lines.",
                        },
                        "x_label": {
                            "type": "string",
                            "description": "Optional X-axis label.",
                        },
                        "y_label": {
                            "type": "string",
                            "description": "Optional Y-axis label.",
                        },
                        "fill": {
                            "type": "boolean",
                            "description": "If true, fill area under lines.",
                        },
                        "x_is_date": {
                            "type": "boolean",
                            "description": "If true, format x-axis as dates.",
                        },
                        "markers": {
                            "type": "boolean",
                            "description": "If true, show dots at data points. Default: true.",
                        },
                    },
                    "required": ["title", "x_values", "series"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        title = args.get("title", "Line Chart")
        x_values = args.get("x_values", [])
        series = args.get("series", [])
        x_label = args.get("x_label", "")
        y_label = args.get("y_label", "")
        fill = args.get("fill", False)
        x_is_date = args.get("x_is_date", False)
        markers = args.get("markers", True)
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.charts.line",
            "execute",
            title=title,
            point_count=len(x_values),
            series_count=len(series),
            source="agent_or_route",
        )

        # Validation
        if not x_values:
            return error_msg(tool_call_id, "No x_values provided for line chart."), None
        if not series:
            return error_msg(tool_call_id, "No series provided for line chart."), None
        for ser in series:
            if "name" not in ser or "y_values" not in ser:
                return error_msg(
                    tool_call_id, "Each series must have 'name' and 'y_values'."
                ), None
            if len(ser["y_values"]) != len(x_values):
                return error_msg(
                    tool_call_id,
                    f"Series '{ser['name']}' has {len(ser['y_values'])} y-values "
                    f"but there are {len(x_values)} x-values. They must match.",
                ), None

        figure = _build_line_figure(
            title, x_values, series, x_label, y_label, fill, x_is_date, markers,
        )
        log_function_call(
            "tools.charts.line", "execute", step="complete", title=title,
        )
        return success_msg(tool_call_id, title, len(x_values)), rich_chart(title, figure)


def _build_line_figure(
    title: str,
    x_values: list,
    series: list[dict],
    x_label: str,
    y_label: str,
    fill: bool,
    x_is_date: bool,
    markers: bool,
) -> dict[str, Any]:
    """Build a Plotly line chart figure dict.

    Returns the figure as a dict via to_dict() for JSON serialization.

    >>> series = [{"name": "Sales", "y_values": [100, 200, 300]}]
    >>> fig = _build_line_figure("Revenue", ["Q1", "Q2", "Q3"], series, "Quarter", "USD", False, False, True)
    >>> isinstance(fig, dict)
    True
    >>> "data" in fig
    True
    >>> fig["layout"]["title"]["text"]
    'Revenue'
    """
    import plotly.graph_objects as go

    fig = go.Figure()

    line_mode = "lines+markers" if markers else "lines"

    for i, ser in enumerate(series):
        color = CHART_COLORS[i % len(CHART_COLORS)]

        trace_kwargs = {
            "x": x_values,
            "y": ser["y_values"],
            "mode": line_mode,
            "name": ser["name"],
            "line": dict(color=color, width=2),
        }

        if markers:
            trace_kwargs["marker"] = dict(size=5, color=color)

        if fill:
            trace_kwargs["fill"] = "tozeroy"
            trace_kwargs["fillcolor"] = f"rgba({_hex_to_rgba(color, 0.15)})"

        fig.add_trace(go.Scatter(**trace_kwargs))

    fig.update_layout(
        title=title,
        xaxis_title=x_label or "",
        yaxis_title=y_label or "",
        height=450,
        margin=dict(l=40, r=20, t=50, b=40),
        hovermode="x unified",
    )

    # Format x-axis as dates if requested
    if x_is_date:
        fig.update_xaxes(type="date")

    return fig.to_dict()


def _hex_to_rgba(hex_color: str, alpha: float) -> str:
    """Convert hex color like '#3b82f6' to rgba like '59, 130, 246, 0.15'."""
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"{r}, {g}, {b}, {alpha}"