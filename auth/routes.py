"""Authentication routes — login, logout."""

from flask import Flask, jsonify, request, session

from app.core.logging import log_function_call


def register_routes(flask_app: Flask) -> None:
    """Register Flask routes for auth endpoints."""

    @flask_app.route("/auth/login", methods=["POST"])
    def login() -> tuple:
        from app.core.services import auth

        data = request.get_json(silent=True) or {}
        username = data.get("username", "")
        password = data.get("password", "")

        log_function_call(
            "auth.routes",
            "login",
            username=username,
            cause="user_request",
        )

        if auth.try_login(username, password):
            log_function_call("auth.routes", "login", step="success", username=username)
            return jsonify({"success": True, "username": username}), 200

        log_function_call("auth.routes", "login", step="failed", username=username)
        return jsonify({"success": False, "error": "Invalid username or password"}), 401

    @flask_app.route("/auth/logout", methods=["POST"])
    def logout() -> tuple:
        from app.core.services import auth

        log_function_call("auth.routes", "logout", cause="user_request")
        auth.do_logout()
        session.clear()
        log_function_call("auth.routes", "logout", step="complete")
        return jsonify({"success": True}), 200
