"""Tests for tools/weather/historical.py — HistoricalWeatherTool with mock API responses."""

import json
from unittest.mock import MagicMock, patch

import pytest

from tools.weather.historical import HistoricalWeatherTool, _dominant_dir


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

MOCK_GEOCODING_URL = "http://fake-geo/api"
MOCK_ARCHIVE_URL = "http://fake-archive/api"


@pytest.fixture
def tool() -> HistoricalWeatherTool:
    """HistoricalWeatherTool wired to fake URLs for unit testing."""
    return HistoricalWeatherTool(
        geocoding_url=MOCK_GEOCODING_URL,
        archive_url=MOCK_ARCHIVE_URL,
    )


@pytest.fixture
def geocoding_response() -> dict:
    """Valid Open-Meteo geocoding for Montreal."""
    return {
        "results": [
            {
                "name": "Montreal",
                "latitude": 45.5017,
                "longitude": -73.5673,
                "country": "Canada",
            }
        ]
    }


@pytest.fixture
def archive_response() -> dict:
    """Minimal Open-Meteo archive response with 2 hourly timesteps."""
    return {
        "hourly": {
            "time": ["2024-07-01T00:00", "2024-07-01T01:00"],
            "temperature_2m": [22.0, 21.5],
            "relative_humidity_2d": [65, 67],
            "precipitation": [0.0, 0.2],
            "wind_speed_10m": [10.0, 12.0],
            "wind_direction_10m": [180, 200],
            "uv_index": [5.0, 4.5],
            "weather_code": [0, 1],
        }
    }


# ---------------------------------------------------------------------------
# _fetch tests
# ---------------------------------------------------------------------------


class TestFetchSuccess:
    """Verify _fetch returns correct summary fields from archive data."""

    def test_returns_summary_for_valid_city_and_date(
        self,
        tool: HistoricalWeatherTool,
        geocoding_response: dict,
        archive_response: dict,
    ) -> None:
        """_fetch geocodes, then fetches archive, and produces a summary dict."""
        with patch("tools.weather.historical.req_mod.get") as mock_get:
            mock_get.side_effect = [
                _fake_response(geocoding_response),
                _fake_response(archive_response),
            ]

            result = tool._fetch("Montreal", "CA", "2024-07-01")

        assert result["display_name"] == "Montreal, Canada"
        assert result["date"] == "2024-07-01"
        assert result["high_temp"] == 22.0
        assert result["low_temp"] == 21.5
        assert result["max_uv"] == 5.0
        assert result["total_precipitation"] == 0.2
        assert result["dominant_wind_direction"] in ("S", "SW")
        assert "charts" in result
        assert len(result["charts"]) == 4  # temp, uv, wind, precipitation

    def test_fetch_without_country_code(
        self,
        tool: HistoricalWeatherTool,
        geocoding_response: dict,
        archive_response: dict,
    ) -> None:
        """Country code is optional — _fetch works with just city + date."""
        with patch("tools.weather.historical.req_mod.get") as mock_get:
            mock_get.side_effect = [
                _fake_response(geocoding_response),
                _fake_response(archive_response),
            ]

            result = tool._fetch("Montreal", "", "2024-07-01")

        assert "error" not in result
        assert result["display_name"] == "Montreal, Canada"


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


class TestFetchErrors:
    """Verify error paths for invalid dates, missing cities, and API failures."""

    def test_invalid_date_format_returns_error(self, tool: HistoricalWeatherTool) -> None:
        """Dates must be YYYY-MM-DD; anything else yields an error dict."""
        result = tool._fetch("Montreal", "", "July-1-2024")

        assert "error" in result
        assert "Invalid date" in result["error"]

    def test_geocoding_miss_returns_error(self, tool: HistoricalWeatherTool) -> None:
        """An empty geocoding result produces a clear error message."""
        with patch("tools.weather.historical.req_mod.get") as mock_get:
            mock_get.return_value = _fake_response({"results": []})

            result = tool._fetch("Narnia", "", "2024-07-01")

        assert "error" in result
        assert "not found" in result["error"]

    def test_api_request_exception_returns_error(self, tool: HistoricalWeatherTool) -> None:
        """A network-level exception is caught and turned into an error dict."""
        with patch("tools.weather.historical.req_mod.get") as mock_get:
            mock_get.side_effect = __import__("requests").exceptions.Timeout(
                "timed out"
            )

            result = tool._fetch("Paris", "", "2024-07-01")

        assert "error" in result
        assert "Weather API request failed" in result["error"]


# ---------------------------------------------------------------------------
# execute tests
# ---------------------------------------------------------------------------


class TestExecute:
    """execute() returns a (tool_msg, rich_content_or_none) tuple."""

    def test_success_returns_tuple_with_rich_content(
        self,
        tool: HistoricalWeatherTool,
        geocoding_response: dict,
        archive_response: dict,
    ) -> None:
        """On a successful fetch, execute bundles summary and chart_bundle."""
        with patch("tools.weather.historical.req_mod.get") as mock_get:
            mock_get.side_effect = [
                _fake_response(geocoding_response),
                _fake_response(archive_response),
            ]

            tool_msg, rich = tool.execute(
                {
                    "city": "Montreal",
                    "date": "2024-07-01",
                    "tool_call_id": "call_h1",
                }
            )

        # tool_msg
        assert tool_msg["role"] == "tool_result"
        summary = json.loads(tool_msg["content"]["result"])
        assert summary["city"] == "Montreal, Canada"
        assert summary["date"] == "2024-07-01"
        assert "high_temp" in summary

        # rich_content
        assert rich is not None
        assert rich["role"] == "rich_content"
        assert rich["content"]["type"] == "chart_bundle"
        assert len(rich["content"]["charts"]) == 4

    def test_error_returns_tuple_with_none_rich(
        self, tool: HistoricalWeatherTool
    ) -> None:
        """On any error, execute returns (error_tool_msg, None)."""
        tool_msg, rich = tool.execute(
            {"city": "Montreal", "date": "bad-date", "tool_call_id": "call_h2"}
        )

        assert rich is None
        parsed = json.loads(tool_msg["content"]["result"])
        assert "error" in parsed


# ---------------------------------------------------------------------------
# _dominant_dir unit tests
# ---------------------------------------------------------------------------


class TestDominantDir:
    """Unit tests for the wind-direction bucketing helper."""

    def test_empty_list_returns_na(self) -> None:
        """An empty list yields 'N/A'."""
        assert _dominant_dir([]) == "N/A"

    def test_north(self) -> None:
        """Directions averaging between 0 and 45 map to N."""
        assert _dominant_dir([10, 20, 30]) == "N"

    def test_south(self) -> None:
        """Directions averaging between 180 and 225 map to S."""
        assert _dominant_dir([185, 190]) == "S"

    def test_northwest(self) -> None:
        """Directions averaging between 315 and 360 map to NW."""
        assert _dominant_dir([330, 340]) == "NW"


# ---------------------------------------------------------------------------
# definition tests
# ---------------------------------------------------------------------------


class TestDefinition:
    """definition() schema check."""

    def test_definition_has_required_params(self, tool: HistoricalWeatherTool) -> None:
        """The definition requires city and date."""
        definition = tool.definition()

        func = definition["function"]
        assert func["name"] == "get_historical_weather"
        assert "city" in func["parameters"]["properties"]
        assert "date" in func["parameters"]["properties"]
        assert set(func["parameters"]["required"]) == {"city", "date"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fake_response(json_body: dict) -> MagicMock:
    mock_resp = MagicMock()
    mock_resp.json.return_value = json_body
    mock_resp.raise_for_status.return_value = None
    return mock_resp