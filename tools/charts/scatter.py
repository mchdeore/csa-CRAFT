"""Scatter chart tool with polynomial fit and residual analysis."""

from typing import Any

from app.core.logging import log_function_call
from tools.charts._shared import CHART_COLORS, error_msg, rich_chart, success_msg


class ScatterChartTool:
    """Build a scatter plot from data points with optional polynomial fit and residuals."""

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draw_scatter_chart",
                "description": (
                    "Draw an interactive scatter plot. "
                    "Pass one or more series of x,y points. "
                    "Use for correlations, distributions, and clusters. "
                    "Optionally add polynomial trendlines and residual analysis."
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
                            "description": "If true, add a fitted curve to each series.",
                        },
                        "fit_degree": {
                            "type": "integer",
                            "description": (
                                "Degree of polynomial fit. 1 = linear, 2 = quadratic, "
                                "3 = cubic, up to 5. Default: 1. Ignored if trendline is false."
                            ),
                        },
                        "show_residuals": {
                            "type": "boolean",
                            "description": (
                                "If true, show a residuals subplot below the scatter plot. "
                                "Requires trendline to be enabled."
                            ),
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
        fit_degree = args.get("fit_degree", 1)
        show_residuals = args.get("show_residuals", False)
        size_by = args.get("size_by", "none")
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.charts.scatter",
            "execute",
            title=title,
            series_count=len(series),
            trendline=trendline,
            fit_degree=fit_degree,
            show_residuals=show_residuals,
            source="agent_or_route",
        )

        if not series:
            return error_msg(tool_call_id, "No series provided for scatter plot."), None
        for s in series:
            if "name" not in s or "points" not in s:
                return error_msg(tool_call_id, "Each series must have 'name' and 'points'."), None
            if not s["points"]:
                return error_msg(tool_call_id, f"Series '{s['name']}' has no points."), None

        # Residuals requires trendline
        if show_residuals and not trendline:
            return error_msg(
                tool_call_id,
                "show_residuals requires trendline to be enabled. "
                "Set trendline=true to compute fit before showing residuals.",
            ), None

        # Clamp fit_degree
        if fit_degree < 1:
            fit_degree = 1
        if fit_degree > 5:
            fit_degree = 5

        figure = _build_scatter_figure(
            title,
            series,
            x_label,
            y_label,
            trendline,
            fit_degree,
            show_residuals,
            size_by,
        )
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
    fit_degree: int,
    show_residuals: bool,
    size_by: str,
) -> dict[str, Any]:
    """Build a scatter figure, optionally with polynomial fits and residual subplot."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # When showing residuals, use a 2-row subplot layout
    if show_residuals and trendline:
        fig = make_subplots(
            rows=2,
            cols=1,
            row_heights=[0.7, 0.3],
            shared_xaxes=True,
            vertical_spacing=0.06,
            subplot_titles=(title, "Residuals"),
        )
    else:
        fig = go.Figure()

    # Store fit data for residuals computation
    fit_data = []

    for i, ser in enumerate(series):
        color = CHART_COLORS[i % len(CHART_COLORS)]
        points = ser["points"]
        xs = [p["x"] for p in points]
        ys = [p["y"] for p in points]
        labels = [p.get("label", "") for p in points]

        # Determine marker size
        marker_size = 10
        if size_by == "x":
            marker_size = [max(5, min(30, abs(v) * 2)) for v in xs]
        elif size_by == "y":
            marker_size = [max(5, min(30, abs(v) * 2)) for v in ys]

        # Row/col for subplot layout when residuals are shown — unused
        # here but kept explicit for clarity

        # Add scatter points
        scatter_trace = go.Scatter(
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

        if show_residuals and trendline:
            fig.add_trace(scatter_trace, row=1, col=1)
        else:
            fig.add_trace(scatter_trace)

        # Add polynomial fit curve
        if trendline and len(xs) >= fit_degree + 1:
            coeffs, fitted_ys, r_squared = _compute_polynomial_fit(xs, ys, fit_degree)

            if coeffs is not None:
                fit_data.append(
                    {
                        "name": ser["name"],
                        "xs": xs,
                        "ys": ys,
                        "fitted_ys": fitted_ys,
                        "coeffs": coeffs,
                        "r_squared": r_squared,
                        "color": color,
                    }
                )

                # Build the fit curve trace
                curve_x, curve_y = _build_fit_curve(xs, coeffs)

                degree_label = f" (degree {fit_degree})" if fit_degree > 1 else ""

                fit_trace = go.Scatter(
                    x=curve_x,
                    y=curve_y,
                    mode="lines",
                    name=f"{ser['name']} fit{degree_label}",
                    line=dict(color=color, dash="dash", width=1.5),
                    hovertemplate=(
                        f"R² = {r_squared:.4f}<br>"
                        f"x: %{{x:,}}<br>fitted y: %{{y:,.2f}}<extra></extra>"
                    ),
                )

                if show_residuals and trendline:
                    fig.add_trace(fit_trace, row=1, col=1)
                else:
                    fig.add_trace(fit_trace)

    # Add residual subplot if requested
    if show_residuals and trendline and fit_data:
        _add_residuals_to_figure(fig, fit_data)

    # Layout
    if show_residuals and trendline:
        fig.update_layout(
            height=650,
            margin=dict(l=40, r=20, t=60, b=40),
            hovermode="closest",
            showlegend=True,
        )
        # Update subplot axes
        fig.update_xaxes(title_text=x_label or "X", row=2, col=1)
        fig.update_yaxes(title_text=y_label or "Y", row=1, col=1)
    else:
        fig.update_layout(
            title=title,
            xaxis_title=x_label or "X",
            yaxis_title=y_label or "Y",
            height=500,
            margin=dict(l=40, r=20, t=50, b=40),
            hovermode="closest",
        )

    return fig.to_dict()


def _compute_polynomial_fit(
    xs: list[float],
    ys: list[float],
    degree: int,
) -> tuple[list[float] | None, list[float], float]:
    """Fit an nth-degree polynomial to (xs, ys). Returns (coefficients, fitted_ys, r_squared)."""
    import numpy as np

    try:
        coeffs = np.polyfit(xs, ys, degree)
        poly = np.poly1d(coeffs)
        fitted_ys = poly(xs).tolist()

        # R-squared calculation
        mean_y = sum(ys) / len(ys)
        ss_res = sum((ys[i] - fitted_ys[i]) ** 2 for i in range(len(ys)))
        ss_tot = sum((y - mean_y) ** 2 for y in ys)
        r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 1.0

        return coeffs.tolist(), fitted_ys, r_squared
    except Exception:
        return None, ys, 0.0


def _build_fit_curve(
    xs: list[float],
    coeffs: list[float],
) -> tuple[list[float], list[float]]:
    """Generate smooth curve points for a polynomial fit.

    Returns (curve_x, curve_y) with 100 points spanning the x range.
    """
    import numpy as np  # type: ignore[import-untyped]

    x_min, x_max = min(xs), max(xs)
    if x_min == x_max:
        x_range = np.array([x_min])
    else:
        x_range = np.linspace(x_min, x_max, 100)

    poly = np.poly1d(coeffs)  # type: ignore[attr-defined]
    curve_y = poly(x_range).tolist()

    # Handle array vs scalar case
    if isinstance(curve_y, (int, float)):
        curve_y = [curve_y]

    # Convert numpy arrays to lists for type safety
    x_list: list[float] = x_range.tolist()  # type: ignore[union-attr]
    y_list: list[float] = list(curve_y) if not isinstance(curve_y, list) else list[float](curve_y)  # type: ignore[misc]

    return x_list, y_list


def _add_residuals_to_figure(
    fig: Any,
    fit_data: list[dict],
) -> None:
    """Add residual traces and a zero-line to the bottom subplot."""
    import plotly.graph_objects as go

    for entry in fit_data:
        name = entry["name"]
        xs = entry["xs"]
        ys = entry["ys"]
        fitted_ys = entry["fitted_ys"]
        color = entry["color"]
        r_squared = entry["r_squared"]

        # Compute residuals: actual - fitted
        residuals = [ys[i] - fitted_ys[i] for i in range(len(ys))]

        # Residual scatter points
        fig.add_trace(
            go.Scatter(
                x=xs,
                y=residuals,
                mode="markers",
                name=f"{name} residuals",
                marker=dict(
                    color=color,
                    size=8,
                    opacity=0.6,
                    line=dict(width=1, color="white"),
                ),
                hovertemplate=(
                    f"R² = {r_squared:.4f}<br>x: %{{x:,}}<br>residual: %{{y:,.2f}}<extra></extra>"
                ),
            ),
            row=2,
            col=1,
        )

    # Add a horizontal zero-line for reference
    all_xs = []
    for entry in fit_data:
        all_xs.extend(entry["xs"])
    x_min, x_max = min(all_xs), max(all_xs)

    fig.add_trace(
        go.Scatter(
            x=[x_min, x_max],
            y=[0, 0],
            mode="lines",
            name="Zero",
            line=dict(color="#9ca3af", dash="dot", width=1),
            showlegend=False,
            hoverinfo="skip",
        ),
        row=2,
        col=1,
    )
