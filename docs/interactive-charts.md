# Interactive Chart Tool Library — Design Decisions

## What Was Built

Seven chart tools for agents to display interactive charts in chat: bar chart, pie chart, scatter plot (with polynomial fit and residuals), heatmap, histogram, line chart, box plot. The agent passes structured data objects through the normal tool-calling loop. Charts render inline as Plotly figures using the existing `rich_content` pipeline.

All tools are also accessible via direct REST routes at `POST /tools/execute/<tool_name>` for testing without the LLM agent.

## Why Separate Tools Instead of One God Tool

**Decision:** Seven distinct tools (`draw_bar_chart`, `draw_pie_chart`, `draw_scatter_chart`, `draw_heatmap`, `draw_histogram`, `draw_line_chart`, `draw_box_plot`) instead of one `draw_chart` with a `type` parameter.

**Why:**

1. **LLM reliability.** LLMs are bad at choosing the right enum value. They reliably call the right function when the function IS the type. `draw_bar_chart` vs `draw_pie_chart` is a clear function name choice the model gets right every time. A `chart_type: "bar" | "pie" | "scatter"` parameter invites hallucinated types.

2. **Self-documenting parameters.** Each tool exposes only the parameters relevant to its chart type. `draw_bar_chart` has `horizontal`, `categories`, `series[].values`. `draw_pie_chart` has `donut`, `show_percentages`, `slices[]`. No union types, no conditional validation, no "this param is ignored if chart_type=X" footnotes.

3. **Clear tool descriptions.** The agent sees three distinct tool descriptions in the system prompt, each describing one chart type. When the user says "compare these categories with a bar chart", the model knows exactly which tool to call. No reasoning about enum values needed.

4. **Extensible.** Adding an eighth chart type means adding one new tool class. No schema migration on the god tool. No risk of breaking existing parameter handling.

**What we did NOT do:**

- No combined "god tool". Every chart type is its own function. The LLM picks reliably.
- No chart bundling yet. Multiple charts in one rich_content would require a `chart_bundle` type. Callbacks already handle this, so a `ChartBundleTool` is a future option.

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

**Why trendline as boolean:** Simple linear regression computed in Python. The agent shouldn't need to calculate slopes. The tool does it. For polynomial fits, use `fit_degree` parameter.

### Scatter — Polynomial Fit & Residuals

The scatter tool supports two advanced parameters:

- `fit_degree` (int, default 1): Degree of polynomial to fit. 1 = linear, 2 = quadratic, 3 = cubic, up to 5. Uses numpy's `polyfit` and `polyval`. R-squared displayed in hover.
- `show_residuals` (bool, default false): Shows a residuals subplot below the scatter. Requires `trendline=true`.

```json
{
    "title": "Polynomial Fit Example",
    "series": [
        {
            "name": "Data",
            "points": [
                {"x": 0, "y": 1},
                {"x": 1, "y": 3},
                {"x": 2, "y": 7},
                {"x": 3, "y": 13},
                {"x": 4, "y": 21}
            ]
        }
    ],
    "trendline": true,
    "fit_degree": 2,
    "show_residuals": true
}
```

**How residuals work:** Uses Plotly `make_subplots(rows=2, cols=1)`. Top row: scatter points + polynomial fit curve. Bottom row: residuals (actual - fitted) as scatter markers with a dashed zero-line at y=0. Height adjusts to 650px.

**Why numpy:** `numpy.polyfit` computes least-squares polynomial coefficients. `numpy.polyval` evaluates them. Both are stable, well-tested. numpy is already a dependency (pandas uses it in excel_tool).

### Heatmap Data Shape

```json
{
    "title": "Correlation Matrix",
    "rows": ["Revenue", "Costs", "Profit"],
    "cols": ["Q1", "Q2", "Q3", "Q4"],
    "values": [
        [100, 200, 150, 300],
        [80,  160, 130, 220],
        [20,  40,  20,  80]
    ],
    "colorscale": "viridis"
}
```

**Parameters:** `title`, `rows`, `cols`, `values` (2D grid), `x_label`, `y_label`, `colorscale` (viridis, rdbu, blues, greens, reds, ylorrd, plasma, grays, and others).

**Plotly:** `go.Heatmap` with hovertemplate showing "row: X, col: Y, value: Z". Height scales with row count.

**Validation:** Row labels, column labels, and values must all match dimensions. Each row must have exactly as many values as there are columns.

### Histogram Data Shape

```json
{
    "title": "Income Distribution",
    "values": [45000, 52000, 61000, 48000, 73000],
    "num_bins": 20,
    "show_curve": true
}
```

**Parameters:** `title`, `values` (flat list of numbers), `num_bins` (optional; auto-computed via Sturges' rule: `ceil(log2(n) + 1)`, minimum 5), `x_label`, `show_curve` (overlay normal distribution), `opacity` (0.3-1.0).

**Plotly:** `go.Histogram`. When `show_curve=true`, computes mean and std of data, generates normal PDF curve scaled by `count * bin_width`, and overlays as `go.Scatter`.

**Why Sturges' rule:** Simple, parameter-free default that works for most datasets. Agent can override with `num_bins` if needed.

### Line Chart Data Shape

```json
{
    "title": "Monthly Revenue",
    "x_values": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "series": [
        {"name": "Revenue", "y_values": [100, 120, 140, 160, 180, 200]},
        {"name": "Costs",   "y_values": [80,  85,  95,  100, 110, 120]}
    ],
    "fill": false,
    "x_is_date": false,
    "markers": true
}
```

**Parameters:** `title`, `x_values`, `series` (with `name` + `y_values`), `x_label`, `y_label`, `fill` (fill under line), `x_is_date` (date formatting), `markers` (show dots).

**Plotly:** `go.Scatter(mode="lines+markers")`. `fill="tozeroy"` with translucent rgba when `fill=true`. `markers=false` hides dots for clean line-only view.

**Validation:** x_values length must match each series' y_values length.

### Box Plot Data Shape

```json
{
    "title": "Salary by Department",
    "groups": [
        {"name": "Engineering", "values": [120, 130, 125, 140, 135, 200]},
        {"name": "Sales",       "values": [80,  90,  85,  95,  88,  400]},
        {"name": "HR",          "values": [70,  75,  72,  78,  74]}
    ],
    "show_points": true,
    "horizontal": false
}
```

**Parameters:** `title`, `groups` (list of `{name, values[]}`), `y_label`, `show_points` (overlay jittered points), `horizontal` (horizontal boxes).

**Plotly:** `go.Box` with `boxpoints="all"` and `jitter=0.3` when `show_points=true`. Each group gets its own color from the shared palette.

**Validation:** Groups must be non-empty. Each group must have `name` and non-empty `values`.

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

- **Default markers:** Size 10, 70% opacity, white border. Overlapping points are readable.
- **Polynomial fit:** Uses numpy `polyfit` for least-squares polynomial regression (degree 1-5). Linear by default. Quadratic and cubic for curves. R-squared shown in fit curve hover.
- **Residuals subplot:** 2-row layout when `show_residuals=true`. Top: data + fit. Bottom: residuals (actual - fitted) with zero reference line. Height 650px.
- **Size by:** When `size_by="x"` or `size_by="y"`, marker size scales with value (capped 5-30px).
- **Hover labels:** Shows custom `label` if provided, plus x,y. Fit curve shows R-squared and fitted y.

### Heatmap Layout

- **Color scale:** Default "viridis". Supports 15+ named color scales (rdbu, blues, greens, reds, ylorrd, plasma, grays, etc.). Unknown names fall back to viridis.
- **Height:** Scales with row count (`max(400, len(rows) * 30 + 150)`). Reads well with many rows.
- **Hover:** Shows "row: X, col: Y, value: Z" in clean format. Thousands separator for readability.
- **Colorbar:** Inline legend on the right side.

### Histogram Layout

- **Auto-binning:** Sturges' rule (`ceil(log2(n) + 1)`, minimum 5) when `num_bins` not provided. Agent can override with a specific number.
- **Normal curve overlay:** When `show_curve=true`, computes mean and standard deviation from data. Generates normal PDF scaled by `count * bin_width` to match histogram y-axis scale. Smooth curve overlay in contrasting color.
- **Opacity:** Default 0.7. Adjustable 0.3-1.0 for visual clarity with overlay.

### Line Chart Layout

- **Mode:** `lines+markers` by default. `markers=false` for clean line-only view.
- **Fill:** `fill="tozeroy"` with translucent rgba fill when enabled. Hex-to-rgba conversion preserves color identity with 15% opacity fill.
- **Date support:** `x_is_date=true` sets x-axis type to "date" for proper time-series formatting.
- **Hover:** `hovermode="x unified"` shows all series values at each x point simultaneously.

### Box Plot Layout

- **Orientation:** Vertical by default. `horizontal=true` swaps axes. Height scales with group count (`max(350, len(groups) * 60 + 150)`).
- **Points overlay:** `boxpoints="all"` with `jitter=0.3` when `show_points=true`. Individual data points visible alongside summary statistics.
- **Colors:** Each group gets a distinct color from the shared 12-color palette.
- **Hover:** Shows group name and value. Clean template with no extra clutter.

---

## Integration Points

### What Changed

| File | Change |
|------|--------|
| `tools/charts/bar.py` | Bar chart tool |
| `tools/charts/pie.py` | Pie chart tool |
| `tools/charts/scatter.py` | Scatter chart tool with polynomial fit and residuals |
| `tools/charts/heatmap.py` | **New.** Heatmap tool |
| `tools/charts/histogram.py` | **New.** Histogram tool |
| `tools/charts/line.py` | **New.** Line chart tool |
| `tools/charts/boxplot.py` | **New.** Box plot tool |
| `tools/charts/_shared.py` | Shared helpers: colors, validation, message builders |
| `tools/charts/__init__.py` | Exports all 7 chart tools |
| `tools/__init__.py` | Re-exports all chart tools |
| `tools/routes.py` | Registers all tools in `POST /tools/execute/<name>` and `GET /tools/list` |
| `chat/agent.py` | ChatDeps has 7 chart tool fields, 7 `_register_*` functions |
| `chat/provider.py` | DeepSeekChat accepts 7 chart tool args |
| `app/core/services.py` | Instantiates 7 chart tool singletons |

### What Did NOT Change

- **Templates:** `chat/templates.py` already renders `dcc.Graph` for any `type: "chart"` message. No change.
- **Callbacks:** `chat/callbacks.py` already processes all `rich_content` with `type: "chart"`. No change.
- **Routes:** No new routes. Charts flow through the existing `/chat/send` route.
- **Store:** Charts serialize into `content_json` like weather and excel charts. No schema change.
- **Architecture test:** Auto-discovers new files in `tools/charts/`. No test update needed.

### Why Routes for Direct Execution

Tools are also accessible via `POST /tools/execute/<tool_name>` for direct testing without the LLM agent. `GET /tools/list` returns all registered tools with descriptions and parameters. This is for debugging, testing, and codepath tracing — every tool invocation appears in structured logs with `caller_module`, `caller_function`, and `cause` fields.

The agent path (`/chat/send` → agent → tool) and the direct route path (`POST /tools/execute/<tool_name>`) are independent. Both hit the same tool instance. Both produce the same rich_content. Both are logged.

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
| **Stacked bars** | Add `stacked: bool` parameter to `BarChartTool`. Change `barmode` to `"stack"`. |
| **Stacked area** | Add `stackgroup` parameter to `LineChartTool`. Plotly supports stacked area fills. |
| **Combined charts** | New `ChartBundleTool` that accepts multiple chart specs and returns `type: "chart_bundle"` rich_content. Callbacks already handle `chart_bundle` type. |
| **Annotation support** | Add `annotations[]` to any tool — dicts with `{x, y, text}`. Plotly annotations API. |
| **Axis range** | Add `x_range: [min, max]` and `y_range: [min, max]` to all tools. Useful when agent knows data bounds. |
| **Download as PNG** | Plotly's `config.toImageButtonOptions`. Already available in chart toolbar. Add to `config` dict in `build_chart_message`. |
| **Dark mode** | Plotly template parameter. Set `template="plotly_dark"` in layout. Wire to app theme setting. |
| **Higher-degree fits** | Scatter already supports up to degree 5. For higher degrees (6+) or splines, add scipy dependency later. |

---

## Key Decisions Summary

1. **Seven tools, not one.** Function name = chart type. LLM picks the right one reliably.
2. **Direct routes for testing.** `POST /tools/execute/<tool_name>` and `GET /tools/list` for debugging without the agent loop.
3. **No rendering changes.** Existing `type: "chart"` pipeline handles all Plotly figures.
4. **Typed data objects.** Agent constructs data, tool validates and renders. No raw column references.
5. **Polynomial fits with numpy.** Degrees 1-5 via `polyfit`/`polyval`. R-squared in hover. Residual subplot for fit quality.
6. **Structured errors.** LLM sees specific error messages and retries with corrected arguments.
7. **No config needed.** All chart tools are pure data→figure transforms. Zero API keys.
