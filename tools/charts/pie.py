"""Pie chart tool."""

from typing import Any

from app.core.logging import log_function_call
from tools.charts._shared import CHART_COLORS, error_msg, rich_chart, success_msg


class PieChartTool:
    """Build a pie/donut chart from labeled values."""

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draw_pie_chart",
                "description": (
                    "Draw an interactive pie chart. "
                    "Pass slices with labels and values. "
                    "Use for proportions, percentages, composition breakdowns."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Chart title displayed at the top.",
                        },
                        "slices": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "label": {
                                        "type": "string",
                                        "description": "Slice label.",
                                    },
                                    "value": {
                                        "type": "number",
                                        "description": "Numeric value for this slice.",
                                    },
                                },
                                "required": ["label", "value"],
                            },
                            "description": "Array of {label, value} objects for each pie slice.",
                        },
                        "donut": {
                            "type": "boolean",
                            "description": "If true, draw as a donut chart with a hole in center.",
                        },
                        "show_percentages": {
                            "type": "boolean",
                            "description": "If true, show percentage labels on slices.",
                        },
                    },
                    "required": ["title", "slices"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        title = args.get("title", "Pie Chart")
        slices = args.get("slices", [])
        donut = args.get("donut", False)
        show_percentages = args.get("show_percentages", False)
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.charts.pie",
            "execute",
            title=title,
            slice_count=len(slices),
            source="agent_or_route",
        )

        if not slices:
            return error_msg(tool_call_id, "No slices provided for pie chart."), None
        for s in slices:
            if "label" not in s or "value" not in s:
                return error_msg(tool_call_id, "Each slice must have 'label' and 'value'."), None

        figure = _build_pie_figure(title, slices, donut, show_percentages)
        log_function_call("tools.charts.pie", "execute", step="complete", title=title)
        return success_msg(tool_call_id, title, len(slices)), rich_chart(title, figure)


def _build_pie_figure(
    title: str,
    slices: list[dict],
    donut: bool,
    show_percentages: bool,
) -> dict[str, Any]:
    """Build a Plotly pie or donut chart figure dict.

    Returns the figure as a dict via to_dict() for JSON serialization.
    Uses CHART_COLORS for slice colors. When donut=True, adds a center hole.

    >>> slices = [{"label": "A", "value": 30}, {"label": "B", "value": 70}]
    >>> fig = _build_pie_figure("Test", slices, donut=False, show_percentages=False)
    >>> isinstance(fig, dict)
    True
    >>> len(fig["data"])
    1
    >>> fig["layout"]["title"]["text"]
    'Test'
    """

    labels = [s["label"] for s in slices]
    values = [s["value"] for s in slices]
    hole = 0.4 if donut else 0
    textinfo = "label+percent" if show_percentages else "label"

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=hole,
                textinfo=textinfo,
                marker=dict(colors=CHART_COLORS[: len(labels)]),
                hovertemplate="%{label}<br>%{value:,} (%{percent})<extra></extra>",
            )
        ]
    )
    fig.update_layout(
        title=title,
        height=450,
        margin=dict(l=20, r=20, t=50, b=20),
    )
    return fig.to_dict()
