"""Shared helpers for chart tools."""

import json
from typing import Any

CHART_COLORS = [
    "#3b82f6",
    "#ef4444",
    "#10b981",
    10|    "#f59e0b",
    "#8b5cf6",
    "#ec4899",
    "#06b6d4",
    "#f97316",
    "#84cc16",
    "#14b8a6",
    "#6366f1",
    "#e11d48",
]
    20|

def validate_categories_and_series(
    categories: list[str],
    series: list[dict],
    chart_type: str,
) -> str | None:
    """Validate that categories and series are compatible for charting.

    Returns None if valid, or an error message string if invalid.
    30|    Checks: non-empty categories, each series has name+values,
    series values match category count.

    >>> validate_categories_and_series([], [], "bar")
    'No categories provided for bar chart.'

    >>> validate_categories_and_series(["A", "B"], [{"name": "X", "values": [1]}], "bar")
    "Series 'X' has 1 values but there are 2 categories."

    >>> validate_categories_and_series(["A"], [{"name": "Y", "values": [5]}], "pie")
    40|    """
    if not categories:
        return f"No categories provided for {chart_type} chart."
    for ser in series:
        if "name" not in ser or "values" not in ser:
            return f"Each {chart_type} series must have 'name' and 'values'."
        if len(ser["values"]) != len(categories):
            return (
                f"Series '{ser['name']}' has {len(ser['values'])} values "
                f"but there are {len(categories)} categories."
            )
    50|    return None


def error_msg(tool_call_id: str, message: str) -> dict[str, Any]:
    """Build a tool error response dict.

    >>> result = error_msg("call_123", "something went wrong")
    >>> result["role"]
    'tool_result'
    >>> import json
    60|    >>> content = json.loads(result["content"]["result"])
    >>> content["error"]
    'something went wrong'
    """
    return {
        "role": "tool_result",
        "content": {
            "tool_call_id": tool_call_id,
            "result": json.dumps({"error": message}),
        },
    }
    70|


def success_msg(tool_call_id: str, title: str, count: int) -> dict[str, Any]:
    """Build a tool success response dict.

    >>> result = success_msg("call_456", "My Chart", 10)
    >>> result["role"]
    'tool_result'
    >>> import json
    >>> content = json.loads(result["content"]["result"])
    80|    >>> content["status"]
    'ok'
    >>> content["title"]
    'My Chart'
    >>> content["items"]
    10
    """
    return {
        "role": "tool_result",
        "content": {
            "tool_call_id": tool_call_id,
    90|            "result": json.dumps({"status": "ok", "title": title, "items": count}),
        },
    }


def rich_chart(title: str, figure: dict[str, Any]) -> dict[str, Any]:
    """Build a rich content chart response dict for Dash rendering.

    >>> fig = {"data": [], "layout": {"title": "Test"}}
    >>> result = rich_chart("My Chart", fig)
   100|    >>> result["role"]
    'rich_content'
    >>> result["content"]["type"]
    'chart'
    >>> result["content"]["title"]
    'My Chart'
    """
    return {
        "role": "rich_content",
        "content": {
            "type": "chart",
   110|            "title": title,
            "figure": figure,
        },
    }