"""Storage routes — workspace CRUD and message persistence."""

from flask import Flask, jsonify, request

from app.core.logging import log_function_call


def register_routes(flask_app: Flask) -> None:
    _register_list_route(flask_app)
    _register_create_route(flask_app)
    _register_load_route(flask_app)
    _register_save_messages_route(flask_app)


def _register_list_route(flask_app: Flask) -> None:
    @flask_app.route("/storage/list/<username>", methods=["GET"])
    def list_workspaces(username: str) -> tuple:
        from app.core.services import store

        log_function_call(
            "storage.routes",
            "list_workspaces",
            username=username,
            cause="user_request",
        )
        workspaces = store.list(username)
        log_function_call(
            "storage.routes",
            "list_workspaces",
            step="complete",
            count=len(workspaces),
        )
        return jsonify({"workspaces": workspaces}), 200


def _register_create_route(flask_app: Flask) -> None:
    @flask_app.route("/storage/create", methods=["POST"])
    def create_workspace() -> tuple:
        from app.core.services import store

        data = request.get_json(silent=True) or {}
        username = data.get("username", "")
        name = data.get("name", "")

        log_function_call(
            "storage.routes",
            "create_workspace",
            username=username,
            name=name,
            cause="user_request",
        )

        if not username or not name.strip():
            return jsonify({"error": "Missing username or name"}), 400

        workspace = store.create(username, name.strip())
        log_function_call(
            "storage.routes",
            "create_workspace",
            step="complete",
            workspace_id=workspace["id"],
        )
        return jsonify(workspace), 201


def _register_load_route(flask_app: Flask) -> None:
    @flask_app.route("/storage/load/<username>/<workspace_id>", methods=["GET"])
    def load_workspace(username: str, workspace_id: str) -> tuple:
        from app.core.services import store

        log_function_call(
            "storage.routes",
            "load_workspace",
            username=username,
            workspace_id=workspace_id,
            cause="user_request",
        )
        workspace = store.load(username, workspace_id)
        if workspace is None:
            log_function_call(
                "storage.routes",
                "load_workspace",
                step="not_found",
                workspace_id=workspace_id,
            )
            return jsonify({"error": "Workspace not found"}), 404
        log_function_call(
            "storage.routes",
            "load_workspace",
            step="complete",
            message_count=len(workspace.get("messages", [])),
        )
        return jsonify(workspace), 200


def _register_save_messages_route(flask_app: Flask) -> None:
    @flask_app.route("/storage/save-messages/<username>/<workspace_id>", methods=["POST"])
    def save_messages(username: str, workspace_id: str) -> tuple:
        from app.core.services import store

        data = request.get_json(silent=True) or {}
        messages = data.get("messages", [])
        log_function_call(
            "storage.routes",
            "save_messages",
            username=username,
            workspace_id=workspace_id,
            message_count=len(messages),
            cause="system",
        )
        store.save_messages(username, workspace_id, messages)
        log_function_call("storage.routes", "save_messages", step="complete")
        return jsonify({"success": True}), 200
