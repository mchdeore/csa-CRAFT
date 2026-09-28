"""Weather forecast tool — Open-Meteo API."""

import json
from typing import Any

import requests as req_mod

from app.core.logging import log_function_call


class WeatherTool:
    """Fetch weather forecast from Open-Meteo and build a Plotly chart."""

    def __init__(self, geocoding_url: str, forecast_url: str) -> None:
        self._geocoding_url = geocoding_url
        self._forecast_url = forecast_url

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get weather forecast for a city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "City name, e.g. 'London'",
                        },
                        "country": {
                            "type": "string",
                            "description": "Optional country code, e.g. 'GB'",
                        },
                    },
                    "required": ["city"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        city = args.get("city", "")
        country = args.get("country", "")
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.weather.forecast",
            "execute",
            city=city,
            country=country,
            source="agent_or_route",
        )

        result = self._fetch(city, country)
        if "error" in result:
            log_function_call(
                "tools.weather.forecast",
                "execute",
                step="error",
                error=result["error"][:200],
            )
            return self._build_error(tool_call_id, result), None

        tool_msg = self._build_tool_msg(tool_call_id, result)
        rich = {
            "role": "rich_content",
            "content": {
                "type": "chart",
                "title": f"Weather — {result['display_name']}",
                "figure": result["figure"],
            },
        }
        log_function_call(
            "tools.weather.forecast",
            "execute",
            step="complete",
            city=result["display_name"],
        )
        return tool_msg, rich

    def _build_error(self, tool_call_id: str, result: dict) -> dict[str, Any]:
        return {
            "role": "tool_result",
            "content": {"tool_call_id": tool_call_id, "result": json.dumps(result)},
        }

    def _build_tool_msg(self, tool_call_id: str, result: dict) -> dict[str, Any]:
        summary = json.dumps(
            {
                "city": result["display_name"],
                "current_temp": result["current_temp"],
                "current_humidity": result["current_humidity"],
                "current_wind": result["current_wind"],
            }
        )
        return {
            "role": "tool_result",
            "content": {"tool_call_id": tool_call_id, "result": summary},
        }

    def _fetch(self, city: str, country: str = "") -> dict[str, Any]:
        try:
            location = self._geocode(city)
            if location is None:
                return {"error": f"City '{city}' not found."}
            return self._fetch_forecast(location)
        except req_mod.RequestException as e:
            return {"error": f"Weather API request failed: {e}."}
        except Exception as e:
            return {"error": f"Failed to process weather data: {e}"}

    def _geocode(self, city: str) -> dict[str, Any] | None:
        log_function_call("tools.weather.forecast", "_geocode", city=city)
        geo_params = {"name": city, "count": 1, "language": "en", "format": "json"}
        geo_resp = req_mod.get(self._geocoding_url, params=geo_params, timeout=10)
        geo_resp.raise_for_status()
        geo_data = geo_resp.json()
        results = geo_data.get("results", [])
        if not results:
            return None
        loc = results[0]
        name = loc.get("name", city)
        country_name = loc.get("country", "")
        return {
            "lat": loc["latitude"],
            "lon": loc["longitude"],
            "display_name": f"{name}, {country_name}" if country_name else name,
        }

    def _fetch_forecast(self, location: dict) -> dict[str, Any]:
        lat, lon = location["lat"], location["lon"]
        display_name = location["display_name"]
        log_function_call(
            "tools.weather.forecast",
            "_fetch_forecast",
            lat=lat,
            lon=lon,
            display_name=display_name,
        )
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
            "forecast_days": 3,
            "timezone": "auto",
        }
        fc_resp = req_mod.get(self._forecast_url, params=params, timeout=10)
        fc_resp.raise_for_status()
        hourly = fc_resp.json()["hourly"]
        figure = _build_forecast_figure(hourly, display_name)
        return {
            "display_name": display_name,
            "figure": figure,
            "current_temp": hourly["temperature_2m"][0],
            "current_humidity": hourly["relative_humidity_2m"][0],
            "current_wind": hourly["wind_speed_10m"][0],
        }


def _build_forecast_figure(hourly: dict, display_name: str) -> dict[str, Any]:
    from plotly.subplots import make_subplots

    times = hourly["time"]
    fig = make_subplots(
        rows=3,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.08,
        subplot_titles=("Temperature (°C)", "Humidity (%)", "Wind Speed (km/h)"),
    )
    _add_temp_trace(fig, times, hourly["temperature_2m"])
    _add_humidity_trace(fig, times, hourly["relative_humidity_2m"])
    _add_wind_trace(fig, times, hourly["wind_speed_10m"])
    fig.update_layout(
        title=f"Weather Forecast — {display_name}",
        height=600,
        showlegend=False,
        margin=dict(l=40, r=20, t=60, b=40),
    )
    return fig.to_dict()


def _add_temp_trace(fig: Any, times: list, temps: list) -> None:
    import plotly.graph_objects as go

    fig.add_trace(
        go.Scatter(
            x=times, y=temps, mode="lines", name="Temperature", line=dict(color="#ef4444", width=2)
        ),
        row=1,
        col=1,
    )


def _add_humidity_trace(fig: Any, times: list, humidity: list) -> None:
    import plotly.graph_objects as go

    fig.add_trace(
        go.Scatter(
            x=times, y=humidity, mode="lines", name="Humidity", line=dict(color="#3b82f6", width=2)
        ),
        row=2,
        col=1,
    )


def _add_wind_trace(fig: Any, times: list, wind: list) -> None:
    import plotly.graph_objects as go

    fig.add_trace(
        go.Scatter(x=times, y=wind, mode="lines", name="Wind", line=dict(color="#10b981", width=2)),
        row=3,
        col=1,
    )
