<!-- PDF page 1 -->

CSA-CRAFT-RD-0001
CRAFT — Collaborative Reasoning and Federated
Technical Knowledge
User and Functional Requirements Document
Version Draft P1
Jun. 1, 2026
LiveLink
RESTRICTION ON USE, PUBLICATION OR DISCLOSURE OF PROPRIETARY INFORMATION
This document and the information contained herein are subject to proprietary rights belonging to the Government of Canada or to a
third party and are to be used only for the purpose of fulfilling the receiving Gateway Partner's or its Related Entities' responsibilities
for the Lunar Gateway under the relevant international agreements. The use of this document or any information contained herein
for any other purpose, and any disclosure or retransfer of this document to any person or entity other than the receiving Gateway
Partner and its Related Entities, are expressly prohibited without the written permission of the Government of Canada, acting
through the Canadian Space Agency.
© HIS MAJESTY THE KING IN RIGHT OF CANADA 2022

---

<!-- PDF page 2 -->

CSA-SEFM-RD-001 Version 1.5 Draft
2
This page Left intentionally blank

---

<!-- PDF page 3 -->

CSA-SEFM-RD-001 Version 1.5 Draft
3
# APPROVALS
This document and all changes to it shall be approved by the appropriate Canadian Space Agency
authority in accordance with CSA configuration management and document control practice. Proposed
changes to the currently approved baselined version of this document shall be forwarded to the CSA
Configuration Management receipt desk, or equivalent designated authority, for evaluation and
submission for approval. Approved changes shall be incorporated in the next revision.
Role Name Signature Date
Prepared By H. Fawzy, Senior
Systems Engineer, SU
Reviewed By M. Bedirian, Senior
Systems Engineer,
CSA FIN
Reviewed By J-F. Cusson, Senior
Engineer (Electrical),
SS&T
Recommended By G. Brassard, SM, SU
Recommended By M. Doyon, Eng. M,
SS&T
Recommended By E. Villeux, CSA Fin.
Approved By M. Bergeron, SESS
Dir, SU
Approved By CIO?
Formatted: French (Canada)

---

<!-- PDF page 4 -->

CSA-SEFM-RD-001 Version 1.5 Draft
4
# REVISION HISTORY
Rev. Description Initials Date
1.0 Initial draft. HF 2026-05-10
1.1 Updated intern proposal
structure and CRAFT
scope.
HF 2026-05-21
1.2 Added use cases,
definitions, and
traceability matrix.
HF 2026-06-01
1.3 Added Agentic AI
requirements and
mapped them to use
cases.
HF 2026-06-02
1.5 Added dedicated
Section 4.2 Agentic AI
Requirements.
HF 2026-06-02

---

<!-- PDF page 5 -->

CSA-SEFM-RD-001 Version 1.5 Draft
5
1 INTRODUCTION
1.1 BACKGROUND
CSA systems engineering activities increasingly depend on access to distributed technical knowledge,
internal standards, historical mission information, engineering analysis artefacts, risk records, and cost
information. The current environment is fragmented across repositories, document stores, discipline tools,
and organizational boundaries, which slows engineering work and reduces the efficiency of knowledge
reuse. The CRAFT platform is intended to address that problem through a production-grade Agentic-
RAG environment for engineering support, not as a pure research exercise.
CRAFT combines Large Language Model capabilities with a federated knowledge base containing CSA
internal documents, standards, and historical data. It introduces autonomous AI agents able to plan,
reason, retrieve information, synthesize grounded answers, support engineering workflows, and maintain
auditable records of their actions.
1.2 PURPOSE
CRAFT is intended to provide CSA engineers and other authorized users with a secure and traceable
platform that can query technical knowledge, support cost estimation, identify risks, detect anomalies, and
generate bilingual engineering reports. This document provides the initial user and functional
requirements specification for CRAFT from the viewpoint of its operational users and stakeholders.
1.3 SCOPE
This document applies to CRAFT as a production platform supporting systems engineering activities
inside CSA, including document management, risk assessment, cost estimation, anomaly detection,
mission planning support, and report generation. The platform is based on an Agentic-RAG architecture
using autonomous agents, retrieval components, orchestration services, memory services, local and
external LLM inference, and integration with CSA enterprise repositories and engineering tools.
1.4 CHANGE AUTHORITY / RESPONSIBILITY
Proposed changes to this document shall be submitted through the applicable CSA configuration
management and technical authority process for consideration and disposition. The baselined version of
this document shall be controlled, and approved changes shall be incorporated into the next authorized
revision.
1.5 CONVENTION AND NOTIFICATION
The requirement verbs in this document shall be interpreted as follows: "shall" indicates a binding
requirement that must be implemented and verified; "should" indicates a desirable goal or good practice;
"may" indicates permission; "will" indicates a statement of fact or declared intent; and "is/are" indicates
descriptive information. Rationales are included to provide clarification, justification, or purpose, but in
the event of inconsistency, the requirement statement takes precedence over the rationale.

---

<!-- PDF page 6 -->

CSA-SEFM-RD-001 Version 1.5 Draft
6
2 DOCUMENTS
2.1 PARENT DOCUMENTS
No parent document has been explicitly identified in the current document draft.
2.2 APPLICABLE DOCUMENTS
ID Document Title Reference
AD-01 CSA-SE-PR-0001 Systems Engineering Methods and Practices
AD-02 Responsible use of artificial
intelligence in government
[https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html)
AD-03 NASA Systems Engineering
Handbook
NASA/SP-2016-6105 Rev2
AD-04 ECSS Systems Engineering
Standard
ECSS-E-ST-10C
AD-05 CSA Data Classification Policy CSA-SEC-POL-003
AD-06 Directive on Automated
Decision-Making
[https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592)
AD-07 AI governance principles [https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/principles.html](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/principles.html)
AD-08 Technology Readiness and Risk
Assessment Guidelines
CSA-ST-GDL-0001
2.3 REFERENCE DOCUMENTS
ID Document Title Reference
RD-01 CRAFT Architecture Design Document (TBD) TBD
RD-02 CRAFT Intern Proposal v1.2 NA
RD-03 Systems Engineering Mission Tailoring Guidelines CSA-SE-GDL-0001

---

<!-- PDF page 7 -->

CSA-SEFM-RD-001 Version 1.5 Draft
7
3 CRAFT CONCEPT DESCRIPTION
3.1 CRAFT OBJECTIVES
CRAFT objectives are to provide CSA with a secure and auditable platform where authorized users can
discover, retrieve, analyze, and use technical knowledge and engineering data through natural language
and structured workflows. The platform shall support engineering decision-making by enabling access to
federated documents, technical standards, historical mission records, cost data, telemetry-derived signals,
and governance-controlled AI assistance.
3.2 CONCEPT OF OPERATIONS
CRAFT will ingest documents from CSA repositories and other relevant engineering sources, extract
structured content, generate embeddings, and maintain searchable vector and graph representations of the
knowledge base. Authorized users will interact with the system through a user interface and APIs, using
natural language queries or structured input forms for specific workflows.
When a user submits a request, the platform will route that request through agent orchestration services
that can decompose the task, retrieve relevant evidence, synthesize an answer, calculate confidence, and
either respond directly or escalate to human review if the action or conclusion is high-risk or low
confidence.
3.3 CRAFT PLATFORM USERS
CRAFT users include CSA systems engineers, Subject Matter Experts, finance engineers, risk managers,
operations engineers, mission control personnel, project managers, technical authorities, and governance
reviewers.
User
Category
Status Definition Notes
Admin Implemented
Users responsible
for CRAFT
administration and
platform support.
Corresponds to CIO team administration functions.
Employees Implemented
Users responsible
for operational,
expert, and
oversight use of
CRAFT.
Expert users are treated as equivalent to oversight users in
this version.
Executives Future
Users who need
executive-level
access to approved
outputs and
summaries.
Not implemented in this version.

---

<!-- PDF page 8 -->

CSA-SEFM-RD-001 Version 1.5 Draft
8
4 USER AND FUNCTIONAL REQUIREMENTS
4.1 FUNCTIONAL REQUIREMENTS
ID Type Requirement Rationale
UMR-001 Mandatory CRAFT shall enable engineers to query the
technical knowledge base in natural
language in English and French.
Supports day-to-day
engineering work
through direct access
to federated
knowledge.
UMR-002 Mandatory CRAFT shall retrieve relevant documents
and present results with source citations.
Traceable retrieval is
central to trust,
explainability, and
engineering
verification.
UMR-003 Mandatory CRAFT shall implement a Retrieval-
Augmented Generation pipeline with a
minimum context window of 8192 tokens.
Provides sufficient
grounded context for
synthesis.
UMR-004 Mandatory CRAFT shall return the top five ranked
documents with cosine similarity score
greater than or equal to 0.72.
Controls retrieval
quality.
UMR-005 Mandatory The retrieval function shall perform hybrid
search combining semantic similarity and
BM25 keyword relevance with a default
weighting of 0.7 semantic and 0.3
keyword.
Balances semantic and
lexical retrieval.
UMR-006 Mandatory Every synthesized answer shall include
traceable source references identifying
document, page, and section where
applicable.
Required for
auditability and
explainability.
UMR-007 Mandatory CRAFT shall calculate and expose a
confidence score between 0 and 1 for
generated outputs.
Confidence supports
escalation and review.
UMR-008 Mandatory Outputs with confidence lower than 0.6
shall trigger escalation to a human reviewer
or subject matter expert.
Low-confidence
outputs shall not be
treated as final
engineering advice.
UMR-009 Mandatory CRAFT shall implement a self-correction
loop allowing retrieval refinement when
initial evidence is insufficient.
Improves retrieval
completeness before
escalation.
UMR-010 Mandatory Generated answers shall be grounded in
retrieved context and shall achieve a
faithfulness score of at least 0.80 using the
selected evaluation framework.
Controls hallucination
risk in engineering use.
UMR-011 Mandatory CRAFT shall implement a multi-agent
architecture in which each agent has one
defined role and responsibility.
Role separation
reduces ambiguity and
supports governance.
UMR-012 Mandatory Each agent shall operate only with its
permitted tools from the tool registry.
Controls scope and
unauthorized action.

---

<!-- PDF page 9 -->

CSA-SEFM-RD-001 Version 1.5 Draft
9
UMR-013 Mandatory The agent orchestrator shall implement a
ReAct loop with a maximum of 10
reasoning steps per query before escalation.
Limits uncontrolled
chains and runtime
cost.
UMR-014 Mandatory CRAFT shall maintain three tiers of agent
memory: episodic, semantic, and
procedural.
Supports continuity,
knowledge reuse, and
workflow learning.
UMR-015 Mandatory Agents shall exchange structured messages
containing agent identifier, action type,
input, output, confidence score, and
timestamp.
Needed for
orchestration control
and audit.
UMR-016 Mandatory CRAFT shall support agent spawning and
termination without service interruption.
Supports availability
and scaling.
UMR-017 Mandatory Agents shall not access data or system
functions outside their authorized scope.
Core data protection
and governance
requirement.
UMR-018 Mandatory The planning function shall decompose
complex user requests into sub-tasks before
dispatching them to specialist agents.
Enables multi-step
workflows.
UMR-019 Mandatory CRAFT shall detect repetitive non-
progressing agent behavior and break the
loop when the same action repeats three
times without progress.
Prevents runaway
loops.
UMR-020 Mandatory CRAFT shall apply guardrails that prevent
off-topic, harmful, or policy-violating agent
outputs.
Supports AI
governance and safe
operation.
UMR-021 Mandatory CRAFT shall require Human-in-the-Loop
approval for actions classified as high-risk.
Protects high-impact
engineering decisions.
UMR-022 Mandatory HITL approval requests shall display the
agent reasoning chain, confidence score,
and source documents used.
Reviewers need
evidence to decide.
UMR-023 Mandatory Authorized engineers shall be able to
approve, reject, or modify agent
recommendations before commitment.
Keeps human authority
in control.
UMR-024 Mandatory Rejected recommendations shall trigger a
feedback loop allowing the agent to re-plan
using the engineer correction.
Supports corrective
iteration.
UMR-025 Mandatory HITL approval requests shall time out after
24 hours if no response is received, and the
requested action shall be cancelled and
flagged for review.
Controls latent pending
actions.
UMR-026 Mandatory All HITL decisions shall be logged with
engineer identifier, decision, and
justification text.
Approval traceability
is required.
UMR-027 Mandatory CRAFT shall maintain an immutable audit
log of agent actions and approval decisions.
Log integrity is
required for
governance.
UMR-028 Mandatory Agent model weights and prompt templates
shall be version controlled and reviewed
before deployment.
Supports controlled
configuration.

---

<!-- PDF page 10 -->

CSA-SEFM-RD-001 Version 1.5 Draft
10
UMR-029 Mandatory Where technically feasible, agent actions
shall be reversible or support rollback.
Limits damage from
incorrect actions.
UMR-030 Mandatory CRAFT shall apply rate limiting per agent,
with a default maximum of 100 LLM calls
per agent per minute.
Protects runtime
stability.
UMR-031 Mandatory CRAFT shall generate mission cost
estimates from historical data.
Supports engineering
and finance planning.
UMR-032 Mandatory Cost similarity matching shall use a
weighted normalized Euclidean distance
method.
Defines the estimation
approach.
UMR-033 Mandatory The platform shall retrieve the five most
similar historical missions for a candidate
estimate.
Provides evidence for
estimates.
UMR-034 Mandatory Cost estimation outputs shall include
confidence information and the source
missions used in the estimate.
Supports reviewer
validation.
UMR-035 Mandatory Any estimate associated with a financial
commitment or baseline decision shall
require Human-in-the-Loop approval
before use.
Protects high-risk
commitments.
UMR-036 Goal CRAFT shall identify and flag risks in
mission documents.
Need to specify the risk
standards supporting
proactive engineering
risk management.
UMR-037 Mandatory The risk function shall use keyword pattern
matching combined with LLM-based
classification.
Defines the risk
identification method.
UMR-038 Mandatory Identified risks shall be classified by
severity.
Supports triage and
governance.
UMR-039 Mandatory Proposed updates to the risk register shall
require Human-in-the-Loop approval
before commitment.
Protects controlled risk
records.
UMR-040 Mandatory Risk outputs shall remain grounded in the
document evidence from which they were
derived.
Controls hallucination
in risk classification.
UMR-041 Mandatory CRAFT shall detect anomalies in telemetry
and system data.
Supports operational
monitoring.
UMR-042 Mandatory The anomaly detection function shall use a
Z-score threshold greater than 2.5 unless
otherwise configured.
Defines the default
anomaly threshold.
UMR-043 Mandatory The anomaly agent shall retrieve similar
historical anomaly cases from the
knowledge base.
Improves diagnosis
and context.
UMR-044 Mandatory High-severity anomalies shall trigger
Human-in-the-Loop acknowledgement or
review.
Protects operations
decisions.
UMR-045 Mandatory All anomaly events and user responses
shall be logged in the audit trail.
Maintains event
traceability.
UMR-046 Mandatory CRAFT shall generate bilingual reports
using approved templates.
Supports CSA
reporting requirements.

---

<!-- PDF page 11 -->

CSA-SEFM-RD-001 Version 1.5 Draft
11
UMR-047 Mandatory The reporting function shall compile data
from approved internal sources including
databases, registers, and retrieved
documents.
Ensures reports use
controlled sources.
UMR-048 Mandatory Narrative report sections shall be grounded
in retrieved evidence and identified source
data.
Prevents fabricated
report content.
UMR-049 Mandatory Report drafts shall support engineer review
before finalization.
Maintains human
review authority.
UMR-050 Mandatory Final reports shall be versioned and logged. Supports document
control.
UMR-051 Mandatory CRAFT shall integrate with existing CSA
document repositories.
Core operational
integration need.
UMR-052 Mandatory CRAFT shall connect to SharePoint and
Confluence through supported APIs.
Implements repository
integration.
UMR-053 Mandatory CRAFT shall support integration with CSA
financial systems such as SAP for cost-
related workflows where authorized.
Supports cost
workflows.
UMR-054 Mandatory CRAFT shall support integration with
mission design and analysis tools such as
STK and MATLAB where operationally
required.
Supports engineering
workflow continuity.
UMR-055 Goal CRAFT should expose approved functions
through REST and GraphQL interfaces to
support controlled interoperability.
Improves
interoperability.
UMR-056 Mandatory CRAFT shall respond to user queries in
less than 5 seconds for 90 percent of
queries under nominal operating
conditions.
Defines performance
target.
UMR-057 Mandatory CRAFT shall provide 99.5 percent
availability during CSA business hours.
Defines availability
target.
UMR-058 Mandatory CRAFT shall protect sensitive CSA data in
accordance with the applicable CSA data
classification policy for the deployment
scope.
Protects sensitive
information.
UMR-059 Mandatory CRAFT shall support at least 500
concurrent users as additional directorates
adopt the platform.
Defines scalability
target.
UMR-060 Mandatory Every final user-facing answer shall
include source references sufficient to
explain the basis of the output.
Defines explainability
requirement.
UMR-061 Mandatory CRAFT shall generate and maintain
decision traceability reports that record the
evidence sources consulted, reasoning
outputs produced, confidence levels
assigned, and human approvals or
rejections associated with
recommendations and decisions.
Supports auditability,
explainability, and
reconstruction of the
decision-making
process. It defines
when reporting is
required
(medium/high-risk
decisions) and what

---

<!-- PDF page 12 -->

CSA-SEFM-RD-001 Version 1.5 Draft
12
information must be
captured.
UMR-062 Mandatory CRAFT shall provide authorized users with
the ability to retrieve and export audit
reports containing a time-stamped history
of significant system activities, including
user requests, agent actions, data sources
accessed, recommendations generated,
decisions taken, and subsequent
modifications. Supports governance,
compliance reviews, lessons learned
activities, and post-decision investigations.
Supports UMR-061
and implement the
reporting capabilities.
It defines who can
access the reports
(authorized users),
what outputs are
expected (exportable
reports), and ties
retention to an external
governing policy rather
than an arbitrary
duration.
4.2 AGENTIC AI REQUIREMENTS
This section defines the specific requirements applicable to the Agentic AI functions of CRAFT. These
requirements apply to autonomous agents, agent orchestration, agent memory, reasoning control, Human-
in-the-Loop review mechanisms, and the safety and governance controls required for operational use
within CSA. In the event of inconsistency between this section and supporting use cases or rationale text,
the requirement statements in this section shall take precedence.
4.2.1 AGENT ARCHITECTURE REQUIREMENTS
The following requirements define the baseline architectural constraints for agent roles, orchestration
behavior, memory structure, message exchange, lifecycle management, and permission boundaries.
Tag Nature of the
Requirement
Requirement Rationale
AAR-001 Mandatory CRAFT shall implement a multi-agent
architecture in which each agent has one
defined role and responsibility.
Clear role separation
reduces ambiguity,
improves control, and
supports verification of
agent behavior.
AAR-002 Mandatory Each agent shall operate with a defined set
of permitted tools from the approved Tool
Registry, and no agent shall access tools
outside its permitted set.
Tool restriction is
required to prevent
unauthorized action and
reduce operational risk.
AAR-003 Mandatory The Agent Orchestrator shall implement a
Reasoning and Acting workflow with a
maximum of 10 reasoning steps per user
request before escalation or termination.
A bounded reasoning
cycle is required to
control runtime cost,
failure propagation, and
runaway execution.
AAR-004 Mandatory CRAFT shall implement agent memory
using three tiers: episodic memory for
current-session context, semantic memory
for persistent knowledge, and procedural
memory for learned workflows.
Tiered memory
supports continuity,
retrieval efficiency, and
controlled reuse of prior
operational knowledge.
AAR-005 Mandatory Agents shall communicate using a
structured message format containing, at a
minimum, agent identifier, action type,
Structured messaging is
required for
orchestration,

---

<!-- PDF page 13 -->

CSA-SEFM-RD-001 Version 1.5 Draft
13
input, output, confidence score, and
timestamp.
traceability, and
auditability.
AAR-006 Mandatory CRAFT shall support agent spawning and
termination without interruption to the
availability of the platform.
Agent lifecycle
flexibility is required
for scaling and
operational resilience.
AAR-007 Mandatory CRAFT shall enforce agent permission
boundaries such that no agent may modify
system configuration or access data
outside its authorized scope.
Permission boundaries
are required to protect
system integrity and
sensitive CSA
information.
4.2.2 AGENT REASONING REQUIREMENTS
The following requirements define how CRAFT agents shall decompose tasks, retrieve evidence, generate
grounded outputs, calculate confidence, and refine retrieval when the initial context is insufficient.
Tag Nature of the
Requirement
Requirement Rationale
ARR-001 Mandatory The planning function shall decompose
complex user requests into sub-tasks
before dispatch to specialist agents.
Task decomposition is
required for multi-step
workflows and
controlled
specialization.
ARR-002 Mandatory The retrieval function shall perform
hybrid search combining semantic
similarity and BM25 keyword relevance,
with a default weighting of 0.7 semantic
and 0.3 keyword unless otherwise
configured.
Hybrid retrieval
improves robustness
across natural language
and domain-specific
terminology.
ARR-003 Mandatory The synthesis function shall cite every
source used in a generated answer by
document identifier and, where available,
page number and section reference.
Source traceability is
required for
explainability and
engineering
verification.
ARR-004 Mandatory Each agent shall calculate and report a
confidence score between 0 and 1 for its
output.
Confidence scoring
supports review,
escalation, and
operational trust.
ARR-005 Mandatory Outputs with confidence lower than 0.6
shall trigger escalation to a human
reviewer or subject matter expert.
Low-confidence outputs
shall not be treated as
authoritative
operational guidance.
ARR-006 Mandatory CRAFT shall implement a self-
correction loop permitting agents to re-
query or refine parameters when the
initial retrieval does not provide
sufficient context.
Refinement is required
to improve evidence
completeness before
escalation.
ARR-007 Mandatory All generated content shall be grounded
in retrieved context and shall achieve a
faithfulness score of at least 0.80 using
the approved evaluation framework.
Grounding and
faithfulness controls are
required to limit
hallucination risk.

---

<!-- PDF page 14 -->

CSA-SEFM-RD-001 Version 1.5 Draft
14
4.2.3 HUMAN-IN-THE-LOOP REQUIREMENTS
The following requirements define the controls by which authorized CSA personnel shall review,
approve, reject, or modify agent-generated recommendations before high-risk actions are committed.
Tag Nature of the
Requirement
Requirement Rationale
HITL-001 Mandatory CRAFT shall implement mandatory
Human-in-the-Loop approval gates for
actions classified as high-risk.
High-impact actions
require explicit human
authority before
execution or
commitment.
HITL-002 Mandatory High-risk actions shall include, at a
minimum, cost commitments, risk
register updates, and mission parameter
changes.
These actions can
materially affect
engineering,
operational, or
governance outcomes.
HITL-003 Mandatory HITL approval requests shall display the
reasoning chain, confidence score, and
source documents used by the agent.
Reviewers require
visibility into the basis
of the recommendation
to make an informed
decision.
HITL-004 Mandatory Authorized engineers shall be able to
approve, reject, or modify any agent
recommendation before it is committed
to the system.
Human reviewers must
retain final authority
over controlled actions.
HITL-005 Mandatory Rejected agent recommendations shall
trigger a feedback loop in which the
agent re-plans using the reviewer
correction where such correction is
provided.
This supports
correction, learning, and
controlled iteration.
HITL-006 Mandatory HITL approval requests shall time out
after 24 hours if no disposition is
provided, and the requested action shall
be cancelled and flagged for review.
Timeout behaviour is
required to prevent
indefinite pending high-
risk actions.
HITL-007 Mandatory All HITL decisions, including approval,
rejection, and modification, shall be
logged with reviewer identifier, decision,
timestamp, and justification text.
Full decision
traceability is required
for governance and
audit.
4.2.4 AGENTIC AI SAFETY AND GOVERNANCE REQUIREMENTS
The following requirements define the safety, control, audit, rollback, rate-limiting, and configuration-
management obligations applicable to the CRAFT agentic AI environment.
Tag Nature of the
Requirement
Requirement Rationale
ASG-001 Mandatory CRAFT shall implement agent guardrails
that prevent agents from generating
content that is off-topic, harmful, or in
violation of CSA data policy.
Guardrails are required
for safe and policy-
compliant operational
use.

---

<!-- PDF page 15 -->

CSA-SEFM-RD-001 Version 1.5 Draft
15
ASG-002 Mandatory Where technically feasible, all agent
actions shall be reversible or shall
support rollback capability.
Reversibility limits the
impact of incorrect or
premature actions.
ASG-003 Mandatory CRAFT shall maintain an immutable
audit log of all agent decisions and agent
actions, and audit entries shall not be
modifiable or deletable through normal
system operations.
Immutable audit
logging is required for
governance, incident
review, and compliance.
ASG-004 Mandatory CRAFT shall implement rate limiting
per agent, with a default maximum of
100 LLM calls per agent per minute
unless otherwise approved and
configured.
Rate limiting is required
to control resource
consumption and
prevent runaway
execution.
ASG-005 Mandatory CRAFT shall detect repetitive non-
progressing agent behaviour and shall
break the loop if the same action is
repeated three times without progress,
after which the workflow shall be
escalated or terminated.
Loop detection is
required to prevent
ineffective or unsafe
repeated execution.
ASG-006 Mandatory Agent model weights, prompt templates,
and equivalent operational inference
configurations shall be version
controlled, reviewed, and approved
before deployment to production.
Configuration control is
required to maintain
reproducibility,
traceability, and
governance discipline.

---

<!-- PDF page 16 -->

CSA-SEFM-RD-001 Version 1.5 Draft
16
APPENDIX A—USER ROLE DEFINITIONS,
OPERATIONAL ASSUMPTIONS, RISK AND MITIGATION,
# AND INITIAL ON-PREMISES INFRASTRUCTURE ROM
Purpose. This appendix is provided as a standalone draft appendix for the CRAFT requirements package.
It defines the current user role structure, records operational assumptions, summarizes key risks and
mitigations, and provides a rough-order-of-magnitude (ROM) estimate for an initial on-premises
deployment. The ROM values are indicative planning figures only and shall not be treated as final design
values. Final architecture, hardware counts, storage capacity, GPU allocation, resiliency design, and
network sizing shall be defined and controlled in the CRAFT Architecture Design Document (RD-01).
A.1 User Role Definitions
User
Category
Status in Current
Version
Definition Primary
Responsibilities
Access Scope
Admin Implemented Administrative users
responsible for
platform
administration and
support,
corresponding to
CIO team functions
or equivalent
authorized
administrators.
User and
permission
administration;
configuration
management;
monitoring;
logging review;
integration
support;
operational
continuity.
Administrative
access limited to
approved
platform
administration
functions and
subject to audit
and security
control.
Employees Implemented Authorized CSA
personnel using
CRAFT for
operational,
analytical,
engineering, and
oversight activities.
This category
includes both
operational users and
expert users; for this
version, expert users
are treated as
equivalent to
oversight users.
Query technical
knowledge;
review retrieved
evidence;
perform
engineering
analysis; review
and disposition
recommendations
where
authorized.
Role-based
access to
approved tools,
documents, and
review functions
in accordance
with need-to-
know and
security
controls.
Executives Not implemented
in current version
Senior stakeholders
requiring executive-
level summaries,
dashboards, or
approved outputs for
governance and
decision support.
Review approved
outputs and
summary
information for
decision support.
Not in scope for
the current
version; to be
defined in a
future revision.

---

<!-- PDF page 17 -->

CSA-SEFM-RD-001 Version 1.5 Draft
17
A.2 Operational Assumptions
Assumption
ID
Operational Assumption Basis
OA-01 The current implementation baseline supports
Admin and Employees only; Executive user
functions are deferred to a future revision.
Section 3.3 revision direction
and current system scope.
OA-02 CRAFT is intended to operate as a production
platform for CSA engineering support rather
than as a research prototype.
Section 1 purpose and scope.
OA-03 The platform target availability is 99.5 percent
during CSA business hours.
UR-NF02 and KPI-06.
OA-04 This standalone Appendix A uses an initial
planning assumption of up to 50 concurrent
users for first deployment sizing. This does not
supersede the formal scalability requirement in
the main requirements document.
Initial deployment ROM
planning assumption; main
document UR-NF04 remains
separate until formally
revised.
OA-05 The platform processes information at the
deployment tier stated in the current draft
baseline and enforces data protection controls
accordingly.
UR-NF03 and related
governance controls.
OA-06 Human-in-the-Loop approval remains
mandatory for high-risk actions.
SR-F08 and Section 4.2.3.
OA-07 Workflow-specific user categorization is
excluded from the current version.
Requested Section 3.3
change.
OA-08 The platform interfaces with existing enterprise
systems including SharePoint, Confluence,
SAP, STK, and MATLAB.
Section 2.3 system boundary.
OA_09 Capability to generate a report providing details
of the process leading to a decision (audit).
UMR-031 and UMR-032
(New requirements.)
A.3 Risk and Mitigation
Risk ID Risk Description Probability Impact Mitigation
AR-01 LLM-generated
technical outputs may
be incorrect or
insufficiently grounded.
Medium High Enforce
grounding and
faithfulness
controls, source
citation, and
confidence-
based escalation.
AR-02 Agents may attempt
actions outside their
authorized scope.
Low High Enforce tool
permission
boundaries, role
restrictions, and
immutable audit
logging.
AR-03 Runaway loops or
excessive inference
calls may consume
Low Medium Apply per-agent
rate limiting,
loop detection,
and escalation or

---

<!-- PDF page 18 -->

CSA-SEFM-RD-001 Version 1.5 Draft
18
local infrastructure
resources.
termination
rules.
AR-04 Human review queues
may delay operational
decisions.
Medium Medium Apply timeout
handling,
escalation rules,
and role-based
review routing.
AR-05 Sensitive information
may be exposed
through retrieval or
response generation.
Low High Enforce data
classification
controls, agent
guardrails,
access control,
and auditability.
AR-06 Confidence scoring
may be poorly
calibrated, causing
over-trust or excessive
escalation.
Medium Medium Perform
calibration
testing and
maintain held-
out evaluation
sets.
AR-07 On-premises
infrastructure may be
undersized for peak
concurrent use.
Medium High Apply staged
rollout, load
testing, and
capacity margin
before
operational
rollout.
A.4 Initial On-Premises Infrastructure Rough Order of Magnitude
Important note. The following sizing values are preliminary ROM planning figures intended to support
budgeting, space, and procurement discussion only. They are not final design commitments. The
definitive server topology, redundancy model, storage architecture, model hosting strategy, and network
design shall be defined in RD-01 CRAFT Architecture Design Document after corpus sizing, benchmark
testing, and security architecture review.
Sizing Item Initial ROM Proposal for
50 Concurrent Users
Comment
Application and API servers 1 to 2 servers Supports UI, API gateway,
tool registry, and
orchestration functions; 2
servers if redundancy is
desired.
LLM/GPU inference servers 1 GPU server initially; 2 if
local redundancy is required
Initial local inference pool for
agent workloads and priority
queries.
Database and vector store
servers
1 primary server plus backup
or replica plan; 2 if HA is
required
PostgreSQL and pgvector
initial deployment sized for
reduced concurrency.
Graph database server 1 server Initial Neo4j deployment;
may be co-hosted in pilot
conditions if workload
remains light.

---

<!-- PDF page 19 -->

CSA-SEFM-RD-001 Version 1.5 Draft
19
Memory and cache server 1 server Redis or equivalent for
session and short-term
memory functions; may be
co-hosted initially if
acceptable.
Monitoring and logging
server
1 server Prometheus, Grafana, central
logging, and audit collection.
Ingestion and parsing worker
servers
1 server Supports document ingestion,
parsing, ETL, and
background processing.
Management or backup
server
0 to 1 server May be implemented as a
separate server or
consolidated into
administrative infrastructure.
Total initial server count Approximately 1 to 2 server
roles
Depends on consolidation
approach, HA posture, and
virtualization platform.
A.5 ROM Storage, GPU, and Network Sizing
Category Initial ROM Proposal for
50 Concurrent Users
Comment
Primary high-performance
storage
10 to 15 TB usable For indexed documents,
vector data, graph data, active
reports, databases, and high-
use working sets.
Archive or lower-cost storage 20 to 40 TB usable For historical documents,
backups, snapshots, and
lower-access content.
Backup retention storage 15 to 30 TB usable Depends on retention policy,
snapshot frequency, and
replication strategy.
GPU allocation 1 to 2 enterprise GPUs
initially
Final quantity depends on
chosen local model size,
concurrency, and latency
targets.
System memory 256 GB to 512 GB aggregate
RAM across core servers
Supports databases, caching,
orchestration, parsing, and
concurrent user sessions.
Core network uplinks Dual 1 Gbps Suitable initial baseline for
east-west traffic across
storage, inference, and
database services; lower
speeds may be acceptable
only for pilot or non-
performance-critical
components.
Storage network 1 Gbps baseline Provides performance margin
for indexing, retrieval, and
backup windows without

---

<!-- PDF page 20 -->

CSA-SEFM-RD-001 Version 1.5 Draft
20
over-sizing the initial
deployment.
External or enterprise
connectivity (TBD)
Redundant enterprise links
sized to synchronization and
user access demand
Exact WAN sizing depends
on SharePoint, Confluence,
SAP, and external repository
traffic patterns.
A.6 Basis for the ROM Estimate
The ROM estimate is derived from the current draft baseline requiring support for an Agentic-RAG
architecture including ingestion, parsing, embeddings, vector storage, graph storage, orchestration,
inference, memory, API, UI, and monitoring functions, while this standalone appendix uses an initial
deployment planning assumption of up to 50 concurrent users.
The estimate also assumes an initial on-premises deployment aligned with CSA control of enterprise data,
auditability, and integration to internal repositories and engineering tools. It includes modest resilience
and capacity margin, but it is intentionally conservative and incomplete for design approval purposes.
A.7 Design Authority Statement
This appendix does not supersede the CRAFT Architecture Design Document. All final implementation
details, including exact hardware bill of materials, virtualization layout, clustering, backup design,
security zoning, disaster recovery, storage classes, and network topology, shall be specified and approved
in RD-01 CRAFT Architecture Design Document before procurement or deployment.

---

<!-- PDF page 21 -->

CSA-SEFM-RD-001 Version 1.5 Draft
21
APPENDIX B—OPERATIONAL USE CASES
For each use case, provide an editable table covering: Use Case ID, Actor, Pre-conditions, Post-
conditions, Main Success Scenario (Step-by-step), and Exception Flows.
Use Case 1: Systems Engineering Documentation Ingestion & Reasoning
- UC-A1: Ingestion and Concept Deduction: Parse incoming space engineering PDFs into a unified
Knowledge Graph (Neo4j). Deduced new concepts, identifies technical contradictions or design
deviations against previously ingested legacy CSA baseline files.
Use Case 2: Global Space Tech Benchmarking & Horizon Scanning
- UC-B1: Cross-Sector Technology Comparison: Run automated web-scrapes and open-access
paper ingestion pipelines. Benchmark global space tech against CSA guidelines,
Federal/Provincial published needs, and Canadian university/private sector research (covering
Rovers, Space Robotics, Space Debris, Earth Observation, etc.).
Use Case 3: Space Engineering Costing Workflow
Develop the detailed engineering flows for these 5 exact sub-use cases:
1. UC-C1: Dublin Core Metadata Extraction: Scan unstructured PDF directories, extract metadata
from Page 1 (Title, Company, Doc Number, Date) via local LLM vision/text extraction, and
format as Dublin Core schema.

---

<!-- PDF page 22 -->

CSA-SEFM-RD-001 Version 1.5 Draft
22
2. UC-C2: Verifiable QA with Deep Citations: Answer user queries (e.g., "what is the mass of the
instrument?") providing the exact text answer along with an explicit hyperlink mapping to the
exact localized file path and page number.
3. UC-C3: Tabular Data Transformation to SQL: Parse complex PDF tables (RAM, Risk Register,
Mass, Power Consumption, TRL) into structured formats using open-source extraction tools (e.g.,
Tabula, Camelot, or LlamaParse) and write to a PostgreSQL database.
4. UC-C4: Parametric Mission Distance Calculation: Calculate mathematical nearest neighbors
using a weighted Mahalanobis or Normalized Euclidean parametric distance algorithm across
historical space missions.
The system must compute the distance D(x,y) between a target mission x and an archive mission y using
the following formula to handle features across different engineering scales (e.g., Mass in kg vs. Power in
Watts):
D(x,y) = √∑wi
n
i=1
(
xi − yi
σi
)
2
Where:
- x
i,yi
: The value of parameter i (e.g., Mass, Power, TRL, Payload Volume) for the target and
archive missions.
- σ
i
: The standard deviation of parameter i across the entire historical CSA mission database (for
normalization).
- w
i
: The user-defined or agent-assigned engineering weight for parameter i, where ∑w
i = 1
.
5. UC-C5: Automated Report Compilation: Draft a comprehensive Microsoft Word (.docx) cost
report via a Python backend (e.g., python-docx), using an approved institutional template and
dynamically injecting data queried directly from the local PostgreSQL database.

---

<!-- PDF page 23 -->

CSA-SEFM-RD-001 Version 1.5 Draft
23
UC-C1 Natural Language Technical Query
Actor: CSA Engineer
Description: The user asks a technical question in natural language. CRAFT retrieves relevant
information from the CSA knowledge base and returns a grounded answer with citations and confidence
information.
Pre-conditions:
The engineer is authenticated in CRAFT.
The knowledge base is indexed with current CSA documents.
Main Success Scenario:
1. The engineer submits a technical question in English or French.
2. The planning function decomposes the request into retrieval sub-tasks.
3. The retrieval function performs hybrid search across the indexed knowledge sources.
4. The synthesis function generates a grounded answer using retrieved evidence.
5. CRAFT presents the answer with source citations and confidence information.
6. The engineer reviews the answer and supporting sources.
Exception Flows:
E1. If confidence is lower than 0.6, the result is escalated for human review.
E2. If relevant evidence is insufficient, CRAFT requests refinement or performs a self-correction loop.
E3. If agent looping is detected, the loop is broken and the user is notified.
Applicable Requirement ID Application in Use Case
UMR-001 Natural language query entry point.
UMR-002 Retrieval with cited sources.
UMR-005 Hybrid search implementation.
UMR-006 Mandatory citations in answer.
UMR-007 Confidence score shown to user.
UMR-008 Escalation on low confidence.
UMR-009 Retrieval self-correction when context is insufficient.
UMR-010 Grounding and faithfulness of response.
UMR-011 Role-based multi-agent support.
UMR-013 Bounded ReAct reasoning loop.
UMR-019 Loop detection and break.

---

<!-- PDF page 24 -->

CSA-SEFM-RD-001 Version 1.5 Draft

---

<!-- PDF page 25 -->

CSA-SEFM-RD-001 Version 1.5 Draft
25
UC-C2 Cost Estimationfrom Historical Data
Actor: CSA Finance Engineer, Systems Engineer
Description: The user provides mission parameters. CRAFT searches historical mission cost data and
generates a cost estimate by analogy using weighted normalized Euclidean distance similarity matching;
as well as parametric estimation using COTS tools like True Planning, SSCM, PCEC, NICM.
Pre-conditions:
Historical mission cost data are available in the approved database.
COTS tools are available are can interface with Excel
The cost estimation workflow and finance tools are operational.
Main Success Scenario:
1. The engineer submits a mission concept document and Product Breakdown structure
2. The planning function creates a Cost Breakdown Structure suitable for parametric analysis
31. The engineer submits mission parameters such as mass, orbit, duration, heritage, lifetime, and
complexity.
42. The planning function decomposes the request into a structured cost feature vector (computing the
parametric distance).
53. The cost estimation function computes similarity against historical missions.
4. CRAFT retrieves the closest historical mission analogues.
5. CRAFT generates a cost estimate by analogy with confidence information and supporting references.
6. CRAFT proposes analysis scenarios for sensitivity analysis using parametric estimation.
7. CRAFT generates a cost estimate using parametric estimation with confidence information and
supporting references.
86. A Human-in-the-Loop approval request is issued for high-risk or commitment-related use.
79. The engineer approves, rejects, or modifies the proposed estimate.
108. Approved estimates are logged in the audit trail.
Exception Flows:
E1. If no acceptable analogue missions are found, the estimate is flagged as low confidence and escalated.
E2. If the estimate is rejected, the workflow re-plans using the engineer correction.
Applicable Requirement ID Application in Use Case
UMR-021 HITL for high-risk actions.
UMR-022 Reasoning chain shown during approval.
UMR-023 Approve, reject, or modify action.
UMR-024 Feedback loop after rejection.
UMR-026 HITL decision logging.
UMR-027 Immutable audit trail.
UMR-031 Mission cost estimation capability.
UMR-032 Weighted normalized Euclidean distance method.
UMR-033 Use of five similar historical missions.
UMR-034 Confidence and cited evidence in estimate.
UMR-035 Approval required before commitment.

---

<!-- PDF page 26 -->

CSA-SEFM-RD-001 Version 1.5 Draft

---

<!-- PDF page 27 -->

CSA-SEFM-RD-001 Version 1.5 Draft
27
UC-C3 Risk Identification and Flagging
Actor: Systems Engineer, Risk Manager
Description: The user requests risk analysis on a mission document or document set. CRAFT identifies
candidate risks, classifies them by severity, and proposes updates to the risk register subject to approval.
Pre-conditions:
The mission document is available in CRAFT or is uploaded by an authorized user.
Risk taxonomy and classification criteria are available.
The risk register is available for controlled update.
Main Success Scenario:
1. The user requests risk analysis on the selected document set.
2. The planning function creates a risk analysis workflow.
3. The risk function scans the content using keyword pattern matching and LLM classification.
4. CRAFT identifies candidate risks and classifies them by severity.
5. CRAFT proposes updates to the risk register.
6. A Human-in-the-Loop approval request is issued before any risk register change is committed.
7. The engineer or risk manager approves, rejects, or modifies the proposed updates.
8. Approved actions are written to the audit trail.
Exception Flows:
E1. If classification confidence is low, the result is flagged as uncertain and mandatory human review
applies.
E2. If repeated non-progressing risk flagging occurs, the loop is broken and escalated.
Applicable Requirement ID Application in Use Case
UMR-017 Permission boundaries protect unrelated systems.
UMR-019 Loop detection for repetitive risk flagging.
UMR-021 Approval required for high-risk controlled actions.
UMR-022 Reasoning chain shown to reviewer.
UMR-023 Reviewer can approve, reject, or modify.
UMR-026 Decision logging.
UMR-027 Immutable audit trail.
UMR-036 Risk identification capability.
UMR-037 Keyword plus LLM classification method.
UMR-038 Severity classification.
UMR-039 Risk register changes require approval.
UMR-040 Risk outputs grounded in source evidence.

---

<!-- PDF page 28 -->

CSA-SEFM-RD-001 Version 1.5 Draft

---

<!-- PDF page 29 -->

CSA-SEFM-RD-001 Version 1.5 Draft
29
UC-C4 Anomaly Detection in System Data
Actor: Operations Engineer, Mission Control
Description: CRAFT monitors telemetry and system data, detects anomalies using a statistical threshold,
retrieves similar historical cases, and notifies operations personnel with confidence and context.
Pre-conditions:
Telemetry data streams are connected to CRAFT ingestion services.
Thresholds and notification rules are configured.
Authorized operations users are defined.
Main Success Scenario:
1. CRAFT monitors incoming telemetry and system data.
2. The anomaly function computes Z-scores against historical baselines.
3. When the configured threshold is exceeded, the anomaly is flagged.
4. CRAFT retrieves similar historical anomaly cases from the knowledge base.
5. CRAFT generates an anomaly report with likely causes, evidence, and confidence information.
6. High-severity anomalies trigger Human-in-the-Loop acknowledgement or review.
7. Operations personnel acknowledge, investigate, or dismiss the anomaly.
8. All anomaly events and decisions are logged.
Exception Flows:
E1. If the data stream is interrupted, CRAFT flags a data gap and pauses anomaly analysis for that stream.
E2. If confidence is low, the anomaly is marked uncertain and routed for human review without
automated action.
Applicable Requirement ID Application in Use Case
UMR-014 Use of semantic and episodic memory for baselines and session
context.
UMR-016 Persistent background anomaly agent lifecycle support.
UMR-019 Loop control for repeated anomaly behavior.
UMR-021 HITL on high-severity anomalies.
UMR-022 Reasoning chain shown in review.
UMR-025 Timeout behavior for unresolved approvals.
UMR-027 Immutable logging.
UMR-030 Rate limiting for anomaly agents.
UMR-041 Anomaly detection capability.
UMR-042 Default Z-score threshold.
UMR-043 Retrieval of similar historical anomaly cases.
UMR-044 Human review for high-severity anomalies.
UMR-045 Event and response logging.

---

<!-- PDF page 30 -->

CSA-SEFM-RD-001 Version 1.5 Draft

---

<!-- PDF page 31 -->

CSA-SEFM-RD-001 Version 1.5 Draft
31
UC-C5 Automated Report Generation
Actor: Systems Engineer, Project Manager
Description: The user requests a structured report. CRAFT compiles data from controlled sources,
generates a bilingual report draft using approved templates, and routes the draft for review before
finalization.
Pre-conditions:
- Approved report templates are available.
- Required data sources are accessible.
- Authorized report users are defined.
Main Success Scenario:
1. The user specifies report type, scope, and period.
2. The planning function decomposes the request into data collection and synthesis tasks.
3. CRAFT queries approved structured and unstructured sources.
4. CRAFT generates narrative sections grounded in retrieved evidence.
5. CRAFT inserts the content into the approved bilingual template.
6. A reviewable draft is presented to the engineer or project manager.
7. The reviewer approves, edits, or requests regeneration.
8. The final report is versioned and logged.
Exception Flows:
- E1. If data are incomplete, CRAFT identifies the gap and flags the affected section for review.
- E2. If the template or source interface fails, CRAFT escalates the issue with an explicit error
record.
Applicable Requirement ID Application in Use Case
UMR-022 Reviewer sees supporting reasoning and sources.
UMR-023 Approve, reject, or modify draft outcome.
UMR-027 Immutable audit trail.
UMR-028 Version-controlled prompts and generation controls.
UMR-029 Draft rollback or discard before commitment.
UMR-046 Bilingual report generation capability.
UMR-047 Compilation from approved internal sources.
UMR-048 Narrative grounded in evidence.
UMR-049 Engineer review before finalization.
UMR-050 Versioning and logging of final reports.

---

<!-- PDF page 32 -->

CSA-SEFM-RD-001 Version 1.5 Draft

---

<!-- PDF page 33 -->

CSA-SEFM-RD-001 Version 1.5 Draft
33
UC-C6Enterprise Cognitive Synthesis Layer for Aerospace Engineering
Lifecycle Management
Actor: Systems Engineer, Cost Analyst, Scientist, Data Governance Officer
Description: The user submits a domain-specific technical query against the CRAFT federated knowledge
corpus. The platform executes multi-turn contextual reasoning over validated institutional data, enforces
governance constraints, and returns a traceable, bilingual response entirely within the secure perimeter.
Pre-conditions:
- Federated data repositories are classified, ingested, and accessible.
- The SEFM is deployed and validated for domain-specific inference.
- Role-based access control policies are defined per directorate.
- Containerized infrastructure is provisioned and hardened.
Main Success Scenario:
1. The authenticated user submits a natural language query via the bilingual integration endpoint.
2. The semantic layer parses the query and routes it to the appropriate knowledge partition.
3. The Hybrid Retrieval Engine executes parallel semantic vector search and explicit relationship
graph traversal.
4. Retrieved context is ranked and passed to the SEFM inference pipeline.
5. The SEFM executes multi-turn reasoning and synthesizes a response with full source traceability.
6. The guardrail compliance layer validates the output against access entitlements and governance
constraints.
7. The validated response is returned to the user with inline traceability references.
8. The transaction is logged to the container-isolated audit trail with full lineage metadata.
Exception Flows:
- E1. If retrieval confidence falls below threshold, CRAFT prompts the user for query refinement
before re-executing.
- E2. If the output breaches a directorate access boundary, the response is redacted at field level
and a governance notice is issued.
- E3. If the inference stack reaches capacity under high concurrency, requests are queued by role
priority and no requests are dropped.
Applicable Requirement ID Application in Use Case
UMR-022 Reviewer sees supporting reasoning and sources.
UMR-023 Approve, reject, or modify draft outcome.
UMR-027 Immutable audit trail.
UMR-028 Version-controlled prompts and generation controls.
UMR-029 Draft rollback or discard before commitment.
UMR-046 Bilingual report generation capability.
UMR-047 Compilation from approved internal sources.
UMR-048 Narrative grounded in evidence.
UMR-049 Engineer review before finalization.
UMR-050 Versioning and logging of final reports.

---

<!-- PDF page 34 -->

CSA-SEFM-RD-001 Version 1.5 Draft

---

<!-- PDF page 35 -->

CSA-SEFM-RD-001 Version 1.5 Draft
35
APPENDIX C—TRACEABILITY TABLES
C.1 User Requirements to Prior Source Requirements
Legacy Requirement ID Mapped UMR IDs
UR-F01 UMR-001, UMR-003, UMR-005, UMR-009
UR-F02 UMR-002, UMR-006, UMR-010, UMR-060
UR-F03 UMR-031, UMR-032, UMR-033, UMR-034, UMR-035
UR-F04 UMR-036, UMR-037, UMR-038, UMR-039, UMR-040
UR-F05 UMR-041, UMR-042, UMR-043, UMR-044, UMR-045
UR-F06 UMR-011, UMR-013, UMR-014, UMR-018
UR-F07 UMR-015, UMR-026, UMR-027, UMR-029
UR-F08 UMR-021, UMR-022, UMR-023, UMR-024, UMR-025
UR-F09 UMR-046, UMR-049, UMR-050
UR-F10 UMR-051, UMR-052
UR-NF01 UMR-056
UR-NF02 UMR-016, UMR-025, UMR-030, UMR-057
UR-NF03 UMR-017, UMR-020, UMR-058
UR-NF04 UMR-016, UMR-059
UR-NF05 UMR-006, UMR-007, UMR-022, UMR-060
C.2 Functional Requirement to Use Case Mapping
UMR ID UC-C1 UC-C2 UC-C3 UC-C4 UC-C5
UMR-001 ✓
UMR-002 ✓
UMR-005 ✓ ✓

---

<!-- PDF page 36 -->

CSA-SEFM-RD-001 Version 1.5 Draft
36
UMR-006 ✓ ✓ ✓
UMR-007 ✓ ✓ ✓ ✓
UMR-008 ✓ ✓ ✓ ✓
UMR-009 ✓
UMR-010 ✓ ✓ ✓ ✓
UMR-011 ✓ ✓ ✓ ✓ ✓
UMR-013 ✓ ✓
UMR-014 ✓
UMR-015 ✓ ✓
UMR-016 ✓
UMR-017 ✓
UMR-018 ✓ ✓ ✓ ✓
UMR-019 ✓ ✓ ✓
UMR-020 ✓ ✓
UMR-021 ✓ ✓ ✓
UMR-022 ✓ ✓ ✓ ✓
UMR-023 ✓ ✓ ✓
UMR-024 ✓
UMR-025 ✓
UMR-026 ✓ ✓
UMR-027 ✓ ✓ ✓ ✓
UMR-028 ✓
UMR-029 ✓ ✓
UMR-030 ✓
UMR-031 ✓
UMR-032 ✓
UMR-033 ✓
UMR-034 ✓
UMR-035 ✓
UMR-036 ✓
UMR-037 ✓
UMR-038 ✓
UMR-039 ✓
UMR-040 ✓
UMR-041 ✓
UMR-042 ✓
UMR-043 ✓
UMR-044 ✓
UMR-045 ✓
UMR-046 ✓
UMR-047 ✓
UMR-048 ✓

---

<!-- PDF page 37 -->

CSA-SEFM-RD-001 Version 1.5 Draft
37
UMR-049 ✓
UMR-050 ✓
UMR-051 ✓
UMR-052 ✓
UMR-053 ✓
UMR-054
UMR-055 ✓ ✓
UMR-056 ✓
UMR-057 ✓ ✓ ✓ ✓ ✓
UMR-058 ✓ ✓ ✓ ✓ ✓
UMR-059 ✓ ✓ ✓ ✓ ✓
UMR-060 ✓ ✓
APPENDIX D—ACRONYMS
Acronym Definition
AI Artificial Intelligence
API Application Programming Interface
CoT Chain-of-Thought
CRAFT Collaborative Reasoning and Federated Technical
Knowledge
CSA Canadian Space Agency
ECSS European Cooperation for Space Standardization
HITL Human-in-the-Loop
LLM Large Language Model
RAG Retrieval-Augmented Generation
RAGAS RAG Assessment evaluation framework
ReAct Reasoning and Acting
REST Representational State Transfer
SAP Systems, Applications, and Products
SESM Space Engineering and Systems Management
STK Satellite Tool Kit
UMR User and Functional Requirement
UFRD User and Functional Requirements Document
