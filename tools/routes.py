"""Tool execution routes — direct tool invocation and codepath tracking.

These routes expose each tool as a REST endpoint at /tools/execute/<name>.
This enables:
  1. Direct tool testing without going through the LLM agent
  2. Route-level logging so tool calls appear in the structured log
  3. Codepath tracing: every tool invocation has a route entry
"""

from flask import Flask, jsonify, request

from app.core.logging import log_function_call


def register_routes(flask_app: Flask) -> None:
    _register_execute_route(flask_app)
    _register_list_route(flask_app)


def _register_execute_route(flask_app: Flask) -> None:
    @flask_app.route("/tools/execute/<tool_name>", methods=["POST"])
    def execute_tool(tool_name: str) -> tuple:
        from app.core.services import (
            bar_chart_tool,
            boxplot_tool,
            document_search_tool,
            excel_tool,
            heatmap_tool,
            histogram_tool,
            historical_weather_tool,
            line_chart_tool,
            news_tool,
            pie_chart_tool,
            scatter_chart_tool,
            text_analysis_tool,
            weather_tool,
        )

        tool_map = {
            "get_weather": ("tools.weather.forecast", weather_tool),
            "get_historical_weather": ("tools.weather.historical", historical_weather_tool),
            "search_news": ("tools.news.search", news_tool),
            "plot_data": ("tools.documents.excel", excel_tool),
            "draw_bar_chart": ("tools.charts.bar", bar_chart_tool),
            "draw_pie_chart": ("tools.charts.pie", pie_chart_tool),
            "draw_scatter_chart": ("tools.charts.scatter", scatter_chart_tool),
            "draw_heatmap": ("tools.charts.heatmap", heatmap_tool),
            "draw_histogram": ("tools.charts.histogram", histogram_tool),
            "draw_line_chart": ("tools.charts.line", line_chart_tool),
            "draw_box_plot": ("tools.charts.boxplot", boxplot_tool),
            "search_documents": ("tools.documents.search", document_search_tool),
            "read_document": ("tools.documents.reader", text_analysis_tool),
        }

        entry = tool_map.get(tool_name)
        if entry is None:
            return jsonify(
                {
                    "error": f"Unknown tool: {tool_name}",
                    "available": list(tool_map.keys()),
                }
            ), 404

        canonical_path, tool = entry
        data = request.get_json(silent=True) or {}
        log_function_call(
            "tools.routes",
            f"execute:{tool_name}",
            destination=canonical_path,
            tool_args=str(data)[:200],
            cause="direct_route",
        )

        try:
            tool_msg, rich = tool.execute(data)
            result = tool_msg.get("content", {}).get("result", "")
            response = {"success": True, "tool": tool_name, "result": result}
            if rich:
                response["has_rich_content"] = True
                response["rich_content_type"] = rich.get("content", {}).get("type", "")
            return jsonify(response), 200
        except Exception as e:
            log_function_call("tools.routes", f"execute:{tool_name}", error=str(e)[:200])
            return jsonify({"error": str(e), "tool": tool_name}), 500


def _register_list_route(flask_app: Flask) -> None:
    @flask_app.route("/tools/list", methods=["GET"])
    def list_tools() -> tuple:
        tools = {
            "get_weather": {
                "description": "Weather forecast",
                "params": ["city", "country"],
            },
            "get_historical_weather": {
                "description": "Historical weather",
                "params": ["city", "date", "country"],
            },
            "search_news": {
                "description": "News search",
                "params": ["query"],
            },
            "plot_data": {
                "description": "Plot Excel/CSV data",
                "params": ["file_id", "x_column", "y_columns"],
            },
            "draw_bar_chart": {
                "description": "Bar chart",
                "params": ["title", "categories", "series"],
            },
            "draw_pie_chart": {
                "description": "Pie chart",
                "params": ["title", "slices"],
            },
            "draw_scatter_chart": {
                "description": "Scatter plot with polynomial fit and residuals",
                "params": ["title", "series", "fit_degree", "show_residuals"],
            },
            "draw_heatmap": {
                "description": "Heatmap",
                "params": ["title", "rows", "cols", "values", "colorscale"],
            },
            "draw_histogram": {
                "description": "Histogram",
                "params": ["title", "values", "num_bins", "show_curve"],
            },
            "draw_line_chart": {
                "description": "Line chart",
                "params": ["title", "x_values", "series", "fill", "markers"],
            },
            "draw_box_plot": {
                "description": "Box plot",
                "params": ["title", "groups", "show_points"],
            },
            "search_documents": {
                "description": "Document search",
                "params": ["query", "source_name"],
            },
            "read_document": {
                "description": "Read document",
                "params": ["path", "source_name"],
            },
        }
        log_function_call("tools.routes", "list_tools")
        return jsonify({"tools": tools}), 200
