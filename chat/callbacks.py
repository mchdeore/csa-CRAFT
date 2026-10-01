"""Chat message callback — handles sending messages, tool results, and rich content."""

import base64
import io
import uuid

import pandas as pd
from dash import ALL, Input, Output, State, no_update

from app.core.dash_app import app
from app.core.logging import log_function_call
from app.core.services import excel_tool, store


# Call the chat route and return the response data
def _send_chat_message(username: str, workspace_id: str, message: str) -> dict:
    import os

    client = app.server.test_client()
    resp = client.post(
        "/chat/send",
        json={
            "username": username,
            "workspace_id": workspace_id,
            "message": message,
        },
        headers={
            "X-Internal-Secret": os.environ.get(
                "INTERNAL_API_SECRET", "cheddar-internal-dev"
            )
        },
    )
    return resp.get_json() or {}


# Render a single rich content item into a session message
def _process_rich_content(session: dict, rc: dict) -> None:
    rc_content = rc["content"]
    msg_type = rc_content.get("type", "")

    if msg_type == "chart":
        _add_chart_message(session, rc_content)
    elif msg_type == "chart_bundle":
        for chart_data in rc_content.get("charts", []):
            _process_rich_content(session, {"role": "rich_content", "content": chart_data})
    elif msg_type == "news_cards":
        _add_news_message(session, rc_content)


def _add_chart_message(session: dict, content: dict) -> None:
    chart_id = str(uuid.uuid4())
    charts = session.get("charts", [])
    charts.append({"chart_id": chart_id, "title": content.get("title", "Chart")})
    session["charts"] = charts
    session["messages"].append(
        {
            "role": "chart",
            "content": {
                "chart_id": chart_id,
                "title": content.get("title", "Chart"),
                "figure": content.get("figure", {}),
            },
        }
    )


def _add_news_message(session: dict, content: dict) -> None:
    session["messages"].append(
        {
            "role": "news_cards",
            "content": {
                "chart_id": str(uuid.uuid4()),
                "query": content.get("query", ""),
                "articles": content.get("articles", []),
            },
        }
    )


@app.callback(
    Output("session-store", "data", allow_duplicate=True),
    Output("chat-input", "value"),
    Input("send-btn", "n_clicks"),
    Input("chat-input", "n_submit"),
    State("chat-input", "value"),
    State("session-store", "data"),
    prevent_initial_call=True,
)
def handle_send(
    n_clicks: int | None,
    n_submit: int | None,
    message: str | None,
    session: dict,
) -> tuple:
    if not message or not message.strip():
        return no_update, no_update
    if not session.get("workspace_id"):
        return no_update, no_update

    username = session.get("username", "")
    workspace_id = session.get("workspace_id", "")
    log_function_call(
        "chat.callbacks",
        "handle_send",
        username=username,
        workspace_id=workspace_id,
        cause="user_request",
    )
    data = _send_chat_message(username, workspace_id, message.strip())
    if not data.get("success"):
        return no_update, no_update

    # Append user message and assistant text
    session["messages"].append({"role": "user", "content": message.strip()})
    if data.get("text"):
        session["messages"].append({"role": "assistant", "content": data["text"]})

    # Process rich contents
    for rc in data.get("rich_contents", []):
        _process_rich_content(session, rc)

    store.save_messages(session["username"], session["workspace_id"], session["messages"])
    log_function_call(
        "chat.callbacks",
        "handle_send",
        step="complete",
        rich_count=len(data.get("rich_contents", [])),
    )
    return session, ""


app.clientside_callback(
    """function(n_clicks_list, ids_list) {
        if (!n_clicks_list || !ids_list) { return ''; }
        var triggeredIdx = n_clicks_list.findIndex(
            function(v) { return v !== undefined && v !== null; }
        );
        if (triggeredIdx < 0) { return ''; }
        var chartId = ids_list[triggeredIdx].index;
        var el = document.getElementById('chart-' + chartId);
        if (el) {
            el.scrollIntoView({behavior: 'smooth', block: 'center'});
            el.style.transition = 'box-shadow 0.3s';
            el.style.boxShadow = '0 0 0 3px #3b82f6';
            setTimeout(function() { el.style.boxShadow = ''; }, 2000);
        }
        return '';
    }""",
    Output("chat-input", "value", allow_duplicate=True),
    Input({"type": "chart-nav-btn", "index": ALL}, "n_clicks"),
    State({"type": "chart-nav-btn", "index": ALL}, "id"),
    prevent_initial_call=True,
)


@app.callback(
    Output("upload-status", "children"),
    Output("chat-input", "value", allow_duplicate=True),
    Input("file-upload", "contents"),
    State("file-upload", "filename"),
    State("file-upload", "last_modified"),
    State("session-store", "data"),
    prevent_initial_call=True,
)
def handle_file_upload(
    contents: str | None,
    filename: str | None,
    last_modified: int | None,
    session: dict,
) -> tuple:
    if contents is None or filename is None:
        return no_update, no_update

    log_function_call(
        "chat.callbacks",
        "handle_file_upload",
        filename=filename,
        cause="user_request",
    )
    try:
        df = _parse_uploaded_file(contents, filename)
        if df.empty:
            return "File is empty — nothing to plot.", no_update

        file_id = str(uuid.uuid4())
        excel_tool.register_upload(file_id, df)

        upload_message = _build_upload_message(filename, file_id, df)
        session["messages"].append({"role": "user", "content": upload_message})

        status = f"✅ Uploaded {filename} ({len(df)} rows, {len(df.columns)} cols)"
        store.save_messages(session["username"], session["workspace_id"], session["messages"])
        return status, ""

    except Exception as e:
        return f"❌ Failed to read file: {e}", no_update


def _parse_uploaded_file(contents: str, filename: str) -> pd.DataFrame:
    _, content_string = contents.split(",", 1)
    decoded = base64.b64decode(content_string)
    if filename.lower().endswith(".csv"):
        return pd.read_csv(io.BytesIO(decoded))
    return pd.read_excel(io.BytesIO(decoded))


def _build_upload_message(filename: str, file_id: str, df: pd.DataFrame) -> str:
    column_list = ", ".join(df.columns[:15])
    if len(df.columns) > 15:
        column_list += f" ... (+{len(df.columns) - 15} more)"
    return (
        f"[Uploaded file: {filename}]\n"
        f"File ID: {file_id}\n"
        f"Rows: {len(df)}, Columns: {len(df.columns)}\n"
        f"Columns: {column_list}\n\n"
        "You can ask me to plot this data. "
        f"For example: 'Plot {df.columns[0]} vs {df.columns[1]}'"
    )
