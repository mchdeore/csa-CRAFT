"""
Radar/spider chart for parametric mission comparison.

Shows: 14 ghost polygons at low opacity (legendonly), uploaded mission as solid
diamond, top-3 matches as semi-transparent colored polygons, z=0 reference ring.
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


def build_radar_chart(comparison_result):
    """Build the full radar chart figure from comparison results."""
    fig = go.Figure()

    dims = comparison_result.get("active_dimensions", [])
    dim_labels = [DIM_LABELS.get(d, d) for d in dims]

    # 14 ghost polygons — hidden by default, hover in legend reveals
    for m in comparison_result.get("all_rankings", []):
        r_values = [m["z_scores"].get(d, 0) for d in dims]
        customdata = [m["raw_values"].get(d) for d in dims]

        fig.add_trace(
            go.Scatterpolar(
                r=r_values,
                theta=dim_labels,
                mode="lines+markers",
                name=m["mission_name"],
                opacity=0.15,
                marker={"size": 4},
                line={"width": 1},
                visible="legendonly",
                customdata=customdata,
                hovertemplate=(
                    "<b>%{fullData.name}</b><br>"
                    "%{theta}: z=%{r:.2f}σ (raw: %{customdata})<extra></extra>"
                ),
            )
        )

    # Uploaded mission — solid diamond
    target_z = comparison_result.get("target_z", {})
    fig.add_trace(
        go.Scatterpolar(
            r=[target_z.get(d, 0) for d in dims],
            theta=dim_labels,
            mode="lines+markers",
            name="Uploaded Mission",
            opacity=1.0,
            marker={"size": 10, "symbol": "diamond"},
            line={"width": 3, "dash": "solid"},
            hovertemplate=(
                "<b>Uploaded</b><br>%{theta}: z=%{r:.2f}σ<extra></extra>"
            ),
        )
    )

    # Top-3 — semi-transparent, fixed colors
    for i, m in enumerate(comparison_result.get("top_n", [])[:3]):
        r_values = [m["z_scores"].get(d, 0) for d in dims]
        fig.add_trace(
            go.Scatterpolar(
                r=r_values,
                theta=dim_labels,
                mode="lines+markers",
                name=f"#{i + 1}: {m['mission_name']} (d={m['distance']:.2f})",
                opacity=0.6,
                marker={"size": 8, "color": TOP3_COLORS[i]},
                line={"width": 2, "color": TOP3_COLORS[i]},
                hovertemplate=(
                    f"<b>#{i + 1}: %{{fullData.name}}</b><br>%{{theta}}: z=%{{r:.2f}}σ<extra></extra>"
                ),
            )
        )

    # z=0 reference ring
    fig.add_trace(
        go.Scatterpolar(
            r=[0] * len(dims),
            theta=dim_labels,
            mode="lines",
            line={"color": "gray", "width": 1, "dash": "dot"},
            opacity=0.3,
            showlegend=False,
            hoverinfo="none",
        )
    )

    fig.update_polars(radialaxis={"range": [-3, 3]})
    fig.update_layout(
        height=550,
        margin={"r": 200},
        legend={"x": 1.1, "y": 1},
    )

    return fig