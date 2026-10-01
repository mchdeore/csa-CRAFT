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

## 3. Requirements → Design

**Primary agent** — UMR-001/011/013/016/018/019/094/095, AAR-001/003/006, ASG-005. Microsoft Agent Framework · `ChatAgent` + `AzureOpenAIChatClient` · `⟨I⟩ ChatProvider` · bounded iteration cap · HITL via `@tool(approval_mode="always_require")`. No blocker. Seam: `ChatProvider`. UC: E2, F1, F4.

**Retrieval + RAG** — UMR-002/003/004/005/006/009/010/060/067, ARR-002–007. Azure AI Search (hybrid vector+BM25) · `⟨I⟩ DataSource` + `⟨I⟩ Tool`. Blocker: IT AI Search deploy. Seam: `HybridRetrievalTool`. UC: E2, F1.

**Audit + traceability** — UMR-015/027/045/061/062/093, AAR-005, ASG-003. `AgentAction` envelope · `⟨I⟩ AgentActionLog` · hash-chained JSONL → Azure Log Analytics. Blocker: IT Log Analytics + immutability. Seam: `AgentActionLog` sink. UC: E2, F1, F4.

**HITL approvals** — UMR-021–026/035/039/044/049, HITL-001–007, ASG-002. Agent Framework `approval_mode` on risky tools · SQLite `ApprovalQueue` + `/admin/approvals/<trace_id>/<decision>` resume routes · Dash reviewer UI (reserved) · Postgres at end state. Blocker: CSA risk taxonomy. Seam: `⟨I⟩ ApprovalQueue`. UC: E2, F1.

**RBAC + data scoping** — UMR-012/017/058/065/066, AAR-002/007. Declarative `permissions.json` (role levels + route rules + public/internal prefixes) · `SqliteDataStore` · `QueryTool.set_user`. Blocker: per-tool RBAC pending. Seam: rule list appends. UC: E2, F1, F4.

**Session + workspace** — UMR-014/092/095. `⟨I⟩ WorkspaceStore` → `SqliteStore` + `SessionScratchStore`. Blocker: session lifecycle design. Seam: `WorkspaceStore` protocol. UC: dream.

**Guardrails + containment** — UMR-020/029/030, ASG-001/004/011. Azure Content Safety · APIM rate limit · Azure Container Apps sandbox. Blocker: procurement. Seam: `GUARDRAIL_HOOK` in tool wrapper + `CodeExecTool` (reserved). UC: dream.

**Connectors + external** — UMR-051–055. `⟨I⟩ DataSource` kind registry (JSON-driven) + MSAL · Flask REST · SAP/STK/MATLAB planned. Blocker: SAP procurement; STK/MATLAB licenses. Seam: `DataSource` classes. UC: F4.

**Domain capabilities** — UMR-007/008/031–034/036–038/040–043/046–048/050/075, ARR-001. New `⟨I⟩ Tool` over existing seams. Reserved stubs today: `ClassifierTool`, `HistoricalMissionTool`, `CostAggregatorTool`, `VendorAggregatorTool`, `CodeExecTool`. Blocker: taxonomy + mission DB + Translator. Seam: uniform pattern. UC: E2, F1.

**Deployment, SLA** — UMR-028/056/057/059/064/069/070/074/085, ASG-006. Azure App Service PBMM · APIM+WAF · SSC LaunchPad HA · stdlib + `python-dotenv` config. Blocker: IT landing zone; LaunchPad. Seam: env-var + SQL migrations. UC: dream.

## 4. Use Cases

**UC-E2 · Risk ID + HITL.** Engineer uploads CADRe Part A → retrieval → classifier tool scores severity → HITL gate (framework `approval_mode`) → approve/reject → register write (planned).

**UC-F1 · Parametric cost + HITL.** Admin requests estimate → 5 similar missions → weighted distance aggregator → HITL gate before commitment.

**UC-F4 · Vendor cost + SAP.** Analyst queries vendor costs → SAP `DataSource` (planned) → extract + aggregate → audit. Blocked: SAP.

Other flows: budget scenarios, anomaly triage, bilingual reports, cross-mission compare — each = new `⟨I⟩ Tool` + (new `⟨I⟩ DataSource`). Core unchanged. No new architecture. Gated by §5.

## 5. Blocked Items

- **Azure AI Search** (IT) — retrieval + citations. Seam: `⟨I⟩ DataSource` + `HybridRetrievalTool`.
- **Azure Log Analytics + immutability** (IT) — tamper-proof audit forwarding; hash-chained JSONL already on disk. Seam: `⟨I⟩ AgentActionLog`.
- **Azure Content Safety + Azure Container Apps** (procurement) — guardrails + code-exec sandbox. Seam: `GUARDRAIL_HOOK` + `CodeExecTool`.
- **Entra ID + SharePoint/SAP** (IT + finance) — CSA corpus + cost data. Seam: `⟨I⟩ DataSource` + MSAL in `⟨I⟩ AuthProvider`.
- **Microsoft Agent Framework access** (if restricted) — SDK installation on PBMM environment. Fallback documented: hand-rolled ReAct loop on `openai.AsyncAzureOpenAI` behind the same `⟨I⟩ ChatProvider`.
- **CSA risk taxonomy** (domain) — risk ID + HITL.
- **Historical mission DB** (finance) — cost estimation.

## 6. System-Health Tooling

- **ruff** — Lint (flake8 + isort + pyupgrade) · pre-commit + CI
- **pyright (strict)** — Type check · protocol conformance · pre-commit + CI
- **pytest + coverage** — Route × role matrix · protocol contracts · audit-envelope invariants · pre-commit + CI
- **doctest** — Every public pure function carries an executable example · `pytest --doctest-modules`
- **architecture tests** — AST-walkers in `app/tests/test_architecture.py`: public-function doctest coverage, stateful-module test coverage, forbidden-import guard
- **bandit** — Security scan · pre-commit
- **pip-audit** — CVE audit · pre-commit + CI
- **detect-secrets** — No credentials in git · pre-commit

Architecture tests enforce protocol boundaries + required files per feature. Code quality: logging coverage, function length, import completeness. Suite: `.pre-commit-config.yaml` + `.github/workflows/ci.yml`. New invariant = new test. No extra infra.
