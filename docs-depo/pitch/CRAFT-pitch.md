---
title: "CRAFT — Architecture Proposal"
margin:
  x: 1.2cm
  y: 0.8cm
fontsize: 8pt
lin: 1.10
---

## Legend
■ Actor · ◇ Gate · ☁ Cloud · ⬡ Terminal · ▦ Store · ⟨I⟩ Protocol · Blue=Auth · Green=Audit

## 1. What CRAFT Is

Proposed audited retrieval-augmented AI assistant for CSA mission engineering and finance. This document describes the target architecture — the seams, the components behind each seam, and the invariants that hold across the system.

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
                    │AzureOA ││ Data   ││  Data   ││LogAnalyt   │
                    │AgentFW ││⟨I⟩WS   ││ShPt     ││AppSvc PBMM │
                    │Foundry ││SQLite  ││SAP      ││LaunchP     │
                    │ContSfty││scratch ││STK      ││ContApp     │
                    │        ││        ││AI Srch  ││Entra       │
                    │        ││⟨I⟩DS   ││⟨I⟩DS    ││APIM        │
                    │        ││        ││         ││            │
                    └────────┘└────────┘└─────────┘└────────────┘
```
In: `/chat/send [base]` `/admin/* [admin]`. Out: thin italic. **Internal data** lives in the CRAFT process + SQLite; **external data** reaches CRAFT through `⟨I⟩ DataSource` adapters (MSAL/OAuth).

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
│⟨I⟩ActLog     ││INTERNAL: LocalFile · SQLite       │
│  │           ││EXTERNAL: ShPt · SAP · STK/MATLAB  │
│  ▼           ││          AzureAISearch            │
│AzureLA       │└──────────────────────────────────┘
└──────────────┘

┌──────────────┐
│Test Surface  │──▶ pre-commit · GitHub Actions
│(audit-green) │
└──────────────┘
```
AGENT_ACTION (green). Connectors ◆. Test surface dotted. Audit JSONL is hash-chained and forwarded to Azure Log Analytics.

## 2c. L3 Internals

### Panel A · Agent

```text
ChatAgent (Agent Framework)
      │
      ▼
  LLM turn ◀──────────────┐
      │                   │
  user_input_req?         │
    │ no                  │
   respond                │
    │ yes (@tool approval_mode)
    ▼                     │
 ApprovalQueue            │
 (Postgres)               │
    │                     │
 ◇ approve/deny           │
    │                     │
  resume ─────────────────┘  (iteration cap)

 →llm_inf → Audit (hash-chained JSONL, green)
 →tool_cl → Audit (hash-chained JSONL, green)
 ⟨I⟩ ChatProvider · ⟨I⟩ AgentActionLog
```

### Panel B · Tools, Storage & Route-Gated Access

Every tool and storage/data-source operation sits behind the same `⟨I⟩` protocol **and** the same HTTP route. The agent calls routes probabilistically; an external caller with a scoped token calls the same routes deterministically. One RBAC gate, one audit envelope, both paths.

```text
┌──── Tool Registry  ⟨I⟩ Tool ─────────────────┐    ┌──── Data Sources  ⟨I⟩ DataSource ────┐
│  documents · charts · query_data             │    │  INTERNAL (connector-backed):        │
│  classifier · hist_mission · cost_agg        │    │    LocalFileSource · SqliteDataStore │
│  vendor_agg · code_exec                      │    │  EXTERNAL (perimeter, MSAL/OAuth):   │
│                                              │    │    SharePoint · SAP · STK/MATLAB     │
│                                              │    │    AzureAISearchSource               │
└──────────────────────────────────────────────┘    └──────────────────────────────────────┘

┌──── Workspace & Audit  ⟨I⟩ WorkspaceStore / ⟨I⟩ AgentActionLog / ⟨I⟩ ApprovalQueue ────┐
│  SqliteStore (workspaces + scratch)   HashChainedJsonlLog (audit → Azure Log Analytics) │
│  SqliteDataStore (per-user scoped)    ApprovalQueue (Postgres, HITL)                    │
└─────────────────────────────────────────────────────────────────────────────────────────┘

                  ▲ internal call                      ▲ internal call
                  │                                    │
┌─────────────────┴────────────────────────────────────┴───────────────────────────────┐
│                        Route-Gated RBAC Layer                                        │
│   POST /tools/execute/<name>    /storage/*    /chat/send    /admin/approvals/*       │
│   before_request: auth · role · trace_id   →   handler   →   after_request: audit    │
│   permissions.json  ·  base(1) < power(2) < admin(3)   ·   role < required → 403     │
└────────────────────┬───────────────────────────────────────────────┬─────────────────┘
                     │                                               │
         ┌───────────┴────────────┐                     ┌────────────┴────────────┐
         │ Caller: Primary Agent  │                     │ Caller: External client │
         │  (Agent Framework)     │                     │  (user-scoped token)    │
         │  probabilistic use     │                     │  deterministic use      │
         └────────────────────────┘                     └─────────────────────────┘
```

Why this matters: granting a token with the right role lets an external service drive CRAFT's tools and storage without going through the agent — a cron job can read documents, a reporting pipeline can hit `query_data`, an upstream workflow can post an approval decision. Audit and RBAC behave identically whichever caller it is.

### Panel C · Auth

```text
Public inbound [/route][role]
  → FlaskRoute → ◇ before_request (hex, blue)
     auth · role · workspace · trace_id
  → handler
  → after_request (audit, green)
  → response

permissions.json : /chat/send → base   /uploads → power   /admin/* → admin
RBAC             : base(1) < power(2) < admin(3)
⟨test⟩ arch invariants (audit-green)
```

## 2d. UC State Models

```text
UC-E2 Risk ID+HITL (Eng):  Req→◇Auth→Retrieval[002-006]→Classifier[036-040]→◇HITL[HITL-001]
                            Approve→RiskReg→Audit→●  Reject→●
UC-F1 Cost+HITL (Fin):     Req→◇Auth→Retrieval(hist)[031]→CostAgg[032-034]→◇HITL[035]
                            Approve→Commit→Audit→●  Reject→●
UC-F4 SAP Conn:            Req→◇Auth→SAPConn[053-055]→VendorExt→Agg→Audit→●
```
●=Terminal. ◇=Gate. Swim lanes: User→Agent→Services→Terminal.

## 3. Use Cases

**UC-E2 · Risk ID + HITL (Engineering).** Engineer uploads a CADRe part; retrieval pulls risk sections from the corpus; a classifier tool scores severity; HITL approves (framework `@tool(approval_mode="always_require")` → `ApprovalQueue` → resume route); a `DataSource` write lands the entry in the risk register. Tools: `DocumentSearchTool`, `ClassifierTool`. Requirements: UMR-002/006, UMR-036–040, HITL-001.

**UC-F1 · Parametric Cost + HITL (Finance).** Admin asks for a mission cost estimate; retrieval returns similar historical missions; an aggregator tool computes weighted distance; HITL approves; the commitment is written. Tools: `HistoricalMissionTool`, `CostAggregatorTool`. Requirements: UMR-031–035.

**UC-F4 · Vendor Cost Roll-up (Finance).** Analyst asks "how much did we spend with vendor X across missions?"; a SAP `DataSource` returns line items; a `VendorAggregatorTool` sums by vendor; a report is returned. Requirements: UMR-053–055.

**UC · Bilingual Chat / RAG (All).** User asks in English or French; retrieval + `DocumentSearchTool` return cited passages; the agent responds with citations and a confidence score. Requirements: UMR-001/002/003/007/010.

New mission flows (budget scenarios, anomaly triage, cross-mission compare) land as new `⟨I⟩ Tool` + optional `⟨I⟩ DataSource` behind the same lane.

## 4. Design Decisions

| Component | Choice | Why |
|---|---|---|
| HTTP surface | **Flask + Dash** reviewer UI | Routes are the integration contract — any token-bearing caller (user, cron, agent) can hit CRAFT; Dash shares the auth and audit perimeter. |
| Agent runtime | **Microsoft Agent Framework** (`agent-framework`, Microsoft's enterprise successor to Semantic Kernel) · `ChatAgent` + `AzureOpenAIChatClient` · `@tool` with `approval_mode` · bounded iteration cap | Microsoft-blessed, Azure-native, long-term support. First-class HITL (function-level approval + workflow-level `RequestPort`), bounded iteration, OpenTelemetry built in. `⟨I⟩ ChatProvider` keeps the swap seam honest. |
| LLM inference | **Azure AI Foundry** (model routing + rate limits + Content Safety) over Canadian PBMM region | Foundry collapses model, rate-limit and guardrail procurement into one line while PBMM residency stays. SDK is `agent_framework.openai.AzureOpenAIChatClient`. |
| Retrieval | **Azure AI Search** hybrid (vector + BM25) via `azure-search-documents`, exposed as `⟨I⟩ DataSource` | Same `⟨I⟩ DataSource` call site across all retrieval; cutover between backends is config, not code. Satisfies UMR-004/005/006. |
| Guardrails + sandbox | **Azure Content Safety** on the deployment + **Azure Container Apps** sandbox via `CodeExecTool` | Content filtering reads inline from the chat response; code-exec runs in an isolated container. UMR-020 / UMR-093. `GUARDRAIL_HOOK` sits in the tool wrapper so wiring is a config change. |
| Identity | **Entra ID + MSAL** behind `⟨I⟩ AuthProvider` | Same token flow for humans and external agents; CSA-standard. |
| Audit sink | **`HashChainedJsonlLog` → Azure Log Analytics** (immutable retention) | Append-only JSONL with SHA-256 chain for tamper detection; KQL at query time; same envelope end-to-end. UMR-027 / ASG-003. |
| HITL queue + memory | **Postgres** (approval queue + 3-tier memory) behind `⟨I⟩ ApprovalQueue` via `psycopg[binary]` | Durable across restarts; UMR-025 TTL, UMR-014 memory. Dash reviewer UI consumes the queue. |
| Session + per-user data | **Managed DB** behind `⟨I⟩ WorkspaceStore` (`SqliteStore` + `SessionScratchStore` shapes) | Swap target already named behind the protocol; per-user scope via `QueryTool.set_user`. |
| Edge | **APIM + App Gateway** (WAF, rate limit) | WAF + rate limit at perimeter; UMR-030. |
| Deployment | **App Service PBMM** + **SSC LaunchPad** HA | HA + landing zone come with LaunchPad; UMR-057. |
| Protocol contracts | `⟨I⟩ Tool`, `⟨I⟩ DataSource`, `⟨I⟩ ChatProvider`, `⟨I⟩ WorkspaceStore`, `⟨I⟩ AgentActionLog`, `⟨I⟩ ApprovalQueue`, `⟨I⟩ AuthProvider` | New capability or backend = one class satisfying a protocol; agent unchanged. Pyright-strict verified. |
| Invariants | pytest + pyright (strict) + ruff + bandit + pip-audit + detect-secrets + doctest coverage + stateful-module coverage | Route × role matrix, protocol contracts, audit-envelope present, every public function has an executable example, every stateful module has a test file. Industry-standard, maintained. |

## 5. Solving the Problems

| Problem (requirement) | How the architecture solves it |
|---|---|
| Cited retrieval (UMR-002/005/006, ARR-002/003) | `DocumentSearchTool` + `TextAnalysisTool` call `AzureAISearchSource` through `⟨I⟩ DataSource`; retrieval response schema carries document / page / section provenance; agent surfaces citations to the user. |
| Grounding + confidence (UMR-007/008/010) | Grounding node sits between retrieve and respond; Foundry evaluation + RAGAS-style scoring emit confidence into `AGENT_ACTION`; threshold check escalates below 0.6. |
| HITL approvals (UMR-021–026, HITL-001–007) | Agent Framework `@tool(approval_mode="always_require")` on risky tools → `user_input_requests` → `ApprovalQueue` (Postgres) → `/admin/approvals/<trace_id>/<decision>` resume route, same auth as routes; decisions logged immutably with reasoning chain, confidence, sources; Dash reviewer UI. |
| RBAC + data scope (UMR-012/017/058, AAR-002/007) | Route-gated declarative `permissions.json` (role levels + public prefixes + internal prefixes + route rules); Entra ID issues tokens; `SqliteDataStore` scoped by `QueryTool.set_user`; classification tags enforced at the data store. |
| Immutable audit (UMR-015/027/045, ASG-003) | `HashChainedJsonlLog` writes append-only JSONL with SHA-256 hash chain, daily rotation, covering every tool call and LLM turn; forwarded to Azure Log Analytics for KQL and immutable retention. |
| Guardrails + sandbox (UMR-020/029/030/093, ASG-001/004/011) | Azure Content Safety on the deployment (`content_filter_results` read inline); `GUARDRAIL_HOOK` in the tool wrapper applies thresholds; `CodeExecTool` runs in Azure Container Apps; APIM rate limit at perimeter. |
| External data (UMR-051–054) | SharePoint, SAP, STK, MATLAB each a `⟨I⟩ DataSource` class with MSAL / OAuth; one JSON row in `data_sources.json`; `AzureAISearchSource` sits behind the same contract for retrieval. |
| Multi-agent + memory (UMR-011/014/018/095, AAR-001/004) | Primary `ChatAgent` + tool registry + session workspace; `agent_id` in `AGENT_ACTION` carries sub-task identity; orchestrator + specialist agents via framework multi-agent primitives + workflow-level `RequestPort`; Postgres holds the three memory tiers; per-session agent factory. |
| Bilingual reports (UMR-001/046/048) | Agent accepts EN/FR free text; Azure Translator + Foundry NLG generate narrative sections; report generator attaches citations and runs through HITL. |
| Interoperability (UMR-055) | REST surface is the contract; routes sit behind APIM + App Gateway (WAF, rate limit); external agents trigger CRAFT with a token; GraphQL layer optional on top. |
| SLA + scale (UMR-056/057/059) | HA App Service + Azure Front Door; autoscale; SSC LaunchPad for the landing zone; health checks + load-test harness. |

## 6. Requirements Traceability

| Capability | Requirements | Design |
|---|---|---|
| Primary agent | UMR-001/011/013/016/018/019/094/095, AAR-001/003/006, ASG-005 | **Microsoft Agent Framework · `ChatAgent` + `AzureOpenAIChatClient` · `⟨I⟩ ChatProvider` · bounded iteration cap** |
| Retrieval + RAG | UMR-002/003/004/005/006/009/010/060/067, ARR-002–007 | Azure AI Search hybrid · `⟨I⟩ DataSource` registry (declarative JSON) · citation + grounding schema |
| Audit + traceability | UMR-015/027/045/061/062/093, AAR-005, ASG-003 | `AgentAction` envelope · `⟨I⟩ AgentActionLog` · hash-chained JSONL → Azure Log Analytics |
| HITL approvals | UMR-021–026/035/039/044/049, HITL-001–007, ASG-002 | Agent Framework `@tool(approval_mode)` · `⟨I⟩ ApprovalQueue` (Postgres) · Dash reviewer UI |
| RBAC + data scope | UMR-012/017/058/065/066, AAR-002/007 | Declarative `permissions.json` (role levels + rules + prefixes) · Entra ID · `SqliteDataStore` · `QueryTool.set_user` |
| Session + workspace | UMR-014/092/095 | `⟨I⟩ WorkspaceStore` → `SqliteStore` + `SessionScratchStore` · per-session agent factory |
| Guardrails + containment | UMR-020/029/030, ASG-001/004/011 | `GUARDRAIL_HOOK` + Azure Content Safety · APIM rate limit · Azure Container Apps sandbox |
| Connectors + external | UMR-051–055 | `⟨I⟩ DataSource` kind registry (JSON-driven) + MSAL · Flask REST · SAP / STK / MATLAB classes |
| Domain capabilities | UMR-007/008/031–050/075, ARR-001 | New `⟨I⟩ Tool` classes over existing registries (`ClassifierTool`, `HistoricalMissionTool`, `CostAggregatorTool`, `VendorAggregatorTool`, `CodeExecTool`) |
| Deployment + SLA | UMR-028/056/057/059/064/069/070/074/085, ASG-006 | Azure App Service PBMM · APIM + WAF · SSC LaunchPad HA · stdlib + `python-dotenv` config loader |

## 7. Dependencies & Blockages

Items the architecture depends on that need to be in place through IT, procurement, or domain partners.

| Dependency | Owner | Satisfies |
|---|---|---|
| Microsoft Agent Framework (`agent-framework` SDK on PBMM) | IT (install access) | Primary agent runtime |
| Azure OpenAI (Canadian PBMM region) | IT (already in CSA tenant) | LLM inference |
| Azure AI Foundry (model routing + rate limits) | IT (procurement) | LLM routing, rate control |
| Azure AI Search (hybrid retrieval) | IT (deploy) | Cited retrieval |
| Azure Content Safety | IT (procurement) | Guardrails |
| Azure Container Apps | IT (deploy) | `CodeExecTool` sandbox |
| Entra ID (app registration + MSAL) | IT | Identity, token flow for humans + external agents |
| Azure Log Analytics (immutable retention policy) | IT | Immutable audit sink |
| APIM + App Gateway (WAF) | IT | Edge security, rate limiting |
| Postgres managed instance | IT | HITL approval queue + 3-tier memory |
| SharePoint access (Graph API, MSAL scope) | IT + finance | SharePoint `DataSource` |
| SAP access (OData endpoint, OAuth scope) | Finance + IT | SAP `DataSource`; UC-F4 |
| STK / MATLAB licenses + Python adapters | Engineering | STK/MATLAB `DataSource` |
| CSA risk taxonomy | Domain | `ClassifierTool` training / rules |
| Historical mission DB | Finance | `HistoricalMissionTool`; UC-F1 |
| SSC LaunchPad HA + landing zone | IT | Deployment |

## 8. System-Health Tooling

| Tool | Role |
|---|---|
| ruff | Lint (flake8 + isort + pyupgrade) · pre-commit + CI |
| pyright (strict) | Type checking · protocol conformance · pre-commit + CI |
| pytest + coverage | Route × role matrix · protocol contracts · audit-envelope invariants · pre-commit + CI |
| doctest | Every public pure function carries an executable example · `pytest --doctest-modules` |
| architecture tests | AST-walkers in `app/tests/test_architecture.py`: doctest coverage, stateful-module test coverage, forbidden-import guard |
| bandit | Security scan · pre-commit |
| pip-audit | Dependency CVE audit · pre-commit + CI |
| detect-secrets | No credentials in git · pre-commit |

**Dependency surface:** `agent-framework` (umbrella; or `agent-framework-core` + `agent-framework-openai` + `agent-framework-foundry`), `openai`, `dash`, `flask`, `flask-login`, `pandas`, `plotly`, `python-dotenv`, `requests`, `werkzeug`, `msal`, `pdfplumber`, `python-docx`, `azure-search-documents`, `psycopg[binary]`, `azure-monitor-opentelemetry`. Each row in §7 adds **one targeted dep** behind an existing protocol — not a tree.
