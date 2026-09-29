"""
Demo Quick routes — Dash pages for three demo profiles.

Three tabs: finance (CADRe + comparison), engineer (compliance + diff),
risk (registers + correlation). Each tab loads profile-specific tools
and UI components. All compute happens server-side via callbacks.
"""

import base64
import io
import json
import uuid

import plotly.graph_objects as go
import plotly.io as pio
from dash import ALL, MATCH, Input, Output, State, ctx, dcc, html, no_update
from flask import jsonify, request

from app.core.config import build_system_prompt
from app.core.dash_app import app
from app.core.logging import log_function_call
from app.core.services import chat_provider, data_store, query_tool, store
from demo.profiles import PROFILES

# ---------------------------------------------------------------------------
# Dimension labels and their data keys
# ---------------------------------------------------------------------------
DIMENSION_LABELS = {
    "mass_kg": "Unit Mass (kg)",
    "power_w_gen": "Power Gen (W)",
    "power_w_nom": "Nominal Power (W)",
    "power_w_peak": "Peak Power (W)",
    "payload_mass_kg": "Payload Mass (kg)",
    "propellant_mass_kg": "Propellant (kg)",
    "delta_v_ms": "Delta-V (m/s)",
    "duration_years": "Duration (yr)",
    "number_spacecraft": "Num Spacecraft",
    "data_gb_day": "Data/Day (GB)",
}

# Colors for top-3 matches
TOP3_COLORS = ["#ff7f0e", "#2ca02c", "#d62728"]

# ---------------------------------------------------------------------------
# Distance engine — z-score normalize, weighted Euclidean distance
# ---------------------------------------------------------------------------

_z_stats_cache = None  # computed once from SQLite, never invalidated


def _compute_population_stats():
    """Load all mission params from cadre_params table, compute mean/stddev per dimension."""
    global _z_stats_cache
    import statistics

    if _z_stats_cache is not None:
        return _z_stats_cache

    rows = data_store._conn.execute("SELECT * FROM cadre_params").fetchall()
    dims = [
        "mass_kg", "power_w_gen", "power_w_nom", "power_w_peak",
        "payload_mass_kg", "propellant_mass_kg", "delta_v_ms",
        "duration_years", "number_spacecraft", "data_gb_day",
    ]

    stats = {}
    for dim in dims:
        vals = [float(r[dim]) for r in rows if r[dim] is not None]
        if len(vals) < 2:
            stats[dim] = {"mean": 0.0, "stddev": 1.0}
        else:
            stats[dim] = {"mean": statistics.mean(vals), "stddev": statistics.stdev(vals)}

    _z_stats_cache = stats
    return stats


def _z_score(value, dim_stats):
    """Convert raw value to z-score using population stats."""
    if value is None or dim_stats["stddev"] == 0:
        return 0.0
    return (value - dim_stats["mean"]) / dim_stats["stddev"]


def _weighted_distance(target_z, mission_z, weights):
    """Weighted Euclidean distance between two z-score vectors."""
    import math

    return math.sqrt(
        sum(weights.get(d, 0) * (target_z.get(d, 0) - mission_z.get(d, 0)) ** 2 for d in weights)
    )


def _compute_comparison(target_params, weight_order, active_dimensions=None, n=5):
    """Run full comparison pipeline against population.

    Returns dict with top_n, all_rankings, target_z, weights, population_stats.
    """
    from tools.costing.distance import compute_comparison as cc_impl

    return cc_impl(target_params, weight_order, active_dimensions, n, data_store)


# ---------------------------------------------------------------------------
# Chart builders
# ---------------------------------------------------------------------------


def _build_radar_chart(comparison_result):
    """Build radar/spider chart: 14 ghost + uploaded solid + top-3 semi."""
    from tools.charts.radar import build_radar_chart as brc

    return brc(comparison_result)


def _build_raw_bar_chart(comparison_result):
    """Build stacked bar with raw values for top-3 matches vs uploaded."""
    from tools.charts.overlaid_bar import build_raw_bar_chart as brbc

    return brbc(comparison_result)


def _build_delta_bar_chart(comparison_result):
    """Build z-score delta bars with green/yellow/red coloring."""
    from tools.charts.overlaid_bar import build_delta_bar_chart as bdbc

    return bdbc(comparison_result)


def _build_distance_breakdown(comparison_result):
    """Build horizontal stacked bar showing per-dimension distance contribution."""
    from tools.charts.overlaid_bar import build_distance_breakdown as bdb

    return bdb(comparison_result)


# ---------------------------------------------------------------------------
# Flask route — demo page serves the Dash layout
# ---------------------------------------------------------------------------


def register_routes(flask_app):
    """Register demo route on flask app."""

    @flask_app.route("/demo", methods=["GET"])
    def demo_page():
        return jsonify({"ok": True, "route": "/demo", "layout": "served by Dash callback"}), 200

    @flask_app.route("/demo/page", methods=["POST"])
    def demo_page_post():
        """Handle AJAX-style page load. Returns profile config for the logged-in user."""
        data = request.get_json(silent=True) or {}
        username = data.get("username", "")

        profile = PROFILES.get(username, PROFILES.get("fredmoney", {}))
        return (
            jsonify(
                {
                    "ok": True,
                    "role": profile.get("role", ""),
                    "display_name": profile.get("display_name", ""),
                    "tools": profile.get("tools", []),
                    "pre_filled_prompts": profile.get("pre_filled_prompts", {}),
                }
            ),
            200,
        )

    @flask_app.route("/demo/chat", methods=["POST"])
    def demo_chat():
        """Chat endpoint for demo — uses demo profile system prompt."""
        data = request.get_json(silent=True) or {}
        username = data.get("username", "")
        workspace_id = data.get("workspace_id", "")
        message = data.get("message", "")

        if not username or not workspace_id or not message.strip():
            return jsonify({"error": "Missing username, workspace_id, or message"}), 400

        profile = PROFILES.get(username, PROFILES.get("fredmoney", {}))
        system_prompt = profile.get("system_prompt", "")

        # Load existing messages, append user message
        existing = store.load(username, workspace_id)
        messages = existing["messages"] if existing else []
        messages.append({"role": "user", "content": message.strip()})

        # Set context on provider
        chat_provider._user_context = {"role": profile.get("role", "")}
        chat_provider._username = username
        chat_provider._workspace_id = workspace_id
        chat_provider._user_role = profile.get("role", "base_user")
        chat_provider._user_flags = []

        # Build a custom system prompt for this call by monkey-patching
        import app.core.config as cfg

        original_build = cfg.build_system_prompt
        cfg.build_system_prompt = lambda uc=None: system_prompt

        try:
            response = chat_provider.get_response(messages)
        finally:
            cfg.build_system_prompt = original_build

        if response.text:
            messages.append({"role": "assistant", "content": response.text})

        store.save_messages(username, workspace_id, messages)
        return (
            jsonify(
                {
                    "success": True,
                    "text": response.text,
                    "rich_contents": response.rich_contents,
                }
            ),
            200,
        )

    @flask_app.route("/demo/ingest", methods=["POST"])
    def demo_ingest():
        """Ingest a base64-encoded file, extract CADRe fields, return results."""
        data = request.get_json(silent=True) or {}
        contents = data.get("contents", "")
        filename = data.get("filename", "")

        if not contents or not filename:
            return jsonify({"error": "Missing contents or filename"}), 400

        from tools.documents.ingest import ingest_document

        result = ingest_document(contents, filename)
        return jsonify(result), 200

    @flask_app.route("/demo/compare", methods=["POST"])
    def demo_compare():
        """Run parametric comparison: extract → compare against population."""
        data = request.get_json(silent=True) or {}
        extracted_fields = data.get("extracted_fields", {})
        weight_order = data.get("weight_order", [])
        active_dimensions = data.get("active_dimensions", None)

        if not extracted_fields or not weight_order:
            return jsonify({"error": "Missing extracted_fields or weight_order"}), 400

        result = _compute_comparison(extracted_fields, weight_order, active_dimensions)
        return jsonify(result), 200

    @flask_app.route("/demo/compliance", methods=["POST"])
    def demo_compliance():
        """Run 5 hardcoded compliance rules on extracted fields."""
        data = request.get_json(silent=True) or {}
        extracted_fields = data.get("extracted_fields", {})

        if not extracted_fields:
            return jsonify({"error": "Missing extracted_fields"}), 400

        from tools.engineering.compliance import run_compliance

        result = run_compliance(extracted_fields)
        return jsonify(result), 200

    @flask_app.route("/demo/risk-register", methods=["POST"])
    def demo_risk_register():
        """Parse risk register from Part C markdown."""
        data = request.get_json(silent=True) or {}
        contents = data.get("contents", "")
        filename = data.get("filename", "")

        if not contents:
            return jsonify({"error": "Missing contents"}), 400

        from tools.risks.parser import parse_risk_register

        result = parse_risk_register(contents, filename)
        return jsonify(result), 200

# ---------------------------------------------------------------------------
# Dash callbacks — all client-server interaction here
# ---------------------------------------------------------------------------


@app.callback(
    Output("demo-page-content", "children"),
    Input("session-store", "data"),
)
def build_demo_page(session):
    """Render the full demo page based on logged-in user profile."""
    if not session or not session.get("logged_in"):
        return html.Div(
            html.H3("Please log in first.", style={"textAlign": "center", "marginTop": "100px"})
        )

    username = session.get("username", "")
    profile = PROFILES.get(username)

    if not profile:
        return html.Div(
            html.H3(
                f"No demo profile for '{username}'.",
                style={"textAlign": "center", "marginTop": "100px"},
            )
        )

    role = profile["role"]
    if role == "finance":
        return _build_finance_tab(profile, session)
    elif role == "engineer":
        return _build_engineer_tab(profile, session)
    elif role == "risk":
        return _build_risk_tab(profile, session)
    else:
        return html.Div(f"Unknown role: {role}")


# ===================== FINANCE TAB =====================


def _build_finance_tab(profile, session):
    """Build the finance profile page: upload → ingest → compare → charts."""
    return html.Div(
        [
            # Header
            html.Div(
                [
                    html.H2(profile["display_name"], style={"margin": "0", "color": "#1e40af"}),
                    html.Span(f"Role: {profile['role']}", style={"color": "#6b7280", "fontSize": "14px"}),
                ],
                style={
                    "padding": "16px 24px",
                    "borderBottom": "2px solid #e5e7eb",
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                },
            ),

            # Stores for data flow
            dcc.Store(id="extracted-fields", storage_type="session"),
            dcc.Store(id="comparison-results", storage_type="session"),
            dcc.Store(id="agent-context", storage_type="session"),
            dcc.Store(id="weight-order", storage_type="session"),
            dcc.Store(id="active-dimensions", storage_type="session"),

            # Main layout: upload area + results area
            html.Div(
                [
                    # Left column — upload + ingestion
                    html.Div(
                        [
                            html.H4("Step 1: Upload CADRe Part A", style={"marginTop": "0"}),
                            _build_upload_area("finance-upload"),
                            html.Div(id="finance-ingest-result", style={"marginTop": "12px"}),

                            # Pre-filled prompts from profile
                            html.H4("Quick Actions", style={"marginTop": "24px"}),
                            *[
                                html.Button(
                                    label,
                                    id={"type": "quick-action", "index": label},
                                    style={
                                        "display": "block",
                                        "width": "100%",
                                        "margin": "4px 0",
                                        "padding": "8px 12px",
                                        "textAlign": "left",
                                        "cursor": "pointer",
                                        "border": "1px solid #d1d5db",
                                        "borderRadius": "6px",
                                        "backgroundColor": "#f9fafb",
                                    },
                                )
                                for label in profile.get("pre_filled_prompts", {})
                            ],
                        ],
                        style={
                            "flex": "0 0 320px",
                            "padding": "16px",
                            "borderRight": "1px solid #e5e7eb",
                            "overflowY": "auto",
                        },
                    ),

                    # Right column — charts + agent
                    html.Div(
                        [
                            # Weight sliders
                            html.Div(id="finance-weight-sliders"),

                            # Dimension toggle
                            html.Div(id="finance-dimension-toggle"),

                            # Charts area
                            html.Div(
                                [
                                    dcc.Tabs(
                                        id="finance-chart-tabs",
                                        value="radar",
                                        children=[
                                            dcc.Tab(label="Radar", value="radar"),
                                            dcc.Tab(label="Raw Bars", value="raw-bars"),
                                            dcc.Tab(label="Z-Score Deltas", value="delta-bars"),
                                            dcc.Tab(label="Breakdown", value="breakdown"),
                                        ],
                                    ),
                                    html.Div(id="finance-chart-content", style={"marginTop": "12px"}),
                                ],
                                style={"marginTop": "16px"},
                            ),

                            # Chat area
                            html.Div(
                                [
                                    html.H4("Ask the Agent", style={"margin": "12px 0 8px 0"}),
                                    html.Div(
                                        id="finance-chat-messages",
                                        style={
                                            "flex": "1",
                                            "overflowY": "auto",
                                            "padding": "12px",
                                            "maxHeight": "300px",
                                            "minHeight": "150px",
                                            "backgroundColor": "#f5f5f5",
                                            "borderRadius": "8px",
                                            "marginBottom": "8px",
                                        },
                                    ),
                                    html.Div(
                                        [
                                            dcc.Input(
                                                id="finance-chat-input",
                                                placeholder="Ask about the comparison...",
                                                type="text",
                                                style={"flex": "1", "padding": "8px"},
                                            ),
                                            html.Button(
                                                "Send",
                                                id="finance-chat-send",
                                                style={
                                                    "padding": "8px 16px",
                                                    "marginLeft": "8px",
                                                },
                                            ),
                                        ],
                                        style={"display": "flex"},
                                    ),
                                ],
                                style={"marginTop": "16px"},
                            ),
                        ],
                        style={"flex": "1", "padding": "16px", "overflowY": "auto"},
                    ),
                ],
                style={"display": "flex", "flex": "1", "overflow": "hidden"},
            ),
        ],
        style={
            "display": "flex",
            "flexDirection": "column",
            "height": "calc(100vh - 60px)",
        },
    )


def _build_upload_area(upload_id):
    """Reusable file upload widget."""
    return dcc.Upload(
        id=upload_id,
        children=html.Div(
            [
                "Drag and drop or ",
                html.A("select a file", style={"color": "#3b82f6", "textDecoration": "underline"}),
            ]
        ),
        style={
            "width": "100%",
            "height": "80px",
            "lineHeight": "80px",
            "borderWidth": "2px",
            "borderStyle": "dashed",
            "borderRadius": "8px",
            "textAlign": "center",
            "borderColor": "#d1d5db",
            "cursor": "pointer",
        },
        multiple=False,
    )


# ===================== ENGINEER TAB =====================


def _build_engineer_tab(profile, session):
    """Build the engineer profile page: upload → compliance → diff."""
    # Placeholder — same structure as finance but with compliance tools
    return html.Div(
        [
            html.Div(
                [
                    html.H2(profile["display_name"], style={"margin": "0", "color": "#1e40af"}),
                    html.Span(f"Role: {profile['role']}", style={"color": "#6b7280", "fontSize": "14px"}),
                ],
                style={
                    "padding": "16px 24px",
                    "borderBottom": "2px solid #e5e7eb",
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                },
            ),
            dcc.Store(id="engineer-extracted-v1", storage_type="session"),
            dcc.Store(id="engineer-extracted-v2", storage_type="session"),
            html.Div(
                [
                    html.Div(
                        [
                            html.H4("Upload Document", style={"marginTop": "0"}),
                            _build_upload_area("engineer-upload-v1"),
                            html.Div(id="engineer-upload-v1-result", style={"marginTop": "12px"}),
                            html.H4("Upload Version 2 (for diff)", style={"marginTop": "16px"}),
                            _build_upload_area("engineer-upload-v2"),
                            html.Div(id="engineer-upload-v2-result", style={"marginTop": "12px"}),
                            html.Button(
                                "Run Compliance Check",
                                id="engineer-compliance-btn",
                                style={
                                    "marginTop": "12px",
                                    "padding": "10px 20px",
                                    "width": "100%",
                                    "cursor": "pointer",
                                    "backgroundColor": "#3b82f6",
                                    "color": "white",
                                    "border": "none",
                                    "borderRadius": "6px",
                                },
                            ),
                            html.Button(
                                "Run Version Diff",
                                id="engineer-diff-btn",
                                style={
                                    "marginTop": "8px",
                                    "padding": "10px 20px",
                                    "width": "100%",
                                    "cursor": "pointer",
                                    "backgroundColor": "#8b5cf6",
                                    "color": "white",
                                    "border": "none",
                                    "borderRadius": "6px",
                                },
                            ),
                            html.Div(id="engineer-compliance-result", style={"marginTop": "12px"}),
                            html.Div(id="engineer-diff-result", style={"marginTop": "12px"}),
                        ],
                        style={
                            "flex": "0 0 320px",
                            "padding": "16px",
                            "borderRight": "1px solid #e5e7eb",
                        },
                    ),
                    html.Div(
                        [
                            # Parameter margin chart placeholder
                            dcc.Graph(id="engineer-margin-chart", style={"height": "400px"}),
                            # Compliance detail area
                            html.Div(id="engineer-compliance-detail", style={"marginTop": "16px"}),
                            # Chat
                            html.H4("Ask the Agent", style={"marginTop": "16px"}),
                            html.Div(
                                id="engineer-chat-messages",
                                style={
                                    "flex": "1",
                                    "overflowY": "auto",
                                    "padding": "12px",
                                    "maxHeight": "250px",
                                    "minHeight": "100px",
                                    "backgroundColor": "#f5f5f5",
                                    "borderRadius": "8px",
                                    "marginBottom": "8px",
                                },
                            ),
                            html.Div(
                                [
                                    dcc.Input(
                                        id="engineer-chat-input",
                                        placeholder="Ask about compliance...",
                                        type="text",
                                        style={"flex": "1", "padding": "8px"},
                                    ),
                                    html.Button(
                                        "Send", id="engineer-chat-send",
                                        style={"padding": "8px 16px", "marginLeft": "8px"},
                                    ),
                                ],
                                style={"display": "flex"},
                            ),
                        ],
                        style={"flex": "1", "padding": "16px"},
                    ),
                ],
                style={"display": "flex", "flex": "1", "overflow": "hidden"},
            ),
        ],
        style={"display": "flex", "flexDirection": "column", "height": "calc(100vh - 60px)"},
    )


# ===================== RISK TAB =====================


def _build_risk_tab(profile, session):
    """Build the risk profile page: upload → parse → heatmap/scatter/correlation."""
    return html.Div(
        [
            html.Div(
                [
                    html.H2(profile["display_name"], style={"margin": "0", "color": "#1e40af"}),
                    html.Span(f"Role: {profile['role']}", style={"color": "#6b7280", "fontSize": "14px"}),
                ],
                style={
                    "padding": "16px 24px",
                    "borderBottom": "2px solid #e5e7eb",
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                },
            ),
            dcc.Store(id="risk-register-data", storage_type="session"),
            dcc.Store(id="risk-register-2-data", storage_type="session"),
            html.Div(
                [
                    html.Div(
                        [
                            html.H4("Upload Part C Risk Register", style={"marginTop": "0"}),
                            _build_upload_area("risk-upload-1"),
                            html.Div(id="risk-upload-1-result", style={"marginTop": "12px"}),
                            html.H4("Upload Second Register (Cross-Compare)", style={"marginTop": "16px"}),
                            _build_upload_area("risk-upload-2"),
                            html.Div(id="risk-upload-2-result", style={"marginTop": "12px"}),
                        ],
                        style={
                            "flex": "0 0 320px",
                            "padding": "16px",
                            "borderRight": "1px solid #e5e7eb",
                        },
                    ),
                    html.Div(
                        [
                            dcc.Tabs(
                                id="risk-chart-tabs",
                                value="heatmap",
                                children=[
                                    dcc.Tab(label="Heatmap", value="heatmap"),
                                    dcc.Tab(label="Scatter", value="scatter"),
                                    dcc.Tab(label="Tornado", value="tornado"),
                                    dcc.Tab(label="Correlation", value="correlation"),
                                ],
                            ),
                            html.Div(id="risk-chart-content", style={"marginTop": "12px"}),
                        ],
                        style={"flex": "1", "padding": "16px"},
                    ),
                ],
                style={"display": "flex", "flex": "1", "overflow": "hidden"},
            ),
        ],
        style={"display": "flex", "flexDirection": "column", "height": "calc(100vh - 60px)"},
    )


# ===================== FINANCE CALLBACKS =====================


@app.callback(
    Output("finance-ingest-result", "children"),
    Output("extracted-fields", "data"),
    Output("weight-order", "data"),
    Output("active-dimensions", "data"),
    Input("finance-upload", "contents"),
    State("finance-upload", "filename"),
    prevent_initial_call=True,
)
def on_finance_upload(contents, filename):
    """Handle file upload — send to /demo/ingest, extract fields."""
    if not contents or not filename:
        return no_update, no_update, no_update, no_update

    log_function_call("demo.routes", "on_finance_upload", filename=filename)

    client = app.server.test_client()
    resp = client.post(
        "/demo/ingest",
        json={"contents": contents, "filename": filename},
    )
    data = resp.get_json() or {}

    if data.get("error"):
        return (
            html.Div(f"❌ {data['error']}", style={"color": "#ef4444"}),
            no_update,
            no_update,
            no_update,
        )

    fields = data.get("fields", {})
    confidence = data.get("confidence", {})

    # Build green card with confidence badges
    field_rows = []
    for key, value in fields.items():
        label = DIMENSION_LABELS.get(key, key)
        conf = confidence.get(key, 0)
        conf_color = "#10b981" if conf >= 0.8 else "#f59e0b" if conf >= 0.5 else "#ef4444"
        field_rows.append(
            html.Div(
                [
                    html.Span(label, style={"fontWeight": "bold", "fontSize": "13px"}),
                    html.Span(
                        f"{value}",
                        style={"marginLeft": "8px", "fontSize": "13px"},
                    ),
                    html.Span(
                        f" {conf:.0%}",
                        style={
                            "marginLeft": "4px",
                            "fontSize": "10px",
                            "color": "white",
                            "backgroundColor": conf_color,
                            "padding": "1px 5px",
                            "borderRadius": "4px",
                        },
                    ),
                ],
                style={"padding": "4px 0"},
            )
        )

    card = html.Div(
        [
            html.Div(
                f"✅ {len(fields)} fields extracted from {filename}",
                style={
                    "fontWeight": "bold",
                    "color": "#059669",
                    "marginBottom": "8px",
                    "fontSize": "14px",
                },
            ),
            html.Div(field_rows),
        ],
        style={
            "padding": "12px",
            "backgroundColor": "#f0fdf4",
            "border": "1px solid #bbf7d0",
            "borderRadius": "8px",
        },
    )

    # Default weight order: all extracted dimensions
    weight_order = list(fields.keys())
    active_dims = list(fields.keys())

    return card, fields, weight_order, active_dims


@app.callback(
    Output("finance-weight-sliders", "children"),
    Input("weight-order", "data"),
    State("extracted-fields", "data"),
)
def build_weight_sliders(weight_order, extracted_fields):
    """Build sortable weight sliders from the weight order."""
    if not weight_order:
        html.Div("Upload a file to see dimension weights.", style={"color": "#999"})

    items = []
    for i, dim in enumerate(weight_order):
        label = DIMENSION_LABELS.get(dim, dim)
        items.append(
            html.Div(
                [
                    html.Span(f"↑↓", style={"cursor": "grab", "marginRight": "8px", "color": "#9ca3af"}),
                    html.Span(label, style={"fontSize": "13px", "flex": "1"}),
                    html.Span(f"#{i + 1}", style={"fontSize": "11px", "color": "#9ca3af"}),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "padding": "6px 8px",
                    "margin": "2px 0",
                    "backgroundColor": "#f3f4f6",
                    "borderRadius": "6px",
                    "border": "1px solid #e5e7eb",
                    "cursor": "grab",
                },
                **{"data-dim": dim},
            )
        )

    return html.Div(
        [
            html.H4("Weight Order (drag to reorder)", style={"margin": "16px 0 8px 0", "fontSize": "14px"}),
            html.Div(
                id="sortable-weight-group",
                children=items,
                style={"maxHeight": "300px", "overflowY": "auto"},
            ),
            html.Div(
                "Top dimension gets highest weight. Click to reorder.",
                style={"fontSize": "11px", "color": "#9ca3af", "marginTop": "4px"},
            ),
        ]
    )


@app.callback(
    Output("finance-dimension-toggle", "children"),
    Input("weight-order", "data"),
    State("active-dimensions", "data"),
)
def build_dimension_toggle(weight_order, active_dimensions):
    """Build a checklist to toggle dimensions on/off."""
    if not weight_order:
        return no_update

    active = set(active_dimensions or weight_order)
    return html.Div(
        [
            html.H4("Active Dimensions", style={"margin": "16px 0 8px 0", "fontSize": "14px"}),
            dcc.Checklist(
                id="dimension-checklist",
                options=[{"label": DIMENSION_LABELS.get(d, d), "value": d} for d in weight_order],
                value=list(active),
                labelStyle={"display": "block", "margin": "2px 0", "fontSize": "13px"},
            ),
            html.Div(
                "Uncheck to remove from comparison.",
                style={"fontSize": "11px", "color": "#9ca3af", "marginTop": "4px"},
            ),
        ]
    )


@app.callback(
    Output("comparison-results", "data"),
    Output("agent-context", "data"),
    Input("dimension-checklist", "value"),
    State("weight-order", "data"),
    State("extracted-fields", "data"),
    prevent_initial_call=True,
)
def on_dimension_change(active_dims, weight_order, extracted_fields):
    """Recalculate comparison when dimensions are toggled."""
    if not active_dims or not extracted_fields or not weight_order:
        raise PreventUpdate

    # Filter weight_order to only active dimensions
    active_order = [d for d in weight_order if d in active_dims]
    if not active_order:
        raise PreventUpdate

    result = _compute_comparison(extracted_fields, active_order, set(active_dims))

    # Build agent context
    agent_ctx = {
        "top_5": [
            {"mission": m["mission_name"], "distance": m["distance"]}
            for m in result.get("top_n", [])
        ],
        "weights": result.get("weights", {}),
        "deltas": {
            m["mission_name"]: m.get("deltas", {})
            for m in result.get("top_n", [])[:3]
        },
    }

    return result, agent_ctx


@app.callback(
    Output("finance-chart-content", "children"),
    Input("finance-chart-tabs", "value"),
    State("comparison-results", "data"),
)
def render_finance_chart(tab, comparison_results):
    """Render the selected chart tab."""
    if not comparison_results:
        return html.Div("Run comparison first.", style={"color": "#999"})

    if tab == "radar":
        fig = _build_radar_chart(comparison_results)
    elif tab == "raw-bars":
        fig = _build_raw_bar_chart(comparison_results)
    elif tab == "delta-bars":
        fig = _build_delta_bar_chart(comparison_results)
    elif tab == "breakdown":
        fig = _build_distance_breakdown(comparison_results)
    else:
        fig = go.Figure()

    return dcc.Graph(figure=fig, config={"displayModeBar": True, "responsive": True})


# ===================== ENGINEER CALLBACKS =====================


@app.callback(
    Output("engineer-upload-v1-result", "children"),
    Output("engineer-extracted-v1", "data"),
    Input("engineer-upload-v1", "contents"),
    State("engineer-upload-v1", "filename"),
    prevent_initial_call=True,
)
def on_engineer_upload_v1(contents, filename):
    """Upload v1 for compliance/diff."""
    if not contents or not filename:
        return no_update, no_update

    client = app.server.test_client()
    resp = client.post("/demo/ingest", json={"contents": contents, "filename": filename})
    data = resp.get_json() or {}

    if data.get("error"):
        return html.Div(f"❌ {data['error']}", style={"color": "#ef4444"}), no_update

    fields = data.get("fields", {})
    return (
        html.Div(
            f"✅ v1: {filename} — {len(fields)} fields",
            style={"color": "#059669", "fontSize": "13px"},
        ),
        fields,
    )


@app.callback(
    Output("engineer-upload-v2-result", "children"),
    Output("engineer-extracted-v2", "data"),
    Input("engineer-upload-v2", "contents"),
    State("engineer-upload-v2", "filename"),
    prevent_initial_call=True,
)
def on_engineer_upload_v2(contents, filename):
    """Upload v2 for diff."""
    if not contents or not filename:
        return no_update, no_update

    client = app.server.test_client()
    resp = client.post("/demo/ingest", json={"contents": contents, "filename": filename})
    data = resp.get_json() or {}

    if data.get("error"):
        return html.Div(f"❌ {data['error']}", style={"color": "#ef4444"}), no_update

    fields = data.get("fields", {})
    return (
        html.Div(
            f"✅ v2: {filename} — {len(fields)} fields",
            style={"color": "#059669", "fontSize": "13px"},
        ),
        fields,
    )


@app.callback(
    Output("engineer-compliance-detail", "children"),
    Input("engineer-compliance-btn", "n_clicks"),
    State("engineer-extracted-v1", "data"),
    prevent_initial_call=True,
)
def on_compliance_check(n_clicks, extracted_fields):
    """Run compliance check on v1 extracted fields."""
    if not extracted_fields:
        raise PreventUpdate

    client = app.server.test_client()
    resp = client.post("/demo/compliance", json={"extracted_fields": extracted_fields})
    data = resp.get_json() or {}

    rules = data.get("rules", [])
    if not rules:
        return html.Div("No compliance results.", style={"color": "#999"})

    rows = []
    for rule in rules:
        name = rule.get("name", "Unknown")
        status = rule.get("status", "unknown")
        detail = rule.get("detail", "")

        if status == "pass":
            color = "#059669"
            bg = "#f0fdf4"
            icon = "✅"
        elif status == "warn":
            color = "#d97706"
            bg = "#fef3c7"
            icon = "⚠️"
        else:
            color = "#dc2626"
            bg = "#fef2f2"
            icon = "❌"

        rows.append(
            html.Tr(
                [
                    html.Td(icon, style={"width": "30px"}),
                    html.Td(name, style={"fontWeight": "bold"}),
                    html.Td(detail, style={"fontSize": "13px"}),
                ],
                style={"backgroundColor": bg},
            )
        )

    return html.Table(
        [
            html.Thead(
                html.Tr(
                    [
                        html.Th(""),
                        html.Th("Rule"),
                        html.Th("Detail"),
                    ]
                )
            ),
            html.Tbody(rows),
        ],
        style={
            "width": "100%",
            "borderCollapse": "collapse",
            "border": "1px solid #e5e7eb",
        },
    )


@app.callback(
    Output("engineer-diff-result", "children"),
    Input("engineer-diff-btn", "n_clicks"),
    State("engineer-extracted-v1", "data"),
    State("engineer-extracted-v2", "data"),
    prevent_initial_call=True,
)
def on_version_diff(n_clicks, v1_fields, v2_fields):
    """Compute diff between v1 and v2 extracted fields."""
    if not v1_fields or not v2_fields:
        raise PreventUpdate

    all_keys = sorted(set(list(v1_fields.keys()) + list(v2_fields.keys())))
    rows = []
    changes = 0

    for key in all_keys:
        v1_val = v1_fields.get(key)
        v2_val = v2_fields.get(key)
        label = DIMENSION_LABELS.get(key, key)

        if v1_val == v2_val:
            arrow = "="
            color = "#6b7280"
        elif v1_val is None:
            arrow = "→"
            color = "#059669"
            changes += 1
        elif v2_val is None:
            arrow = "←"
            color = "#dc2626"
            changes += 1
        else:
            try:
                pct = abs(float(v2_val) - float(v1_val)) / abs(float(v1_val)) * 100
                if pct > 5:
                    arrow = f"{'↑' if float(v2_val) > float(v1_val) else '↓'} {pct:.1f}%"
                    color = "#dc2626"
                else:
                    arrow = f"{'↑' if float(v2_val) > float(v1_val) else '↓'} {pct:.1f}%"
                    color = "#d97706"
            except (ValueError, ZeroDivisionError):
                arrow = "→"
                color = "#6b7280"
            changes += 1

        rows.append(
            html.Tr(
                [
                    html.Td(label, style={"fontWeight": "bold"}),
                    html.Td(str(v1_val or "—"), style={"textAlign": "center"}),
                    html.Td(str(v2_val or "—"), style={"textAlign": "center"}),
                    html.Td(arrow, style={"textAlign": "center", "color": color}),
                ]
            )
        )

    return html.Div(
        [
            html.Div(
                f"{changes} field changes detected",
                style={"fontWeight": "bold", "marginBottom": "8px"},
            ),
            html.Table(
                [
                    html.Thead(
                        html.Tr(
                            [
                                html.Th("Field"),
                                html.Th("v1"),
                                html.Th("v2"),
                                html.Th("Δ"),
                            ]
                        )
                    ),
                    html.Tbody(rows),
                ],
                style={
                    "width": "100%",
                    "borderCollapse": "collapse",
                    "border": "1px solid #e5e7eb",
                },
            ),
        ]
    )


# ===================== RISK CALLBACKS =====================


@app.callback(
    Output("risk-upload-1-result", "children"),
    Output("risk-register-data", "data"),
    Input("risk-upload-1", "contents"),
    State("risk-upload-1", "filename"),
    prevent_initial_call=True,
)
def on_risk_upload_1(contents, filename):
    """Upload first risk register."""
    if not contents or not filename:
        return no_update, no_update

    client = app.server.test_client()
    resp = client.post(
        "/demo/risk-register",
        json={"contents": contents, "filename": filename},
    )
    data = resp.get_json() or {}

    if data.get("error"):
        return html.Div(f"❌ {data['error']}", style={"color": "#ef4444"}), no_update

    risk_count = len(data.get("risks", []))
    return (
        html.Div(
            f"✅ {filename}: {risk_count} risks parsed",
            style={"color": "#059669", "fontSize": "13px"},
        ),
        data,
    )


@app.callback(
    Output("risk-upload-2-result", "children"),
    Output("risk-register-2-data", "data"),
    Input("risk-upload-2", "contents"),
    State("risk-upload-2", "filename"),
    prevent_initial_call=True,
)
def on_risk_upload_2(contents, filename):
    """Upload second risk register for cross-comparison."""
    if not contents or not filename:
        return no_update, no_update

    client = app.server.test_client()
    resp = client.post(
        "/demo/risk-register",
        json={"contents": contents, "filename": filename},
    )
    data = resp.get_json() or {}

    if data.get("error"):
        return html.Div(f"❌ {data['error']}", style={"color": "#ef4444"}), no_update

    risk_count = len(data.get("risks", []))
    return (
        html.Div(
            f"✅ {filename}: {risk_count} risks parsed",
            style={"color": "#059669", "fontSize": "13px"},
        ),
        data,
    )


@app.callback(
    Output("risk-chart-content", "children"),
    Input("risk-chart-tabs", "value"),
    State("risk-register-data", "data"),
    State("risk-register-2-data", "data"),
)
def render_risk_chart(tab, register1, register2):
    """Render risk visualizations based on active tab."""
    if not register1:
        return html.Div("Upload a risk register first.", style={"color": "#999"})

    risks = register1.get("risks", [])

    if tab == "heatmap":
        return _build_risk_heatmap(risks)
    elif tab == "scatter":
        return _build_risk_scatter(risks)
    elif tab == "tornado":
        return _build_risk_tornado(risks)
    elif tab == "correlation":
        return _build_correlation_scatter(risks, register2)
    else:
        return html.Div("Unknown tab", style={"color": "#999"})


def _build_risk_heatmap(risks):
    """Build 5x5 probability x impact heatmap."""
    # Count risks in each cell
    grid = {}
    for r in risks:
        prob = r.get("probability", 3)
        impact = r.get("impact", 3)
        key = (int(prob), int(impact))
        grid[key] = grid.get(key, 0) + 1

    z = [[grid.get((p, i), 0) for i in range(1, 6)] for p in range(1, 6)]

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=[1, 2, 3, 4, 5],
            y=[5, 4, 3, 2, 1],
            colorscale="YlOrRd",
            text=[[str(v) if v else "" for v in row] for row in z],
            texttemplate="%{text}",
            textfont={"size": 16},
        )
    )
    fig.update_layout(
        title="Risk Heatmap — Probability × Impact",
        xaxis_title="Impact (1-5)",
        yaxis_title="Probability (1-5)",
        height=400,
    )
    return dcc.Graph(figure=fig, config={"responsive": True})


def _build_risk_scatter(risks):
    """Scatter plot of all risks with probability vs impact."""
    probs = [r.get("probability", 3) for r in risks]
    impacts = [r.get("impact", 3) for r in risks]
    names = [r.get("title", f"Risk {i}")[:40] for i, r in enumerate(risks)]
    scores = [p * i for p, i in zip(probs, impacts)]

    fig = go.Figure(
        data=go.Scatter(
            x=impacts,
            y=probs,
            mode="markers+text",
            text=names,
            textposition="top center",
            marker=dict(
                size=[max(s, 8) for s in scores],
                color=scores,
                colorscale="RdYlGn_r",
                showscale=True,
                colorbar=dict(title="Risk Score"),
            ),
        )
    )
    fig.update_layout(
        title="Risk Scatter — Probability vs Impact",
        xaxis_title="Impact",
        yaxis_title="Probability",
        height=400,
    )
    return dcc.Graph(figure=fig, config={"responsive": True})


def _build_risk_tornado(risks):
    """Build uncertainty tornado chart for top N risks with three-point estimates."""
    from tools.risks.parser import build_tornado_chart

    return dcc.Graph(figure=build_tornado_chart(risks), config={"responsive": True})


def _build_correlation_scatter(risks, register2):
    """Cross-register correlation scatter of paired probabilities."""
    if not register2 or not register2.get("risks"):
        return html.Div("Upload second register for cross-comparison.", style={"color": "#999"})

    risks2 = register2.get("risks", [])

    # Simple title-based matching for demo
    from difflib import SequenceMatcher

    pairs = []
    for r1 in risks:
        t1 = r1.get("title", "").lower()
        best_match = None
        best_score = 0
        for r2 in risks2:
            t2 = r2.get("title", "").lower()
            score = SequenceMatcher(None, t1, t2).ratio()
            if score > best_score:
                best_score = score
                best_match = r2

        if best_score > 0.4:
            pairs.append((r1, best_match, best_score))

    if not pairs:
        return html.Div("No matching risks found between registers.", style={"color": "#999"})

    probs1 = [p[0].get("probability", 3) for p in pairs]
    probs2 = [p[1].get("probability", 3) for p in pairs]
    names = [p[0].get("title", "")[:40] for p in pairs]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=probs1,
            y=probs2,
            mode="markers+text",
            text=names,
            textposition="top center",
            marker=dict(size=10),
            name="Paired risks",
        )
    )
    # Diagonal line (perfect agreement)
    fig.add_trace(
        go.Scatter(
            x=[1, 5],
            y=[1, 5],
            mode="lines",
            line=dict(dash="dash", color="gray"),
            name="Agreement",
        )
    )
    fig.update_layout(
        title="Cross-Register Correlation — Probability Assessment",
        xaxis_title="Register 1 Probability",
        yaxis_title="Register 2 Probability",
        xaxis=dict(range=[0.5, 5.5]),
        yaxis=dict(range=[0.5, 5.5]),
        height=400,
    )
    return dcc.Graph(figure=fig, config={"responsive": True})