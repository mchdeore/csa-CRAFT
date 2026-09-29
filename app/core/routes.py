"""Central Flask route registrar — calls register_routes() on each feature.

Route map (codepaths):
  /auth/*      — login, logout
  /chat/*      — send message, upload file
  /storage/*   — workspace CRUD, message persistence
  /tools/*     — direct tool execution, tool listing
  /debug/*     — route introspection and diagnostics
"""

from flask import Flask, jsonify

from app.core.logging import log_function_call


def register_all(app: Flask) -> None:
    from auth.routes import register_routes as register_auth_routes
    from chat.routes import register_routes as register_chat_routes
    from demo.routes import register_routes as register_demo_routes
    from storage.routes import register_routes as register_storage_routes
    from tools.routes import register_routes as register_tool_routes

    register_auth_routes(app)
    register_chat_routes(app)
    register_demo_routes(app)
    register_storage_routes(app)
    register_tool_routes(app)
    _register_debug_routes(app)

    log_function_call("app.routes", "register_all", route_count=len(app.url_map._rules))


def _register_debug_routes(app: Flask) -> None:
    @app.route("/debug/routes", methods=["GET"])
    def list_routes() -> tuple:
        routes = []
        for rule in app.url_map.iter_rules():
            if rule.endpoint == "static":
                continue
            routes.append(
                {
                    "path": rule.rule,
                    "methods": sorted((rule.methods or set()) - {"OPTIONS", "HEAD"}),
                    "endpoint": rule.endpoint,
                }
            )
        routes.sort(key=lambda r: r["path"])
        return jsonify({"routes": routes, "count": len(routes)}), 200

    @app.route("/debug/pipeline", methods=["GET"])
    def show_pipeline() -> tuple:
        pipeline = {
            "codepaths": {
                "chat": {
                    "route": "POST /chat/send",
                    "flow": [
                        "chat.routes:send_message",
                        "chat.provider:get_response",
                        "chat.provider:_make_provider (Azure OpenAI client)",
                        "chat.agent:create_agent (PydanticAI agent)",
                        "chat.agent:tool:* → tools.weather.forecast / tools.charts.bar / etc.",
                        "storage.store:save_messages",
                    ],
                },
                "auth": {
                    "routes": ["POST /auth/login", "POST /auth/logout"],
                    "flow": ["auth.routes → auth.provider:try_login / do_logout"],
                },
                "storage": {
                    "routes": [
                        "GET /storage/list/<username>",
                        "POST /storage/create",
                        "GET /storage/load/<username>/<workspace_id>",
                        "POST /storage/save-messages/<username>/<workspace_id>",
                    ],
                    "flow": ["storage.routes → storage.store:SqliteStore"],
                },
                "tools": {
                    "routes": ["GET /tools/list", "POST /tools/execute/<tool_name>"],
                    "flow": [
                        "tools.routes → tools.weather.forecast:WeatherTool",
                        "tools.routes → tools.weather.historical:HistoricalWeatherTool",
                        "tools.routes → tools.charts.bar:BarChartTool",
                        "tools.routes → tools.charts.pie:PieChartTool",
                        "tools.routes → tools.charts.scatter:ScatterChartTool",
                        "tools.routes → tools.news.search:NewsTool",
                        "tools.routes → tools.documents.search:DocumentSearchTool",
                        "tools.routes → tools.documents.reader:TextAnalysisTool",
                        "tools.routes → tools.documents.excel:ExcelTool",
                    ],
                },
                "connectors": {
                    "flow": ["connectors.local_files:LocalFileSource"],
                },
            },
            "logging": {
                "structured_json": "storage/database/log/cheddar.jsonl",
                "trace_id": "8-char UUID per request, propagated to all log lines",
                "fields": "caller_module, caller_function, cause, step, source",
                "coverage": "every public function in every module emits FUNCTION_CALL",
            },
        }
        return jsonify(pipeline), 200
