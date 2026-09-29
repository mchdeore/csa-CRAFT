"""Wire protocol interfaces to concrete implementations."""

from app.core.config import (
    AZURE_COHERE_API_KEY,
    AZURE_COHERE_ENDPOINT,
    AZURE_COHERE_RERANK_MODEL,
    CONNECTORS_ROOT,
    GUARDIAN_API_KEY,
    GUARDIAN_SEARCH_URL,
    OPEN_METEO_ARCHIVE_URL,
    OPEN_METEO_FORECAST_URL,
    OPEN_METEO_GEOCODING_URL,
)
from app.core.protocols import AuthProvider, ChatProvider, WorkspaceStore
from auth.provider import InMemoryAuth
from chat.provider import DeepSeekChat
from connectors.local_files import LocalFileSource
from connectors.protocols import DataSource
from storage.query_tool import QueryTool
from storage.store import SqliteDataStore, SqliteStore
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

# Build tools from config
weather_tool = WeatherTool(
    geocoding_url=OPEN_METEO_GEOCODING_URL,
    forecast_url=OPEN_METEO_FORECAST_URL,
)
historical_weather_tool = HistoricalWeatherTool(
    geocoding_url=OPEN_METEO_GEOCODING_URL,
    archive_url=OPEN_METEO_ARCHIVE_URL,
)
news_tool = NewsTool(
    guardian_api_key=GUARDIAN_API_KEY,
    guardian_search_url=GUARDIAN_SEARCH_URL,
    cohere_endpoint=AZURE_COHERE_ENDPOINT,
    cohere_api_key=AZURE_COHERE_API_KEY,
    cohere_model=AZURE_COHERE_RERANK_MODEL,
)
excel_tool = ExcelTool()

# Interactive chart tools — no config needed, pure data → figure
bar_chart_tool = BarChartTool()
pie_chart_tool = PieChartTool()
scatter_chart_tool = ScatterChartTool()
heatmap_tool = HeatmapTool()
histogram_tool = HistogramTool()
line_chart_tool = LineChartTool()
boxplot_tool = BoxPlotTool()

# Data sources for document tools
data_sources: dict[str, DataSource] = {
    "local_documents": LocalFileSource(CONNECTORS_ROOT),
}
document_search_tool = DocumentSearchTool(data_sources)
text_analysis_tool = TextAnalysisTool(data_sources)

# Unified data store + query tool for workspace-scoped and global data
data_store = SqliteDataStore()
query_tool = QueryTool(data_store)

# Wire singletons
auth: AuthProvider = InMemoryAuth()
store: WorkspaceStore = SqliteStore()
chat_provider: ChatProvider = DeepSeekChat(
    weather=weather_tool,
    historical_weather=historical_weather_tool,
    news=news_tool,
    excel=excel_tool,
    bar_chart=bar_chart_tool,
    pie_chart=pie_chart_tool,
    scatter_chart=scatter_chart_tool,
    heatmap=heatmap_tool,
    histogram=histogram_tool,
    line_chart=line_chart_tool,
    boxplot=boxplot_tool,
    doc_search=document_search_tool,
    text_analysis=text_analysis_tool,
    query_tool=query_tool,
)
