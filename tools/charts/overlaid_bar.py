"""
Overlaid bar charts for parametric comparison.

Three chart types:
1. Raw bar — group bars with opacity toggle for top-3 missions vs uploaded
2. Z-score delta bar — green/yellow/red based on delta magnitude
3. Distance breakdown — horizontal stacked bar showing per-dimension % contribution
"""

import plotly.graph_objects as go

# Colors for top-3 matches
TOP3_COLORS = ["#ff7f0e", "#2ca02c", "#d62728"]

# Human-readable dimension labels
DIM_LABELS = {
    "mass_kg": "Unit Mass (kg)",
    "power_w_gen": "Power Gen (W)",
    "power_w_nom": "Nominal Power (W)",
    "power_w_peak": "Peak Power (W)",
    "payload_mass_kg": "Payload Mass (kg)",
    "propellant_mass_kg": "Propellant (kg)",
    "delta_v_ms": "Delta-V (m/s)",
    "duration_years": "Duration (yr)",
    "number_spacecraft": "Spacecraft",
    "data_gb_day": "Data/Day (GB)",
}


def build_raw_bar_chart(comparison_result):
    """Build raw value bar chart — group bars for uploaded + top-3 by dimension.

    All traces at base 0.25 opacity. A separate dcc.Checklist callback
    handles opacity toggling via dash.Patch, but since we're rendering
    server-side here, we set base opacity 0.25 and add legendgroup for grouping.
    """
    fig = go.Figure()
    dims = comparison_result.get("active_dimensions", [])
    dim_labels = [DIM_LABELS.get(d, d) for d in dims]
    target_z = comparison_result.get("target_z", {})

    # Uploaded mission — solid bar (opacity 1.0 since it's the reference)
    uploaded_raw = []
    for d in dims:
        # Convert target_z back to approximate raw using population stats
        stats = comparison_result.get("population_stats", {}).get(d, {"mean": 0, "stddev": 1})
        raw = target_z.get(d, 0) * stats["stddev"] + stats["mean"]
        uploaded_raw.append(round(raw, 1))

    fig.add_trace(
        go.Bar(
            x=dim_labels,
            y=uploaded_raw,
            name="Uploaded",
            opacity=1.0,
            marker_color="#1f77b4",
            legendgroup="uploaded",
        )
    )

    # Top-3 missions
    for i, m in enumerate(comparison_result.get("top_n", [])[:3]):
        raw_values = [m["raw_values"].get(d) or 0 for d in dims]
        fig.add_trace(
            go.Bar(
                x=dim_labels,
                y=raw_values,
                name=f"#{i + 1}: {m['mission_name']}",
                opacity=i * 0.1 + 0.25,
                marker_color=TOP3_COLORS[i],
                legendgroup=f"top-{i}",
            )
        )

    fig.update_layout(
        barmode="group",
        title="Raw Parameter Comparison — Uploaded vs Top-3",
        height=400,
        legend={"orientation": "h", "y": 1.1},
    )

    return fig


def build_delta_bar_chart(comparison_result):
    """Build z-score delta bar chart — green/yellow/red per dimension per mission.

    Green: |delta| < 0.5σ, Yellow: < 1.0σ, Red: > 1.5σ.
    """
    fig = go.Figure()
    dims = comparison_result.get("active_dimensions", [])
    dim_labels = [DIM_LABELS.get(d, d) for d in dims]

    threshold_green = 0.5
    threshold_yellow = 1.0
    threshold_red = 1.5

    for i, m in enumerate(comparison_result.get("top_n", [])[:3]):
        deltas = m.get("deltas", {})
        y_values = [deltas.get(d, 0) for d in dims]

        # Per-bar color based on delta magnitude
        colors = []
        for y in y_values:
            ay = abs(y)
            if ay <= threshold_green:
                colors.append("#10b981")  # green
            elif ay <= threshold_yellow:
                colors.append("#f59e0b")  # yellow
            else:
                colors.append("#ef4444")  # red

        fig.add_trace(
            go.Bar(
                x=dim_labels,
                y=y_values,
                name=f"#{i + 1}: {m['mission_name']}",
                marker_color=colors,
                opacity=0.8,
            )
        )

    # Reference lines at ±0.5σ, ±1σ
    fig.add_hline(
        y=threshold_green,
        line_dash="dash",
        line_color="gray",
        opacity=0.3,
        annotation_text="±0.5σ",
    )
    fig.add_hline(
        y=-threshold_green,
        line_dash="dash",
        line_color="gray",
        opacity=0.3,
    )

    fig.update_layout(
        barmode="group",
        title="Z-Score Deltas — Top-3 vs Uploaded (σ)",
        yaxis_title="Z-Score Delta (σ)",
        height=400,
        legend={"orientation": "h", "y": 1.1},
    )

    return fig


def build_distance_breakdown(comparison_result):
    """Build horizontal stacked bar showing per-dimension contribution to total distance.

    Each bar = one top-3 match. Segments = weight * delta² / total * 100%.
    """
    fig = go.Figure()
    dims = comparison_result.get("active_dimensions", [])
    weights = comparison_result.get("weights", {})

    # Color per dimension — match chart palette
    dim_colors = [
        "#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6",
        "#ec4899", "#06b6d4", "#f97316", "#84cc16", "#14b8a6",
    ]

    # Dummy legend traces for each dimension
    for j, dim in enumerate(dims):
        label = DIM_LABELS.get(dim, dim)
        fig.add_trace(
            go.Bar(
                x=[0],
                y=["_placeholder"],
                name=label,
                orientation="h",
                marker_color=dim_colors[j % len(dim_colors)],
                showlegend=True,
                visible="legendonly",
            )
        )

    for i, m in enumerate(comparison_result.get("top_n", [])[:3]):
        deltas = m.get("deltas", {})
        total_contrib = sum(
            weights.get(d, 0) * deltas.get(d, 0) ** 2 for d in dims
        )

        # Build stacked bar — one segment per dimension
        cumulative = 0
        for j, dim in enumerate(dims):
            w = weights.get(dim, 0)
            delta = deltas.get(dim, 0)
            contrib = (w * delta * delta / total_contrib * 100) if total_contrib > 0 else 0

            fig.add_trace(
                go.Bar(
                    x=[contrib],
                    y=[f"#{i + 1}: {m['mission_name']}"],
                    orientation="h",
                    name=DIM_LABELS.get(dim, dim),
                    marker_color=dim_colors[j % len(dim_colors)],
                    showlegend=False,
                    hovertemplate=(
                        f"{DIM_LABELS.get(dim, dim)}: %{{x:.1f}}%<extra></extra>"
                    ),
                )
            )

    fig.update_layout(
        barmode="stack",
        title="Distance Breakdown — Per-Dimension Contribution",
        xaxis_title="Contribution (%)",
        height=350 + 80 * min(3, len(comparison_result.get("top_n", []))),
        bargap=0.2,
    )

    return fig