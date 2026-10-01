---
title: "CRAFT — Pitch Package"
margin:
  x: 1.2cm
  y: 0.8cm
fontsize: 8pt
lin: 1.10
---

## Legend
■ Actor · ◇ Gate · ☁ Cloud · ⬡ Terminal · ▦ Store · ···· Planned · ⟨I⟩ Protocol · Blue=Auth · Green=Audit

## 1. What CRAFT Is

Audited retrieval-augmented AI assistant for CSA mission engineering and finance. Scratchpad MVPs the seams. Nothing ships — pattern is the point.

## 2a. L1 System Context

```text
┌─────────────────┐
│Mission Eng      │──▶┌──────────────────────────────────────────┐
│Systems Eng      │──▶│                CRAFT                     │
│Program Admin    │──▶│           Flask + Dash                   │
│HITL Reviewer    │──▶│                                          │
└─────────────────┘   └──┬────────┬─────────┬──────────┬────────┘
                         ▼        ▼         ▼          ▼
                    ┌────────┐┌────────┐┌─────────┐┌────────────┐
                    │LLM & AI││Internal││External ││Ops & Audit │
                    │AzureOA ││ Data   ││ Data(d) ││LogAnalyt(d)│
                    │AgentFW ││LocalFs ││ShPt     ││AppSvc PBMM │
                    │Foundry ││SQLite  ││SAP      ││LaunchP(d)  │
                    │(d)     ││⟨I⟩DS  ││STK      ││ContApp(d)  │
                    │ContSfty││⟨I⟩WS  ││AI Srch  ││            │
                    │(d)     ││        ││⟨I⟩DS   ││Entra(d)    │
                    │        ││        ││         ││APIM(d)     │
                    └────────┘└────────┘└─────────┘└────────────┘
```
In: `/chat/send [base]` `/admin/* [admin]`. Out: thin italic. (d)=planned/dashed. **Internal data** lives in the CRAFT process + SQLite; **external data** reaches CRAFT through `⟨I⟩ DataSource` adapters (MSAL/OAuth).

## 2b. L2 Container

```text
┌────────────────────────────────────────────────────────────┐
│         Route-Gated RBAC Layer (auth-blue)                 │
│  /chat/send [base] · /uploads [power] · /admin/* [admin]  │
└───────────────────────┬────────────────────────────────────┘
        ┌───────────────┼──────────────────┐
        ▼               ▼                  ▼
┌──────────────┐┌──────────────┐┌─────────────────────────┐
│Primary Agent ││Tool Registry ││Storage ⟨I⟩WsStore       │
│Microsoft     ││⟨I⟩ Tool      ││▦WStore ▦Data(RBAC)      │
│Agent         ││              ││▦AuditLog JSONL(hash)    │
│Framework     ││              ││                          │
│⟨I⟩ChatProv   ││              ││                          │
│  AGNT_ACT ───┼┼── AGNT_ACT ──┼┼──▶                       │
└──────┬───────┘└──────┬───────┘└─────────────────────────┘
       │               │
       ▼               ▼
┌──────────────┐┌──────────────────────────────────┐
│Audit Sink    ││Connectors (perimeter):            │
│⟨I⟩ActLog     ││INTERNAL: LocalFile                │
│  │           ││EXTERNAL: ShPt(d) · SAP(d) ·       │
│  ▼           ││          STK/MATLAB(d) · AISrch(d)│
│AzureLA(d)    │└──────────────────────────────────┘
└──────────────┘

┌──────────────┐
│Test Surface  │──▶ pre-commit · GitHub Actions
│(audit-green) │
└──────────────┘
```
AGENT_ACTION (green). Connectors ◆. Test surface dotted. Audit JSONL is hash-chained today → Azure Log Analytics at end state.

## 2c. L3 Internals

```text
Panel A · Agent:   ChatAgent (Agent Framework)         Panel B · Tools/Connectors:
                   │                                   ··Tool Protocol··
                   ▼                                   documents · charts · query_data
             LLM turn ◀──┐                             classifier(r) · hist_mission(r)
                   │     │                             cost_agg(r) · vendor_agg(r) · code_exec(r)
                   ▼     │                             ··DataSource Protocol··
         user_input_req? │                             INTERNAL: LocalFile · SqliteDataStore
                 │ no    │                             EXTERNAL(d): ShPt · SAP · STK · AISrch
          respond        │
                 │ yes (@tool approval_mode)
                 ▼       │
         ApprovalQueue   │                             POST /tools/exec/<name>
         (SQLite)        │                             ◇HITL via framework approval
                 │       │                             ◆Filesystem Cloud SAP
         ◇ approve/deny  │
                 │       │
            resume ──────┘  (iteration cap)
            →llm_inf → Audit (hash-chained JSONL, green)
            →tool_cl → Audit (hash-chained JSONL, green)
            ⟨I⟩ChatProvider
            ⟨I⟩AgentActionLog

Panel C · Auth:  Public inbound [/route][role]
                 → FlaskRoute → ◇ before_request (hex, blue)
                 auth · role · ws · traceID
                 → handler → after_request (audit, green)
                 → response
              permissions.json: /send→base /upload→power /admin→admin
              RBAC: base(1) < power(2) < admin(3)
              ⟨test⟩ arch invariants (audit-green)
```
(r) = reserved stub satisfying `⟨I⟩ Tool`; agent sees the schema, raises `NotImplementedError` on call.

## 2d. UC State Models

```text
UC-E2 Risk ID+HITL (Eng):  Req→◇Auth→Retrieval[002-006]→Classifier[036-040]→◇HITL[HITL-001]
                            Approve→RiskReg(d)→Audit→●  Reject→●
UC-F1 Cost+HITL (Fin):     Req→◇Auth→Retrieval(hist)[031]→CostAgg[032-034]→◇HITL[035]
                            Approve→Commit(d)→Audit→●  Reject→●
UC-F4 SAP Conn (blocked):  Req→◇Auth→SAPConn(d)[053-055]→VendorExt→Agg→Audit→●(blocker:SAP)
```
●=Terminal. ◇=Gate. (d)=planned. Swim lanes: User→Agent→Services→Terminal.

## 3. Use Cases

**UC-E2 · Risk ID + HITL (Engineering).** Engineer uploads a CADRe part; retrieval pulls risk sections from the corpus; a classifier tool scores severity; HITL approves (framework `@tool(approval_mode="always_require")` → SQLite `ApprovalQueue` → resume route); a `DataSource` write lands the entry in the risk register. Tools: `DocumentSearchTool`, `ClassifierTool`. Requirements: UMR-002/006, UMR-036–040, HITL-001.

**UC-F1 · Parametric Cost + HITL (Finance).** Admin asks for a mission cost estimate; retrieval returns similar historical missions; an aggregator tool computes weighted distance; HITL approves; the commitment is written. Tools: `HistoricalMissionTool`, `CostAggregatorTool`. Requirements: UMR-031–035.

**UC-F4 · Vendor Cost Roll-up (Finance).** Analyst asks "how much did we spend with vendor X across missions?"; a `DataSource` (SAP connector at end state, CSV fixtures today) returns line items; a `VendorAggregatorTool` sums by vendor; a report is returned. Requirements: UMR-053–055.

**UC · Bilingual Chat / RAG (All).** User asks in English or French; retrieval + `DocumentSearchTool` return cited passages; the agent responds with citations and a confidence score. Requirements: UMR-001/002/003/007/010.

New mission flows (budget scenarios, anomaly triage, cross-mission compare) land as new `⟨I⟩ Tool` + optional `⟨I⟩ DataSource` behind the same lane.

## 4. Design Decisions

| Component | End-state choice | Current alternative | Why |
|---|---|---|---|
| HTTP surface | **Flask + Dash** reviewer UI | — (live) | Routes are the integration contract — any token-bearing caller (user, cron, agent) can hit CRAFT; Dash shares the auth and audit perimeter. |
| Agent runtime | **Microsoft Agent Framework** (`agent-framework`, GA April 2026 — Microsoft's enterprise successor to Semantic Kernel) · `ChatAgent` + `AzureOpenAIChatClient` · `@tool` with `approval_mode` · bounded iteration cap | — (live) | Microsoft-blessed, Azure-native, long-term support. First-class HITL (function-level approval + workflow-level `RequestPort`), bounded iteration, OpenTelemetry built in. `⟨I⟩ ChatProvider` keeps the swap seam honest. |
| LLM inference | **Azure AI Foundry** (model routing + rate limits + Content Safety) | **Azure OpenAI direct** (Canadian PBMM region) via `AzureOpenAIChatClient` | Foundry collapses model, rate-limit and guardrail procurement into one line while PBMM residency stays. SDK stays `agent_framework.openai.AzureOpenAIChatClient`; the endpoint URL changes. |
| Retrieval | **Azure AI Search** hybrid (vector + BM25) via `azure-search-documents` | **`LocalFileSource`** via `⟨I⟩ DataSource` with filename / path search | Same `⟨I⟩ DataSource` call site; cutover is config. Satisfies UMR-004/005/006. |
| Guardrails + sandbox | **Azure Content Safety** on the deployment + **Azure Container Apps** sandbox | Guardrail hook disabled (`GUARDRAIL_HOOK=""`); `CodeExecTool` slot reserved | End-state wires into the tool wrapper CRAFT already runs. UMR-020 / UMR-093. |
| Identity | **Entra ID + MSAL** | Local `AuthProvider` stub; SQLite users seeded by `scripts/seed.py` | Same token flow for humans and external agents; CSA-standard. |
| Audit sink | **Azure Log Analytics** (immutable retention) | **Hash-chained JSONL** on disk via `HashChainedJsonlLog`; `python -m app.core.audit verify` | KQL at end state; grep today; UMR-027 / ASG-003. Same envelope, same chain property — forwarder at deploy time. |
| HITL queue + memory | **Postgres** (approval queue + 3-tier memory) via `psycopg[binary]` | **SQLite `ApprovalQueue`** + `/admin/approvals/*` resume routes; reviewer UI reserved | Durable across restarts; UMR-025 TTL, UMR-014 memory. Swap behind `⟨I⟩ ApprovalQueue`. |
| Session + per-user data | **Managed DB** behind `⟨I⟩ WorkspaceStore` | SQLite file-local (`SqliteStore` + `SqliteDataStore`) | Swap target already named behind the protocol. |
| Edge | **APIM + App Gateway** (WAF) | Direct App Service | WAF + rate limit at perimeter; UMR-030. |
| Deployment | **App Service PBMM** + **SSC LaunchPad** HA | Single-region App Service | HA + landing zone come with LaunchPad; UMR-057. |
| Protocol contracts | `⟨I⟩ Tool`, `⟨I⟩ DataSource`, `⟨I⟩ ChatProvider`, `⟨I⟩ WorkspaceStore`, `⟨I⟩ AgentActionLog`, `⟨I⟩ ApprovalQueue` | — (live) | New capability or backend = one class satisfying a protocol; agent unchanged. Pyright-strict verified. |
| Invariants | pytest + pyright (strict) + ruff + bandit + pip-audit + detect-secrets + doctest coverage + stateful-module coverage | — (live) | Route × role matrix, protocol contracts, audit-envelope present, every public function has an executable example, every stateful module has a test file. Industry-standard, maintained. |

## 5. Solving the Problems — Today and at End State

| Problem (requirement) | How the architecture solves it today | How it solves it at end state (Azure-consolidated) |
|---|---|---|
| Cited retrieval (UMR-002/005/006, ARR-002/003) | `DocumentSearchTool` + `TextAnalysisTool` over `LocalFileSource`; retrieval response schema carries document / page / section provenance. | Replace `LocalFileSource` with `AzureAISearchSource` (hybrid semantic + BM25); same `⟨I⟩ DataSource` call site, same citation schema. |
| Grounding + confidence (UMR-007/008/010) | Grounding node sits between retrieve and respond; emits confidence into `AGENT_ACTION`; escalates below 0.6. | Foundry evaluation + RAGAS-style scoring plug into the same node; threshold remains code-side. |
| HITL approvals (UMR-021–026, HITL-001–007) | Agent Framework `@tool(approval_mode="always_require")` → `user_input_requests` → SQLite `ApprovalQueue` → `/admin/approvals/<trace_id>/<decision>` resume route, same auth as routes; decisions logged immutably with reasoning chain, confidence, sources. | Postgres approval queue, Dash reviewer UI, Content Safety + Foundry rate limits layer in front; `⟨I⟩ ApprovalQueue` + `⟨I⟩ ChatProvider` unchanged. |
| RBAC + data scope (UMR-012/017/058, AAR-002/007) | Route-gated declarative `permissions.json` (role levels + public prefixes + internal prefixes + route rules); `SqliteDataStore` scoped by `QueryTool.set_user`; per-tool RBAC column staged. | Entra ID issues tokens; same role check in `before_request`; classification tags enforced at the data store. |
| Immutable audit (UMR-015/027/045, ASG-003) | `HashChainedJsonlLog` writes append-only JSONL with SHA-256 hash chain; daily rotation; covers every tool call and LLM turn; `python -m app.core.audit verify` validates the chain. | Forward the same envelope to Log Analytics (immutability policy); KQL replaces grep. |
| Guardrails + sandbox (UMR-020/029/030/093, ASG-001/004/011) | `GUARDRAIL_HOOK` hook point in tool wrapper (`""` today, no-op); `CodeExecTool` reserved stub; rate limit at APIM-like proxy. | Content Safety on the hook (`content_filter_results` read directly from the SDK response); Azure Container Apps for code-exec; Foundry rate controls. |
| External data (UMR-051–054) | `LocalFileSource` reads mirrors / CSV fixtures of the CSA corpus and SAP line items; UC-E2 / F1 / F4 lanes run end-to-end. | SharePoint, SAP, STK, MATLAB each land as a `⟨I⟩ DataSource` class with MSAL / OAuth; one JSON row in `data_sources.json`. |
| Multi-agent + memory (UMR-011/014/018/095, AAR-001/004) | Primary agent (Agent Framework `ChatAgent`) + tool registry + session workspace; `agent_id` in `AGENT_ACTION` already carries sub-task identity. | Add orchestrator + specialist agents via the framework's multi-agent primitives + workflow-level `RequestPort`; Postgres holds the three memory tiers; per-session agent factory. |
| Bilingual reports (UMR-001/046/048) | Agent accepts EN/FR free text; report generator attaches citations and runs through HITL. | Azure Translator + Foundry NLG for narrative sections; same template + evidence pipeline. |
| Interoperability (UMR-055) | REST surface is the contract today; schema documented; external agents can trigger CRAFT with a token. | Same routes behind APIM + App Gateway (WAF, rate limit); GraphQL layer optional on top. |
| SLA + scale (UMR-056/057/059) | Single-instance App Service with health checks; load-test harness in place. | HA App Service + Azure Front Door; autoscale; SSC LaunchPad for the landing zone. |

## 6. Requirements Traceability

| Capability | Requirements | Design |
|---|---|---|
| Primary agent | UMR-001/011/013/016/018/019/094/095, AAR-001/003/006, ASG-005 | **Microsoft Agent Framework · `ChatAgent` + `AzureOpenAIChatClient` · `⟨I⟩ ChatProvider` · bounded iteration cap** |
| Retrieval + RAG | UMR-002/003/004/005/006/009/010/060/067, ARR-002–007 | Hybrid search tool · `⟨I⟩ DataSource` registry (declarative JSON) · citation + grounding schema |
| Audit + traceability | UMR-015/027/045/061/062/093, AAR-005, ASG-003 | `AgentAction` envelope · `⟨I⟩ AgentActionLog` · hash-chained JSONL → Azure Log Analytics |
| HITL approvals | UMR-021–026/035/039/044/049, HITL-001–007, ASG-002 | Agent Framework `@tool(approval_mode)` · `⟨I⟩ ApprovalQueue` (SQLite today) · Dash reviewer UI reserved · Postgres end state |
| RBAC + data scope | UMR-012/017/058/065/066, AAR-002/007 | Declarative `permissions.json` (role levels + rules + prefixes) · `SqliteDataStore` · `QueryTool.set_user` |
| Session + workspace | UMR-014/092/095 | `⟨I⟩ WorkspaceStore` → `SqliteStore` + `SessionScratchStore` (end state); per-session agent factory |
| Guardrails + containment | UMR-020/029/030, ASG-001/004/011 | `GUARDRAIL_HOOK` hook point · APIM rate limit · Azure Container Apps sandbox |
| Connectors + external | UMR-051–055 | `⟨I⟩ DataSource` kind registry (JSON-driven) + MSAL · Flask REST · SAP / STK / MATLAB classes |
| Domain capabilities | UMR-007/008/031–050/075, ARR-001 | New `⟨I⟩ Tool` classes over existing registries (reserved stubs today) |
| Deployment + SLA | UMR-028/056/057/059/064/069/070/074/085, ASG-006 | Azure App Service PBMM · APIM + WAF · SSC LaunchPad HA · stdlib + `python-dotenv` config loader |

## 7. Blockages (End State / Current Alternative)

| End-state component | Current alternative |
|---|---|
| Azure AI Search (hybrid retrieval) | `LocalFileSource` + file-name / path search |
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
| Microsoft Agent Framework (if access restricted) | Hand-rolled ReAct loop on `openai.AsyncAzureOpenAI` behind same `⟨I⟩ ChatProvider` |
| Postgres (HITL queue + 3-tier memory) | SQLite `approvals` table + resume routes |

## 8. System-Health Tooling

| Tool | Role |
|---|---|
| ruff | Lint (flake8 + isort + pyupgrade) · pre-commit + CI |
| pyright (strict) | Type checking · protocol conformance · pre-commit + CI |
| pytest + coverage | Route × role matrix · protocol contracts · audit-envelope invariants · pre-commit + CI |
| doctest | Every public pure function carries an executable example · `pytest --doctest-modules` |
| architecture tests | AST-walkers in `app/tests/test_architecture.py`: doctest coverage, stateful-module test coverage, forbidden-import guard (no direct `pydantic` / `pydantic_ai` / `langchain` / `langgraph` in our source) |
| bandit | Security scan · pre-commit |
| pip-audit | Dependency CVE audit · pre-commit + CI |
| detect-secrets | No credentials in git · pre-commit |

**Dependency surface:** `agent-framework` (umbrella; or narrower `agent-framework-core` + `agent-framework-openai` + `agent-framework-foundry`), `openai` (via framework), `dash`, `flask`, `flask-login`, `pandas`, `plotly`, `python-dotenv`, `requests`, `werkzeug`, `msal`, `pdfplumber`, `python-docx`. Agent Framework pulls `pydantic` and related Microsoft/Azure packages transitively. Each end-state row above adds **one targeted dep** behind an existing protocol — not a tree.
