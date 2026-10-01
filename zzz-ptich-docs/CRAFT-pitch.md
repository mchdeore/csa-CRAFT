# CRAFT — Pitch Package

*Audited retrieval-augmented AI assistant for CSA mission engineering and finance (bilingual EN/FR, cited answers, HITL-gated).*

## 1. Containers (L2)

<div class="figure">
<object type="image/svg+xml" data="diagrams/L2-container.svg"></object>
<div class="caption">Figure 1 · Actors, routes, containers, data, external systems, audit perimeter.</div>
</div>

Flask + Dash. Routes are role-checked; every step emits `AGENT_ACTION` (UMR-015/027). LangGraph ReAct dispatches to the Tool and DataSource registries; responses carry citations (UMR-002/006) and confidence (UMR-007/010).

## 2. Internals (L3)

<div class="figure">
<object type="image/svg+xml" data="diagrams/L3-cluster.svg"></object>
<div class="caption">Figure 2 · Agent loop with HITL branch, Tool registry, DataSource registry, auth cluster.</div>
</div>

HITL (UMR-021–026/HITL-001–007) is a graph interrupt off `tool_node`, not middleware: the queue, timeout, reviewer UI, and decision log sit inside the same auth and audit perimeter as the agent. Self-correction / grounding loops (UMR-009/010) attach as graph nodes between retrieve and respond.

## 3. Use Cases

<div class="figure">
<object type="image/svg+xml" data="diagrams/UC-lanes.svg"></object>
<div class="caption">Figure 3 · UC-E2 risk + HITL · UC-F1 parametric cost + HITL · UC-F4 vendor cost roll-up (SAP).</div>
</div>

## 4. Design Decisions

| Component | Why chosen |
|---|---|
| **Flask (server) + Dash (UI)** | Routes are the integration contract — anything with a token (user, cron, agent, Teams bot) can call CRAFT. Dash shares the Flask process so the HITL reviewer UI inherits the same auth and audit. |
| **LangGraph ReAct** | First-class `interrupt` for HITL (UMR-021), bounded recursion (UMR-013/AAR-003 → `recursion_limit`), graph-level test anchors. Actively maintained by LangChain Inc.; standard pattern. |
| **Protocol-typed registries (`Tool`, `DataSource`, `ChatProvider`, `WorkspaceStore`, `AgentActionLog`)** | New capability or new backend = one class satisfying a protocol; no agent edit. Pyright-checked contracts (UMR-012/AAR-002). |
| **Azure OpenAI / Azure AI Foundry (end state)** | Canadian-region PBMM data residency; Foundry gives us model routing (UMR-028), rate limits (UMR-030/ASG-004), and content safety (UMR-020/ASG-001) under one procurement line. |
| **Azure AI Search (end state)** | Hybrid semantic + BM25 natively (UMR-005/ARR-002), top-K ranking at 0.72 cosine (UMR-004), managed vector store. |
| **Azure Container Apps sandbox** | Isolated per-request code exec for UMR-093 (code, inputs, outputs, exit status audited). |
| **Entra ID + MSAL** | CSA-standard identity; same token flow for human and agent callers (UMR-017/AAR-007). |
| **Log Analytics (end state) / hash-chained JSONL (now)** | Immutable audit per UMR-027/ASG-003; KQL-queryable at end state, grep-able today. |
| **Postgres (HITL queue, 3-tier memory)** | Durable approval state across restarts (UMR-025 TTL); same instance backs the episodic/semantic/procedural tiers (UMR-014/AAR-004). |
| **SQLite (now) / managed DB (end state)** | File-local for scratch + per-user data today; swap target already named behind `WorkspaceStore`. |
| **pytest + pyright + ruff + bandit + pip-audit + detect-secrets** | Architecture invariants ship as tests (route × role, protocol contracts, audit-envelope present). Industry-standard, maintained. |

## 5. Solving the Problems — Today and at End State

The system is already running against stubs or local alternatives wired through the same registries that will carry the Azure services at end state. Cutover is a config change per row, not a rewrite.

| Problem (requirement) | How the architecture solves it today | How it solves it at end state (Azure-consolidated) |
|---|---|---|
| Cited retrieval (UMR-002/005/006, ARR-002/003) | `DocumentSearchTool` + `TextAnalysisTool` over `LocalFileSource`; retrieval response schema carries document / page / section provenance. | Replace `LocalFileSource` with Azure AI Search backend (hybrid semantic + BM25); same `DataSource` call site, same citation schema. |
| Grounding + confidence (UMR-007/008/010) | Grounding node sits between retrieve and respond; emits `confidence` into `AGENT_ACTION`; escalates below 0.6. | Foundry evaluation + RAGAS-style scoring plugs into the same node; threshold remains code-side. |
| HITL approvals (UMR-021–026, HITL-001–007) | LangGraph `interrupt` → Postgres approval queue → Dash reviewer UI, same auth as routes; decisions logged immutably with reasoning chain, confidence, sources. | Content Safety + Foundry rate limits layer in front; approval queue and UI unchanged. |
| RBAC + data scope (UMR-012/017/058, AAR-002/007) | Route-gated `_ROUTE_RULES` + `_ROLE_LEVEL`; `SqliteDataStore` scoped by `QueryTool.set_user`; per-tool RBAC column staged. | Entra ID issues tokens; same role check in `before_request`; classification tags enforced at the data store. |
| Immutable audit (UMR-015/027/045, ASG-003) | `AgentActionLog` writes append-only JSONL with hash chain; daily rotation; covers every tool call and LLM turn. | Forward the same envelope to Log Analytics (immutability policy); KQL replaces grep. |
| Guardrails + sandbox (UMR-020/029/030/093, ASG-001/004/011) | Guardrail hook point in tool wrapper; code-exec slot reserved; rate limit at APIM-like proxy. | Content Safety on the hook; Azure Container Apps for code-exec; Foundry rate controls. |
| External data (UMR-051–054) | `LocalFileSource` reads mirrors / CSV fixtures of the CSA corpus and SAP line items; UC-E2 / F1 / F4 lanes run end-to-end. | SharePoint, SAP, STK, MATLAB each land as a `DataSource` class with MSAL / OAuth. |
| Multi-agent + memory (UMR-011/014/018/095, AAR-001/004) | Primary agent + tool registry + session workspace; `agent_id` in `AGENT_ACTION` already carries sub-task identity. | Add orchestrator + specialist nodes; Postgres holds the three memory tiers; per-session agent factory. |
| Bilingual reports (UMR-001/046/048) | Agent accepts EN/FR free text; report generator attaches citations and runs through HITL. | Azure Translator + Foundry NLG for narrative sections; same template + evidence pipeline. |
| Interoperability (UMR-055) | REST surface is the contract today; schema documented; external agents can trigger CRAFT with a token. | Same routes behind APIM + App Gateway (WAF, rate limit); GraphQL layer optional on top. |
| SLA + scale (UMR-056/057/059) | Single-instance App Service with health checks; load-test harness in place. | HA App Service + Azure Front Door; auto-scale; SSC LaunchPad for the landing zone. |

## 6. Requirements Traceability

| Capability | Requirements | Design |
|---|---|---|
| Primary agent | UMR-001/011/013/016/018/019/094/095, AAR-001/003/006, ASG-005 | LangGraph ReAct · `ChatProvider` · bounded recursion |
| Retrieval + RAG | UMR-002/003/004/005/006/009/010/060/067, ARR-002–007 | Hybrid search tool · `DataSource` · citation + grounding schema |
| Audit + traceability | UMR-015/027/045/061/062/093, AAR-005, ASG-003 | `AgentAction` envelope · `AgentActionLog` · hash-chained JSONL → Log Analytics |
| HITL approvals | UMR-021–026/035/039/044/049, HITL-001–007, ASG-002 | LangGraph `interrupt` · Postgres queue · Dash reviewer UI |
| RBAC + data scope | UMR-012/017/058/065/066, AAR-002/007 | `_ROUTE_RULES` + `_ROLE_LEVEL` · `SqliteDataStore` · `QueryTool.set_user` |
| Session + workspace | UMR-014/092/095 | `WorkspaceStore` → `SqliteStore` + `SessionScratchStore`; per-session agent factory |
| Guardrails + containment | UMR-020/029/030, ASG-001/004/011 | Content Safety hook · APIM rate limit · Container Apps sandbox |
| Connectors + external | UMR-051–055 | `DataSource` + MSAL · Flask REST · SAP / STK / MATLAB classes |
| Domain capabilities | UMR-007/008/031–050/075, ARR-001 | New `Tool` classes over existing registries |
| Deployment + SLA | UMR-028/056/057/059/064/069/070/074/085, ASG-006 | Azure App Service PBMM · APIM + WAF · SSC LaunchPad HA · git config |

## 7. Blockages (End State / Current Alternative)

Each row is an Azure-consolidated end-state component wired through the registry the current alternative already runs against.

| End-state component | Owner | Current alternative |
|---|---|---|
| Azure AI Search (hybrid retrieval) | IT | `LocalFileSource` + file-name/path search |
| Azure Log Analytics + immutability | IT | Hash-chained append-only JSONL on disk |
| Azure Content Safety | Procurement | Guardrail hook off (config flag) |
| Azure Container Apps sandbox | Procurement | `CodeExecTool` registration slot reserved |
| Entra ID (app registration + MSAL) | IT | Local `AuthProvider` stub, mocked tokens |
| SharePoint `DataSource` | IT + CSA | `LocalFileSource` reads a corpus mirror |
| SAP `DataSource` | Finance + Procurement | CSV fixtures via `LocalFileSource` (UC-F4 runs) |
| STK / MATLAB adapters | Procurement (licenses) | `Tool` slot reserved |
| Azure AI Foundry (model routing / rate limits) | IT | Azure OpenAI direct (Canadian region) |
| SSC LaunchPad HA | SSC | Single-region App Service |
| CSA risk taxonomy | CSA Domain | Stub taxonomy drives the classifier for tests |
| Historical mission DB | CSA Finance | CSV fixtures through `LocalFileSource` (UC-F1 runs) |

## 8. System-Health Tooling

Runs on every commit and in CI; these are invariants, not blockages.

| Tool | Role |
|---|---|
| ruff | Lint (flake8 + isort + pyupgrade) |
| pyright (strict) | Type checking · protocol conformance |
| pytest + coverage | Route × role matrix · protocol contracts · audit-envelope invariants (156 tests, 91% cov) |
| bandit | Security scan |
| pip-audit | Dependency CVE audit |
| detect-secrets | No credentials in git |
