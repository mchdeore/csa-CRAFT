"""Chat message UI templates — message bubbles, charts, news cards."""

from dash import dcc, html

CHART_WRAPPER_STYLE = {
    "padding": "10px 14px",
    "margin": "6px 0",
    "borderRadius": "8px",
    "backgroundColor": "#f0fdf4",
    "border": "1px solid #bbf7d0",
    "maxWidth": "95%",
    "alignSelf": "flex-start",
}

CHART_TITLE_STYLE = {
    "fontWeight": "bold",
    "fontSize": "14px",
    "color": "#374151",
    "marginBottom": "8px",
}

INPUT_BAR_STYLE = {
    "display": "flex",
    "flexWrap": "wrap",
    "padding": "10px",
    "borderTop": "1px solid #ddd",
    "gap": "8px",
}

UPLOAD_BUTTON_STYLE = {
    "padding": "10px 16px",
    "cursor": "pointer",
    "border": "1px solid #d1d5db",
    "borderRadius": "6px",
    "backgroundColor": "#f9fafb",
    "fontSize": "14px",
}

NEWS_TITLE_STYLE = {
    "fontWeight": "600",
    "fontSize": "14px",
    "color": "#1d4ed8",
    "textDecoration": "none",
}
NEWS_HEADER_STYLE = {"display": "flex", "alignItems": "center", "justifyContent": "space-between"}
NEWS_SNIPPET_STYLE = {"fontSize": "12px", "color": "#6b7280", "margin": "4px 0 0"}
READ_MORE_STYLE = {"cursor": "pointer", "color": "#3b82f6", "fontSize": "12px", "marginTop": "4px"}
NEWS_BODY_STYLE = {"fontSize": "12px", "color": "#374151", "marginTop": "6px", "lineHeight": "1.5"}
NEWS_CARD_STYLE = {
    "padding": "10px 12px",
    "margin": "4px 0",
    "border": "1px solid #e5e7eb",
    "borderRadius": "6px",
    "backgroundColor": "#fff",
}


def build_message(role: str, content: object) -> html.Div:
    """Build a chat message bubble. Handles text, charts, and news cards."""
    is_user = role == "user"

    if role == "chart" and isinstance(content, dict):
        return build_chart_message(content)
    if role == "news_cards" and isinstance(content, dict):
        return build_news_cards(content)

    return html.Div(
        [
            html.Strong("You" if is_user else "Assistant"),
            html.P(str(content), style={"margin": "4px 0 0", "whiteSpace": "pre-wrap"}),
        ],
        style={
            "padding": "10px 14px",
            "margin": "6px 0",
            "borderRadius": "8px",
            "backgroundColor": "#e3f2fd" if is_user else "#f5f5f5",
            "maxWidth": "80%",
            "alignSelf": "flex-end" if is_user else "flex-start",
        },
    )


def build_chart_message(content: dict) -> html.Div:
    chart_id = content.get("chart_id", "")
    title = content.get("title", "Chart")
    figure_dict = content.get("figure", {})

    if not figure_dict:
        return html.Div(
            html.P("Chart data not available.", style={"color": "#999"}),
            style={"padding": "10px", "margin": "6px 0"},
        )

    # Build the chart title and graph
    return html.Div(
        [
            html.Div(title, style=CHART_TITLE_STYLE),
            dcc.Graph(
                id={"type": "chart-graph", "index": chart_id},
                figure=figure_dict,
                config={"displayModeBar": True, "responsive": True},
                style={"width": "100%"},
            ),
        ],
        id=f"chart-{chart_id}",
        style=CHART_WRAPPER_STYLE,
    )


def build_news_cards(content: dict) -> html.Div:
    articles = content.get("articles", [])
    query = content.get("query", "News results")
    if not articles:
        return _empty_news(query)
    cards = [_build_news_card(a) for a in articles]
    return html.Div(
        [
            html.Div(
                [
                    html.Strong("News Results"),
                    html.Span(
                        f" for '{query}'",
                        style={"color": "#6b7280", "fontSize": "13px"},
                    ),
                ],
                style={"marginBottom": "8px"},
            ),
            html.Div(cards),
        ],
        style={
            "padding": "10px 14px",
            "margin": "6px 0",
            "borderRadius": "8px",
            "backgroundColor": "#fefce8",
            "border": "1px solid #fef08a",
            "maxWidth": "95%",
            "alignSelf": "flex-start",
        },
    )


def _empty_news(query: str) -> html.Div:
    return html.Div(
        [
            html.Strong("News Search"),
            html.P(f"No articles found for '{query}'.", style={"color": "#999"}),
        ],
        style={
            "padding": "10px 14px",
            "margin": "6px 0",
            "borderRadius": "8px",
            "backgroundColor": "#f5f5f5",
            "maxWidth": "80%",
            "alignSelf": "flex-start",
        },
    )


def _build_news_card_header(title: str, url: str, score: float) -> html.Div:
    score_color = "#059669" if score > 0.5 else "#d97706" if score > 0.2 else "#9ca3af"
    return html.Div(
        [
            html.A(title, href=url, target="_blank", style=NEWS_TITLE_STYLE),
            html.Span(
                f"{score:.0%}" if score > 0 else "",
                style={
                    "fontSize": "11px",
                    "color": score_color,
                    "marginLeft": "8px",
                    "fontWeight": "600",
                },
            ),
        ],
        style=NEWS_HEADER_STYLE,
    )


def _build_news_card(article: dict) -> html.Div:
    card_id = f"news-card-{hash(article.get('url', '')) & 0xFFFFFFFF}"
    score = article.get("relevance_score", 0)
    title = article.get("title", "Untitled")
    url = article.get("url", "#")
    snippet = (article.get("snippet", "") or "")[:150] + "..."
    body = article.get("body_preview", "") or ""

    return html.Div(
        [
            _build_news_card_header(title, url, score),
            html.P(snippet, style=NEWS_SNIPPET_STYLE),
            html.Details(
                [
                    html.Summary("Read more", style=READ_MORE_STYLE),
                    html.P(body, style=NEWS_BODY_STYLE),
                ]
            ),
        ],
        id=card_id,
        style=NEWS_CARD_STYLE,
    )


def build_chat_area(session: dict) -> html.Div:
    workspace_id = session.get("workspace_id", "")
    if not workspace_id:
        return html.Div(
            html.P(
                "Select or create a workspace to start chatting.",
                style={"color": "#999", "marginTop": "40px", "textAlign": "center"},
            ),
            style={"flex": "1"},
        )
    messages = session.get("messages", [])
    msg_els = [build_message(m["role"], m["content"]) for m in messages]
    if not msg_els:
        msg_els = [html.P("No messages yet.", style={"color": "#999"})]
    return html.Div(
        [
            build_chat_messages_panel(msg_els),
            build_chat_input_bar(),
            html.Div(id="scroll-trigger", style={"display": "none"}),
        ],
        style={"flex": "1", "display": "flex", "flexDirection": "column"},
    )


def build_chat_messages_panel(msg_els: list) -> html.Div:
    return html.Div(
        msg_els,
        id="chat-messages",
        style={
            "flex": "1",
            "overflowY": "auto",
            "padding": "20px",
            "display": "flex",
            "flexDirection": "column",
        },
    )


def _upload_widget() -> dcc.Upload:
    return dcc.Upload(
        id="file-upload",
        children=html.Button("📎 Upload", style=UPLOAD_BUTTON_STYLE),
        multiple=False,
        max_size=10 * 1024 * 1024,
        style={"display": "inline-block"},
    )


def build_chat_input_bar() -> html.Div:
    return html.Div(
        [
            _upload_widget(),
            dcc.Input(
                id="chat-input",
                placeholder="Type a message...",
                type="text",
                style={"flex": "1", "padding": "10px"},
                debounce=False,
            ),
            html.Button("Send", id="send-btn", style={"padding": "10px 20px", "marginLeft": "8px"}),
            html.Div(
                id="upload-status",
                style={"fontSize": "12px", "color": "#6b7280", "marginTop": "4px"},
            ),
        ],
        style=INPUT_BAR_STYLE,
    )
