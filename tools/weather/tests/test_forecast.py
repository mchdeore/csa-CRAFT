"""Tests for tools/weather/forecast.py — WeatherTool with mock API responses."""

import json
from unittest.mock import MagicMock, patch

import pytest

from tools.weather.forecast import WeatherTool


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

MOCK_GEOCODING_URL = "http://fake-geo/api"
MOCK_FORECAST_URL = "http://fake-fc/api"


@pytest.fixture
def tool() -> WeatherTool:
    """Return a WeatherTool wired to fake URLs for safe unit testing."""
    return WeatherTool(
        geocoding_url=MOCK_GEOCODING_URL,
        forecast_url=MOCK_FORECAST_URL,
    )


@pytest.fixture
def geocoding_response() -> dict:
    """A valid Open-Meteo geocoding response for London."""
    return {
        "results": [
            {
                "id": 2643743,
                "name": "London",
                "latitude": 51.5074,
                "longitude": -0.1278,
                "country": "United Kingdom",
            }
        ]
    }


@pytest.fixture
def forecast_response() -> dict:
    """A minimal Open-Meteo hourly forecast response with 2 timesteps."""
    return {
        "hourly": {
            "time": ["2025-06-01T00:00", "2025-06-01T01:00"],
            "temperature_2m": [15.2, 14.8],
            "relative_humidity_2m": [72, 74],
            "wind_speed_10m": [12.3, 11.7],
            "weather_code": [1, 2],
        }
    }


@pytest.fixture
def empty_geocoding_response() -> dict:
    """A geocoding response with no results — city not found."""
    return {"results": []}


# ---------------------------------------------------------------------------
# _fetch tests
# ---------------------------------------------------------------------------


class TestFetchSuccess:
    """Test WeatherTool._fetch returns correct structure on success."""

    def test_returns_display_name_and_current_values(
        self, tool: WeatherTool, geocoding_response: dict, forecast_response: dict
    ) -> None:
        """_fetch geocodes the city, then fetches forecast, and bundles results."""
        with patch("tools.weather.forecast.req_mod.get") as mock_get:

            # Two call pattern: first geocode, then forecast
            mock_get.side_effect = [
                _fake_response(geocoding_response),
                _fake_response(forecast_response),
            ]

            result = tool._fetch("London")

        assert result["display_name"] == "London, United Kingdom"
        assert result["current_temp"] == 15.2
        assert result["current_humidity"] == 72
        assert result["current_wind"] == 12.3

        # Figure dict comes from Plotly — just check it exists
        assert "figure" in result
        assert isinstance(result["figure"], dict)


# ---------------------------------------------------------------------------
# execute tests
# ---------------------------------------------------------------------------


class TestExecute:
    """Test execute() returns the expected (tool_msg, rich_content_or_none) tuple."""

    def test_returns_tuple_with_rich_content_on_success(
        self, tool: WeatherTool, geocoding_response: dict, forecast_response: dict
    ) -> None:
        """On success, execute returns (tool_msg, rich_content_dict)."""
        with patch("tools.weather.forecast.req_mod.get") as mock_get:
            mock_get.side_effect = [
                _fake_response(geocoding_response),
                _fake_response(forecast_response),
            ]

            tool_msg, rich = tool.execute(
                {"city": "London", "country": "GB", "tool_call_id": "call_1"}
            )

        # tool_msg structure
        assert tool_msg["role"] == "tool_result"
        result = json.loads(tool_msg["content"]["result"])
        assert result["city"] == "London, United Kingdom"
        assert "current_temp" in result

        # rich_content structure
        assert rich is not None
        assert rich["role"] == "rich_content"
        assert rich["content"]["type"] == "chart"
        assert "London" in rich["content"]["title"]
        assert "figure" in rich["content"]

    def test_returns_tuple_with_none_rich_on_geocode_failure(
        self, tool: WeatherTool, empty_geocoding_response: dict
    ) -> None:
        """When geocoding returns no results, execute returns (tool_msg, None)."""
        with patch("tools.weather.forecast.req_mod.get") as mock_get:
            mock_get.return_value = _fake_response(empty_geocoding_response)

            tool_msg, rich = tool.execute(
                {"city": "NowhereTown", "tool_call_id": "call_2"}
            )

        assert rich is None
        result = json.loads(tool_msg["content"]["result"])
        assert "error" in result
        assert "not found" in result["error"]


# ---------------------------------------------------------------------------
# _geocode tests
# ---------------------------------------------------------------------------


class TestGeocode:
    """Test _geocode — city lookup from Open-Meteo geocoding API."""

    def test_returns_location_dict(self, tool: WeatherTool, geocoding_response: dict) -> None:
        """Successful geocoding extracts lat, lon, and display_name."""
        with patch("tools.weather.forecast.req_mod.get") as mock_get:
            mock_get.return_value = _fake_response(geocoding_response)

            location = tool._geocode("London")

        assert location is not None
        assert location["lat"] == 51.5074
        assert location["lon"] == -0.1278
        assert location["display_name"] == "London, United Kingdom"

    def test_returns_none_when_no_results(
        self, tool: WeatherTool, empty_geocoding_response: dict
    ) -> None:
        """When API returns empty results list, _geocode returns None."""
        with patch("tools.weather.forecast.req_mod.get") as mock_get:
            mock_get.return_value = _fake_response(empty_geocoding_response)

            location = tool._geocode("Atlantis")

        assert location is None


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


class TestErrorHandling:
    """Verify error paths in _fetch and execute."""

    def test_fetch_returns_error_on_request_exception(self, tool: WeatherTool) -> None:
        """A requests.RequestException in _fetch produces an error dict."""
        with patch("tools.weather.forecast.req_mod.get") as mock_get:
            mock_get.side_effect = __import__("requests").exceptions.ConnectionError(
                "no network"
            )

            result = tool._fetch("Paris")

        assert "error" in result
        assert "Weather API request failed" in result["error"]

    def test_geocode_failure_returns_error_in_execute(
        self, tool: WeatherTool, empty_geocoding_response: dict
    ) -> None:
        """execute converts a geocoding miss into an error tool_msg, no rich content."""
        with patch("tools.weather.forecast.req_mod.get") as mock_get:
            mock_get.return_value = _fake_response(empty_geocoding_response)

            tool_msg, rich = tool.execute(
                {"city": "Xyzzy", "tool_call_id": "call_3"}
            )

        assert rich is None
        assert tool_msg["role"] == "tool_result"
        parsed = json.loads(tool_msg["content"]["result"])
        assert "error" in parsed
        assert "not found" in parsed["error"]


# ---------------------------------------------------------------------------
# definition tests
# ---------------------------------------------------------------------------


class TestDefinition:
    """Ensure the tool definition matches the expected function-calling schema."""

    def test_definition_has_expected_structure(self, tool: WeatherTool) -> None:
        """definition() returns a valid function-calling descriptor."""
        definition = tool.definition()

        assert definition["type"] == "function"
        func = definition["function"]
        assert func["name"] == "get_weather"
        assert "city" in func["parameters"]["properties"]
        assert func["parameters"]["required"] == ["city"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fake_response(json_body: dict) -> MagicMock:
    """Build a mock requests.Response with a .json() that returns json_body."""
    mock_resp = MagicMock()
    mock_resp.json.return_value = json_body
    mock_resp.raise_for_status.return_value = None
    return mock_resp