"""Excel/CSV import and plot tool."""

import json
from typing import Any

import pandas as pd

from app.core.logging import log_function_call


class ExcelTool:
    """Parse uploaded Excel/CSV data and build interactive Plotly charts."""

    def __init__(self, uploaded_files_store: dict[str, pd.DataFrame] | None = None) -> None:
        self._uploaded: dict[str, pd.DataFrame] = uploaded_files_store or {}

    def register_upload(self, file_id: str, df: pd.DataFrame) -> None:
        log_function_call(
            "tools.documents.excel",
            "register_upload",
            file_id=file_id,
            rows=len(df),
            cols=len(df.columns),
        )
        self._uploaded[file_id] = df

    # OpenAI tool definition schema
    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "plot_data",
                "description": (
                    "Plot data from an uploaded Excel or CSV file. "
                    "Specify which columns to put on X and Y axes."
                ),
                "parameters": _plot_data_parameters(),
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        file_id = args.get("file_id", "")
        x_column = args.get("x_column", "")
        y_columns = args.get("y_columns", [])
        chart_title = args.get("chart_title", "")
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.documents.excel",
            "execute",
            file_id=file_id,
            x_column=x_column,
            source="agent_or_route",
        )

        df = self._uploaded.get(file_id)
        if df is None:
            return self._error(tool_call_id, f"No file found with ID '{file_id}'."), None

        error = _validate_columns(df, x_column, y_columns)
        if error:
            return self._error(tool_call_id, error), None

        title = chart_title or f"{', '.join(y_columns)} vs {x_column}"
        figure = _build_figure(df, x_column, y_columns, title)
        tool_msg = _build_success_msg(tool_call_id, file_id, x_column, y_columns, len(df))
        content = {"type": "chart", "title": title, "figure": figure}
        rich = {"role": "rich_content", "content": content}
        log_function_call(
            "tools.documents.excel",
            "execute",
            step="complete",
            title=title,
            rows=len(df),
        )
        return tool_msg, rich

    # Build error tool message
    def _error(self, tool_call_id: str, message: str) -> dict[str, Any]:
        return {
            "role": "tool_result",
            "content": {
                "tool_call_id": tool_call_id,
                "result": json.dumps({"error": message}),
            },
        }


# Validate requested columns exist in the dataframe
def _validate_columns(df: pd.DataFrame, x_column: str, y_columns: list[str]) -> str | None:
    if x_column not in df.columns:
        return f"Column '{x_column}' not found. Available: {', '.join(df.columns)}"
    missing = [c for c in y_columns if c not in df.columns]
    if missing:
        return f"Columns not found: {', '.join(missing)}. Available: {', '.join(df.columns)}"
    return None


_EXCEL_COLORS = ["#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899"]


# Build a Plotly figure from dataframe columns
def _build_figure(
    df: pd.DataFrame,
    x_column: str,
    y_columns: list[str],
    title: str,
) -> dict[str, Any]:
    import plotly.graph_objects as go

    fig = go.Figure()
    for i, y_col in enumerate(y_columns):
        color = _EXCEL_COLORS[i % len(_EXCEL_COLORS)]
        fig.add_trace(
            go.Scatter(
                x=df[x_column],
                y=df[y_col],
                mode="lines+markers",
                name=y_col,
                line=dict(color=color, width=2),
                marker=dict(size=6, color=color),
            )
        )
    fig.update_layout(
        title=title,
        xaxis_title=x_column,
        yaxis_title=", ".join(y_columns),
        height=450,
        margin=dict(l=40, r=20, t=50, b=40),
        hovermode="x unified",
    )
    return fig.to_dict()


# Build the OpenAI tool parameters schema for plot_data
def _plot_data_parameters() -> dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "file_id": {
                "type": "string",
                "description": "The ID of the uploaded file to plot.",
            },
            "x_column": {
                "type": "string",
                "description": "Column name for the X axis.",
            },
            "y_columns": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of column names for the Y axis (can be one or more).",
            },
            "chart_title": {
                "type": "string",
                "description": "Optional chart title. Generated from columns if omitted.",
            },
        },
        "required": ["file_id", "x_column", "y_columns"],
    }


# Build the tool_result message for a successful plot
def _build_success_msg(
    tool_call_id: str,
    file_id: str,
    x_column: str,
    y_columns: list[str],
    row_count: int,
) -> dict[str, Any]:
    return {
        "role": "tool_result",
        "content": {
            "tool_call_id": tool_call_id,
            "result": json.dumps(
                {
                    "status": "ok",
                    "file_id": file_id,
                    "x_column": x_column,
                    "y_columns": y_columns,
                    "rows_plotted": row_count,
                }
            ),
        },
    }
