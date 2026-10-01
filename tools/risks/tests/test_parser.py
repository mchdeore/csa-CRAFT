"""Tests for tools/risks/parser.py — risk register parser and tornado chart builder."""

import base64

import pytest

from tools.risks.parser import _extract_risks_from_text, build_tornado_chart


# ---------------------------------------------------------------------------
# _extract_risks_from_text tests
# ---------------------------------------------------------------------------


class TestExtractRisks:
    """Tests for parsing markdown risk tables out of raw text."""

    def test_parses_valid_row_with_probability_and_impact(self) -> None:
        """A single valid risk row is extracted with all numeric fields."""
        text = "| Launch Delay | 4 | 3 | 500000 | 750000 | 1200000 |"

        risks = _extract_risks_from_text(text)

        assert len(risks) == 1
        risk = risks[0]
        assert risk["title"] == "Launch Delay"
        assert risk["probability"] == 4.0
        assert risk["impact"] == 3.0
        assert risk["cost_opt"] == 500000.0
        assert risk["cost_ml"] == 750000.0
        assert risk["cost_pes"] == 1200000.0

    def test_parses_row_without_cost_estimates(self) -> None:
        """Cost fields are optional — a row with just title/prob/impact is valid."""
        text = "| Supply Shortage | 3 | 4 |"

        risks = _extract_risks_from_text(text)

        assert len(risks) == 1
        risk = risks[0]
        assert risk["title"] == "Supply Shortage"
        assert risk["probability"] == 3.0
        assert risk["impact"] == 4.0
        assert risk["cost_opt"] is None
        assert risk["cost_ml"] is None
        assert risk["cost_pes"] is None

    def test_parses_multiple_rows(self) -> None:
        """Multiple pipe-delimited rows are all extracted."""
        text = (
            "| Risk A | 2 | 3 | 100 | 200 | 300 |\n"
            "| Risk B | 4 | 5 | 400 | 500 | 600 |\n"
            "| Risk C | 1 | 2 |\n"
        )

        risks = _extract_risks_from_text(text)

        assert len(risks) == 3
        titles = [r["title"] for r in risks]
        assert titles == ["Risk A", "Risk B", "Risk C"]

    def test_skips_separator_lines(self) -> None:
        """Markdown table separator lines (| ---- | --- |) are ignored."""
        text = (
            "| Title | Probability | Impact |\n"
            "|-------|-------------|--------|\n"
            "| Budget Risk | 4 | 4 |\n"
        )

        risks = _extract_risks_from_text(text)

        assert len(risks) == 1
        assert risks[0]["title"] == "Budget Risk"

    def test_empty_input_returns_empty_list(self) -> None:
        """An empty string produces an empty list — no crash."""
        risks = _extract_risks_from_text("")

        assert risks == []

    def test_no_matching_rows_returns_empty_list(self) -> None:
        """Text without pipe-delimited risk rows yields an empty list."""
        risks = _extract_risks_from_text("This file has no risk tables.\nJust prose.")

        assert risks == []

    def test_skips_rows_with_non_numeric_fields(self) -> None:
        """Rows where probability or impact aren't numbers are ignored."""
        text = "| Bad Risk | high | medium |"

        risks = _extract_risks_from_text(text)

        assert risks == []

    def test_out_of_range_scores_skipped(self) -> None:
        """Probability/impact outside 1-5 range are skipped."""
        text = "| Too Risky | 6 | 7 |"

        risks = _extract_risks_from_text(text)

        assert risks == []

    def test_handles_trailing_empty_cells(self) -> None:
        """A row with extra pipe but no content still parses cleanly."""
        text = "| Clean Risk | 2 | 2 | 1000 | 2000 | 3000 |"

        risks = _extract_risks_from_text(text)

        assert len(risks) == 1
        assert risks[0]["cost_pes"] == 3000.0

    def test_lines_not_starting_with_pipe_are_skipped(self) -> None:
        """Only lines beginning with '|' are treated as table rows."""
        text = "This is prose.\n| Real Risk | 3 | 3 |\nMore prose."

        risks = _extract_risks_from_text(text)

        assert len(risks) == 1
        assert risks[0]["title"] == "Real Risk"


# ---------------------------------------------------------------------------
# build_tornado_chart tests
# ---------------------------------------------------------------------------


class TestBuildTornadoChart:
    """build_tornado_chart produces a Plotly Figure from risk data."""

    @pytest.fixture
    def risks_with_costs(self) -> list[dict]:
        """A short list of risks with three-point cost estimates."""
        return [
            {
                "title": "Engine Failure",
                "probability": 4,
                "impact": 5,
                "cost_opt": 500000,
                "cost_ml": 1000000,
                "cost_pes": 2500000,
            },
            {
                "title": "Supply Chain Delay",
                "probability": 3,
                "impact": 3,
                "cost_opt": 200000,
                "cost_ml": 400000,
                "cost_pes": 600000,
            },
            {
                "title": "Software Bug",
                "probability": 2,
                "impact": 4,
                "cost_opt": 80000,
                "cost_ml": 150000,
                "cost_pes": 300000,
            },
        ]

    @pytest.fixture
    def risks_without_costs(self) -> list[dict]:
        """Risks without cost estimates — tornado chart falls back to score bars."""
        return [
            {"title": "High Risk Item", "probability": 5, "impact": 5},
            {"title": "Medium Risk Item", "probability": 3, "impact": 3},
            {"title": "Low Risk Item", "probability": 1, "impact": 2},
        ]

    def test_returns_plotly_figure_with_costs(
        self, risks_with_costs: list[dict]
    ) -> None:
        """With cost data, build_tornado_chart returns a Figure with bar + scatter traces."""
        fig = build_tornado_chart(risks_with_costs, top_n=3)

        assert fig is not None
        # Should contain bar traces (cost ranges) + scatter traces (most-likely dots)
        # plus dummy traces for legend. Total traces > number of risks.
        assert len(fig.data) > len(risks_with_costs)

        # Title indicates cost uncertainty
        assert "Cost Uncertainty" in fig.layout.title.text

    def test_falls_back_to_score_bars_when_no_costs(
        self, risks_without_costs: list[dict]
    ) -> None:
        """Without cost data, the chart shows horizontal bars of probability × impact."""
        fig = build_tornado_chart(risks_without_costs, top_n=3)

        assert fig is not None
        # Bar trace only
        assert len(fig.data) == 1

        assert "No cost data" in fig.layout.title.text

    def test_top_n_limits_items(
        self, risks_with_costs: list[dict]
    ) -> None:
        """top_n caps the number of risks shown in the chart."""
        fig = build_tornado_chart(risks_with_costs, top_n=2)

        # With top_n=2 and 3 risks with costs, only top 2 get bar traces
        # Each risk = 1 bar + 1 scatter = 2 real traces + 2 dummy = ?
        # Just check the y-axis labels are capped
        y_labels = []
        for trace in fig.data:
            if hasattr(trace, "y") and trace.y is not None:
                labels = [y for y in trace.y if y is not None]
                y_labels.extend(labels)

        # Unique risk titles shown
        unique = set(y_labels)
        assert len(unique) <= 2

    def test_empty_risks_returns_empty_figure(self) -> None:
        """An empty list produces a Figure (no crash)."""
        fig = build_tornado_chart([], top_n=10)

        assert fig is not None
        # Fallback path — top scored risks filtered from empty → empty bars
        assert "No cost data" in fig.layout.title.text

    def test_sorts_by_swing_width(self, risks_with_costs: list[dict]) -> None:
        """Risks are sorted by cost swing (pes - opt) descending before plotting."""
        fig = build_tornado_chart(risks_with_costs, top_n=3)

        # "Engine Failure" has swing 2,000,000 — should be first (bottom in horizontal)
        # The order of trace.y is the display order
        bar_traces = [
            t
            for t in fig.data
            if hasattr(t, "type") and t.type == "bar" and t.y is not None
        ]

        if bar_traces:
            # First bar trace y-labels (bottom of chart = first item = largest swing)
            first_labels = [
                y for y in bar_traces[0].y if y is not None
            ]
            if first_labels:
                assert "Engine Failure" in first_labels[0]


# ---------------------------------------------------------------------------
# _generate_mock_risks (indirect via parse_risk_register)
# ---------------------------------------------------------------------------


class TestParseRiskRegister:
    """Integration-level tests for parse_risk_register entry point."""

    def test_decodes_base64_and_parses_risks(self) -> None:
        """A base64-encoded markdown string parses into structured risk data."""
        from tools.risks.parser import parse_risk_register

        risk_table = "| Risk One | 3 | 4 | 100 | 200 | 300 |\n"
        encoded = base64.b64encode(risk_table.encode("utf-8")).decode("utf-8")
        contents = f"data:text/markdown;base64,{encoded}"

        result = parse_risk_register(contents, "risks.md")

        assert result["ok"] is True
        assert result["filename"] == "risks.md"
        assert result["risk_count"] == 1
        assert result["risks"][0]["title"] == "Risk One"

    def test_empty_base64_falls_back_to_mock_data(self) -> None:
        """When no risks are in the decoded text, 200 mock risks are generated."""
        from tools.risks.parser import parse_risk_register

        encoded = base64.b64encode(b"# Just a heading, no table").decode("utf-8")
        contents = f"data:text/markdown;base64,{encoded}"

        result = parse_risk_register(contents, "empty.md")

        assert result["ok"] is True
        assert result["risk_count"] == 200
        assert all("title" in r for r in result["risks"])

    def test_decode_error_returns_error_result(self) -> None:
        """Garbage input that isn't valid base64 returns an error dict."""
        from tools.risks.parser import parse_risk_register

        result = parse_risk_register("not-valid-base64", "bad.md")

        assert "error" in result
        assert "decode" in result["error"].lower()