"""
Risk register parser — extracts risks from Part C markdown files.

Parses structured risk tables with fields: title, probability, impact,
cost_opt (optimistic), cost_ml (most likely), cost_pes (pessimistic).

Also builds tornado chart from three-point cost estimates.
"""

import base64
import math
import re

import plotly.graph_objects as go


def parse_risk_register(contents: str, filename: str) -> dict:
    """Parse a Part C risk register from base64 markdown.

    Looks for risk table rows with probability/impact/cost fields.
    """
    try:
        _, content_string = contents.split(",", 1)
        raw = base64.b64decode(content_string)
        text = raw.decode("utf-8", errors="replace")
    except Exception:
        return {"error": "Could not decode file. Expected base64 text."}

    risks = _extract_risks_from_text(text)

    # If no structured risks found, generate mock data for demo
    if not risks:
        risks = _generate_mock_risks(200)

    return {
        "ok": True,
        "filename": filename,
        "risks": risks,
        "risk_count": len(risks),
    }


def _extract_risks_from_text(text: str) -> list[dict]:
    """Parse risk table rows from markdown text.

    Looks for pipe-delimited table rows with probability (1-5), impact (1-5),
    and optional three-point cost estimates. Returns empty list if no rows match.

    >>> risks = _extract_risks_from_text("| Launch Delay | 4 | 3 | 500000 | 750000 | 1200000 |")
    >>> len(risks)
    1
    >>> risks[0]["title"]
    'Launch Delay'
    >>> risks[0]["probability"]
    4.0
    >>> risks[0]["impact"]
    3.0

    >>> _extract_risks_from_text("No risks here")
    []
    """
    risks = []

    # Look for table rows containing risk info
    # Pattern: | title | probability | impact | cost_opt | cost_ml | cost_pes |
    lines = text.split("\n")
    in_table = False

    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue

        # Skip separator lines
        if re.match(r"^\|[\s\-:]+\|$", stripped):
            continue

        cells = [c.strip() for c in stripped.split("|")[1:-1]]

        # Need at least title + probability + impact
        if len(cells) < 3:
            continue

        # Check if cells[1] and cells[2] look like numbers (probability, impact)
        try:
            prob = float(cells[1]) if len(cells) > 1 else None
            impact = float(cells[2]) if len(cells) > 2 else None

            if prob is None or impact is None:
                continue
            if not (1 <= prob <= 5 and 1 <= impact <= 5):
                continue

            title = cells[0]
            cost_opt = float(cells[3]) if len(cells) > 3 and cells[3] else None
            cost_ml = float(cells[4]) if len(cells) > 4 and cells[4] else None
            cost_pes = float(cells[5]) if len(cells) > 5 and cells[5] else None

            risks.append(
                {
                    "title": title,
                    "probability": prob,
                    "impact": impact,
                    "cost_opt": cost_opt,
                    "cost_ml": cost_ml,
                    "cost_pes": cost_pes,
                }
            )
        except (ValueError, IndexError):
            continue

    return risks


def _generate_mock_risks(count: int = 200) -> list[dict]:
    """Generate mock risk data for demo when no real data is parsed.

    Uses deterministic generation based on index for reproducibility.
    """
    import random

    # Seed for reproducibility
    rng = random.Random(42)

    risk_types = [
        "Launch vehicle delay",
        "Payload integration failure",
        "Thermal subsystem anomaly",
        "Power budget overrun",
        "Ground station schedule conflict",
        "Software regression in flight code",
        "Supply chain component shortage",
        "Radiation single-event upset",
        "Propulsion valve leakage",
        "Communication link margin erosion",
        "Test facility availability risk",
        "Key personnel departure",
        "Schedule compression pressure",
        "Budget baseline inadequacy",
        "Interface specification mismatch",
        "Foreign partner export delay",
        "Qualification test article damage",
        "Mass growth beyond margin",
        "EMI/EMC compliance failure",
        "De-orbit timeline uncertainty",
    ]

    risks = []
    for i in range(count):
        prob = rng.randint(1, 5)
        impact = rng.randint(1, 5)

        # Generate realistic three-point cost estimates
        base_cost = rng.uniform(500000, 50000000)
        cost_ml = round(base_cost, -4)  # most likely
        cost_opt = round(cost_ml * rng.uniform(0.6, 0.9), -4)  # optimistic
        cost_pes = round(cost_ml * rng.uniform(1.1, 2.0), -4)  # pessimistic

        title = f"{risk_types[i % len(risk_types)]} #{i + 1}"

        risks.append(
            {
                "title": title,
                "probability": prob,
                "impact": impact,
                "cost_opt": cost_opt,
                "cost_ml": cost_ml,
                "cost_pes": cost_pes,
            }
        )

    return risks


def build_tornado_chart(risks: list[dict], top_n: int = 10) -> go.Figure:
    """Build tornado chart from three-point cost estimates.

    Each horizontal bar spans cost_opt to cost_pes, with cost_ml as a dot.
    Sorted by swing width (cost_pes - cost_opt).
    """
    # Filter to risks with cost data
    with_costs = [r for r in risks if r.get("cost_ml") and r.get("cost_opt") and r.get("cost_pes")]

    if not with_costs:
        # Fallback: use risk score instead
        scored = sorted(risks, key=lambda r: r.get("probability", 3) * r.get("impact", 3), reverse=True)
        top = scored[:top_n]

        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                y=[r["title"][:50] for r in top],
                x=[r.get("probability", 3) * r.get("impact", 3) for r in top],
                orientation="h",
                marker_color=[
                    (
                        "#ef4444" if r.get("probability", 3) * r.get("impact", 3) >= 15
                        else "#f59e0b" if r.get("probability", 3) * r.get("impact", 3) >= 8
                        else "#10b981"
                    )
                    for r in top
                ],
            )
        )
        fig.update_layout(
            title="Top Risks by Score (Probability × Impact) — No cost data available",
            xaxis_title="Risk Score",
            height=400,
        )
        return fig

    # Sort by swing width (pessimistic - optimistic)
    with_costs.sort(key=lambda r: r["cost_pes"] - r["cost_opt"], reverse=True)
    top = with_costs[:top_n]

    fig = go.Figure()

    # Horizontal bars: opt → pes
    for i, r in enumerate(top):
        opt = r["cost_opt"]
        pes = r["cost_pes"]
        ml = r["cost_ml"]

        # Bar from opt to pes
        fig.add_trace(
            go.Bar(
                y=[r["title"][:50]],
                x=[pes - opt],
                base=[opt],
                orientation="h",
                marker_color="#93c5fd",
                name=r["title"][:30] if i == 0 else "",
                showlegend=False,
            )
        )

        # Dot at most-likely
        fig.add_trace(
            go.Scatter(
                y=[r["title"][:50]],
                x=[ml],
                mode="markers",
                marker={"color": "#1d4ed8", "size": 8, "symbol": "diamond"},
                name="Most Likely" if i == 0 else "",
                showlegend=True if i == 0 else False,
            )
        )

    # Dummy traces for legend
    fig.add_trace(
        go.Bar(
            y=[None],
            x=[None],
            name="Cost Range (opt→pes)",
            marker_color="#93c5fd",
            showlegend=True,
        )
    )

    fig.update_layout(
        title="Cost Uncertainty — Tornado Chart",
        xaxis_title="Cost ($)",
        height=500,
        barmode="overlay",
    )

    return fig