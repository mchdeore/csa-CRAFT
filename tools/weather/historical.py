"""Historical weather tool — Open-Meteo Archive API."""

import json
from datetime import datetime
from typing import Any

import requests as req_mod

from app.core.logging import log_function_call

WIND_DIR_BUCKETS = {
    (0, 45): "N",
    (45, 90): "NE",
    (90, 135): "E",
    (135, 180): "SE",
    (180, 225): "S",
    (225, 270): "SW",
    (270, 315): "W",
    (315, 360): "NW",
}


class HistoricalWeatherTool:
    """Fetch historical weather data from Open-Meteo Archive API and build Plotly charts."""

    def __init__(self, geocoding_url: str, archive_url: str) -> None:
        self._geocoding_url = geocoding_url
        self._archive_url = archive_url

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_historical_weather",
                "description": (
                    "Get historical weather data for a city on a specific past date. "
                    "Returns temperature, humidity, UV index, wind direction, "
                    "wind speed, and precipitation. Builds interactive charts."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "City name, e.g. 'Montreal' or 'Toronto'",
                        },
                        "country": {
                            "type": "string",
                            "description": "Optional country code, e.g. 'CA' or 'US'",
                        },
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format, e.g. '2024-07-01'",
                        },
                    },
                    "required": ["city", "date"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        city = args.get("city", "")
        country = args.get("country", "")
        date_str = args.get("date", "")

        log_function_call(
            "tools.weather.historical",
            "execute",
            city=city,
            date=date_str,
            source="agent_or_route",
        )

        result = self._fetch(city, country, date_str)

        if "error" in result:
            log_function_call(
                "tools.weather.historical",
                "execute",
                step="error",
                error=result["error"][:200],
            )
            return self._build_error(args.get("tool_call_id", ""), result), None

        tool_msg = self._build_success_msg(args, result)
        chart_bundle = {
            "role": "rich_content",
            "content": {"type": "chart_bundle", "charts": result.get("charts", [])},
        }
        log_function_call(
            "tools.weather.historical",
            "execute",
            step="complete",
            city=result["display_name"],
            date=date_str,
        )
        return tool_msg, chart_bundle

    def _build_error(self, tool_call_id: str, result: dict) -> dict[str, Any]:
        return {
            "role": "tool_result",
            "content": {"tool_call_id": tool_call_id, "result": json.dumps(result)},
        }

    def _build_success_msg(self, args: dict[str, Any], result: dict) -> dict[str, Any]:
        tool_summary = json.dumps(
            {
                "city": result["display_name"],
                "date": result["date"],
                "high_temp": result["high_temp"],
                "low_temp": result["low_temp"],
                "max_uv": result["max_uv"],
                "total_precipitation": result["total_precipitation"],
                "dominant_wind_direction": result["dominant_wind_direction"],
            }
        )
        return {
            "role": "tool_result",
            "content": {"tool_call_id": args.get("tool_call_id", ""), "result": tool_summary},
        }

    def _fetch(self, city: str, country: str, date_str: str) -> dict[str, Any]:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return {"error": f"Invalid date '{date_str}'. Use YYYY-MM-DD format."}

        try:
            location = self._geocode(city)
            if location is None:
                return {
                    "error": (
                        f"City '{city}' not found. Try a different name or add a country code."
                    )
                }
            return self._fetch_archive(location, date_str)
        except req_mod.RequestException as e:
            return {"error": f"Weather API request failed: {e}."}
        except Exception as e:
            return {"error": f"Failed to process weather data: {e}"}

    def _geocode(self, city: str) -> dict[str, Any] | None:
        log_function_call("tools.weather.historical", "_geocode", city=city)
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

    def _fetch_archive(self, location: dict, date_str: str) -> dict[str, Any]:
        lat, lon = location["lat"], location["lon"]
        display_name = location["display_name"]
        log_function_call(
            "tools.weather.historical",
            "_fetch_archive",
            lat=lat,
            lon=lon,
            date=date_str,
        )
        archive_params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": date_str,
            "end_date": date_str,
            "hourly": (
                "temperature_2m,relative_humidity_2d,"
                "precipitation,wind_speed_10m,wind_direction_10m,"
                "uv_index,weather_code"
            ),
            "timezone": "auto",
        }
        return _process_archive_response(self._archive_url, archive_params, display_name, date_str)


def _dominant_dir(wind_dir: list) -> str:
    if not wind_dir:
        return "N/A"
    avg_dir = sum(wind_dir) / len(wind_dir)
    for (lo, hi), label in WIND_DIR_BUCKETS.items():
        if lo <= avg_dir < hi:
            return label
    return "N"


def _process_archive_response(
    archive_url: str,
    params: dict,
    display_name: str,
    date_str: str,
) -> dict[str, Any]:
    ar_resp = req_mod.get(archive_url, params=params, timeout=15)
    ar_resp.raise_for_status()
    ar_data = ar_resp.json()
    hourly = ar_data["hourly"]

    return {
        "display_name": display_name,
        "date": date_str,
        "high_temp": max(hourly["temperature_2m"]),
        "low_temp": min(hourly["temperature_2m"]),
        "max_uv": max(hourly["uv_index"]),
        "total_precipitation": round(sum(hourly["precipitation"]), 1),
        "dominant_wind_direction": _dominant_dir(hourly["wind_direction_10m"]),
        "charts": _build_charts(display_name, date_str, hourly),
    }


def _build_charts(display_name: str, date_str: str, hourly: dict) -> list[dict[str, Any]]:
    times = hourly["time"]
    charts = []
    charts.append(_chart_temperature(times, hourly["temperature_2m"], display_name, date_str))
    charts.append(_chart_uv(times, hourly["uv_index"], display_name, date_str))
    charts.append(
        _chart_wind(
            times, hourly["wind_speed_10m"], hourly["wind_direction_10m"], display_name, date_str
        )
    )
    charts.append(_chart_precipitation(times, hourly["precipitation"], display_name, date_str))
    return charts


def _chart_temperature(times: list, temps: list, name: str, date: str) -> dict[str, Any]:
    import plotly.graph_objects as go

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=times,
            y=temps,
            mode="lines+markers",
            name="Temperature",
            line=dict(color="#ef4444", width=2),
            fill="tozeroy",
            fillcolor="rgba(239,68,68,0.1)",
        )
    )
    fig.update_layout(
        title=f"Temperature — {name} ({date})",
        yaxis_title="°C",
        height=350,
        margin=dict(l=40, r=20, t=50, b=40),
    )
    return {"type": "chart", "title": f"Temperature — {name} ({date})", "figure": fig.to_dict()}


def _chart_uv(times: list, uv_index: list, name: str, date: str) -> dict[str, Any]:
    import plotly.graph_objects as go

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=times,
            y=uv_index,
            name="UV Index",
            marker=dict(color="#f59e0b", line=dict(color="#d97706", width=1)),
        )
    )
    fig.update_layout(
        title=f"UV Index — {name} ({date})",
        yaxis_title="UV Index",
        height=350,
        margin=dict(l=40, r=20, t=50, b=40),
    )
    return {"type": "chart", "title": f"UV Index — {name} ({date})", "figure": fig.to_dict()}


def _build_polar_data(wind_dir: list, wind_speed: list) -> tuple[list, list]:
    r_list = []
    theta_list = []
    for i, d in enumerate(wind_dir):
        if d is not None and d >= 0:
            theta_list.append(d)
            r_list.append(wind_speed[i] if i < len(wind_speed) else 0)
    return r_list, theta_list


def _chart_wind(
    times: list,
    wind_speed: list,
    wind_dir: list,
    name: str,
    date: str,
) -> dict[str, Any]:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[[{"type": "polar"}, {"type": "xy"}]],
        subplot_titles=("Wind Direction", "Wind Speed"),
    )
    polar_r, polar_theta = _build_polar_data(wind_dir, wind_speed)
    fig.add_trace(
        go.Scatterpolar(
            r=polar_r,
            theta=polar_theta,
            mode="markers",
            marker=dict(color="#3b82f6", size=5, opacity=0.6),
            name="Wind",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=times,
            y=wind_speed,
            mode="lines",
            name="Wind Speed",
            line=dict(color="#10b981", width=2),
        ),
        row=1,
        col=2,
    )
    fig.update_layout(
        title=f"Wind — {name} ({date})",
        height=400,
        margin=dict(l=40, r=20, t=50, b=40),
    )
    return {"type": "chart", "title": f"Wind — {name} ({date})", "figure": fig.to_dict()}


def _chart_precipitation(times: list, precip: list, name: str, date: str) -> dict[str, Any]:
    import plotly.graph_objects as go

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=times,
            y=precip,
            name="Precipitation",
            marker=dict(color="#06b6d4", line=dict(color="#0891b2", width=0.5)),
        )
    )
    fig.update_layout(
        title=f"Precipitation (mm) — {name} ({date})",
        yaxis_title="mm",
        height=350,
        margin=dict(l=40, r=20, t=50, b=40),
        xaxis=dict(rangeslider=dict(visible=True), type="date"),
    )
    return {
        "type": "chart",
        "title": f"Rain/Precipitation — {name} ({date})",
        "figure": fig.to_dict(),
    }
