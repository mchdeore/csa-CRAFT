# Interactive Chart Tool Library — Design Decisions

## What Was Built

Three new tools for agents to display interactive charts in chat: bar chart, pie chart, scatter plot. The agent passes structured data objects through the normal tool-calling loop. Charts render inline as Plotly figures using the existing `rich_content` pipeline.

## Why Three Separate Tools Instead of One God Tool

**Decision:** Three distinct tools (`draw_bar_chart`, `draw_pie_chart`, `draw_scatter_chart`) instead of one `draw_chart` with a `type` parameter.

**Why:**

1. **LLM reliability.** LLMs are bad at choosing the right enum value. They reliably call the right function when the function IS the type. `draw_bar_chart` vs `draw_pie_chart` is a clear function name choice the model gets right every time. A `chart_type: "bar" | "pie" | "scatter"` parameter invites hallucinated types.

2. **Self-documenting parameters.** Each tool exposes only the parameters relevant to its chart type. `draw_bar_chart` has `horizontal`, `categories`, `series[].values`. `draw_pie_chart` has `donut`, `show_percentages`, `slices[]`. No union types, no conditional validation, no "this param is ignored if chart_type=X" footnotes.

3. **Clear tool descriptions.** The agent sees three distinct tool descriptions in the system prompt, each describing one chart type. When the user says "compare these categories with a bar chart", the model knows exactly which tool to call. No reasoning about enum values needed.

4. **Extensible.** Adding a fourth chart type (line, area, histogram, heatmap) means adding one new tool class. No schema migration on the god tool. No risk of breaking existing parameter handling.

**What we did NOT do:**

- **No `draw_line_chart` yet.** The scatter tool with `mode="lines"` covers line charts. A dedicated line tool can be added later when users ask for time series with date axis handling.
- **No `draw_heatmap` or `draw_histogram` yet.** Those require 2D data grids or binning logic. Wait for user demand before building.

---

## How Charts Flow Through the System

```
User: "Compare Q1-Q4 revenue and costs"

        ↓

PydanticAI agent sees draw_bar_chart tool
        
        ↓

Agent calls: draw_bar_chart(
    title="Q1-Q4 Revenue vs Costs",
    categories=["Q1", "Q2", "Q3", "Q4"],
    series=[
        {"name": "Revenue", "values": [100, 200, 150, 300]},
        {"name": "Costs",   "values": [80,  160, 130, 220]},
    ]
)

        ↓

BarChartTool.execute() → builds plotly Figure → returns (tool_msg, rich_content)

tool_msg: {role: "tool_result", content: {result: "{status: ok, title: ..., items: 4}"}}
rich_content: {role: "rich_content", content: {type: "chart", title: "...", figure: {...}}}

        ↓

Agent returns ChatResponse(text=..., rich_contents=[...])

        ↓

chat/routes.py → chat/callbacks.py → _process_rich_content()

        ↓

Session gets chart message:
{role: "chart", content: {chart_id: "uuid", title: "...", figure: {...}}}

        ↓

chat/templates.py → build_chart_message() → dcc.Graph(figure=...)

        ↓

Plotly renders interactive chart in browser ✅
```

**Why this path:** The existing weather and excel tools already produce `rich_content` with `type: "chart"`. The new chart tools plug into the same pipeline. Zero new rendering code. Zero new callback logic. The system already knows how to display Plotly figures.

---

## Data Object Design

Each tool accepts typed data objects, not raw column references or file IDs. The agent constructs the data from whatever source it has — uploaded files, API results, its own computations.

### Bar Chart Data Shape

```json
{
    "title": "Q1-Q4 Revenue",
    "categories": ["Q1", "Q2", "Q3", "Q4"],
    "series": [
        {
            "name": "Revenue",
            "values": [100, 200, 150, 300]
        }
    ],
    "x_label": "Quarter",
    "y_label": "USD (thousands)",
    "horizontal": false
}
```

**Why categories + series with values, not a DataFrame:** The agent decides what data to show. It might extract categories from a news article, compute aggregates from raw data, or pull numbers from a user query. Forcing a DataFrame or file reference limits the tool to uploaded spreadsheet data only.

**Why multiple series:** A single bar chart often compares multiple metrics. One tool call instead of N.

### Pie Chart Data Shape

```json
{
    "title": "Market Share",
    "slices": [
        {"label": "Product A", "value": 45},
        {"label": "Product B", "value": 30},
        {"label": "Product C", "value": 25}
    ],
    "donut": false,
    "show_percentages": true
}
```

**Why slices, not categories+values like bar chart:** Pie charts have exactly one dimension — each slice is one label+value pair. The flat `slices[]` array is the natural shape. Different interface, different mental model.

**Why `donut` as a boolean:** Donut vs pie is a visual preference, not a data difference. Same data, different hole size. One parameter is enough.

### Scatter Chart Data Shape

```json
{
    "title": "Height vs Weight",
    "series": [
        {
            "name": "Adults",
            "points": [
                {"x": 170, "y": 70, "label": "Alice"},
                {"x": 180, "y": 85, "label": "Bob"},
                {"x": 165, "y": 60, "label": "Carol"}
            ]
        }
    ],
    "x_label": "Height (cm)",
    "y_label": "Weight (kg)",
    "trendline": true
}
```

**Why `series[].points[]` with x,y objects:** Each point is a discrete observation. Optional `label` field lets the agent annotate points (e.g. outlier names). The agent builds these from whatever data it has — no constraints on data source.

**Why trendline as boolean:** Simple linear regression computed in Python. The agent shouldn't need to calculate slopes. The tool does it. When users need polynomial or exponential fits, add a `trendline_type` parameter.

---

## Figure Building

### Color Palette

12 colors, shared across all chart types:

```python
_CHART_COLORS = [
    "#3b82f6",
    "#ef4444",
    "#10b981",
    "#f59e0b",
    "#8b5cf6",
    "#ec4899",
    "#06b6d4",
    "#f97316",
    "#84cc16",
    "#14b8a6",
    "#6366f1",
    "#e11d48",
]
```

**Why 12 colors:** Covers the practical maximum of series anyone puts on one chart. More than 12 series on a bar chart is unreadable. The agent should split it into multiple charts instead.

**Why these specific colors:** Tailwind palette. High contrast, colorblind-friendly pairings. Familiar to anyone who's used Tailwind CSS. No design tool needed.

### Bar Chart Layout

- **Grouped bars:** `barmode="group"` — side by side, not stacked. Stacked bars are harder to read for comparisons. If users ask for stacked, add a `stacked` parameter.
- **Horizontal mode:** Swaps x and y. Useful for long category labels. Height scales with category count (`max(400, len(categories) * 40 + 150)`).
- **Value labels:** `textposition="outside"` — numbers above each bar. Reduces eye travel to y-axis.

### Pie Chart Layout

- **Donut mode:** `hole=0.4` when `donut=True`. Visual preference. Same data.
- **Percentages:** `textinfo="label+percent"` when `show_percentages=True`. Disabled by default to avoid clutter with many small slices.
- **Hover:** Shows label, raw value, and percentage. Both label and value matter for pie interpretation.

### Scatter Chart Layout

- **Default markers:** Size 10, 70% opacity, white border. Visible but not overwhelming. Overlapping points are readable because of partial transparency.
- **Trendline:** Simple linear regression (least squares). Computed in Python, not Plotly's built-in trendline (which has limits). Dashed line, same color as points, lighter weight (1.5px).
- **Size by:** When `size_by="x"` or `size_by="y"`, marker size scales with value (capped 5–30px). Useful for bubble-chart-like emphasis. Default is constant size — uniform markers for correlation plots.
- **Hover labels:** Shows custom `label` field if provided, plus x,y values. If no labels, just x,y.

---

## Integration Points

### What Changed

| File | Change |
|------|--------|
| `tools/interactive_charts.py` | **New.** Three tool classes + figure builders |
| `tools/__init__.py` | Added exports for BarChartTool, PieChartTool, ScatterChartTool |
| `chat/agent.py` | Added 3 fields to ChatDeps, 3 `_register_*` functions, 3 `@agent.tool` wrappers |
| `chat/provider.py` | DeepSeekChat.__init__ accepts 3 new tool args, passes to ChatDeps |
| `app/core/services.py` | Instantiates 3 chart tool singletons, passes to DeepSeekChat |

### What Did NOT Change

- **Templates:** `chat/templates.py` already renders `dcc.Graph` for any `type: "chart"` message. No change.
- **Callbacks:** `chat/callbacks.py` already processes all `rich_content` with `type: "chart"`. No change.
- **Routes:** No new routes. Charts flow through the existing `/chat/send` route.
- **Store:** Charts serialize into `content_json` like weather and excel charts. No schema change.
- **Architecture test:** Auto-discovers `tools/interactive_charts.py` from the `tools/` folder. No test update needed.

### Why No New Routes

Charts aren't a user-facing endpoint. The user doesn't say "I want to hit `/chart/bar`". The user says "compare these numbers" and the agent decides to call `draw_bar_chart`. The tool executes inside the agent's tool-calling loop during `/chat/send`. Same pattern as weather, news, excel.

Adding a route would create a public API for chart generation that nothing calls. YAGNI. If a future feature needs chart-as-a-service, add `POST /chat/tools/chart` to `chat/routes.py` then. For now, the agent is the only caller.

---

## Validation & Error Handling

### Bar Chart Validation

- Categories must not be empty
- Each series must have `name` and `values`
- Each series' `values` length must match `categories` length
- Mismatch error: "Series 'Revenue' has 3 values but there are 4 categories."

### Pie Chart Validation

- Slices must not be empty
- Each slice must have `label` and `value`
- No length mismatch possible — each slice is independent

### Scatter Chart Validation

- Series must not be empty
- Each series must have `name` and `points`
- Each series' points must not be empty

### Error Propagation

Validation errors become `tool_result` messages with `{"error": "..."}`. The LLM sees the error and retries with corrected arguments (PydanticAI retries=2). After 2 retries, the agent gives up and reports the error to the user.

**Why structured errors in tool_result:** The LLM can read JSON error messages and fix its arguments. A string error like "something went wrong" gives the LLM nothing to work with. A specific error like "Series 'Revenue' has 3 values but there are 4 categories" lets the LLM count and correct.

---

## Future Extensions

| What | How |
|------|-----|
| **Line chart** | New `LineChartTool` with `mode="lines+markers"`. Good for time series. |
| **Stacked bars** | Add `stacked: bool` parameter to `BarChartTool`. Change `barmode` to `"stack"`. |
| **Histogram** | New `HistogramChartTool` with `values[]` and `bins` parameter. Plotly's `go.Histogram`. |
| **Heatmap** | New `HeatmapChartTool` with 2D `grid[][]` and `row_labels[]`/`col_labels[]`. |
| **Combined charts** | New `ChartBundleTool` that accepts multiple chart specs and returns `type: "chart_bundle"` rich_content. Callbacks already handle `chart_bundle` type (see `_process_rich_content`). |
| **Annotation support** | Add `annotations[]` to any tool — dicts with `{x, y, text}`. Plotly annotations API. |
| **Axis range** | Add `x_range: [min, max]` and `y_range: [min, max]` to all tools. Useful when agent knows data bounds. |
| **Download as PNG** | Plotly's `config.toImageButtonOptions`. Already available in chart toolbar. Add to `config` dict in `build_chart_message`. |
| **Dark mode** | Plotly template parameter. Set `template="plotly_dark"` in layout. Wire to app theme setting. |

---

## Key Decisions Summary

1. **Three tools, not one.** Function name = chart type. LLM picks the right one reliably.
2. **No new routes.** Charts are tool output, not API endpoints. Flow through existing `/chat/send`.
3. **No rendering changes.** Existing chart pipeline handles Plotly figures for all types.
4. **Typed data objects.** Agent constructs data, tool validates and renders. No raw column references.
5. **Structured errors.** LLM sees specific error messages and retries with corrected arguments.
6. **No config needed.** Tools are pure data→figure transforms. Zero API keys, zero URLs.