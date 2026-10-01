# CRAFT — Pitch Package

*Audited retrieval-augmented AI assistant for CSA mission engineering and finance.*

## 1. Containers & Context (L2)

<div class="figure">
<object type="image/svg+xml" data="diagrams/L2-container.svg"></object>
<div class="caption">Figure 1 · Actors, external systems, routes, containers, and the audit + RBAC perimeters.</div>
</div>

## 2. Internals (L3)

<div class="figure">
<object type="image/svg+xml" data="diagrams/L3-cluster.svg"></object>
<div class="caption">Figure 2 · Primary agent loop, tool registry, data-source registry, and auth cluster.</div>
</div>

## 3. Use Cases (One-Sheet)

<div class="figure">
<object type="image/svg+xml" data="diagrams/UC-lanes.svg"></object>
<div class="caption">Figure 3 · Three use-case lanes laid out left-to-right with UC IDs and swim-lane dividers.</div>
</div>

## 4. Requirements → Design

| Capability | Requirements | Design seam | Use cases |
|---|---|---|---|
| Primary agent | UMR-001/011/013/016/018/019/094/095, AAR-001/003/006, ASG-005 | LangGraph ReAct · `ChatProvider` · `recursion_limit=25` | E2, F1, F4 |
| Retrieval + RAG | UMR-002/003/004/005/006/009/010/060/067, ARR-002–007 | Azure AI Search (hybrid vector + BM25) · `DataSource` + `Tool` | E2, F1 |
| Audit + traceability | UMR-015/027/045/061/062/093, AAR-005, ASG-003 | `AgentAction` envelope · `AgentActionLog` · JSONL → Log Analytics | E2, F1, F4 |
| HITL approvals | UMR-021–026/035/039/044/049, HITL-001–007, ASG-002 | LangGraph `interrupt` · Postgres queue · Dash review UI | E2, F1 |
| RBAC + data scoping | UMR-012/017/058/065/066, AAR-002/007 | `_ROUTE_RULES` + `_ROLE_LEVEL` · `SqliteDataStore` · `QueryTool.set_user` | E2, F1, F4 |
| Session + workspace | UMR-014/092/095 | `WorkspaceStore` → `SqliteStore` + `SessionScratchStore` | all |
| Guardrails + containment | UMR-020/029/030, ASG-001/004/011 | Azure Content Safety · APIM rate limit · Container Apps sandbox | all |
| Connectors + external | UMR-051–055 | `DataSource` + MSAL · Flask REST · SAP / STK / MATLAB adapters | F4 |
| Domain capabilities | UMR-007/008/031–034/036–038/040–043/046–048/050/075, ARR-001 | New `Tool` instances over existing seams | E2, F1 |
| Deployment, SLA | UMR-028/056/057/059/064/069/070/074/085, ASG-006 | Azure App Service PBMM · APIM + WAF · SSC LaunchPad HA · git config | all |

## 5. Development Flags & System-Health Tooling

| Item | Kind | Owner / tool | Notes |
|---|---|---|---|
| Azure AI Search | Dev flag | IT | Hybrid retrieval + citations. Seam: `DataSource` + `HybridRetrievalTool`. |
| Log Analytics + immutability | Dev flag | IT | Tamper-proof audit sink. Seam: `AgentActionLog`. |
| Content Safety + Container Apps | Dev flag | Procurement | Guardrails + sandboxed code exec. Seam: `CodeExecTool`. |
| Entra ID + SharePoint / SAP | Dev flag | IT + Finance | CSA corpus + cost data. Seam: `DataSource`. |
| CSA risk taxonomy | Dev flag | Domain | Risk ID + HITL classification. |
| Historical mission DB | Dev flag | Finance | Parametric cost estimation. |
| ruff | Health | pre-commit + CI | Lint (flake8 + isort + pyupgrade). |
| pyright | Health | pre-commit + CI | Strict type checking. |
| pytest + coverage | Health | pre-commit + CI | 156 tests, 91% coverage. |
| bandit | Health | pre-commit | Security scan. |
| pip-audit | Health | pre-commit | Dependency CVE audit. |
| detect-secrets | Health | pre-commit | No credentials in git. |
