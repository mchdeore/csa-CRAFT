# 08 — Delete weather + news tools; reserve pitch tool slots

**Status:** planned · depends on `03-agent-azure-sdk.md`, `07-data-sources-registry.md`

## Why

Weather and news tools are demo filler. The CRAFT pitch is RAG over CSA mission docs; weather/news have no place in any of the use cases (UC-E2 Risk, UC-F1 Cost, UC-F4 Vendor, UC Bilingual RAG). Keeping them in the registry pollutes `/tools/list`, bloats the system prompt (which currently namechecks "Montreal weather" + "news"), and keeps external dependencies on Open-Meteo and Guardian around for no reason.

At the same time the pitch names several tool slots the current code has nothing for: `ClassifierTool` (UC-E2), `HistoricalMissionTool` (UC-F1), `CostAggregatorTool` (UC-F1), `VendorAggregatorTool` (UC-F4), `CodeExecTool` (ASG-001/004/011 reserved). This plan deletes the demo tools and leaves `NotImplementedError` stubs in their place so the registry and the agent factory know they exist.

## Scope

**In**
- Delete `tools/weather/` and `tools/news/` entirely (code + tests + READMEs).
- Delete `OPEN_METEO_*`, `GUARDIAN_*`, `AZURE_COHERE_*` from the env schema (plan 01 already excludes them; drop any lingering references).
- Delete all weather / news / Cohere wiring from `app/core/services.py` and `chat/agent.py`.
- Rewrite `app/core/system_prompt.txt` — tool-agnostic RAG prompt. No Montreal, no weather, no news.
- Add reserved tool stubs:
  - `tools/classifier/` (risk classifier — UC-E2).
  - `tools/historical_mission/` (UC-F1 retrieval).
  - `tools/cost_aggregator/` (UC-F1 aggregation).
  - `tools/vendor_aggregator/` (UC-F4 aggregation).
  - `tools/code_exec/` (ASG-reserved sandbox slot).

Each stub implements `⟨I⟩ Tool`, exposes a plausible `definition()` (so the agent can see the schema), and `execute(...)` raises `NotImplementedError("reserved — see plans/08…")`.

**Out**
- Actual implementation of any reserved tool. Each is a separate future plan.
- The CSA risk taxonomy (pitch marks it blocked, drives the real classifier).

## Files touched

- **Delete**
  - `tools/weather/` (whole folder incl. `__init__.py`, `forecast.py`, `historical.py`, `README.md`, tests).
  - `tools/news/` (whole folder).
- **Edit**
  - `app/core/services.py` — remove `weather_tool`, `historical_weather_tool`, `news_tool`, Cohere wiring, and matching kwargs on the chat provider constructor.
  - `chat/agent.py` — remove the three tool registrations and matching entries from the `TOOLS` list / `ChatDeps` fields.
  - `tools/routes.py` — remove `get_weather`, `get_historical_weather`, `search_news` from `tool_map` and from the `list_tools` payload.
  - `app/.env.example` — remove any `OPEN_METEO_*`, `GUARDIAN_*`, `AZURE_COHERE_*` lines (plan 01 should already have done this; verify).
  - `tools/__init__.py` — stop re-exporting the deleted classes; add the reserved stubs.
  - `tools/README.md` — update list.
- **New**
  - `app/core/system_prompt.txt` — tool-agnostic RAG prompt.
  - `tools/classifier/__init__.py` + `classifier.py` with `ClassifierTool` stub.
  - `tools/historical_mission/__init__.py` + `historical_mission.py` with `HistoricalMissionTool` stub.
  - `tools/cost_aggregator/__init__.py` + `cost_aggregator.py` with `CostAggregatorTool` stub.
  - `tools/vendor_aggregator/__init__.py` + `vendor_aggregator.py` with `VendorAggregatorTool` stub.
  - `tools/code_exec/__init__.py` + `code_exec.py` with `CodeExecTool` stub.
  - Each new folder gets a short `README.md` describing the reserved purpose.

## Stub template

```python
# tools/classifier/classifier.py
from typing import Any

class ClassifierTool:
    """Reserved — UC-E2 risk classifier. See plans/08-delete-weather-news.md."""

    risky = True  # HITL interrupt will fire when ENABLE_HITL=1

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "classify_risk",
                "description": "Score risk severity for a CADRe part. RESERVED — not implemented.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "excerpt": {"type": "string", "description": "Text excerpt to classify."},
                    },
                    "required": ["excerpt"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict | None]:
        raise NotImplementedError("classify_risk: reserved — see plans/08-delete-weather-news.md")
```

Same pattern for the other four stubs with their own schemas.

## System-prompt rewrite

```text
# app/core/system_prompt.txt
You are CRAFT, an assistant for Canadian Space Agency mission engineering and
finance. You answer by retrieving cited passages from the local corpus, running
small analyses on retrieved data, and drawing charts when a visual helps.

Rules:
- Prefer calling the document search tool over guessing.
- Always carry citations through to the user.
- If a tool is marked RESERVED, say the capability is not available yet; do not fabricate a result.
- Keep responses concise. Say "I don't know" when the corpus doesn't support an answer.
```

No "Montreal", no weather, no news.

## Workflow

**Pre-check**
- Plans 03 and 07 shipped.
- `chat/agent.py` uses the plain `TOOLS: list[Tool]` pattern from plan 03.

**Do**
1. `git rm -r tools/weather tools/news`.
2. Delete references in `app/core/services.py`, `chat/agent.py`, `tools/routes.py`, `tools/__init__.py`, `tools/README.md`.
3. Write `app/core/system_prompt.txt` and point `build_system_prompt` (in `app/core/config.py` or wherever it moved) at `settings.SYSTEM_PROMPT_FILE`.
4. Create the five reserved tool folders with stubs + READMEs.
5. Register the stubs in `app/core/services.py` and in the `TOOLS` list used by `chat/agent.py`, so they appear in `/tools/list` and in the agent's schema list.
6. Rewrite tests: delete `tools/weather/tests` and `tools/news/tests`; add trivial `tools/<stub>/tests/test_schema.py` for each new stub asserting the schema shape and that `execute` raises `NotImplementedError`.

**Verify**
- `grep -rEi "weather|open.?meteo|guardian|cohere|rerank|montreal" --include='*.py' --include='*.md' --include='*.txt' --include='*.json'` returns zero outside git history.
- `pytest -q` green.
- `curl /tools/list` (with internal header or `ENABLE_DEBUG_ROUTES` + admin) lists the real tools and the five reserved stubs; weather / news absent.
- Chat round-trip against the real Azure model: asking the model to call `classify_risk` returns a tool-error message routed through the `AgentAction` audit.

**Commit**
`refactor(tools): drop weather/news demo tools; reserve pitch tool slots`

**Rollback**
`git restore -SW . && git checkout -- tools/weather tools/news`

## Verification checklist

- [ ] `tools/weather` and `tools/news` folders don't exist.
- [ ] No `OPEN_METEO_*`, `GUARDIAN_*`, `AZURE_COHERE_*` references anywhere.
- [ ] `app/core/system_prompt.txt` has no demo nouns.
- [ ] Five reserved stub folders exist, each with a `README.md`, a stub class, and a trivial test.
- [ ] `/tools/list` shows real + reserved; no demo.
- [ ] `pytest` green.

## Out of scope

- Implementing any reserved tool. Each is a separate follow-up plan.
- The actual CSA risk taxonomy (pitch marks it blocked).
- UI badging for "reserved" vs "live" tools.

---

## Reasoning / justification extracts

**User instructions:**
- "get rid of the openmeteo stuff and weather stuff, clean that up too, no tools or anything for that".
- "we also only have local sql and no external data connectors for now but make sure to keep abstractions so it can be added later".
- "proper routes".

**Pitch tool list (reserved today, implemented later):**
- `DocumentSearchTool` + `TextAnalysisTool` — already live, kept.
- `ClassifierTool` (UC-E2, Risk ID) — reserved stub here.
- `HistoricalMissionTool` + `CostAggregatorTool` (UC-F1, Parametric Cost) — reserved stubs.
- `VendorAggregatorTool` (UC-F4, Vendor Cost Roll-up) — reserved stub.
- `CodeExecTool` (ASG-001/004/011 sandbox) — reserved stub.

Pitch §3 names each use case and its required tools; §4 Design Decisions "Guardrails + sandbox" row calls `CodeExecTool` reserved; §7 Blockages lists the CSA risk taxonomy as blocking the classifier.

**Why `risky = True` on `ClassifierTool`:**
Pitch §2 Internals, Panel A shows the HITL interrupt branching off the tool call. UC-E2 explicitly runs through HITL ("Engineer uploads a CADRe part … classifier tool scores severity; HITL approves"). Marking the stub `risky` lets the HITL plumbing (plan 13) exercise end-to-end even before the real classifier lands.

**Why keep the reserved slots in-tree (vs delete and recreate later):**
Readers (humans and agents) opening `tools/` see the full pitch surface and know what's live versus reserved. Pyright-strict picks up any accidental call site. The "swap target already named behind the protocol" posture pitch §4 argues for.
