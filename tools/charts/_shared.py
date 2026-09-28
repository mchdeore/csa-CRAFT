"""Shared helpers for chart tools."""

import json
from typing import Any

CHART_COLORS = [
    "#3b82f6",
    "#ef4444",
    "#10b981",
    "#f59e0b",
    "#8b5cf6",
    "#ec4899",
    "#06b6d4",
    "#f97316",
    "#84cc16",
    "#14b8a6",
    "#6366f1",
    "#e11d48",
]


def validate_categories_and_series(
    categories: list[str],
    series: list[dict],
    chart_type: str,
) -> str | None:
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
    return None


def error_msg(tool_call_id: str, message: str) -> dict[str, Any]:
    return {
        "role": "tool_result",
        "content": {
            "tool_call_id": tool_call_id,
            "result": json.dumps({"error": message}),
        },
    }


def success_msg(tool_call_id: str, title: str, count: int) -> dict[str, Any]:
    return {
        "role": "tool_result",
        "content": {
            "tool_call_id": tool_call_id,
            "result": json.dumps({"status": "ok", "title": title, "items": count}),
        },
    }


def rich_chart(title: str, figure: dict[str, Any]) -> dict[str, Any]:
    return {
        "role": "rich_content",
        "content": {
            "type": "chart",
            "title": title,
            "figure": figure,
        },
    }
