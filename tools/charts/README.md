# tools/charts

Chart tools the agent can call: `BarChartTool`, `PieChartTool`, `ScatterChartTool`, `HeatmapTool`, `HistogramTool`, `LineChartTool`, `BoxPlotTool`. Seven distinct tools instead of one god-tool so the LLM picks reliably by function name. Charts render inline as Plotly figures via the `rich_content` pipeline.
