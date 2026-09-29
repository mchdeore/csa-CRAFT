# CRAFT Design Requirements Tabulation

_Source: CSA-SEFM-RD-0001 (UMR Document v1.5) and CRAFT-Req-Arch-Document-V3_

| Req ID | Type | Requirement Summary | Implementation Status | How Satisfied / Path to Satisfaction |
|--------|------|---------------------|----------------------|--------------------------------------|
| UMR-001 | Mandatory | Accept natural language queries in English and French | Partial | Chat interface accepts free-text queries via PydanticAI agent; French language detection not yet implemented. Add language detection middleware to satisfy. |
| UMR-002 | Mandatory | Retrieve documents with source citations | Partial | `DocumentSearchTool` and `TextAnalysisTool` retrieve files from local sources; citation format (document, page, section) not yet structured. Extend retrieval response schema to include provenance metadata. |
| UMR-003 | Mandatory | RAG pipeline with minimum 8192-token context window | Partial | Agent uses OpenAI-compatible model via PydanticAI with configurable context; no formal RAG chunking/embedding pipeline yet. Add vector store (pgvector) and chunk-aware retrieval to satisfy. |
| UMR-004 | Mandatory | Return top 5 ranked documents with cosine similarity ≥ 0.72 | Incomplete | No vector similarity search implemented. Requires embedding pipeline, vector store, and ranked retrieval with configurable threshold. COMMENT : tbr — more data and cases needed first |
| UMR-005 | Mandatory | Hybrid search: 0.7 semantic + 0.3 BM25 keyword | Incomplete | No hybrid search. Current search is file-name/path matching. Requires BM25 index + vector embeddings with fusion scoring. COMMENT : tbr — depends on UMR-004 |
| UMR-006 | Mandatory | Traceable source references (document, page, section) | Incomplete | Document reader returns text but no page/section locators. Requires chunk-level metadata preserved through ingestion. COMMENT : tbr — depends on UMR-004 |
| UMR-007 | Mandatory | Confidence score 0–1 for generated outputs | Incomplete | No confidence scoring. Requires evidence-coverage scoring module per V3 spec (not token probabilities). COMMENT : tbr — depends on UMR-004 |
| UMR-008 | Mandatory | Escalation when confidence < 0.6 | Incomplete | No escalation mechanism. Requires confidence scoring (UMR-007) + HITL routing (UMR-021). COMMENT : tbr — depends on UMR-004 |
| UMR-009 | Mandatory | Self-correction loop for retrieval refinement | Incomplete | No retrieval retry logic. Agent has retries=4 for LLM calls but no retrieval-specific refinement loop. COMMENT : tbr — depends on UMR-004 |
| UMR-010 | Mandatory | Faithfulness score ≥ 0.80 (grounding) | Incomplete | No grounding/faithfulness evaluation framework. Requires RAGAS or equivalent evaluation pipeline. COMMENT : tbr — depends on UMR-004 |
| UMR-011 | Mandatory | Multi-agent architecture with defined roles | Partial | Single PydanticAI agent with tool registry. Architecture supports adding specialized agents; delegation and accountability model not yet implemented per V3 revision. |
| UMR-012 | Mandatory | Agents operate only with permitted tools from registry | Partial | `tools/registry.py` exists and tools are registered per agent. Tool permission boundaries per role not enforced; version control of permissions not implemented. |
| UMR-013 | Mandatory | ReAct loop with max 10 reasoning steps per query | Partial | PydanticAI agent supports iterative reasoning; no explicit step counter or max-step enforcement. Add step-bounded execution loop. |
| UMR-014 | Mandatory | Three-tier agent memory: episodic, semantic, procedural | Incomplete | No memory tiers. Session state is ephemeral. Requires Redis/similar for episodic, vector store for semantic, workflow store for procedural. COMMENT : tbr — depends on UMR-004 |
| UMR-015 | Mandatory | Structured agent messages (id, action, input, output, confidence, timestamp) | Partial | Structured JSON logging with timestamps, route tracking, and tool_call_id exists; not yet a full inter-agent message schema with agent ID, action, input, output, confidence in one envelope. COMMENT : existing logging and routes provide foundation — extend to full protocol |
| UMR-016 | Mandatory | Agent spawning/termination without service interruption | Partial | FastAPI/Dash architecture supports independent request handling; no dynamic agent lifecycle management. |
| UMR-017 | Mandatory | Agents cannot access data outside authorized scope | Partial | Route-gated architecture with role-based permission checks (`_has_permission`, `_ROLE_ROUTES`) enforces 401/403 on protected routes. Per-agent tool-level RBAC not yet implemented. COMMENT : route gating already restricts what agents can access — extend to per-tool permissions |
| UMR-018 | Mandatory | Planning function decomposes complex requests into sub-tasks | Incomplete | No task decomposition. Single agent handles entire request. Requires planner agent with sub-task dispatch. COMMENT : tbr |
| UMR-019 | Mandatory | Loop detection: break after 3 repeated non-progressing actions | Incomplete | No loop detection logic. PydanticAI retries are for errors, not behavioral loops. COMMENT : tbr |
| UMR-020 | Mandatory | Guardrails prevent off-topic/harmful/policy-violating outputs | Incomplete | No guardrail layer. Relies on LLM system prompt only. Requires content filtering/guardrail middleware. COMMENT : tbr |
| UMR-021 | Mandatory | HITL approval for high-risk actions | Incomplete | No HITL approval workflow. Requires approval queue, risk classification, and reviewer routing. COMMENT : tbr |
| UMR-022 | Mandatory | HITL requests display reasoning chain, confidence, sources | Incomplete | No HITL UI. Requires approval interface showing agent reasoning trace. COMMENT : tbr |
| UMR-023 | Mandatory | Engineers can approve/reject/modify recommendations | Incomplete | No approval interface. Requires HITL review UI with approve/reject/modify actions. COMMENT : tbr |
| UMR-024 | Mandatory | Rejected recommendations trigger feedback re-planning | Incomplete | No feedback loop from human rejection. Requires agent re-planning on rejection. COMMENT : tbr |
| UMR-025 | Mandatory | HITL timeout after 24 hours, action cancelled and flagged | Incomplete | No HITL timeout mechanism. Requires approval queue with TTL. COMMENT : tbr |
| UMR-026 | Mandatory | HITL decisions logged with reviewer ID, decision, justification | Incomplete | No HITL decision logging. Requires audit log for approval actions. COMMENT : tbr |
| UMR-027 | Mandatory | Immutable audit log of agent actions and approvals | Partial | `app/core/logging.py` provides structured JSON logging with daily rotation. Not immutable (append-only with tamper detection not implemented). Extend with write-once audit store. |
| UMR-028 | Mandatory | Model weights and prompt templates version controlled | Partial | System prompt defined in code under git. Model config in `app/core/config.py`. No formal versioning/approval workflow for prompt changes. |
| UMR-029 | Mandatory | Agent actions reversible or support rollback | Incomplete | No rollback capability. Current tools are read-only (search, weather, charts) so low risk, but write actions would need undo support. COMMENT : tbr |
| UMR-030 | Mandatory | Rate limiting per agent (default 100 LLM calls/min) | Incomplete | No rate limiting. Requires per-agent/session/task rate limiter with configurable thresholds. |
| UMR-031 | Mandatory | Generate mission cost estimates from historical data | Incomplete | No cost estimation module. Requires historical mission database and parametric distance algorithm. |
| UMR-032 | Mandatory | Cost similarity via weighted normalized Euclidean distance | Incomplete | No similarity algorithm. Requires implementation of the distance formula with configurable weights. |
| UMR-033 | Mandatory | Retrieve 5 most similar historical missions | Incomplete | No historical mission database or similarity search. |
| UMR-034 | Mandatory | Cost estimates include confidence and source missions | Incomplete | No cost estimation pipeline. |
| UMR-035 | Mandatory | HITL approval before cost commitments | Incomplete | No HITL for financial actions. Depends on UMR-021. |
| UMR-036 | Goal | Identify and flag risks in mission documents | Incomplete | No risk identification module. Requires keyword + LLM classification pipeline. |
| UMR-037 | Mandatory | Risk function: keyword pattern matching + LLM classification | Incomplete | No risk analysis pipeline. |
| UMR-038 | Mandatory | Classify identified risks by severity | Incomplete | No risk classification. |
| UMR-039 | Mandatory | Risk register updates require HITL approval | Incomplete | No risk register or HITL integration. |
| UMR-040 | Mandatory | Risk outputs grounded in document evidence | Incomplete | No risk analysis pipeline. |
| UMR-041 | Mandatory | Detect anomalies in telemetry and system data | Incomplete | No telemetry ingestion or anomaly detection. |
| UMR-042 | Mandatory | Anomaly detection via Z-score threshold > 2.5 | Incomplete | No anomaly detection module. |
| UMR-043 | Mandatory | Retrieve similar historical anomaly cases | Incomplete | No anomaly knowledge base. |
| UMR-044 | Mandatory | High-severity anomalies trigger HITL review | Incomplete | No anomaly severity routing. |
| UMR-045 | Mandatory | Anomaly events and responses logged in audit trail | Incomplete | No anomaly logging. |
| UMR-046 | Mandatory | Generate bilingual reports using approved templates | Incomplete | No bilingual report generation. Requires template engine with EN/FR support. |
| UMR-047 | Mandatory | Reports compiled from approved internal sources | Incomplete | No report compilation from controlled sources. |
| UMR-048 | Mandatory | Narrative report sections grounded in retrieved evidence | Incomplete | No evidence-grounded report generation. |
| UMR-049 | Mandatory | Report drafts support engineer review before finalization | Incomplete | No report review workflow. |
| UMR-050 | Mandatory | Final reports versioned and logged | Incomplete | No report versioning. |
| UMR-051 | Mandatory | Integrate with existing CSA document repositories | Partial | `connectors/` module provides a pluggable data-source architecture with `local_files.py`. Extensible to SharePoint/Confluence with additional connector implementations. |
| UMR-052 | Mandatory | Connect to SharePoint and Confluence via APIs | Incomplete | Connector architecture exists but no SharePoint/Confluence implementations. |
| UMR-053 | Mandatory | Integration with CSA financial systems (SAP) | Incomplete | No SAP integration. Connector architecture supports adding it. |
| UMR-054 | Mandatory | Integration with mission design tools (STK, MATLAB) | Incomplete | No STK/MATLAB integration. |
| UMR-055 | Goal | REST and GraphQL interfaces for interoperability | Partial | FastAPI provides REST endpoints. No GraphQL layer. Add GraphQL schema to satisfy. |
| UMR-056 | Mandatory | Query response < 5 seconds for 90% of queries | Partial | Architecture supports fast responses; no performance benchmarking or SLA enforcement. Requires load testing and optimization. |
| UMR-057 | Mandatory | 99.5% availability during business hours | Incomplete | No HA deployment. Single-instance architecture. Requires redundancy, health checks, and monitoring. |
| UMR-058 | Mandatory | Protect sensitive data per CSA classification policy | Incomplete | No data classification enforcement. Auth module provides basic user authentication but no data-level access control. |
| UMR-059 | Mandatory | Support 500+ concurrent users | Incomplete | No load testing or horizontal scaling. FastAPI supports async but deployment not scaled. |
| UMR-060 | Mandatory | Every answer includes source references | Incomplete | Merged into UMR-006 in V3. Same status. |
| UMR-061 | Mandatory | Decision traceability reports (evidence, reasoning, confidence, approvals) | Incomplete | No decision traceability reporting. Logging exists but not structured for decision reconstruction. |
| UMR-062 | Mandatory | Audit reports with timestamped history of system activities | Partial | JSON logging captures requests and tool calls with timestamps. Not yet exportable as audit reports. Extend with reporting UI and export capability. |

## Agentic AI Requirements — Agent Architecture (AAR)

| Req ID | Type | Requirement Summary | Implementation Status | How Satisfied / Path to Satisfaction |
|--------|------|---------------------|----------------------|--------------------------------------|
| AAR-001 | Mandatory | Multi-agent architecture, each agent with one defined role | Partial | Single PydanticAI agent exists. Architecture supports adding role-specific agents. Implement orchestrator + specialist agent pattern. |
| AAR-002 | Mandatory | Agents use only permitted tools from Tool Registry | Partial | Tool registry exists (`tools/registry.py`). Tools registered per agent type. Per-agent permission enforcement not yet implemented. |
| AAR-003 | Mandatory | Orchestrator: ReAct workflow, max 10 reasoning steps | Incomplete | No orchestrator with step-bounded ReAct loop. PydanticAI agent runs unbounded. |
| AAR-004 | Mandatory | Three-tier memory: episodic, semantic, procedural | Incomplete | No memory system. Same as UMR-014. |
| AAR-005 | Mandatory | Structured messages: agent ID, action, input, output, confidence, timestamp | Incomplete | No structured inter-agent message format. Same as UMR-015. |
| AAR-006 | Mandatory | Agent spawning/termination without platform interruption | Partial | FastAPI process model supports independent handling. No dynamic agent lifecycle. Same as UMR-016. |
| AAR-007 | Mandatory | Agent permission boundaries enforced | Incomplete | No per-agent permission enforcement. Same as UMR-017. |

## Agentic AI Requirements — Agent Reasoning (ARR)

| Req ID | Type | Requirement Summary | Implementation Status | How Satisfied / Path to Satisfaction |
|--------|------|---------------------|----------------------|--------------------------------------|
| ARR-001 | Mandatory | Planning function decomposes requests into sub-tasks | Incomplete | No planner. Same as UMR-018. |
| ARR-002 | Mandatory | Hybrid search: 0.7 semantic + 0.3 BM25 | Incomplete | Same as UMR-005. |
| ARR-003 | Mandatory | Cite every source by document ID, page, section | Incomplete | Same as UMR-006. |
| ARR-004 | Mandatory | Confidence score 0–1 per agent output | Incomplete | Same as UMR-007. |
| ARR-005 | Mandatory | Escalation when confidence < 0.6 | Incomplete | Same as UMR-008. |
| ARR-006 | Mandatory | Self-correction loop for retrieval refinement | Incomplete | Same as UMR-009. |
| ARR-007 | Mandatory | Grounding with faithfulness ≥ 0.80 | Incomplete | Same as UMR-010. |

## Human-in-the-Loop Requirements (HITL)

| Req ID | Type | Requirement Summary | Implementation Status | How Satisfied / Path to Satisfaction |
|--------|------|---------------------|----------------------|--------------------------------------|
| HITL-001 | Mandatory | Mandatory HITL approval gates for high-risk actions | Incomplete | No approval workflow. Requires risk-tier classification + approval queue. |
| HITL-002 | Mandatory | High-risk: cost commitments, risk register updates, mission parameter changes | Incomplete | No risk classification of actions. |
| HITL-003 | Mandatory | HITL requests show reasoning chain, confidence, sources | Incomplete | No HITL UI. Same as UMR-022. |
| HITL-004 | Mandatory | Engineers can approve/reject/modify recommendations | Incomplete | Same as UMR-023. |
| HITL-005 | Mandatory | Rejected recommendations trigger agent re-planning with correction | Incomplete | Same as UMR-024. |
| HITL-006 | Mandatory | HITL timeout after 24 hours; action cancelled and flagged | Incomplete | Same as UMR-025. |
| HITL-007 | Mandatory | HITL decisions logged with reviewer ID, decision, timestamp, justification | Incomplete | Same as UMR-026. |

## Agentic AI Safety and Governance (ASG)

| Req ID | Type | Requirement Summary | Implementation Status | How Satisfied / Path to Satisfaction |
|--------|------|---------------------|----------------------|--------------------------------------|
| ASG-001 | Mandatory | Guardrails prevent off-topic/harmful/policy-violating content | Incomplete | Same as UMR-020. |
| ASG-002 | Mandatory | Agent actions reversible or support rollback | Incomplete | Same as UMR-029. Current tools are read-only. |
| ASG-003 | Mandatory | Immutable audit log of all agent decisions and actions | Partial | Structured logging exists. Not yet immutable (no append-only/tamper-detection). |
| ASG-004 | Mandatory | Rate limiting: 100 LLM calls/agent/minute default | Incomplete | Same as UMR-030. |
| ASG-005 | Mandatory | Loop detection: break after 3 repeated non-progressing actions | Incomplete | Same as UMR-019. |
| ASG-006 | Mandatory | Model weights, prompts, configs version controlled before deployment | Partial | Code is git-versioned. No formal review/approval gate for prompt changes in deployment pipeline. |

---

## Summary

| Category | Total | Satisfied/Partial | Incomplete |
|----------|-------|-------------------|------------|
| UMR (Functional) | 62 | 16 partial | 46 |
| AAR (Agent Architecture) | 7 | 3 partial | 4 |
| ARR (Agent Reasoning) | 7 | 0 | 7 |
| HITL (Human-in-the-Loop) | 7 | 0 | 7 |
| ASG (Safety & Governance) | 6 | 2 partial | 4 |
| **Total** | **89** | **21 partial** | **68** |

### Key Architectural Strengths (Path to Satisfaction)
- **Pluggable tool registry** — supports adding new tools per agent role (UMR-012, AAR-002)
- **Connector architecture** — extensible to SharePoint, Confluence, SAP (UMR-051–054)
- **FastAPI async backend** — supports scaling and concurrent sessions (UMR-056, UMR-059)
- **PydanticAI agent framework** — supports multi-agent patterns, tool binding, structured output (UMR-011, AAR-001)
- **Structured JSON logging** — foundation for audit trail (UMR-027, UMR-062, ASG-003)
- **Git-versioned configuration** — foundation for config control (UMR-028, ASG-006)

### Critical Gaps Requiring New Subsystems
1. **Vector/embedding pipeline** — pgvector + BM25 hybrid search (UMR-003–005, ARR-002)
2. **Confidence & grounding evaluation** — RAGAS or equivalent (UMR-007, UMR-010, ARR-004, ARR-007)
3. **HITL approval workflow** — approval queue, risk classification, reviewer UI (UMR-021–026, HITL-001–007)
4. **Agent memory system** — Redis episodic + vector semantic + workflow procedural (UMR-014, AAR-004)
5. **Domain modules** — cost estimation, risk identification, anomaly detection, report generation (UMR-031–050)
6. **Guardrails & safety** — content filtering, loop detection, rate limiting (UMR-019–020, ASG-001–005)
