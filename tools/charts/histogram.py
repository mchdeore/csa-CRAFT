"""Histogram chart tool."""

import math
from typing import Any

from app.core.logging import log_function_call
from tools.charts._shared import CHART_COLORS, error_msg, rich_chart, success_msg


class HistogramTool:
    """Build an interactive histogram from a list of numeric values."""

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draw_histogram",
                "description": (
                    "Draw an interactive histogram. "
                    "Pass a flat list of numbers. "
                    "Use for distribution analysis, outlier detection, "
                    "and seeing data shape."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Chart title displayed at the top.",
                        },
                        "values": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "Flat list of numeric values to histogram.",
                        },
                        "num_bins": {
                            "type": "integer",
                            "description": (
                                "Number of bins. Auto-computed using Sturges' rule "
                                "if not provided."
                            ),
                        },
                        "x_label": {
                            "type": "string",
                            "description": "Optional X-axis label.",
                        },
                        "show_curve": {
                            "type": "boolean",
                            "description": (
                                "If true, overlay a normal distribution curve "
                                "computed from the data mean and standard deviation."
                            ),
                        },
                        "opacity": {
                            "type": "number",
                            "description": "Bar opacity from 0.3 to 1.0. Default 0.7.",
                        },
                    },
                    "required": ["title", "values"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        title = args.get("title", "Histogram")
        values = args.get("values", [])
        num_bins = args.get("num_bins")
        x_label = args.get("x_label", "")
        show_curve = args.get("show_curve", False)
        opacity = args.get("opacity", 0.7)
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.charts.histogram",
            "execute",
            title=title,
            value_count=len(values),
            source="agent_or_route",
        )

        if not values:
            return error_msg(tool_call_id, "No values provided for histogram."), None
        if num_bins is not None and num_bins < 1:
            return error_msg(tool_call_id, "num_bins must be at least 1."), None
        if opacity < 0.3 or opacity > 1.0:
            return error_msg(tool_call_id, "opacity must be between 0.3 and 1.0."), None

        # Auto-compute bins using Sturges' rule if not provided
        if num_bins is None:
            num_bins = _sturges_bin_count(values)

        figure = _build_histogram_figure(title, values, num_bins, x_label, show_curve, opacity)
        log_function_call(
            "tools.charts.histogram", "execute", step="complete",
            title=title, bins=num_bins,
        )
        return success_msg(tool_call_id, title, len(values)), rich_chart(title, figure)


def _sturges_bin_count(values: list[float]) -> int:
    """Compute optimal bin count using Sturges' rule: ceil(log2(n) + 1)."""
    n = len(values)
    if n < 2:
        return 5
    return max(5, math.ceil(math.log2(n) + 1))


def _build_histogram_figure(
    title: str,
    values: list[float],
    num_bins: int,
    x_label: str,
    show_curve: bool,
    opacity: float,
) -> dict[str, Any]:
    """Build a Plotly histogram figure dict with optional normal curve overlay.

    Returns the figure as a dict via to_dict() for JSON serialization.

    >>> fig = _build_histogram_figure("Distribution", [1.0, 2.0, 3.0, 4.0, 5.0], 5, "Value", False, 0.7)
    >>> isinstance(fig, dict)
    True
    >>> "data" in fig
    True
    >>> fig["layout"]["title"]["text"]
    'Distribution'
    """
    import plotly.graph_objects as go

    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=values,
            nbinsx=num_bins,
            opacity=opacity,
            marker_color=CHART_COLORS[0],
            name="Data",
            hovertemplate="Range: %{x}<br>Count: %{y}<extra></extra>",
        )
    )

    # Overlay normal distribution curve
    if show_curve and len(values) >= 2:
        _add_normal_curve(fig, values, num_bins)

    fig.update_layout(
        title=title,
        xaxis_title=x_label or "Value",
        yaxis_title="Frequency",
        height=450,
        margin=dict(l=40, r=20, t=50, b=40),
        bargap=0.05,
    )

    return fig.to_dict()


def _add_normal_curve(fig: Any, values: list[float], num_bins: int) -> None:
    """Overlay a normal distribution curve computed from data mean and std."""
    import plotly.graph_objects as go

    n = len(values)
    mean = sum(values) / n
    variance = sum((v - mean) ** 2 for v in values) / n
    std = math.sqrt(variance)

    if std == 0:
        return

    # Generate curve over x-range spanning ±4 standard deviations
    x_min = min(values)
    x_max = max(values)
    padding = (x_max - x_min) * 0.2
    x_range = [x_min - padding, x_max + padding]

    step = (x_range[1] - x_range[0]) / 200
    bin_width = (x_max - x_min) / num_bins
    curve_x = []
    curve_y = []

    x = x_range[0]
    for _ in range(201):
        curve_x.append(x)
        exponent = -((x - mean) ** 2) / (2 * variance)
        pdf_value = (1 / (std * math.sqrt(2 * math.pi))) * math.exp(exponent)
        # Scale PDF by count * bin_width to match histogram y-axis
        curve_y.append(pdf_value * len(values) * bin_width)
        x += step

    fig.add_trace(
        go.Scatter(
            x=curve_x,
            y=curve_y,
            mode="lines",
            name="Normal fit",
            line=dict(color=CHART_COLORS[1], width=2),
        )
    )