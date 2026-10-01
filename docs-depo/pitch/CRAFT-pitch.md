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
└─────────────────┘   └──┬─────────┬─────────┬─────────┬────────┘
                         │         │         │         │
                         ▼         ▼         ▼         ▼
                    ┌─────────┐┌────────┐┌────────┐┌────────────┐
                    │LLM & AI ││Data Src││ID+Edge ││Ops & Audit │
                    │AzureOA  ││LocalFs ││Entra(d)││LogAnalyt(d)│
                    │AI Srch  ││ShPt(d) ││APIM(d) ││AppSvc PBMM │
                    │ContSfty ││SAP(d)  ││AppGW(d)││LaunchP(d)  │
                    │(d)      ││STK(d)  ││        ││ContApp(d)  │
                    └─────────┘└────────┘└────────┘└────────────┘
```
In: `/chat/send [base]` `/admin/* [admin]`. Out: thin italic. (d)=planned/dashed.

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
│⟨I⟩ChatProvider││⟨I⟩ Tool     ││▦WStore ▦Data(RBAC)      │
│              ││              ││▦AuditLog JSONL          │
│  AGNT_ACT ───┼┼── AGNT_ACT ──┼┼──▶                      │
└──────┬───────┘└──────┬───────┘└─────────────────────────┘
       │               │
       ▼               ▼
┌──────────────┐┌──────────────────────────────────┐
│Audit Sink    ││Connectors (perimeter):            │
│⟨I⟩ActLog     ││LocalFile · ShPt(d) · SAP(d) ·     │
│  │           ││STK/MATLAB(d)    ◆ diamond hd      │
│  ▼           │└──────────────────────────────────┘
│AzureLA(d)    │
└──────────────┘

┌──────────────┐
│Test Surface  │──▶ pre-commit · GitHub Actions
│(audit-green) │
└──────────────┘
```
AGENT_ACTION (green). Connectors ◆. Test surface dotted.

## 2c. L3 Internals

```text
Panel A · Agent:   chatbot◀─▶ToolNode   Panel B · Tools/Connectors:
                   │        │           ··Tool Protocol··        
                   ▼        │           weather docs charts      
              ◇_should_continue         query_data code-exec(d)  
                   │                    ··DataSource Protocol··  
                   ▼                    LocalFile ShPt(d) SAP(d) 
              END limit=25              STK(d)                   
              →llm_inf→Audit(green)     ◇HITL Gate(high-risk)   
              →tool_cl→Audit(green)     POST /tools/exec/<name>  
              ⟨I⟩ChatProvider            ◆Filesystem Cloud SAP   
              ⟨I⟩AgentActionLog                                  
Panel C · Auth:  Public inbound [/route][role]                   
                 →FlaskRoute→◇before_req(hex,blue)              
                 auth·role·ws·traceID                            
                 →handler→after_req(audit,green)                 
                 →response                                       
              _ROUTE_RULES: /send→base /upload→power /admin→admin 
              RBAC: base(1)<power(2)<admin(3)                     
              ⟨test⟩ arch invariants (audit-green)                
```

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

**Primary agent** — UMR-001/011/013/016/018/019/094/095, AAR-001/003/006, ASG-005. LangGraph ReAct · `ChatProvider` · `recursion_limit=25`. No blocker. Seam: `ChatProvider`. UC: E2, F1, F4.

**Retrieval + RAG** — UMR-002/003/004/005/006/009/010/060/067, ARR-002–007. Azure AI Search (hybrid vector+BM25) · `DataSource`+`Tool`. Blocker: IT AI Search deploy. Seam: `HybridRetrievalTool`. UC: E2, F1.

**Audit + traceability** — UMR-015/027/045/061/062/093, AAR-005, ASG-003. `AgentAction` envelope · `AgentActionLog` · JSONL→Log Analytics. Blocker: IT Log Analytics+immutability. Seam: `AgentActionLog` sink. UC: E2, F1, F4.

**HITL approvals** — UMR-021–026/035/039/044/049, HITL-001–007, ASG-002. LangGraph `interrupt` · Postgres queue · Dash UI. Blocker: CSA risk taxonomy. Seam: `ChatProvider`+interrupt. UC: E2, F1.

**RBAC + data scoping** — UMR-012/017/058/065/066, AAR-002/007. `_ROUTE_RULES`+`_ROLE_LEVEL`+`SqliteDataStore`+`QueryTool.set_user`. Blocker: per-tool RBAC pending. Seam: rule list appends. UC: E2, F1, F4.

**Session + workspace (V3)** — UMR-014/092/095. Split `WorkspaceStore`→`SqliteStore`+`SessionScratchStore`. Blocker: session lifecycle design. Seam: `WorkspaceStore` protocol. UC: dream.

**Guardrails + containment** — UMR-020/029/030, ASG-001/004/011. Azure Content Safety · APIM rate limit · Container Apps sandbox. Blocker: procurement. Seam: `CodeExecTool`. UC: dream.

**Connectors + external** — UMR-051–055. `DataSource`+MSAL · Flask REST · SAP/STK/MATLAB planned. Blocker: SAP procurement; STK/MATLAB licenses. Seam: `DataSource` classes. UC: F4.

**Domain capabilities** — UMR-007/008/031–034/036–038/040–043/046–048/050/075, ARR-001. New `Tool` over existing seams. Blocker: taxonomy+mission DB+Translator. Seam: uniform pattern. UC: E2, F1.

**Deployment, SLA** — UMR-028/056/057/059/064/069/070/074/085, ASG-006. Azure App Service PBMM · APIM+WAF · SSC LaunchPad HA · git config. Blocker: IT landing zone; LaunchPad. Seam: env-var+SQL migrations. UC: dream.

## 4. Use Cases

**UC-E2 · Risk ID + HITL.** Engineer uploads CADRe Part A → retrieval → LLM classifier → HITL gate → approve/reject → register write (planned).

**UC-F1 · Parametric cost + HITL.** Admin requests estimate → 5 similar missions → Euclidean distance → HITL gate before commitment.

**UC-F4 · Vendor cost + SAP.** Analyst queries vendor costs → SAP connector (DataSource planned) → extract+aggregate → audit. Blocked: SAP.

Other flows: budget scenarios, anomaly triage, bilingual reports, cross-mission compare — each = new `Tool`+(new `DataSource`). Core unchanged. No new architecture. Gated by §5.

## 5. Blocked Items

- **Azure AI Search** (IT) — retrieval+citations. Seam: `DataSource`+`HybridRetrievalTool`.
- **Log Analytics+immutability** (IT) — tamper-proof audit. Seam: `AgentActionLog`.
- **Content Safety+Container Apps** (procurement) — guardrails+sandbox. Seam: `CodeExecTool`.
- **Entra ID+SharePoint/SAP** (IT+finance) — CSA corpus+cost data. Seam: `DataSource`.
- **CSA risk taxonomy** (domain) — risk ID+HITL.
- **Historical mission DB** (finance) — cost estimation.

## 6. System-Health Tooling

- **ruff** — Lint (flake8+isort+pyupgrade) · pre-commit+CI
- **pyright** — Strict type check · pre-commit+CI
- **pytest+cov** — 156 tests, 91% coverage · pre-commit+CI
- **bandit** — Security scan · pre-commit
- **pip-audit** — CVE audit · pre-commit
- **detect-secrets** — No credentials in git · pre-commit

Architecture tests enforce protocol boundaries+required files per feature. Code quality: logging coverage, function length, import completeness. Suite: `.pre-commit-config.yaml`+`.github/workflows/ci.yml`. New invariant=new test. No extra infra.