"""PydanticAI agent harness for Cheddar Chat."""

from dataclasses import dataclass, field
from typing import Any

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from app.core.logging import log_function_call
from tools.charts import (
    BarChartTool,
    BoxPlotTool,
    HeatmapTool,
    HistogramTool,
    LineChartTool,
    PieChartTool,
    ScatterChartTool,
)
from tools.documents import DocumentSearchTool, ExcelTool, TextAnalysisTool
from tools.news import NewsTool
from tools.weather import HistoricalWeatherTool, WeatherTool


@dataclass
class ChatDeps:
    """Dependencies injected into every tool call.

    username, workspace_id, user_role are set by the route handler
    before calling get_response. They flow into tool closures so
    every tool can scope data and check permissions by role.
    """

    username: str = ""
    workspace_id: str = ""
    user_role: str = "base_user"
    user_flags: list[str] = field(default_factory=list)
    weather: WeatherTool | None = None
    historical_weather: HistoricalWeatherTool | None = None
    news: NewsTool | None = None
    excel: ExcelTool | None = None
    bar_chart: BarChartTool | None = None
    pie_chart: PieChartTool | None = None
    scatter_chart: ScatterChartTool | None = None
    heatmap: HeatmapTool | None = None
    histogram: HistogramTool | None = None
    line_chart: LineChartTool | None = None
    boxplot: BoxPlotTool | None = None
    doc_search: DocumentSearchTool | None = None
    text_analysis: TextAnalysisTool | None = None
    query_tool: Any = None
    rich_contents: list[dict] = field(default_factory=list)


def _extract(tool_msg: dict[str, Any]) -> str:
    return tool_msg.get("content", {}).get("result", "")


def _collect(ctx: RunContext[ChatDeps], rich: dict[str, Any] | None) -> None:
    if rich:
        ctx.deps.rich_contents.append(rich)


def _log_tool(name: str, args: dict[str, Any], has_rich: bool) -> None:
    log_function_call(
        "chat.agent",
        f"tool:{name}",
        tool_args=str(args)[:200],
        has_rich_content=has_rich,
    )


def create_agent(
    model_name: str,
    provider: OpenAIProvider,
    system_prompt: str,
) -> Agent[ChatDeps, str]:
    """Build the pydantic-ai Agent with all Cheddar tools."""
    model = OpenAIChatModel(model_name, provider=provider)
    agent: Agent[ChatDeps, str] = Agent(
        model,
        system_prompt=system_prompt,
        retries=4,
    )
    _register_weather(agent)
    _register_historical_weather(agent)
    _register_news(agent)
    _register_excel(agent)
    _register_bar_chart(agent)
    _register_pie_chart(agent)
    _register_scatter_chart(agent)
    _register_heatmap(agent)
    _register_histogram(agent)
    _register_line_chart(agent)
    _register_boxplot(agent)
    _register_doc_search(agent)
    _register_text_analysis(agent)
    _register_query_data(agent)
    return agent


def _register_weather(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def get_weather(ctx: RunContext[ChatDeps], city: str = "", country: str = "") -> str:
        """Get weather forecast for a city. Provide the city parameter."""
        if not city:
            return "Error: city is required. Call get_weather(city='...')."
        args = {"city": city, "country": country, "tool_call_id": ""}
        tool_msg, rich = ctx.deps.weather.execute(args)
        _log_tool("get_weather", {"city": city, "country": country}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_historical_weather(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def get_historical_weather(
        ctx: RunContext[ChatDeps], city: str = "", date: str = "", country: str = ""
    ) -> str:
        """Get historical weather for a city on a past date (YYYY-MM-DD)."""
        if not city:
            return "Error: city is required. Call with city='<city name>'."
        if not date:
            return "Error: date is required in YYYY-MM-DD format."
        args = {"city": city, "date": date, "country": country, "tool_call_id": ""}
        tool_msg, rich = ctx.deps.historical_weather.execute(args)
        _log_tool("get_historical_weather", {"city": city, "date": date}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_news(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def search_news(ctx: RunContext[ChatDeps], query: str = "") -> str:
        """Search for recent news articles. Provide a query string."""
        if not query:
            return "Error: query is required. Call search_news(query='...')."
        tool_msg, rich = ctx.deps.news.execute({"query": query, "tool_call_id": ""})
        _log_tool("search_news", {"query": query}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_excel(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def plot_data(
        ctx: RunContext[ChatDeps],
        file_id: str = "",
        x_column: str = "",
        y_columns: str = "",
        chart_title: str = "",
    ) -> str:
        """Plot data from an uploaded Excel or CSV file."""
        if not file_id:
            return "Error: file_id is required. Please provide the file ID to plot."
        args = {
            "file_id": file_id,
            "x_column": x_column,
            "y_columns": y_columns,
            "chart_title": chart_title,
            "tool_call_id": "",
        }
        tool_msg, rich = ctx.deps.excel.execute(args)
        _log_tool("plot_data", {"file_id": file_id}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_doc_search(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def search_documents(
        ctx: RunContext[ChatDeps],
        query: str = "",
        source_name: str = "local_documents",
    ) -> str:
        """Search for files in available data sources."""
        if not query:
            return "Error: query is required. Please provide a search query."
        args = {"query": query, "source_name": source_name, "tool_call_id": ""}
        tool_msg, rich = ctx.deps.doc_search.execute(args)
        _log_tool("search_documents", {"query": query}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_bar_chart(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def draw_bar_chart(
        ctx: RunContext[ChatDeps],
        title: str = "Chart",
        categories: list[str] | None = None,
        series: list[dict] | None = None,
        x_label: str = "",
        y_label: str = "",
        horizontal: bool = False,
    ) -> str:
        """Draw an interactive bar chart from categories and values."""
        if not categories or not series:
            return "Error: categories and series are required for a bar chart."
        args = {
            "title": title,
            "categories": categories,
            "series": series,
            "x_label": x_label,
            "y_label": y_label,
            "horizontal": horizontal,
            "tool_call_id": "",
        }
        tool_msg, rich = ctx.deps.bar_chart.execute(args)
        _log_tool("draw_bar_chart", {"title": title}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_pie_chart(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def draw_pie_chart(
        ctx: RunContext[ChatDeps],
        title: str = "Chart",
        slices: list[dict] | None = None,
        donut: bool = False,
        show_percentages: bool = False,
    ) -> str:
        """Draw an interactive pie or donut chart from labeled values."""
        if not slices:
            return "Error: slices are required for a pie chart."
        args = {
            "title": title,
            "slices": slices,
            "donut": donut,
            "show_percentages": show_percentages,
            "tool_call_id": "",
        }
        tool_msg, rich = ctx.deps.pie_chart.execute(args)
        _log_tool("draw_pie_chart", {"title": title}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_scatter_chart(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def draw_scatter_chart(
        ctx: RunContext[ChatDeps],
        title: str = "Chart",
        series: list[dict] | None = None,
        x_label: str = "",
        y_label: str = "",
        trendline: bool = False,
        fit_degree: int = 1,
        show_residuals: bool = False,
        size_by: str = "none",
    ) -> str:
        """Draw an interactive scatter plot from x,y point series.

        Supports polynomial fit and residuals.
        """
        if not series:
            return "Error: series data is required for a scatter chart."
        args = {
            "title": title,
            "series": series,
            "x_label": x_label,
            "y_label": y_label,
            "trendline": trendline,
            "fit_degree": fit_degree,
            "show_residuals": show_residuals,
            "size_by": size_by,
            "tool_call_id": "",
        }
        tool_msg, rich = ctx.deps.scatter_chart.execute(args)
        _log_tool(
            "draw_scatter_chart",
            {"title": title, "fit_degree": fit_degree},
            rich is not None,
        )
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_heatmap(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def draw_heatmap(
        ctx: RunContext[ChatDeps],
        title: str = "Chart",
        rows: list[str] | None = None,
        cols: list[str] | None = None,
        values: list[list] | None = None,
        x_label: str = "",
        y_label: str = "",
        colorscale: str = "viridis",
    ) -> str:
        """Draw an interactive heatmap from a 2D grid of values."""
        if not rows or not cols or not values:
            return "Error: rows, cols, and values are required for a heatmap."
        args = {
            "title": title,
            "rows": rows,
            "cols": cols,
            "values": values,
            "x_label": x_label,
            "y_label": y_label,
            "colorscale": colorscale,
            "tool_call_id": "",
        }
        tool_msg, rich = ctx.deps.heatmap.execute(args)
        _log_tool("draw_heatmap", {"title": title}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_histogram(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def draw_histogram(
        ctx: RunContext[ChatDeps],
        title: str = "Chart",
        values: list[float] | None = None,
        num_bins: int | None = None,
        x_label: str = "",
        show_curve: bool = False,
        opacity: float = 0.7,
    ) -> str:
        """Draw an interactive histogram from a list of numeric values."""
        if not values:
            return "Error: values are required for a histogram."
        args = {
            "title": title,
            "values": values,
            "num_bins": num_bins,
            "x_label": x_label,
            "show_curve": show_curve,
            "opacity": opacity,
            "tool_call_id": "",
        }
        tool_msg, rich = ctx.deps.histogram.execute(args)
        _log_tool("draw_histogram", {"title": title}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_line_chart(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def draw_line_chart(
        ctx: RunContext[ChatDeps],
        title: str = "Chart",
        x_values: list[str] | None = None,
        series: list[dict] | None = None,
        x_label: str = "",
        y_label: str = "",
        fill: bool = False,
        x_is_date: bool = False,
        markers: bool = True,
    ) -> str:
        """Draw an interactive line chart from ordered series data."""
        if not x_values or not series:
            return "Error: x_values and series are required for a line chart."
        args = {
            "title": title,
            "x_values": x_values,
            "series": series,
            "x_label": x_label,
            "y_label": y_label,
            "fill": fill,
            "x_is_date": x_is_date,
            "markers": markers,
            "tool_call_id": "",
        }
        tool_msg, rich = ctx.deps.line_chart.execute(args)
        _log_tool("draw_line_chart", {"title": title}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_boxplot(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def draw_box_plot(
        ctx: RunContext[ChatDeps],
        title: str = "Chart",
        groups: list[dict] | None = None,
        y_label: str = "",
        show_points: bool = False,
        horizontal: bool = False,
    ) -> str:
        """Draw an interactive box plot comparing distributions across groups."""
        if not groups:
            return "Error: groups are required for a box plot."
        args = {
            "title": title,
            "groups": groups,
            "y_label": y_label,
            "show_points": show_points,
            "horizontal": horizontal,
            "tool_call_id": "",
        }
        tool_msg, rich = ctx.deps.boxplot.execute(args)
        _log_tool("draw_box_plot", {"title": title}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_text_analysis(agent: Agent[ChatDeps, str]) -> None:
    @agent.tool
    def read_document(
        ctx: RunContext[ChatDeps],
        path: str = "",
        source_name: str = "local_documents",
    ) -> str:
        """Read and extract text from a document."""
        if not path:
            return "Error: path is required. Please provide the document path."
        args = {"path": path, "source_name": source_name, "tool_call_id": ""}
        tool_msg, rich = ctx.deps.text_analysis.execute(args)
        _log_tool("read_document", {"path": path}, rich is not None)
        _collect(ctx, rich)
        return _extract(tool_msg)


def _register_query_data(agent: Agent[ChatDeps, str]) -> None:
    """Register the unified query_data tool on the agent.

    The tool lets the model query, store, list, or delete data by key.
    The store scopes everything by user role — base_user sees own workspace
    data + public datasets, admin sees everything.
    """

    @agent.tool
    def query_data(
        ctx: RunContext[ChatDeps],
        key: str = "",
        action: str = "query",
        value: dict | None = None,
    ) -> str:
        """Query, store, list, or delete data by key name.

        Use action='query' to read data, action='store' to save data,
        action='list' to see available keys, action='delete' to remove data.

        For store action, provide a value dict with the data to save.
        """
        qt = ctx.deps.query_tool
        if qt is None:
            return "Data tool not available."

        # Set user context from deps so the tool scopes data correctly
        qt.set_user(
            username=ctx.deps.username,
            workspace_id=ctx.deps.workspace_id,
            user_role=ctx.deps.user_role,
            user_flags=ctx.deps.user_flags,
        )

        args: dict[str, Any] = {"action": action, "key": key}
        if value is not None:
            args["value"] = value

        tool_msg, _ = qt.execute(args)
        _log_tool("query_data", {"action": action, "key": key}, False)
        return _extract(tool_msg)
