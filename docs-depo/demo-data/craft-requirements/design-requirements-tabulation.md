# CRAFT Design Requirements Tabulation

_Source: CSA-SEFM-RD-0001 (UMR Document v1.5) and CRAFT-Req-Arch-Document-V3_

## Agent Framework Decision

- **Current**: PydanticAI (single-agent)
- **Target**: TBD — evaluating **LangGraph** (Python-native, production-proven multi-agent) vs **Pi** (pi.dev, Python SDK wrapping Node.js core, strong tool-use agent)
- **Decision driver**: Need multi-agent orchestration with Python Flask routing. Pi is appealing as coding-agent-first orchestrator with tool delegation primitives. LangGraph is safer/more proven.

---

| Req IDs | Type | Requirement Summary | Implementation Status | Timeline | How Satisfied / Path to Satisfaction |
|---------|------|---------------------|----------------------|----------|--------------------------------------|
| UMR-001 | Mandatory | Accept natural language queries in English and French | Partial | Soon | Chat interface accepts free-text queries via PydanticAI agent; French language detection not yet implemented. Add language detection middleware to satisfy. |
| UMR-002 | Mandatory | Retrieve documents with source citations | Partial | Soon | `DocumentSearchTool` and `TextAnalysisTool` retrieve files from local sources; citation format (document, page, section) not yet structured. Extend retrieval response schema to include provenance metadata. |
| UMR-003 | Mandatory | RAG pipeline with minimum 8192-token context window | Partial | Soon | Agent uses OpenAI-compatible model via PydanticAI with configurable context; no formal RAG chunking/embedding pipeline yet. Add vector store and chunk-aware retrieval to satisfy. |
    20|| UMR-004 | Mandatory | Return top 5 ranked documents with cosine similarity ≥ 0.72 | Incomplete | Next | No vector similarity search implemented. Requires embedding pipeline, vector store, and ranked retrieval with configurable threshold. COMMENT : [NOT BUILT] vector store / embedding pipeline |
| UMR-005, ARR-002 | Mandatory | Hybrid search: 0.7 semantic + 0.3 BM25 keyword | Incomplete | Next | No hybrid search. Current search is file-name/path matching. Requires BM25 index + vector embeddings with fusion scoring. COMMENT : [NOT BUILT] vector store / embedding pipeline; Azure AI Search supports hybrid natively |
| UMR-006, UMR-060, ARR-003 | Mandatory | Traceable source references (document, page, section) — every answer includes source references | Incomplete | Next | Document reader returns text but no page/section locators. Requires chunk-level metadata preserved through ingestion. COMMENT : [NOT BUILT] vector store / source citation pipeline; every citation must be independently verifiable |
| UMR-007, ARR-004 | Mandatory | Confidence score 0–1 for generated outputs (per agent) | Incomplete | Later | No confidence scoring. Requires evidence-coverage scoring module per V3 spec (not token probabilities). COMMENT : [NOT BUILT] confidence/grounding evaluation pipeline; plan Azure Foundry tools |
| UMR-008, ARR-005 | Mandatory | Escalation when confidence < 0.6 | Incomplete | Later | No escalation mechanism. Requires confidence scoring + HITL routing. COMMENT : [NOT BUILT] confidence pipeline + HITL system; threshold is a safety gate, must not be bypassable |
| UMR-009, ARR-006 | Mandatory | Self-correction loop for retrieval refinement | Incomplete | Later | No retrieval retry logic. Agent has retries=4 for LLM calls but no retrieval-specific refinement loop. COMMENT : [NOT BUILT] vector store / embedding pipeline; each refinement iteration must log what changed and why |
| UMR-010, ARR-007 | Mandatory | Faithfulness score ≥ 0.80 (grounding) | Incomplete | Later | No grounding/faithfulness evaluation framework. Requires RAGAS or equivalent evaluation pipeline. COMMENT : [NOT BUILT] confidence/grounding evaluation pipeline; ungrounded outputs are a data safety risk |
| UMR-011, AAR-001 | Mandatory | Multi-agent architecture, each agent with one defined role | Partial | Next | Single PydanticAI agent with tool registry. Architecture supports adding specialized agents; delegation and accountability model not yet implemented per V3 revision. COMMENT : [PARTIAL] framework decision pending (LangGraph vs Pi) |
    30|| UMR-012, AAR-002 | Mandatory | Agents operate only with permitted tools from registry | Partial | Soon | `tools/registry.py` exists and tools are registered per agent. Tool permission boundaries per role not enforced; version control of permissions not implemented. |
| UMR-013 | Mandatory | ReAct loop with max 10 reasoning steps per query | Partial | Soon | PydanticAI agent supports iterative reasoning; no explicit step counter or max-step enforcement. Add step-bounded execution loop. |
| AAR-003 | Mandatory | Orchestrator agent: ReAct workflow, max 10 reasoning steps | Incomplete | Later | No orchestrator with step-bounded ReAct loop. PydanticAI agent runs unbounded. COMMENT : [NOT BUILT] multi-agent orchestrator; single agent only; waiting on framework migration |
| UMR-014, AAR-004 | Mandatory | Three-tier agent memory: episodic, semantic, procedural | Incomplete | Later | No memory tiers. Session state is ephemeral. COMMENT : [NOT BUILT] agent memory architecture; can use PostgreSQL for all tiers, Redis optional as cache layer later |
| UMR-015, AAR-005 | Mandatory | Structured agent messages: agent ID, action, input, output, confidence, timestamp | Partial | Soon | Structured JSON logging with timestamps, route tracking, and tool_call_id exists; not yet a full inter-agent message schema with agent ID, action, input, output, confidence in one envelope. COMMENT : [PARTIAL] JSON logging exists; needs full inter-agent message schema |
| UMR-016, AAR-006 | Mandatory | Agent spawning/termination without service interruption | Partial | Later | FastAPI/Dash architecture supports independent request handling; no dynamic agent lifecycle management. |
| UMR-017, AAR-007 | Mandatory | Agents cannot access data outside authorized scope; permission boundaries enforced | Partial | Soon | Route-gated architecture with role-based permission checks (`_has_permission`, `_ROLE_ROUTES`) enforces 401/403 on protected routes. Per-agent tool-level RBAC not yet implemented. COMMENT : [PARTIAL] route gating built; per-tool RBAC not built |
| UMR-018, ARR-001 | Mandatory | Planning function decomposes complex requests into sub-tasks | Incomplete | Later | No task decomposition. Single agent handles entire request. COMMENT : [NOT BUILT] waiting on framework migration + orchestrator agent; sub-task traceability required for audit |
| UMR-019, ASG-005 | Mandatory | Loop detection: break after 3 repeated non-progressing actions | Incomplete | Later | No loop detection logic. PydanticAI retries are for errors, not behavioral loops. COMMENT : [NOT BUILT] orchestrator loop control; also need agent reasoning/tool-execution logs to diagnose loops |
| UMR-020, ASG-001 | Mandatory | Guardrails prevent off-topic/harmful/policy-violating outputs | Incomplete | Soon | No guardrail layer. Relies on LLM system prompt only. COMMENT : [NOT BUILT] Azure Foundry content safety + RBAC + tool permissions handle this |
    40|| UMR-021, HITL-001 | Mandatory | HITL approval gates for high-risk actions | Incomplete | Later | No HITL approval workflow. Requires approval queue, risk classification, and reviewer routing. COMMENT : [NOT BUILT] HITL approval system; Dash UI exists as foundation |
| HITL-002 | Mandatory | Define high-risk actions: cost commitments, risk register updates, mission parameter changes | Incomplete | Later | No risk classification of actions. COMMENT : [NOT BUILT] HITL approval system; needs CSA expert to define risk tiers |
| UMR-022, HITL-003 | Mandatory | HITL requests display reasoning chain, confidence, sources | Incomplete | Later | No HITL UI. Requires approval interface showing agent reasoning trace. COMMENT : [NOT BUILT] HITL approval system + confidence pipeline; reviewer must see full thought process |
| UMR-023, HITL-004 | Mandatory | Engineers can approve/reject/modify recommendations | Incomplete | Later | No approval interface. Requires HITL review UI with approve/reject/modify actions. COMMENT : [NOT BUILT] HITL approval system; Dash UI exists as foundation; actions must be logged and immutable |
| UMR-024, HITL-005 | Mandatory | Rejected recommendations trigger agent re-planning with correction | Incomplete | Later | No feedback loop from human rejection. Requires agent re-planning on rejection. COMMENT : [NOT BUILT] HITL approval system + planner architecture; rejection reason must be structured input |
| UMR-025, HITL-006 | Mandatory | HITL timeout after 24 hours; action cancelled and flagged | Incomplete | Later | No HITL timeout mechanism. Requires approval queue with TTL. COMMENT : [NOT BUILT] HITL approval system; stale approvals are a security risk |
| UMR-026, HITL-007 | Mandatory | HITL decisions logged with reviewer ID, decision, timestamp, justification | Incomplete | Later | No HITL decision logging. COMMENT : [NOT BUILT] HITL approval system + immutable audit log; full audit chain: who decided what, when, why |
| UMR-027, ASG-003 | Mandatory | Immutable audit log of agent actions and approvals | Partial | Soon | `app/core/logging.py` provides structured JSON logging with daily rotation. Not immutable (append-only with tamper detection not implemented). Extend with write-once audit store. |
| UMR-028, ASG-006 | Mandatory | Model weights and prompt templates version controlled | Partial | Soon | System prompt defined in code under git. Model config in `app/core/config.py`. No formal versioning/approval workflow for prompt changes. |
| UMR-029, ASG-002 | Mandatory | Agent actions reversible or support rollback | Incomplete | Later | No rollback capability. Current tools are read-only (search, weather, charts) so low risk. COMMENT : [NOT BUILT] wait until later in development with more tools, architecture, and use cases |
| UMR-030, ASG-004 | Mandatory | Rate limiting per agent (default 100 LLM calls/min) | Incomplete | Soon | No rate limiting. COMMENT : [NOT BUILT] use Azure Foundry rate controls, or implement locally if preferred |
    50|| UMR-031 | Mandatory | Generate mission cost estimates from historical data | Incomplete | Later | No cost estimation module. COMMENT : [NOT BUILT] simple formatted ingestion and tagging pipeline once more data + stable DB exists |
| UMR-032 | Mandatory | Cost similarity via weighted normalized Euclidean distance | Incomplete | Later | No similarity algorithm. COMMENT : [NOT BUILT] needs design session + more data for testing; depends on embeddings |
| UMR-033 | Mandatory | Retrieve 5 most similar historical missions | Incomplete | Later | No historical mission database or similarity search. COMMENT : [NOT BUILT] needs structured DB; also must define "similar" — cost? mission type? payload? |
| UMR-034 | Mandatory | Cost estimates include confidence and source missions | Incomplete | Later | No cost estimation pipeline. COMMENT : [NOT BUILT] waiting on cost estimation tools and workflow |
| UMR-035 | Mandatory | HITL approval before cost commitments | Incomplete | Later | No HITL for financial actions. COMMENT : [NOT BUILT] waiting on cost estimation tools and workflow |
| UMR-036 | Goal | Identify and flag risks in mission documents | Incomplete | Later | No risk identification module. COMMENT : [NOT BUILT] what is a "risk"? needs CSA domain definition. Are we training on labeled data? Who builds the dataset and evaluation criteria? |
| UMR-037 | Mandatory | Risk function: keyword pattern matching + LLM classification | Incomplete | Later | No risk analysis pipeline. COMMENT : [NOT BUILT] risk identification architecture; plan finetune on Azure Foundry |
| UMR-038 | Mandatory | Classify identified risks by severity | Incomplete | Later | No risk classification. COMMENT : [NOT BUILT] risk identification architecture; severity rubric needs CSA expert |
| UMR-039 | Mandatory | Risk register updates require HITL approval | Incomplete | Later | No risk register or HITL integration. COMMENT : [NOT BUILT] risk identification architecture + HITL approval system |
| UMR-040 | Mandatory | Risk outputs grounded in document evidence | Incomplete | Later | No risk analysis pipeline. COMMENT : [NOT BUILT] risk identification architecture + source citation pipeline |
    60|| UMR-041 | Mandatory | Detect anomalies in telemetry and system data | Incomplete | Later | No telemetry ingestion or anomaly detection. COMMENT : [NOT BUILT] anomaly detection architecture; needs real telemetry feed |
| UMR-042 | Mandatory | Anomaly detection via Z-score threshold > 2.5 | Incomplete | Later | No anomaly detection module. COMMENT : [NOT BUILT] anomaly detection architecture |
| UMR-043 | Mandatory | Retrieve similar historical anomaly cases | Incomplete | Later | No anomaly knowledge base. COMMENT : [NOT BUILT] anomaly detection architecture; needs curated case library |
| UMR-044 | Mandatory | High-severity anomalies trigger HITL review | Incomplete | Later | No anomaly severity routing. COMMENT : [NOT BUILT] anomaly detection architecture + HITL approval system |
| UMR-045 | Mandatory | Anomaly events and responses logged in audit trail | Incomplete | Later | No anomaly logging. COMMENT : [NOT BUILT] anomaly detection architecture + immutable audit log |
| UMR-046 | Mandatory | Generate bilingual reports using approved templates | Incomplete | Later | No bilingual report generation. COMMENT : [NOT BUILT] Azure has NL services, translation, audio analysis — can build report tools around these cheaply | Use **Azure OpenAI GPT-4o mini** (~$0.15-$0.65/1M tokens) for cost-effective NLG; **Azure Translator** ($10/1M chars, 2M free/month) for document translation; expose via **APIM + Application Gateway** (internal VNet + WAF) for secure connector access. See `/data/research/azure-ai-services-bilingual-reports-secure-api-research.md`. |
| UMR-047 | Mandatory | Reports compiled from approved internal sources | Incomplete | Later | No report compilation from controlled sources. COMMENT : [NOT BUILT] report generation architecture + MS365/SharePoint connector |
| UMR-048 | Mandatory | Narrative report sections grounded in retrieved evidence | Incomplete | Later | No evidence-grounded report generation. COMMENT : [NOT BUILT] report generation architecture + source citation pipeline |
| UMR-049 | Mandatory | Report drafts support engineer review before finalization | Incomplete | Later | No report review workflow. COMMENT : [NOT BUILT] report generation architecture + HITL approval system |
| UMR-050 | Mandatory | Final reports versioned and logged | Incomplete | Later | No report versioning. COMMENT : [NOT BUILT] can use DB timestamps and metadata columns to track versions and updates |
    70|| UMR-051 | Mandatory | Integrate with existing CSA document repositories | Partial | Soon | `connectors/` module provides a pluggable data-source architecture with `local_files.py`. Extensible to SharePoint/Confluence with additional connector implementations. |
| UMR-052 | Mandatory | Connect to SharePoint and Confluence via APIs | Incomplete | Soon | Connector architecture exists but no SharePoint/Confluence implementations. COMMENT : [PARTIAL] connector framework built (local_files); SharePoint/MS365 connector not built |
| UMR-053 | Mandatory | Integration with CSA financial systems (SAP) | Incomplete | Later | No SAP integration. COMMENT : [NOT BUILT] SAP connector; needs CSA finance team input |
| UMR-054 | Mandatory | Integration with mission design tools (STK, MATLAB) | Incomplete | Later | No STK/MATLAB integration. COMMENT : [NOT BUILT] STK/MATLAB connectors; needs license procurement |
| UMR-055 | Goal | REST and GraphQL interfaces for interoperability | Partial | Soon | FastAPI provides REST endpoints. No GraphQL layer. Add GraphQL schema to satisfy. |
| UMR-056 | Mandatory | Query response < 5 seconds for 90% of queries | Partial | Later | Architecture supports fast responses; no performance benchmarking or SLA enforcement. Requires load testing and optimization. |
| UMR-057 | Mandatory | 99.5% availability during business hours | Incomplete | Later | No HA deployment. Single-instance architecture. Requires redundancy, health checks, and monitoring. COMMENT : [NOT CONFIGURED] deployment/infra; Azure webapp agreed, HA up to IT |
| UMR-058 | Mandatory | Protect sensitive data per CSA classification policy | Incomplete | Next | No data classification enforcement. Auth module provides basic user authentication but no data-level access control. COMMENT : [NOT BUILT] tag data with classification, use RBAC + user scope from user table |
| UMR-059 | Mandatory | Support 500+ concurrent users | Incomplete | Later | No load testing or horizontal scaling. FastAPI supports async but deployment not scaled. COMMENT : [NOT CONFIGURED] deployment/infra; Azure webapp auto-scaling available |
| UMR-061 | Mandatory | Decision traceability reports (evidence, reasoning, confidence, approvals) | Incomplete | Later | No decision traceability reporting. Logging exists but not structured for decision reconstruction. COMMENT : [NOT BUILT] HITL + confidence + source citation pipelines; JSON logging exists |
    80|| UMR-062 | Mandatory | Audit reports with timestamped history of system activities | Partial | Soon | JSON logging captures requests and tool calls with timestamps. Not yet exportable as audit reports. Extend with reporting UI and export capability. |

---

## Summary

| Category | Total | Next | Soon | Later |
|----------|-------|------|------|-------|
| All Requirements (merged) | 57 | 5 | 15 | 37 |

### Timeline Legend
    90|- **Next** (5) — Prerequisites for core functionality; do immediately after framework migration
- **Soon** (15) — Important but not blocking; within first few sprints
- **Later** (37) — Depends on other systems being built first

### Merged Duplicates
AAR/ARR/HITL/ASG requirements that were exact duplicates of UMR requirements have been merged into the UMR row under the **Req IDs** column. This collapses 89 rows → 57 rows while preserving all requirement coverage.

### Key Architectural Strengths (Path to Satisfaction)
- **Pluggable tool registry** — supports adding new tools per agent role (UMR-012, AAR-002)
   100|- **Connector architecture** — extensible to SharePoint, Confluence, SAP (UMR-051–054)
- **FastAPI async backend** — supports scaling and concurrent sessions (UMR-056, UMR-059)
- **PydanticAI agent framework** — supports multi-agent patterns, tool binding, structured output (UMR-011, AAR-001)
- **Structured JSON logging** — foundation for audit trail (UMR-027, UMR-062)
- **Git-versioned configuration** — foundation for config control (UMR-028)

### Critical Gaps Requiring New Subsystems
1. **Vector/embedding pipeline** — Azure AI Search available; chunking + indexing needed (UMR-003–006, 009–010)
2. **Confidence & grounding evaluation** — RAGAS or equivalent; Azure Foundry tools (UMR-007–010)
3. **HITL approval workflow** — approval queue, risk classification, reviewer UI (UMR-021–026)
    110|4. **Agent memory system** — PostgreSQL for all tiers, Redis optional later (UMR-014)
5. **Domain modules** — cost estimation, risk identification, anomaly detection, report generation (UMR-031–050)
6. **Guardrails & safety** — content filtering, loop detection, rate limiting (UMR-019–020, 029–030)