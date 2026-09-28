"""Workspace and sidebar UI templates."""

from dash import dcc, html

from chat.templates import build_chat_area

_SIDEBAR_STYLE = {
    "width": "280px",
    "padding": "20px",
    "borderRight": "1px solid #ddd",
    "overflowY": "auto",
    "flexShrink": "0",
}


def _build_header(username: str) -> list:
    return [
        html.H2("Cheddar Chat"),
        html.P(username, style={"color": "#666"}),
        html.Hr(),
    ]


def _build_create_section() -> list:
    return [
        dcc.Input(
            id="new-ws-name",
            placeholder="New workspace name",
            type="text",
            style={"width": "100%", "marginBottom": "6px", "padding": "6px"},
        ),
        html.Button("Create", id="create-ws-btn", style={"width": "100%", "padding": "6px"}),
        html.Hr(),
    ]


def _build_logout_button() -> html.Button:
    return html.Button("Logout", id="logout-btn", style={"width": "100%", "padding": "6px"})


def build_sidebar(
    username: str,
    workspaces: list[dict],
    session: dict | None = None,
) -> html.Div:
    children = [
        *_build_header(username),
        *_build_create_section(),
        html.H4("Workspaces"),
        html.Div(_build_ws_buttons(workspaces), id="ws-list"),
        _build_charts_section(session),
        html.Hr(),
        _build_logout_button(),
    ]
    return html.Div(children, style=_SIDEBAR_STYLE)


def _build_ws_buttons(workspaces: list[dict]) -> list:
    return [
        html.Button(
            ws["name"],
            id={"type": "ws-btn", "index": ws["id"]},
            style={
                "display": "block",
                "width": "100%",
                "textAlign": "left",
                "padding": "8px",
                "margin": "4px 0",
                "cursor": "pointer",
                "border": "1px solid #ddd",
                "borderRadius": "4px",
                "backgroundColor": "#fff",
            },
        )
        for ws in workspaces
    ]


def _chart_nav_button(chart: dict) -> html.Button:
    return html.Button(
        chart.get("title", "Chart"),
        id={"type": "chart-nav-btn", "index": chart.get("chart_id", "")},
        style=CHART_NAV_STYLE,
    )


CHART_NAV_STYLE = {
    "display": "block",
    "width": "100%",
    "textAlign": "left",
    "padding": "6px",
    "margin": "3px 0",
    "cursor": "pointer",
    "fontSize": "12px",
    "border": "1px solid #d1fae5",
    "borderRadius": "4px",
    "backgroundColor": "#f0fdf4",
    "color": "#065f46",
}


def _build_charts_section(session: dict | None) -> html.Div:
    charts_data = (session or {}).get("charts", [])
    if not charts_data:
        return html.Div(
            [
                html.Hr(),
                html.H4("Charts"),
                html.P(
                    "No charts yet. Ask for weather!", style={"fontSize": "12px", "color": "#999"}
                ),
            ]
        )
    buttons = [_chart_nav_button(c) for c in charts_data]
    return html.Div(
        [
            html.Hr(),
            html.H4(f"Charts ({len(charts_data)})"),
            html.Div(buttons, id="chart-list"),
        ]
    )


def build_main(
    username: str,
    workspaces: list[dict],
    session: dict,
) -> html.Div:
    return html.Div(
        [
            build_sidebar(username, workspaces, session),
            build_chat_area(session),
        ],
        style={"display": "flex", "height": "100vh"},
    )
