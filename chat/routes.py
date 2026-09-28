"""Chat routes — send messages, upload files.

Codepath: POST /chat/send → load workspace → append user msg → provider.get_response → save messages
"""

from flask import Flask, jsonify, request

from app.core.logging import get_user_context, log_function_call


def register_routes(flask_app: Flask) -> None:
    _register_send_route(flask_app)
    _register_upload_route(flask_app)


def _register_send_route(flask_app: Flask) -> None:
    @flask_app.route("/chat/send", methods=["POST"])
    def send_message() -> tuple:
        from app.core.services import chat_provider, store

        data = request.get_json(silent=True) or {}
        username = data.get("username", "")
        workspace_id = data.get("workspace_id", "")
        message = data.get("message", "")
        if not username or not workspace_id or not message.strip():
            return jsonify({"error": "Missing username, workspace_id, or message"}), 400

        log_function_call(
            "chat.routes",
            "send_message",
            step="load_workspace",
            username=username,
            workspace_id=workspace_id,
        )
        existing = store.load(username, workspace_id)
        messages = existing["messages"] if existing else []
        messages.append({"role": "user", "content": message.strip()})

        log_function_call(
            "chat.routes",
            "send_message",
            step="call_provider",
            message_count=len(messages),
        )
        chat_provider._user_context = get_user_context()
        response = chat_provider.get_response(messages)
        if response.text:
            messages.append({"role": "assistant", "content": response.text})

        log_function_call(
            "chat.routes",
            "send_message",
            step="save_messages",
            rich_count=len(response.rich_contents),
        )
        store.save_messages(username, workspace_id, messages)
        return jsonify(
            {
                "success": True,
                "text": response.text,
                "rich_contents": response.rich_contents,
            }
        ), 200


def _register_upload_route(flask_app: Flask) -> None:
    @flask_app.route("/chat/upload", methods=["POST"])
    def upload_file() -> tuple:
        from app.core.services import excel_tool

        data = request.get_json(silent=True) or {}
        file_id = data.get("file_id", "")
        columns = data.get("columns", [])
        rows = data.get("rows", [])

        if not file_id:
            return jsonify({"error": "Missing file_id"}), 400

        import pandas as pd

        df = pd.DataFrame(rows, columns=columns)
        excel_tool.register_upload(file_id, df)

        return jsonify(
            {
                "success": True,
                "file_id": file_id,
                "row_count": len(df),
                "column_count": len(df.columns),
            }
        ), 200
