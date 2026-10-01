---
title: "CRAFT — Pitch Package"
margin:
  x: 1.2cm
  y: 0.8cm
fontsize: 8pt
lin: 1.10
---

## Legend
■ Actor · ◇ Gate · ☁ Cloud · ⬡ Terminal · ▦ Store · ···· Planned · ⟨I⟩ Protocol · Blue=Auth · Green=Audit · (today) · (next) · (end-state)

## 1. Containers (L2)

### Figure 1 · L2 — Containers, Actors, External Systems

```text
┌─────────────────┐
│Mission Eng      │──▶┌──────────────────────────────────────────┐
│Systems Eng      │──▶│                CRAFT                     │
│Program Admin    │──▶│           Flask + Dash                   │
│HITL Reviewer    │──▶│                                          │
└─────────────────┘   └──┬─────────┬─────────┬─────────┬────────┘
                         │         │         │         │
                         ▼         ▼         ▼         ▼
                    ┌─────────┐┌────────┐┌────────┐┌────────────┐
                    │LLM & AI ││Data Src││ID+Edge ││Ops & Audit │
                    │AzureOA  ││LocalFs ││Local(t)││JSONL(t)    │
                    │AI Srch(e)│ShPt(e)││Entra(e)││LogAnalyt(e)│
                    │ContSfty ││SAP(e) ││APIM(e) ││AppSvc PBMM │
                    │(e)      ││STK(e) ││AppGW(e)││LaunchP(e)  │
                    └─────────┘└────────┘└────────┘└────────────┘
```
In: `/chat/send [base]` `/admin/* [admin]`. Out: thin italic. (t)=today, (e)=end-state.

**Agent runtime, stage one (today).** The primary agent is a bounded ReAct loop written directly on `openai.AsyncAzureOpenAI` — ~250 lines in `chat/agent.py`. The pattern is: LLM turn → tool-call parse → tool.execute → audit → repeat, capped by `AGENT_RECURSION_LIMIT=25`. One primary agent, ten tools, HITL interrupt as an exception-and-resume pattern. **No orchestration framework installed.** Microsoft documents this exact "hand-roll it on the SDK" pattern; Azure OpenAI's native tool-calling (`tools=` request / `tool_calls` response) is the only contract we need.

**Agent runtime, stage two (if and when).** Azure does not mandate an orchestration framework. If a trigger below materialises, we swap behind the stable `⟨I⟩ ChatProvider` protocol — one class change, no routes / audit / storage / data-source impact. Two candidates, ranked by Azure-native fit:

1. **Microsoft Agent Framework** (GA April 2026, Microsoft's enterprise-ready successor to Semantic Kernel; the Microsoft-blessed choice for Azure-consolidated deployments). First-class Azure OpenAI + Foundry integration, multi-language SDK (Python / C# / Java), long-term support commitment.
2. **LangGraph** (third-party, LangChain Inc.). Rich ecosystem (LangSmith, retriever abstractions), but adds a `pydantic` + `langchain-*` dep tree. Fine, not Azure-native.

Triggers that would make either worth adopting: ≥ 3 specialist agents coordinating under a planner, dynamic tool composition from user input, LangSmith tracing as a procurement line, or hybrid-retrieval chains with self-correction loops that grow past ~400 lines.

### Figure 2 · L1 Context

```text
┌─────────────────┐
│Mission Eng      │──▶┌──────────────────────────────────────────┐
│Systems Eng      │──▶│                CRAFT                     │
│Program Admin    │──▶│           Flask + Dash                   │
│HITL Reviewer    │──▶│                                          │
└─────────────────┘   └──────────────────────────────────────────┘
```

## 2. Internals (L3)

### Figure 3 · L3 — Internal Clusters

```text
Panel A · Agent (today = Azure SDK direct):
   User msg → chatbot node → should_continue?
                              │
             respond ◀────────┤
                              │
                           tool_call ──▶ Tool exec ──▶ Audit ──▶ loop (max 25)
                                                │
                                           ◇ HITL gate (if risky) ──▶ ApprovalQueue
                                                                        │
                                                                   ◇ approve/deny
                                                                        │
                                                                   resume loop
Panel A · Agent (end-state = LangGraph swap-in behind ⟨I⟩ ChatProvider):
   Same shape; `interrupt_before=["tool_node"]` instead of AgentPaused exception.

Panel B · Tool Registry (⟨I⟩ Tool):
   documents  charts  query_data              ← live today
   classifier(r)  historical_mission(r)       ← reserved stubs
   cost_aggregator(r)  vendor_aggregator(r)
   code_exec(r)
   POST /tools/execute/<name>  — validated, audited

Panel C · DataSource Registry (⟨I⟩ DataSource):
   LocalFile                                  ← live today
   SharePoint(e)  SAP(e)  STK/MATLAB(e)  AzureAISearch(e)
   per-request · RBAC-scoped · MSAL/OAuth (e)
   response carries doc/page/section + confidence

Panel D · Auth / Route gate:
   Public inbound [/route][role]
     → FlaskRoute → ◇ before_request (auth · role · trace_id)
     → handler
     → ◇ after_request (audit emit)
     → response
   permissions.json: base(1) < power(2) < admin(3)
   role < required → 403     unregistered route → 404 (before auth)
```

(r) = reserved. `NotImplementedError` stub satisfying `⟨I⟩ Tool`; agent sees the schema, factory enumerates.

HITL (UMR-021–026 / HITL-001–007) is a graph interrupt off `tool_node`, not middleware: the queue, timeout, reviewer UI, and decision log sit inside the same auth and audit perimeter as the agent. Self-correction / grounding loops (UMR-009/010) attach as graph nodes between retrieve and respond.

## 3. Use Cases

### Figure 4 · Generic Use-Case Lane

```text
USER         AGENT        SERVICES                      TERMINAL
────────────────────────────────────────────────────────────────
Caller ──▶ ◇ Auth ──▶ Agent ──▶ DataSource ──▶ Tool ──▶ ●
          role·trace  ReAct     retrieve        process·plan   audit·end
                                       │
                                       ▼
                                  ◇ HITL (if risky)
                                       │
                                       ▼
                                  DataSource write (e)
```

Role check · AgentAction audit · HITL interrupt stay fixed; the Tool and DataSource behind each block are swapped per use case.

**UC-E2 · Risk ID + HITL (Engineering).** Engineer uploads a CADRe part; retrieval pulls risk sections from the corpus; a classifier tool scores severity; HITL approves; a DataSource write lands the entry in the risk register. Tools: `DocumentSearchTool`, `ClassifierTool`. Requirements: UMR-002/006, UMR-036–040, HITL-001.

**UC-F1 · Parametric Cost + HITL (Finance).** Admin asks for a mission cost estimate; retrieval returns similar historical missions; an aggregator tool computes weighted distance; HITL approves; the commitment is written. Tools: `HistoricalMissionTool`, `CostAggregatorTool`. Requirements: UMR-031–035.

**UC-F4 · Vendor Cost Roll-up (Finance).** Analyst asks "how much did we spend with vendor X across missions?"; a DataSource (SAP connector at end state, CSV fixtures today) returns line items; a `VendorAggregatorTool` sums by vendor; a report is returned. Requirements: UMR-053–055.

**UC · Bilingual Chat / RAG (All).** User asks in English or French; retrieval + `DocumentSearchTool` return cited passages; the agent responds with citations and a confidence score. Requirements: UMR-001/002/003/007/010.

New mission flows (budget scenarios, anomaly triage, cross-mission compare) land as new `Tool` + optional `DataSource` behind the same lane.

## 4. Design Decisions

Component / end-state choice / current alternative / why. "Today" is what ships on this branch after the refactor; "end state" is the Azure-consolidated target.

| Component | End-state choice | Current alternative (today) | Why |
|---|---|---|---|
| HTTP surface | **Flask + Dash** reviewer UI | — (live) | Routes are the integration contract — any token-bearing caller (user, cron, agent) can hit CRAFT; Dash shares the auth and audit perimeter. |
| Agent runtime | **Azure OpenAI SDK direct** (hand-rolled ReAct loop in `chat/agent.py`). If a trigger materialises: **Microsoft Agent Framework** (Azure-native, GA April 2026) OR **LangGraph** (third-party) — both swap behind `⟨I⟩ ChatProvider` | — (live, Azure SDK direct, no framework) | Azure does **not** require an orchestration framework; the SDK's native tool-calling is sufficient for one primary agent + ~10 tools. Minimum dep surface (no `pydantic`, no `langchain-*`, no `semantic-kernel`). ~250 lines carry bounded recursion, HITL interrupt, tool-call audit. Framework swap deferred until multi-agent, dynamic tool composition, or vendor-tracing requirements land. |
| LLM inference | **Azure AI Foundry** (Azure IQ) — model routing + rate limits + Content Safety | **Azure OpenAI direct** (Canadian PBMM region, Chat Completions API, native tool-calling, structured outputs) | Foundry collapses model routing, rate-limit and guardrail procurement into one line while PBMM residency stays. SDK stays `openai.AsyncAzureOpenAI`; the endpoint URL changes. |
| Retrieval | **Azure AI Foundry index / Azure AI Search** hybrid (vector + BM25) | **LocalFileSource** via `⟨I⟩ DataSource` with filename/path search | Same `⟨I⟩ DataSource` call site; cutover is config. Satisfies UMR-004/005/006. |
| Guardrails + sandbox | **Content Safety** + **Azure Container Apps** | Guardrail hook disabled (`GUARDRAIL_HOOK=""`); `CodeExecTool` slot reserved | End-state wires into the tool wrapper CRAFT already runs. UMR-020 / UMR-093. |
| Identity | **Entra ID + MSAL** | Local `AuthProvider` stub; SQLite users seeded by `scripts/seed.py` | Same token flow for humans and external agents; CSA-standard. |
| Audit sink | **Azure Log Analytics** (immutable retention) | **Hash-chained JSONL** on disk via `HashChainedJsonlLog`; `python -m app.core.audit verify` | KQL at end state; grep today; UMR-027 / ASG-003. Same envelope, same chain property — forwarder at deploy time. |
| HITL queue + memory | **Postgres** (approval queue + 3-tier memory) | **SQLite `approvals` table** + resume routes (`/admin/approvals/<trace_id>/<decision>`); reviewer UI reserved | Durable across restarts; UMR-025 TTL, UMR-014 memory. Swap behind `⟨I⟩ ApprovalQueue`. |
| Session + per-user data | **Managed DB** behind `⟨I⟩ WorkspaceStore` | SQLite file-local (`SqliteStore` + `SqliteDataStore`) | Swap target already named behind the protocol. |
| Edge | **APIM + App Gateway** (WAF) | Direct App Service | WAF + rate limit at perimeter; UMR-030. |
| Deployment | **App Service PBMM** + **SSC LaunchPad HA** | Single-region App Service | HA + landing zone come with LaunchPad; UMR-057. |
| Protocol contracts | `⟨I⟩ Tool`, `⟨I⟩ DataSource`, `⟨I⟩ ChatProvider`, `⟨I⟩ WorkspaceStore`, `⟨I⟩ AgentActionLog`, `⟨I⟩ ApprovalQueue` | — (live) | New capability or backend = one class satisfying a protocol; agent unchanged. Pyright-strict verified. |
| Invariants | pytest + pyright (strict) + ruff + bandit + pip-audit + detect-secrets + doctest coverage + stateful-module coverage | — (live) | Route × role matrix, protocol contracts, audit-envelope present, every public function has an executable example, every stateful module has a test file. Industry-standard, maintained. |

### Azure services and orchestration frameworks — explicit stage map

A one-glance view of what Azure services and what orchestration framework (if any) are in use at each stage. "Today" is the shipping MVP; "Next" is reached by adding one targeted dep and one class behind an existing protocol; "End state" is the Azure-consolidated target.

**Correction on a common assumption.** Azure OpenAI does **not** require any orchestration framework. The SDK's native tool-calling (`tools=` request / `tool_calls` response) is a self-contained contract; Microsoft's own documentation shows the hand-rolled pattern. The Azure-native framework option — if we ever decide to adopt one — is Microsoft Agent Framework (GA April 2026). LangChain / LangGraph are third-party alternatives, not Azure requirements.

| Capability | Today (Azure SDK direct, no framework) | Next (one dep, one class) | End state (Azure IQ / Foundry) |
|---|---|---|---|
| LLM transport | `openai.AsyncAzureOpenAI` → Azure OpenAI (PBMM) | same | same, endpoint behind Azure AI Foundry |
| Agent runtime | Hand-rolled ReAct loop in `chat/agent.py`; `AGENT_RECURSION_LIMIT=25`; `AgentPaused` exception-and-resume for HITL | **unchanged** | Trigger-driven swap behind `⟨I⟩ ChatProvider`: either **Microsoft Agent Framework** (Azure-native, deeper Foundry integration) or **LangGraph** (third-party, richer tracing via LangSmith). Triggered by multi-agent, dynamic tools, or vendor-tracing requirements. |
| Tool schemas | Each `⟨I⟩ Tool.definition()` returns an OpenAI JSON Schema dict; passed verbatim to `tools=` | same | same (framework-native tool decorators would also work, not required) |
| Guardrails | `GUARDRAIL_HOOK=""` — hook call site in tool wrapper, no-op | `GUARDRAIL_HOOK="azure_content_safety"` — read `content_filter_results` from the SDK response in the hook | Content Safety deployment-side + explicit `azure-ai-contentsafety` SDK if needed |
| Retrieval | `LocalFileSource` filesystem search via `⟨I⟩ DataSource` | Add `azure-search-documents`; one new `AzureAISearchSource` class; one JSON row in `data_sources.json` | Hybrid (vector + BM25) in Azure AI Search |
| External connectors | — | SharePoint via `msgraph-sdk`; SAP via `requests` (OData); STK/MATLAB via vendor Python APIs — each one `⟨I⟩ DataSource` class, one JSON row | same |
| Identity | `InMemoryAuth` hydrated from SQLite via `scripts/seed.py` | Replace `InMemoryAuth` body with MSAL-backed check; `msal` already a dep | Entra ID; same `⟨I⟩ AuthProvider` contract |
| HITL queue | `SqliteApprovalQueue` + `/admin/approvals/*` routes | Replace with `PostgresApprovalQueue` behind `⟨I⟩ ApprovalQueue`; add `psycopg[binary]` | Postgres, same schema |
| Audit sink | `HashChainedJsonlLog` on disk | Sidecar forwarder reads the JSONL; no code change in-repo | Azure Log Analytics (immutable retention) |
| Code-exec sandbox | `CodeExecTool` reserved stub | Local Docker runner behind `⟨I⟩ Tool` | Azure Container Apps |
| Grounding / confidence | Prompt engineering + second LLM call via same `openai` client | add RAGAS-style scorer behind a `GroundingTool` | Foundry evaluation plugs into the same node |
| Observability | pytest + pyright + ruff + bandit + pip-audit + detect-secrets | add OpenTelemetry via `azure-monitor-opentelemetry` on the Flask app | Azure Monitor + Log Analytics; LangSmith only if LangGraph is adopted |

**Rule of thumb.** The LLM transport (Azure OpenAI) is live from day one. Every other Azure service is a reserved slot behind an existing protocol — adding it is one targeted dep and one class, not a rewrite. Orchestration frameworks (Microsoft Agent Framework or LangChain / LangGraph) are explicitly deferred; we adopt one only when the triggers in the Agent-runtime row materialise, and the choice at that point favours the Azure-native option.

## 5. Solving the Problems — Today and at End State

The system is already running against stubs or local alternatives wired through the same registries that will carry the Azure services at end state. Cutover is a config change per row, not a rewrite.

| Problem (requirement) | How the architecture solves it today | How it solves it at end state (Azure-consolidated) |
|---|---|---|
| Cited retrieval (UMR-002/005/006, ARR-002/003) | `DocumentSearchTool` + `TextAnalysisTool` over `LocalFileSource`; retrieval response schema carries document/page/section provenance. | Replace `LocalFileSource` with Azure AI Search backend (hybrid semantic + BM25); same `DataSource` call site, same citation schema. |
| Grounding + confidence (UMR-007/008/010) | Grounding node sits between retrieve and respond; emits confidence into `AGENT_ACTION`; escalates below 0.6. | Foundry evaluation + RAGAS-style scoring plug into the same node; threshold remains code-side. |
| HITL approvals (UMR-021–026, HITL-001–007) | **`AgentPaused` exception from the ReAct loop → SQLite `approvals` table → `/admin/approvals/<trace_id>/<decision>` resume route**, same auth as routes; decisions logged immutably with reasoning chain, confidence, sources. | Postgres approval queue, Dash reviewer UI, Content Safety + Foundry rate limits layer in front; `⟨I⟩ ApprovalQueue` + `⟨I⟩ ChatProvider` unchanged. |
| RBAC + data scope (UMR-012/017/058, AAR-002/007) | Route-gated **`permissions.json`** (role levels, public prefixes, internal prefixes, route rules all declarative); `SqliteDataStore` scoped by `QueryTool.set_user`; per-tool RBAC column staged. | Entra ID issues tokens; same role check in `before_request`; classification tags enforced at the data store. |
| Immutable audit (UMR-015/027/045, ASG-003) | **`HashChainedJsonlLog` writes append-only JSONL with SHA-256 hash chain**; daily rotation; covers every tool call and LLM turn; `python -m app.core.audit verify` validates the chain. | Forward the same envelope to Log Analytics (immutability policy); KQL replaces grep. |
| Guardrails + sandbox (UMR-020/029/030/093, ASG-001/004/011) | Guardrail hook point in tool wrapper (`GUARDRAIL_HOOK=""` today); code-exec slot reserved as `CodeExecTool` stub; rate limit at APIM-like proxy. | Content Safety on the hook; Azure Container Apps for code-exec; Foundry rate controls. |
| External data (UMR-051–054) | `LocalFileSource` reads mirrors / CSV fixtures of the CSA corpus and SAP line items; UC-E2 / F1 / F4 lanes run end-to-end. | SharePoint, SAP, STK, MATLAB each land as a `DataSource` class with MSAL / OAuth. |
| Multi-agent + memory (UMR-011/014/018/095, AAR-001/004) | Primary agent (hand-rolled ReAct) + tool registry + session workspace; `agent_id` in `AGENT_ACTION` already carries sub-task identity. | Add orchestrator + specialist nodes (LangGraph swap-in behind `⟨I⟩ ChatProvider`); Postgres holds the three memory tiers; per-session agent factory. |
| Bilingual reports (UMR-001/046/048) | Agent accepts EN/FR free text; report generator attaches citations and runs through HITL. | Azure Translator + Foundry NLG for narrative sections; same template + evidence pipeline. |
| Interoperability (UMR-055) | REST surface is the contract today; schema documented; external agents can trigger CRAFT with a token. | Same routes behind APIM + App Gateway (WAF, rate limit); GraphQL layer optional on top. |
| SLA + scale (UMR-056/057/059) | Single-instance App Service with health checks; load-test harness in place. | HA App Service + Azure Front Door; autoscale; SSC LaunchPad for the landing zone. |

## 6. Requirements Traceability

| Capability | Requirements | Design |
|---|---|---|
| Primary agent | UMR-001/011/013/016/018/019/094/095, AAR-001/003/006, ASG-005 | **Azure OpenAI SDK direct · hand-rolled ReAct loop · `⟨I⟩ ChatProvider` · `AGENT_RECURSION_LIMIT=25`** (framework swap-in reserved — Microsoft Agent Framework preferred Azure-native, LangGraph as third-party alternative) |
| Retrieval + RAG | UMR-002/003/004/005/006/009/010/060/067, ARR-002–007 | Hybrid search tool · `⟨I⟩ DataSource` registry (declarative JSON) · citation + grounding schema |
| Audit + traceability | UMR-015/027/045/061/062/093, AAR-005, ASG-003 | `AgentAction` envelope · `⟨I⟩ AgentActionLog` · **hash-chained JSONL** → Log Analytics |
| HITL approvals | UMR-021–026/035/039/044/049, HITL-001–007, ASG-002 | **`AgentPaused` + `⟨I⟩ ApprovalQueue` (SQLite today)** · Dash reviewer UI reserved · Postgres end state |
| RBAC + data scope | UMR-012/017/058/065/066, AAR-002/007 | **`permissions.json`** (role levels + rules + prefixes) · `SqliteDataStore` · `QueryTool.set_user` |
| Session + workspace | UMR-014/092/095 | `⟨I⟩ WorkspaceStore` → `SqliteStore` + `SessionScratchStore` (end state); per-session agent factory |
| Guardrails + containment | UMR-020/029/030, ASG-001/004/011 | **`GUARDRAIL_HOOK` hook point** · APIM rate limit · Container Apps sandbox |
| Connectors + external | UMR-051–055 | `⟨I⟩ DataSource` kind registry (JSON-driven) + MSAL · Flask REST · SAP / STK / MATLAB classes |
| Domain capabilities | UMR-007/008/031–050/075, ARR-001 | New `⟨I⟩ Tool` classes over existing registries (reserved stubs today) |
| Deployment + SLA | UMR-028/056/057/059/064/069/070/074/085, ASG-006 | Azure App Service PBMM · APIM + WAF · SSC LaunchPad HA · env-var config via `environs`-free stdlib settings loader |

## 7. Blockages (End State / Current Alternative)

Each row is an Azure-consolidated end-state component wired through the registry the current alternative already runs against.

| End-state component | Current alternative |
|---|---|
| Azure AI Search (hybrid retrieval) | `LocalFileSource` + file-name/path search |
| Azure Log Analytics + immutability | Hash-chained append-only JSONL on disk + `audit verify` CLI |
| Azure Content Safety | Guardrail hook off (`GUARDRAIL_HOOK=""`) |
| Azure Container Apps sandbox | `CodeExecTool` registration slot reserved |
| Entra ID (app registration + MSAL) | Local `AuthProvider` stub, mocked tokens, SQLite-backed user table |
| SharePoint `DataSource` | `LocalFileSource` reads a corpus mirror |
| SAP `DataSource` | CSV fixtures via `LocalFileSource` (UC-F4 runs) |
| STK / MATLAB adapters | `⟨I⟩ Tool` slot reserved |
| Azure AI Foundry (model routing / rate limits) | Azure OpenAI direct (Canadian region) |
| SSC LaunchPad HA | Single-region App Service |
| CSA risk taxonomy | Stub taxonomy drives the classifier for tests |
| Historical mission DB | CSV fixtures through `LocalFileSource` (UC-F1 runs) |
| Microsoft Agent Framework / LangGraph (multi-agent orchestration) | Hand-rolled bounded ReAct loop on Azure OpenAI SDK; swap behind `⟨I⟩ ChatProvider` if triggers land |
| Postgres (HITL queue + 3-tier memory) | SQLite `approvals` table + resume routes |

## 8. System-Health Tooling

Runs on every commit and in CI; these are invariants, not blockages.

| Tool | Role |
|---|---|
| ruff | Lint (flake8 + isort + pyupgrade) |
| pyright (strict) | Type checking · protocol conformance |
| pytest + coverage | Route × role matrix · protocol contracts · audit-envelope invariants |
| **doctest** | Every public pure function carries an executable example; `pytest --doctest-modules` runs them |
| **architecture tests** | AST-walkers in `app/tests/test_architecture.py` fail CI if a public function lacks a doctest or a stateful module lacks a `tests/test_*.py`; forbidden-import guard rejects `pydantic`, `pydantic_ai`, `langchain`, `langgraph`, `semantic-kernel`, `agent-framework` from the installed set until a swap-in trigger fires |
| bandit | Security scan |
| pip-audit | Dependency CVE audit |
| detect-secrets | No credentials in git |

**Dependency surface (today):** `dash`, `flask`, `flask-login`, `openai`, `pandas`, `plotly`, `python-dotenv`, `requests`, `werkzeug`, `msal`, `pdfplumber`, `python-docx`. Twelve runtime packages. Each pitch end-state row adds **one targeted dep** behind an existing protocol — not a tree.
