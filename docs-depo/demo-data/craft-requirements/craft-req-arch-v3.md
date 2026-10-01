<!-- PDF page 1 -->

1. Introduction
### 1.1 Background
CSA engineers need fast and reliable access to technical information. Today this
information sits in many places: file systems, document tools, and separate team folders.
This slows engineeringeffortdown. CRAFT is built to fix this. CRAFT is a working tool for
real engineering tasks. It is not a research experiment.
CRAFT combines a Large Language Model (LLM — an artificial intelligence model trained
on text, which can read and write natural language) with a shared knowledge base. The
knowledge base holds CSA documents, standards, and past mission data. CRAFT uses a
software agent: a program driven by the LLM that can plan a task, look up information,
write an answer, and record what it did.
### 1.2 Purpose
CRAFT gives CSA engineers a secure and traceable tool. It answers technical questions,
helps estimate cost, finds risks, monitors for unusual system behaviour, and writes
reports. This document lists what CRAFT must do, from the point of view of the people who
will use it.
### 1.3 Scope
This document covers CRAFT as a production system used across CSA engineering teams.
It covers document handling, document search, risk review, cost estimation, anomaly
detection, mission planning support, and report writing. It also covers connections to
CSA's existing systems.
CRAFT uses an Agentic-RAG design. RAG means Retrieval-Augmented Generation: the
model looks up real documents before it writes an answer. Agentic means a software
agent plans and carries out the work, including choosing how to search within the bounds
set by UMR-094.
Explicitly out of scope. The following are not part of CRAFT, in this phase or as currently
specified:
- Multiple agents by default. CRAFT uses one accountable primary agent. Delegation
is the exception, justified case by case under UMR-011.
- Fixed agent role hierarchies. Roles are not imposed in advance. Control is held at
the tool boundary under UMR-012.
- Self-evolving agent harnesses. An agent shall not modify its own instructions, tools
or code, and shall not modify procedural memory outside the approved change
process.
- Free-form shell or command-line access by agents. File search is available only
through the parameterised interface in UMR-094.

---

<!-- PDF page 2 -->

- Personal devices, individual OneDrive accounts, and production CSA repositories,
until each is onboarded through the approved process in UMR-051.
- French-language output and interface, until phase 2.
1.4 Who can change this document
Only CSA's document control process can approve a change. Anyone proposing a change
sends it through that process. Approved changes appear in the next issued version.
### 1.5 Word meanings and precedence
- SHALL — a firm rule. It must be built and it must be verified.
- SHALL NOT — a firm prohibition.
- SHOULD — recommended, but not required.
- MAY — permitted and optional. MAY is never used to express a prohibition in this
document.
- WILL— a statement of what is planned or expected.
- CONFIGURABLE — a value an authorized person can change without changing this
document. Every configurable value has a parameter identifier and an entry in
Annex B.
- BASELINE VALUE — the value approved for use now. An interim baseline value
applies until test evidence replaces it.
The Type column has these values: Mandatory, Mandatory (revised), Mandatory (new),
Goal, and Withdrawn. A Withdrawn identifier is retained as a pointer so traceability does
not break. No mandatory requirement may depend on a Goal.
Precedence. Section 4.1 holds the governing requirement text. Section 4.2 gives additional
detail for the software agents. Where Section 4.2 and Section 4.1 appear to differ, Section
4.1 governs. Where a Rationale appears to differ from its requirement, the requirement text
governs.
### 1.6 Requirement tag meanings
Tag Stands for Used for
UMR User and Mission
Requirement
The governing requirements
in Section 4.1
AAR Agent Architecture
Requirement
How agents are built and
bounded (Section 4.2.1)
ARR Agent Reasoning
Requirement
How agents plan, search
and answer (Section 4.2.2)
HITL Human-In-The-Loop
Requirement
Human review and approval
(Section 4.2.3)
ASG Agent Safety and Safety, limits and oversight

---

<!-- PDF page 3 -->

Tag Stands for Used for
Governance Requirement (Section 4.2.4)
UC Use case Appendix B of the source
requirements document, as
corrected in Annex C
PARAM Configurable parameter Annex B register entries
OP Open point Annex E items awaiting a
CSA decision
RC Review comment Annex F reconciliation
register
ADR Architecture Decision
Record
Held in the Architecture
Design Document
### 1.7 Verification methods
- I —Inspection. Read the product, the configuration, or the document.
- A — Analysis. Calculate or reason from data.
- D —Demonstration. Run the system and observe the behaviour.
- T — Test. Run a defined procedure and compare results against a stated criterion.
1.8 Terms used in this document
Term Plain meaning
Agent A program, driven by the language model,
that plans and carries out a task
API Application Programming Interface —a
defined way for one system to call another
Azure Microsoft Azure —the cloud platform
CRAFT runs on
BM25 A standard keyword ranking method. It
scores a document by how often the query
words appear in it, adjusted for length and
word rarity
Chunk A piece of a document, stored and searched
as a unit
Context window The total amount of text a language model
can consider in one request, measured in
tokens
Deduplicate Remove repeated passages so the same
text is not counted twice in the evidence
Delegation The primary agent asking a subagent to

---

<!-- PDF page 4 -->

Term Plain meaning
complete a bounded subtask
Dense retrieval Search by meaning, using embeddings. Also
called vector search or semantic search
Embedding A list of numbers that represents the
meaning of a piece of text
Ephemeral Held only for the life of the session, then
destroyed
Episodic memory Governed conversation and task history for
the current session
Fusion Combining two ranked result lists into one
ranked list, after putting their scores on a
common scale
Grounding Writing answers only from retrieved
evidence
Knowledge graph A stored map of facts and the links between
them
MATLAB A commercial engineering calculation and
modelling product
Normalize Put scores from different search methods
onto a common scale so they can be
compared
Parameterizedinterface A tool that accepts a fixed set of named
inputs, rather than a free-form command
string
PBMM Protected B, Medium integrity, Medium
availability— the Government of Canada
cloud security control profile CRAFT is
assessed against
Primary agent The single agent accountable to the user for
a session and for the final answer
Procedural memory Approved guidance for a repeated task,
such as instruction files, runbooks and
templates
Prompt The written instruction given to the language
model
Prompt injection Hidden instructions placed inside a
document, intended to change agent
behavior

---

<!-- PDF page 5 -->

Term Plain meaning
Retrieval path The record of which search tools an agent
used, in what order, to find the evidence
behind an answer
REST, GraphQL Two common styles of API
Recall@k, Precision@k, MRR, nDCG, F1 Standard measures of how good a ranked
list of search results is
SAP The commercial product used as CSA's
financial system of record
Semantic memory Curated, source-backed durable
knowledge, held independently of any one
conversation
Session One continuous conversation between a
user and CRAFT, from opening to close
Source agreement Whether several independent sources say
the same thing
Sparse retrieval Search by keyword, such as BM25
SSC Shared Services Canada
STK Systems Tool Kit —a commercial mission
analysis product
Token A word-piece of text. Models measure text
length in tokens
Unsupported claim A statement in an answer that no retrieved
passage backs up
Z-score A measure of how far a data point sits from
the normal range
2. Related Documents
### 2.1 Parent documents
No parent requirements document exists above CSA-CRAFT-RD-0001. CRAFT is the top of
its own requirement tree. AD-01, CSA-SE-PR-0001, remains the process authority for how
this document is written and controlled.
Document number. CSA has confirmed the document number as CSA-CRAFT-RD-0001.
The source file header carried CSA-SEFM-RD-001, which is superseded. The header shall
be corrected at reissue.
### 2.2 Documents CRAFT must follow
ID Reference Title

---

<!-- PDF page 6 -->

ID Reference Title
AD-01 CSA-SE-PR-0001 Systems Engineering
Methods and Practices
AD-02 Canada&#46;ca Responsible use of artificial
intelligence in government
AD-03 NASA/SP-2016-6105 Rev 2 NASA Systems Engineering
Handbook
AD-04 ECSS-E-ST-10C European Cooperation for
Space Standardization
Systems Engineering
Standard
AD-05 CSA-SEC-POL-003 CSA Data Classification
Policy
AD-07 Canada&#46;ca AI governance principles
AD-08 CSA-ST-GDL-0001 Technology Readiness and
Risk Assessment Guidelines
### 2.3 Documents used for background
ID Reference Title Status
RD-01 CSA-CRAFT-AD-
0001
CRAFT Architecture
Design Document
Draft A1 is a cover
page only. Treated
as not available. See
Section 5.3
RD-02 N/A CRAFT Intern
Proposal
Available
RD-03 CSA-SE-GDL-0001 Systems Engineering
Mission Tailoring
Guidelines
Available
RD-04 CSA-SEFM-RD-0001,
Appendix B
CRAFT Operational
Use Cases
Recovered in P9.
UC-A1, UC-B1, UC-
C1 to UC-C9
RD-05 CSA-SEFM-RD-0001,
Appendix C
CRAFT Traceability
Tables
Recovered in P9.
Completed in P11
RD-06 tbs-sct&#46;canada.ca Treasury Board
Directive on
Automated
Decision-Making
CRAFT does not
claim compliance.
See OP-14
RD-07 CSA-SEFM-RD-0001,
Appendix A
User Roles,
Operational
Assumptions, Risk
Controlled copy. The
infrastructure
estimate is

---

<!-- PDF page 7 -->

ID Reference Title Status
and Initial
Infrastructure
Estimate
withdrawn in full
RD-08 requirements-
analysis&#46;docx
CRAFT
Requirements
Technical Review
Commentary and
Responses
Reconciled in Annex
F, RC-01 to RC-19
### 2.4 Approval block
Role Authority
Prepared by Senior Systems Engineer, Sun-Earth System
Science
Reviewed by Senior Systems Engineer, CSA Finance
Reviewed by Senior Engineer, Electrical, Space Science
and Technology
Recommended by Senior Manager, Sun-Earth System Science
Recommended by Engineering Manager, Space Science and
Technology
Recommended by CSA Finance
Approved by Director, Sun-Earth System Science
If a further approval authority is required for the PBMM authorization, it shall be added by
name and title through the change process.
3. What CRAFT Is Meant to Do
### 3.1 Main goals
CRAFT gives CSA a safe and traceable place where authorized people can find, check, and
use technical knowledge and engineering data. People work with CRAFT through a
conversation, asking questions in plain language and following up. CRAFT helps engineers
make better decisions.
### 3.2 How CRAFT works, step by step
In the proof of concept, CRAFT imports documents from the controlled Engineering
Costing corpus (UMR-051, UMR-091). It checks the classification of each document
against the Protected B ceiling. It splits each document into chunks, converts each chunk
into an embedding, and keeps a search index and a knowledge graph.

---

<!-- PDF page 8 -->

A user opens a session. One primary agent is accountable for that session (UMR-095). The
user asks a question. CRAFT plans the task. It searches using the default hybrid method:
keyword and meaning-based retrieval, normalised onto a common scale, fused, and
deduplicated. Where the question needs a different approach, the primary agent may
select another authorized retrieval tool and iterate (UMR-094). Retrieval stays selective:
CRAFT places the relevant evidence in the model request, not as much as will fit.
CRAFT writes an answer from the retrieved evidence, records which retrieval path it used,
and scores its confidence from evidence coverage, citations, traceability, source
agreement, retrieval quality, and any claims it could not support. If the task is high-risk, or
the confidence is below the approved threshold, a person reviews the result before it is
used.
### 3.3 Who uses CRAFT
User group Status What they do Notes
Engineers and
analysts
Built now Ask questions, run
analysis, draft
reports
Hold the Requester
role, and Reviewer
where appropriate
Technical authorities
and delegated
authorities
Built now Approve
recommendations,
high-risk actions and
final reports
Hold the Approver or
Backup approver
role
Governance, audit
and security staff
Built now Review the audit
record, traceability
reports and PBMM
control evidence
Hold the Auditor or
Security authority
role
Platform support
staff
Built now Run and maintain
the platform
Hold the
Administrator role.
Cannot approve
requests or alter
audit records
Executives Planned for later Read summaries
and approved
results
Not built yet
### 3.4 Roles and responsibilities
Required by UMR-065. Every CRAFT user holds at least one role. A role grants only the
permissions listed for it. These are user roles. Agents do not hold user roles; agent
permissions are bound at the tool level under UMR-012.
Role Who it is for May do Shall not do
Requester Any authorized CSA Open sessions, ask Approve their own

---

<!-- PDF page 9 -->

Role Who it is for May do Shall not do
engineer or analyst questions, run
searches, request
cost estimates and
risk reviews, run
mission planning
comparisons,
generate draft
reports, use the
session workspace,
see their own history
request. Mark a
report final. Change
any configurable
parameter. Read the
audit store
Reviewer Subject-matter
experts and
technical leads
Everything a
Requester may do.
Review low-
confidence answers
routed under UMR-
008. Correct or
reject an agent
recommendation
Give final approval
for a high-risk action.
Change any
configurable
parameter
Approver Technical
authorities, project
managers,
delegated financial
or risk authorities
Approve, reject or
edit any
recommendation
before it becomes
final. Approve high-
risk actions. Mark a
report final. Approve
changes to the
official risk list
Approve a request
they submitted
themselves (UMR-
065.1). Change or
delete an audit
record
Backup approver An alternate for each
Approver. Named
holders TBC
(PARAM-37)
Act as Approver
when a request
escalates on
timeout under UMR-
025
As for Approver
Parameter owner The CRAFT technical
authority and named
delegates
Change a
configurable
parameter in Annex
B, with a recorded
reason and
evidence. Approve
the authorized tool
set under UMR-012
and UMR-094
Approve operational
requests. Change an
audit record

---

<!-- PDF page 10 -->

Role Who it is for May do Shall not do
Auditor Governance
reviewers, internal
audit, security
assessors
Read and export the
full audit record,
including retrieval
paths, delegation
records and code
execution records.
Produce traceability
reports
Hold the
Administrator role.
Submit, review or
approve operational
requests
Administrator CRAFT platform
support staff
Manage the
platform, deploy
releases, manage
accounts and role
assignments,
manage connectors
and the tool registry
Change or delete an
audit record,
prevented
technically by ASG-
008. Approve
operational
requests. Hold the
Auditor role
Security authority The CRAFT security
assessor under the
PBMM authorization
Review the PBMM
control mapping,
classification
rejections, the
unlabelled-
document
population, code
execution logs,
blocked tool
attempts, and
workspace exports
Change the
configuration or
approve operational
requests
Least privilege. A user shall be given the lowest role that lets them do their work. Role
assignments shall be reviewed at the approved interval (PARAM-36).
Phase note. The proof of concept may operate with a small number of people covering
several roles, but the separation in UMR-065.1 shall hold: the requester and the approver
shall be different people, and the auditor shall not be the administrator.
4. What CRAFT Must Do
### 4.1 Core requirements
Column meanings: ID is the tracking number. Type is how firm the rule is. Requirement is
the rule. Rationale says why it exists. V is the verification method (I, A, D, T). Note records
what changed.
<!-- PDF page 11 -->

ID Type Requirement Rationale V Note
UMR-001 Mandatory
(revised)
CRAFT shall
accept
questions
written as
free text, in
English or in
French,
within a
conversation
al session as
defined in
UMR-095.
CRAFT shall
detect the
language of
the question.
Language
detection
accuracy
shall be
measured
against the
approved
acceptance
question set.
The
minimum
accuracy is a
configurable
setting
(PARAM-01).
Engineers
must be able
to ask in
their own
words and
follow up.
T Linked to the
session
model inV3
UMR-002 Mandatory
(revised)
CRAFT shall
retrieve
documents
that match
the question,
and shall
attach to
every
retrieved
passage the
identity of
The answer
must be
checkable.
D Citation
content in
UMR-006

---

<!-- PDF page 12 -->

ID Type Requirement Rationale V Note
the
document it
came from.
UMR-003 Mandatory
(revised)
CRAFT shall
supply the
language
model with
enough
retrieved
evidence to
answer the
questions in
the approved
acceptance
set. The
minimum
total request
context shall
be a
configurable
setting
(PARAM-02),
covering
instructions,
user query,
conversation
history,
retrieved
evidence
and
generated
output. It is
not the size
of a stored
chunk;
chunk size is
PARAM-39.
Models with
a larger
context
window are
permitted.
The earlier
wording did
not say
whether
8192 meant
a chunk or
the model
context
window. It is
the request
context, and
it is a
compatibility
floor rather
than a target.
A larger
window is
not a reason
to send more
evidence:
long prompts
dilute the
passages
that matter,
which
degrades
both answer
quality and
the
grounding
measure in
UMR-010.
T Selectivity
rule added in
V3from RC-

---

<!-- PDF page 13 -->

ID Type Requirement Rationale V Note
Retrieval
shall remain
selective and
relevant.
CRAFT shall
not fill the
available
context
indiscriminat
ely.
UMR-004 Mandatory
(revised)
CRAFT shall
find and rank
matching
documents
using both
keyword
retrieval and
meaning-
based
retrieval.
CRAFT shall
normalise
the scores
from each
method onto
a common
scale, fuse
them into a
single
ranking, and
deduplicate
the result.
CRAFT shall
not simply
append the
top results of
each
method. The
number of
results, the
filter
threshold,
The review
asked how
results from
the two
methods are
ranked
against each
other.
Appending
raw lists
distorts what
the model
sees,
because two
methods
produce
scores on
different
scales. A
threshold is
acceptable
once
measured;
the earlier
0.72 was
unacceptabl
e only
because it
was asserted
without
evidence.
T Normalise,
fuse,
deduplicate
added inV3
from RC-04.
Top-5-
append
fallback
withdrawn.
0.72 restored
as a
candidate to
validate.
Measuremen
t scope
widened to
UMR-094

---

<!-- PDF page 14 -->

ID Type Requirement Rationale V Note
the fusion
method and
the ranking
method shall
be
configurable
settings
(PARAM-03).
Threshold
values,
including the
candidate
value of
0.72, shall
be validated
against
measured
retrieval
performance
on the
approved
acceptance
set before
use in
operation.
Quality shall
be measured
across all
retrieval
paths,
including
agent-
selected
retrieval
under UMR-
094, not only
the default
path.
UMR-005 Mandatory
(revised)
CRAFT shall
retrieve
using BM25
Fixing the
weights for
Phase 1
accelerates
I, T Phase 1
weights
fixed,
interface

---

<!-- PDF page 15 -->

ID Type Requirement Rationale V Note
keyword
search and
vector
search
together,
behind a
single
common
retrieval
interface.
The interface
shall allow
the retrieval
methods, the
fusion
weights, and
any
reranking
step to be
changed
without
changing the
calling code.
The weights
shall be a
configurable
setting
(PARAM-04).
Phase 1
baseline: 0.7
semantic
and 0.3
lexical.
delivery. A
common
interface
means later
phases can
add
configurable
weights,
reranking,
metadata
search and
other
algorithms
without
refactoring.
retained, RC-
06
UMR-006 Mandatory
(revised)
Every answer
shall name,
for each fact
used: the
source
document,
its version,
and the page
or section of
the cited
People must
be able to
check the
work.
D "If possible"
removed.
UMR-060
merged in

---

<!-- PDF page 16 -->

ID Type Requirement Rationale V Note
passage.
Where the
source
format has
no page or
section
markers,
CRAFT shall
give the
passage
locator it
holds.
UMR-007 Mandatory
(revised)
CRAFT shall
give every
answer a
confidence
score
between 0
and 1. The
score shall
be
computed
from:
evidence
coverage;
the presence
and quality
of citations;
source
traceability;
agreement
between
independent
sources;
retrieval
quality; and
the
identification
of claims the
retrieved
evidence
does not
Multiplied
token
probabilities
fall towards
zero as an
answer
lengthens,
regardless of
correctness,
and hosted
models often
do not return
them at all.
The six
named
inputs are
observable,
model-
independent
and testable.
T Inputs
extended in
V3from RC-
07 and RC-
08. Removes
a hidden
constraint on
UMR-081

---

<!-- PDF page 17 -->

ID Type Requirement Rationale V Note
support.
CRAFT shall
not compute
confidence
from the
joint
probability of
generated
tokens.
CRAFT shall
demonstrate
that the
score
separates
correct
answers
from
incorrect
answers on
the approved
acceptance
set.
UMR-008 Mandatory
(revised)
If an
answer's
confidence
score is
below the
approved
threshold,
CRAFT shall
route the
answer to
the assigned
human
reviewer role
before it is
used. The
threshold
shall be a
configurable
setting per
risk tier
A single fixed
number for
every task
contradicts
the risk-
tiering rule in
UMR-010.
T Baseline
value

---

<!-- PDF page 18 -->

ID Type Requirement Rationale V Note
(PARAM-06).
Interim
baseline
value: 0.6.
UMR-009 Mandatory
(revised)
If a retrieval
result does
not meet the
configured
sufficiency
condition,
CRAFT shall
search again
with
adjusted
terms or a
different
authorized
retrieval tool
under UMR-
094. The
number of
retries shall
be a
configurable
setting
(PARAM-05).
An uncapped
retry
conflicts
with the loop
control in
UMR-019.
T Linked to
agent
retrieval in
P13
UMR-010 Mandatory
(revised)
CRAFT shall
write
answers only
from
retrieved
evidence.
CRAFT shall
measure
grounding
against the
approved
acceptance
set, using the
approved
checking
method. The
A number
without an
agreed
method,
data set and
tool means
nothing.
Removing
the gate
entirely
leaves no
control.
T Split.
Insufficient-
evidence
behaviour in
UMR-086

---

<!-- PDF page 19 -->

ID Type Requirement Rationale V Note
pass score,
the sample
method and
the checking
tool shall be
written down
before
acceptance
testing. The
pass score
shall be a
configurable
setting per
risk tier
(PARAM-07).
UMR-011 Mandatory
(revised)
CRAFT shall
use one
accountable
primary
agent for
each
session.
CRAFT shall
not impose
fixed agent
roles and
shall not use
multiple
agents by
default. The
primary
agent may
delegate a
bounded
subtask to a
subagent
only where
delegation
demonstrabl
y improves
quality,
speed,
The review
said multi-
agent roles
were not well
defined and
it was not
clear why
they were
needed. The
response
settles it:
most tasks
need one
agent, so the
question of
how to
govern many
agents was
solving a
problem
CRAFT does
not have.
Requiring a
recorded
justification
prevents
delegation
I, T Rewritten in
V3from RC-
15 and RC-
16.
Registered-
role-per-
agent rule
withdrawn.
OP-30
closed

---

<!-- PDF page 20 -->

ID Type Requirement Rationale V Note
isolation or
capability,
measured
against the
criteria in
PARAM-45.
Every
delegation
shall record
the subtask,
the reason,
the bounds
set, and the
result. The
primary
agent
remains
accountable
for the final
response.
becoming
the default
by habit.
UMR-012 Mandatory
(revised)
Every agent,
primary or
delegated,
shall use
only the
tools listed
in the
approved
tool registry
for its task,
including
retrieval
tools. Tool
permissions
shall be held
under
version
control and
approved by
the
Parameter
owner role.
With fixed
roles
withdrawn
under UMR-
011, the tool
boundary
becomes the
primary
control
surface.
What an
agent may
do is defined
by what it
may call.
T Elevated in
P13. Now the
main agent
control, and
explicitly
covers
retrieval
tools
<!-- PDF page 21 -->

ID Type Requirement Rationale V Note
UMR-013 Mandatory
(revised)
Agents shall
run within a
budget
covering
time used,
tokens used,
tool calls
made,
reasoning
steps taken,
delegated
subtasks,
and
estimated
cost. Each
limit shall be
a
configurable
setting per
task type,
per
requester
and per risk
tier (PARAM-
09 to
PARAM-13).
When a limit
is reached,
CRAFT shall
stop safely,
return any
useful partial
result,
record the
reason, and
ask the user
what to do
next. For
high-risk
tasks, CRAFT
shall
escalate to
A step count
alone does
not reflect
real cost,
time or risk.
Delegation
adds a cost
dimension
that did not
previously
exist.
T Delegation
budget
added in P13

---

<!-- PDF page 22 -->

ID Type Requirement Rationale V Note
the assigned
human role.
UMR-014 Mandatory
(revised)
CRAFT shall
hold three
kinds of
memory.
Episodic
memory is
the governed
conversation
and task
history for a
session.
Semantic
memory is
curated,
source-
backed
durable
knowledge,
held
independentl
y of any one
conversation
; an entry
shall cite its
source and
shall be
reviewable.
Procedural
memory is
approved
guidance for
a repeated
task, such as
instruction
files,
runbooks
and
templates.
Procedural
memory
The review
asked what
semantic
memory
means and
proposed
episodic
memory as
conversation
history. The
response
tightens
both:
semantic
memory
must be
curated and
source-
backed, not
whatever the
system
happened to
retain, and
procedural
memory
must be
approved
rather than
self-written.
Uncontrolled
self-
modification
of
procedures
is how an
agent's
behaviour
drifts without
anyone
approving
I, T Definitions
tightened in
V3from RC-
11 to RC-14

---

<!-- PDF page 23 -->

ID Type Requirement Rationale V Note
shall be held
under
version
control and
shall be
changed only
through the
approved
process; an
agent shall
not modify it.
Each kind
shall have a
defined
retention
period
(PARAM-27),
a defined
deletion
path, and
isolation per
user and per
data
classificatio
n.
the change.
UMR-015 Mandatory Every
message
between
agents shall
include the
sending
agent
identifier, the
action, the
input, the
output, a
confidence
score and a
timestamp.
Needed to
control and
review agent
behaviour.
I Unchanged
UMR-016 Mandatory
(revised)
CRAFT shall
allow an
agent to be
The review
read the
original
D Clarified,
RC-09

---

<!-- PDF page 24 -->

ID Type Requirement Rationale V Note
started or
stopped
while the
platform
continues to
serve
requests.
Requests
already
running shall
not fail. This
concerns
platform
availability
during agent
lifecycle
changes.
Session
persistence
is covered by
UMR-095.
wording as
implying
persistent
session-
bound
agents. The
two
concerns are
now
separated.
UMR-017 Mandatory
(revised)
An agent
shall not
read, change
or delete
data, system
functions or
system
settings
outside the
permissions
recorded for
its tools in
the approved
tool registry.
Protects
data and
keeps
control of
the system.
T Bound to the
tool registry
in P13
UMR-018 Mandatory
(revised)
CRAFT shall
break a
complex
request into
steps and
record the
plan. Where
Needed for
tasks with
several
steps.
T Delegation
recording
added

---

<!-- PDF page 25 -->

ID Type Requirement Rationale V Note
a step is
delegated,
CRAFT shall
record which
subagent
executed it.
Verification
is against the
approved
multi-step
acceptance
tasks.
UMR-019 Mandatory
(revised)
If an agent
repeats an
action that
matches the
approved
repetition
test, and no
new
information
is produced,
CRAFT shall
stop the task
and escalate
it to the
assigned
human role.
The number
of repetitions
allowed shall
be a
configurable
setting
(PARAM-14).
Interim
baseline
value: 3.
Prevents
wasted and
unsafe
repeated
execution,
including
repeated
retrieval
attempts
under UMR-
094.
T Aligned with
ASG-005
UMR-020 Mandatory
(revised)
CRAFT shall
filter
generated
content
A filter with
no measured
false-block
rate can
T Criteria
added

---

<!-- PDF page 26 -->

ID Type Requirement Rationale V Note
against the
approved
content
policy list.
Filter
performance
shall be
measured
against the
approved
adversarial
test set. The
minimum
block rate
and the
maximum
false-block
rate shall be
configurable
settings
(PARAM-08).
make CRAFT
unusable.
UMR-021 Mandatory
(revised)
CRAFT shall
obtain
approval
from an
authorized
person
before
carrying out
any action
classified as
high-risk
under UMR-
082.
Protects
important
engineering
decisions
from being
made by AI
alone.
T One
classificatio
n scheme
UMR-022 Mandatory
(revised)
Every
approval
request shall
show the
agent's
reasoning,
its
confidence
A reviewer
needs the
evidence
and the route
by which it
was found.
D Retrieval
path added
in P13

---

<!-- PDF page 27 -->

ID Type Requirement Rationale V Note
score, the
source
documents
used, and
the retrieval
path under
ARR-010.
UMR-023 Mandatory
(revised)
A person
holding the
Approver
role defined
under UMR-
065 shall be
able to
approve,
reject or edit
any
recommend
ation before
it becomes
final.
A person
makes the
final
decision.
D "Authorized"
now defined
UMR-024 Mandatory
(revised)
If a
recommend
ation is
rejected,
CRAFT shall
allow the
agent to try
again using
the
reviewer's
correction.
The number
of retries
after
rejection
shall be a
configurable
setting
(PARAM-15).
An uncapped
retry loop is
a cost and
safety risk.
T Retry cap
added
UMR-025 Mandatory
(revised)
If no decision
is recorded
Silent
cancellation
T Escalation,
safety

---

<!-- PDF page 28 -->

ID Type Requirement Rationale V Note
within the
approval
timeout,
CRAFT shall
escalate the
request to
the Backup
approver.
The timeout
shall be a
configurable
setting per
risk tier
(PARAM-16).
Interim
baseline
value: 24
hours. If no
decision is
recorded
after
escalation,
CRAFT shall
cancel the
request and
flag it for
review. If no
Backup
approver is
named,
CRAFT shall
not cancel
the request;
it shall keep
it open and
flag it. CRAFT
shall not
cancel a
request that
reports a
high-severity
operational
of a safety
escalation is
not
acceptable,
and a blank
role must not
become a
silent
cancellation.
exception,
unnamed-
backup case

---

<!-- PDF page 29 -->

ID Type Requirement Rationale V Note
anomaly.
UMR-026 Mandatory Every
approval
decision
shall be
logged with
the person's
identity, the
decision, the
time and the
reason.
Needed to
prove who
approved
what.
I Unchanged
UMR-027 Mandatory
(revised)
CRAFT shall
write every
agent action
and every
approval
decision to
append-only
storage,
including
retrieval
paths,
delegation
records,
workspace
exports and
code
execution
records. No
platform
role,
including
administrato
r, shall be
able to
change or
delete a
record.
Record
integrity
shall be
verifiable by
"Permanent
and
unchangeabl
e" could not
be tested.
The new
agent
capabilities
each
produce
records that
must be
covered.
T Scope
widened in
P13

---

<!-- PDF page 30 -->

ID Type Requirement Rationale V Note
the approved
cryptographi
c check.
UMR-028 Mandatory
(revised)
Every version
of an agent's
model
settings,
prompts,
tool
permissions
and
procedural
memory
shall be held
under
version
control, and
shall be
reviewed and
approved by
the assigned
technical
authority
before
operational
use. An
agent shall
not modify
its own
settings,
prompts,
tools, code
or
procedural
memory.
The review
confirmed
self-evolving
agent
harnesses
are out of
scope, and
the response
extends that
to
procedural
memory.
I Procedural
memory
added inV3
from RC-14
UMR-029 Mandatory
(revised)
CRAFT shall
classify
every agent
action into
one of three
groups under
UMR-082:
"Reversible
where
feasible"
could not be
tested.
T Split into
UMR-087,
UMR-088
<!-- PDF page 31 -->

ID Type Requirement Rationale V Note
read-only,
reversible, or
irreversible.
For a
reversible
action,
CRAFT shall
check the
action before
running it,
save the
earlier state
or a version
marker, write
a log entry,
and provide
a way to
undo the
change.
UMR-030 Mandatory
(revised)
CRAFT shall
limit
resource use
for each
user, each
session,
each task
and each
agent. The
limits shall
cover
tokens, tasks
running at
the same
time,
estimated
cost, tool
calls, call
rate,
delegated
subtasks,
retrieval
iterations,
Agent-
selected
retrieval and
delegation
are both
unbounded
without
explicit
limits: an
agent that
may choose
how to
search may
also choose
to search
many times.
T Retrieval
iterations
and
delegation
added in P13

---

<!-- PDF page 32 -->

ID Type Requirement Rationale V Note
and code
execution
time and
memory
(PARAM-42).
Each limit
shall be a
configurable
setting with
an interim
baseline
value in
force before
first
operational
use. Soft
limits shall
warn and
reduce the
rate of new
work. Hard
limits shall
stop the task
safely.
UMR-031 Mandatory
(revised)
CRAFT shall
produce
mission cost
estimates
from past
mission
data.
Estimate
accuracy
shall be
measured by
a back-test
against past
missions
with known
cost. The
minimum
accuracy
An estimate
with no
measured
accuracy
cannot be
relied on.
T Accuracy
criterion
added

---

<!-- PDF page 33 -->

ID Type Requirement Rationale V Note
shall be a
configurable
setting
(PARAM-17).
UMR-032 Mandatory
(revised)
CRAFT shall
compare
missions
using a
documented
, repeatable
comparison
method that
adjusts for
different
measuremen
t scales. The
method and
its weights
shall be
configurable
settings
under
version
control
(PARAM-18).
Interim
baseline
method:
weighted
normalised
Euclidean
distance.
Locking one
formula
before
testing
repeats a
defect
corrected
elsewhere.
I, T Baseline
method
UMR-033 Mandatory
(revised)
CRAFT shall
find the
closest
matching
past
missions to
support a
new cost
estimate.
The number
The right
count
depends on
how much
history
exists.
T Baseline
value

---

<!-- PDF page 34 -->

ID Type Requirement Rationale V Note
returned and
the similarity
cutoff shall
be
configurable
settings
(PARAM-19).
UMR-034 Mandatory
(revised)
A cost
estimate
shall include
an
uncertainty
range and a
machine-
readable list
of the past
missions
used as
evidence.
A reviewer
must be able
to check the
estimate and
see how
uncertain it
is.
D Defined
meaning
UMR-035 Mandatory
(revised)
A cost
estimate tied
to a
spending
decision or
an approved
baseline
shall be
classified as
high-risk
under UMR-
082 and shall
require
approval
before use.
Protects the
organization
from acting
on an
unapproved
estimate.
T One
classificatio
n scheme
UMR-036 Mandatory
(revised)
CRAFT shall
identify and
flag possible
risks found
in mission
documents.
The official
risk list is
UMR-037 to
UMR-040 are
mandatory
and depend
on this
capability.
T Risk
standard
TBC, OP-08

---

<!-- PDF page 35 -->

ID Type Requirement Rationale V Note
handled at
Protected B
under
PBMM. The
risk standard
CRAFT
applies is
TBC.
UMR-037 Mandatory
(revised)
CRAFT shall
find risks
using one or
more
approved
detection
methods.
The methods
used and
their settings
shall be
configurable
and under
version
control.
Locking one
method
before
testing
repeats the
defect
corrected in
UMR-005.
I, T Method set
configurable
UMR-038 Mandatory
(revised)
Every risk
CRAFT
reports shall
carry a
severity level
from the
severity
scale
defined in
UMR-082.
Helps decide
which risks
need
attention
first.
D One scale
UMR-039 Mandatory Any change
proposed to
the official
risk list shall
require
approval by
an
authorized
person
Protects the
controlled
risk record.
T Unchanged

---

<!-- PDF page 36 -->

ID Type Requirement Rationale V Note
before it is
saved.
UMR-040 Mandatory
(revised)
Every risk
CRAFT
reports shall
cite evidence
found in the
source
document,
and shall
meet the
grounding
rule in UMR-
010.
Prevents
invented
risks.
T Linked to
grounding
test
UMR-041 Mandatory
(revised)
CRAFT shall
detect and
report
configured
anomalies in
approved,
monitored
data feeds
and system
health
information,
using
configurable
rules, limits
and trend
checks.
The scope
must stay
limited to
data CRAFT
can reach.
T Report
content in
UMR-089
UMR-042 Mandatory
(revised)
CRAFT shall
flag unusual
data points
using a
configurable
statistical
trigger
(PARAM-20).
A trigger
value shall
be set for
each data
One fixed Z-
score for
every data
source
assumes
every signal
behaves the
same way.
T Trigger
required
before
operation

---

<!-- PDF page 37 -->

ID Type Requirement Rationale V Note
source and
each
anomaly
type before
that source
is monitored
in operation.
UMR-043 Mandatory
(revised)
When CRAFT
flags an
anomaly, it
shall retrieve
similar past
anomalies
from the
knowledge
base. The
number
returned and
the similarity
cutoff shall
be
configurable
settings
(PARAM-21).
Helps
diagnose a
new problem
faster.
T Same
treatment as
UMR-033
UMR-044 Mandatory
(revised)
An anomaly
at or above
the high
severity level
defined in
UMR-082
shall be sent
to the
assigned
human role.
CRAFT shall
record
whether it
was
acknowledge
d and shall
keep the
item open
"Serious"
was
undefined.
T One severity
scale

---

<!-- PDF page 38 -->

ID Type Requirement Rationale V Note
until a
person
closes it.
UMR-045 Mandatory Every
detected
anomaly and
every human
response to
it shall be
written to the
audit record.
Keeps a full
history for
later review.
I Unchanged
UMR-046 Mandatory
(revised)
In phase 1,
CRAFT shall
produce
reports in
English,
using the
approved
report
templates.
Reports
include
costing
reports and
reports that
answer
engineering
questions or
reasoning
requests.
French
report
generation is
deferred to
phase 2.
The template
control
applies. The
report scope
gives UMR-
090 a
defined
object.
D Report
scope stated
UMR-047 Mandatory
(revised)
Reports shall
be built only
from sources
listed in the
approved
source
register
Ensures
reports use
controlled
information.
I Bound to
register and
ceiling

---

<!-- PDF page 39 -->

ID Type Requirement Rationale V Note
(UMR-051).
Every source
in the
register shall
be at or
below the
Protected B
ceiling in
UMR-058.
UMR-048 Mandatory The written
parts of a
report shall
be based on
retrieved
evidence
and shall
cite it, under
UMR-006
and UMR-
010.
Prevents
invented
report
content.
T Linked to
grounding
UMR-049 Mandatory
(revised)
CRAFT shall
not allow a
report to be
marked final
until an
authorized
reviewer
records an
approval.
A person
must
approve the
final
product.
T Made
enforceable
UMR-050 Mandatory Final reports
shall be held
under
version
control and
written to the
audit record.
Supports
document
control and
traceability.
I Unchanged
UMR-051 Mandatory
(revised)
CSA shall
maintain an
approved
source
register
listing every
The review
asked
whether
CRAFT must
scrape
documents
I, T Five
onboarding
controls
named inV3
from RC-01

---

<!-- PDF page 40 -->

ID Type Requirement Rationale V Note
repository,
system and
data feed
CRAFT is
permitted to
read, with
the
classificatio
n and owner
of each.
CRAFT shall
read only
from sources
in the
register. In
Phase 1 the
register shall
contain only
the
controlled
Engineering
Costing
document
corpus.
Personal
devices,
individual
OneDrive
accounts
and
production
CSA
repositories
shall not be
added until
each has
passed a
separately
approved
onboarding
process that
defines, at
from
individual
machines.
The answer
is no.
Naming the
five
onboarding
controls
prevents a
source being
added later
on the
strength of
convenience
alone.
<!-- PDF page 41 -->

ID Type Requirement Rationale V Note
minimum:
(a)
ownership;
(b) access
permissions;
(c) data
classificatio
n; (d)
retention; (e)
audit
controls.
UMR-052 Mandatory
(revised)
CRAFT shall
connect to
SharePoint
and
Confluence
through
documented
APIs, and to
any other
repository
listed in the
approved
source
register.
These
connectors
shall be built
in the
source-
onboarding
phase, not in
Phase 1.
CSA's target
state is that
all
repositories
move to CSA
SharePoint.
CRAFT shall
not depend
on
Phase 1 uses
a controlled
corpus, so
the
connectors
are not
needed yet.
D Deferred to
the source-
onboarding
phase

---

<!-- PDF page 42 -->

ID Type Requirement Rationale V Note
Confluence-
specific
behaviour
that would
prevent that
move.
UMR-053 Mandatory
(revised)
CRAFT shall
connect to
the CSA
financial
system of
record listed
in the
approved
source
register, for
approved
cost tasks. It
is handled at
Protected B
under
PBMM.
Access shall
be read-only
under UMR-
083.
Supports
cost
workflows
without
putting the
system of
record at
risk.
T In scope at
Protected B
UMR-054 Mandatory
(revised)
CRAFT shall
connect to
the mission
design tools
listed in the
approved
source
register,
which
currently
include STK
and MATLAB.
Keeps
engineering
workflows
connected.
D Traced to
UC-C8
UMR-055 Mandatory
(revised)
CRAFT shall
expose
approved
functions to
Controlled
interfaces
are essential
in a system
I, T Seven
criteria
separated

---

<!-- PDF page 43 -->

ID Type Requirement Rationale V Note
other
systems
through
documented
, version-
controlled,
secured
interfaces.
CRAFT may
use REST,
GraphQL,
event-based
messaging or
another
approved
style. Every
interface
shall define:
(a) its inputs;
(b) its
outputs; (c)
its error
handling; (d)
its access
rules; (e) its
activity
logging; (f) its
compatibility
rules; (g) its
plan for
retiring old
versions.
built from
many parts.
UMR-056 Mandatory
(revised)
CRAFT shall
meet a fixed
response-
time target
for each
interactive
request
class,
measured
under the
A task the
user starts
and collects
later is not
measured by
response
time.
T Report
generation
bound to
UMR-090

---

<!-- PDF page 44 -->

ID Type Requirement Rationale V Note
approved
load profile.
The targets
are: simple
question, 5
seconds;
retrieval-only
question, 5
seconds;
multi-step
analysis,
TBC. Report
generation is
not an
interactive
class; it runs
on demand
as a
background
task under
UMR-090.
Meeting a
target shall
not reduce
answer
quality,
safety
filtering or
citation
completenes
s.
UMR-057 Mandatory
(revised)
CRAFT shall
measure and
report
availability
during
approved
operating
hours. The
calculation
shall be
written down
End-to-end
availability
cannot be
promised by
the CRAFT
application
alone.
A, I Owner and
milestone

---

<!-- PDF page 45 -->

ID Type Requirement Rationale V Note
and
approved,
stating what
counts as
planned
maintenance
, what
counts as an
outside
failure, and
how
incidents are
classified. It
shall
separate
what the
CRAFT team
controls
from outside
services,
including
Azure
hosting,
identity,
model
providers,
data sources
and network.
The target
shall be
consistent
with the
Medium
availability
level in
PBMM
(PARAM-25).
UMR-058 Mandatory
(revised)
CRAFT shall
handle
information
according to
CSA-SEC-
A ceiling
alone is not a
control.
Protected B
covers the
T OP-04 and
OP-16
closed

---

<!-- PDF page 46 -->

ID Type Requirement Rationale V Note
POL-003.
CRAFT shall
be assessed
and
authorized at
the
Protected B /
Medium
integrity /
Medium
availability
(PBMM)
profile. The
highest
classificatio
n CRAFT is
approved to
hold is
Protected B.
CRAFT shall
detect and
reject the
ingestion of
any
document or
data feed
carrying a
classificatio
n above
Protected B,
and shall
record every
rejection in
the audit
record.
financial
system of
record and
the official
risk list.
UMR-059 Mandatory
(revised)
CRAFT shall
support 500
active
requests
being
processed at
the same
The
definition of
concurrency
is kept,
because the
original
wording
T Fixed by CSA
decision

---

<!-- PDF page 47 -->

ID Type Requirement Rationale V Note
time, under
the approved
load profile.
This is a fixed
target.
could not be
tested.
UMR-060 Withdrawn Merged into
UMR-006.
Identifier
retained as a
pointer. No
separate
requirement
applies.
The old
wording was
a weaker
duplicate of
UMR-006.
— Merged
UMR-061 Mandatory
(revised)
CRAFT shall
produce
traceability
reports in the
approved
export
format,
recording the
evidence
used, the
retrieval
path, the
reasoning
produced,
the
confidence
given, any
delegation,
and the
human
approvals or
rejections
made, for
every
medium-risk
and high-risk
decision
under UMR-
082.
Supports
audit and the
ability to
reconstruct
a decision.
D Retrieval
path and
delegation
added in P13

---

<!-- PDF page 48 -->

ID Type Requirement Rationale V Note
UMR-062 Mandatory
(revised)
A user
holding the
Auditor role
shall be able
to export a
time-
stamped
activity
history in the
approved
export
format,
covering
user
requests,
agent
actions,
retrieval
paths,
delegations,
sources
used,
recommend
ations,
decisions
and later
changes.
Supports
governance
reviews and
investigation
s.
D Scope
widened in
P13
UMR-063 Mandatory
(new)
CSA shall
maintain a
Configurable
Parameter
Baseline
Register
(Annex B).
Every
configurable
setting shall
have an entry
recording the
parameter
identifier, the
interim
Without the
register,
"configurabl
e" means
"no control".
I Completes
the three-
layer model

---

<!-- PDF page 49 -->

ID Type Requirement Rationale V Note
baseline
value, the
owner, the
evidence
status and
the next
review date.
A
configurable
setting shall
not be left
unset in an
operational
system.
UMR-064 Mandatory
(new)
CSA shall
maintain an
approved
acceptance
data set:
questions,
correct
answers and
source
passages,
held under
version
control. It
shall be used
to verify
UMR-001,
UMR-003,
UMR-004,
UMR-005,
UMR-007,
UMR-010,
UMR-018
and UMR-
094, and
reviewed
when the
corpus or the
model
Several
requirement
s depend on
this data set.
Nothing
required it to
exist.
I UMR-094
added to the
list in P13

---

<!-- PDF page 50 -->

ID Type Requirement Rationale V Note
changes.
UMR-065 Mandatory
(revised)
CRAFT shall
authenticate
every user
through the
approved
CSA Azure
identity
service
before any
request is
accepted.
CRAFT shall
enforce role-
based
access
control using
the role list
in Section
3.4. Every
user shall
hold at least
one role, and
a role shall
grant only
the
permissions
listed for it.
CRAFT shall
record the
role under
which every
action was
performed.
A Protected
B system
cannot run
on a single
all-powerful
account.
T Role list, OP-
13 closed
UMR-065.1 Mandatory
(new)
CRAFT shall
enforce
separation of
duties. The
user who
submits a
request shall
not be the
Self-
approval
makes an
approval
record
worthless.
T Added with
the role list
<!-- PDF page 51 -->

ID Type Requirement Rationale V Note
user who
approves it.
The user who
holds the
Auditor role
shall not
hold the
Administrato
r role.
UMR-066 Mandatory
(new)
CRAFT shall
enforce, at
query time,
the access
permissions
held by the
source
repository
for the
requesting
user, on
every
retrieval
path,
including
agent-
selected
retrieval and
file search
under UMR-
094. A user
shall not
receive, cite
or see a
passage
from a
document
they are not
permitted to
read in the
source
system.
At a
Protected B
ceiling this is
the primary
control
preventing
disclosure. A
retrieval tool
that reads
the corpus
directly
would
otherwise
bypass
index-level
trimming.
T Scope
widened to
all paths in
P13
UMR-067 Mandatory CRAFT shall T Chunk size

---

<!-- PDF page 52 -->

ID Type Requirement Rationale V Note
(new) import,
parse, split
and index
documents
from sources
in the
approved
source
register.
CRAFT shall
read the
classificatio
n label of
every
document
before
indexing it
and apply
the check in
UMR-058. In
the proof of
concept, a
document
with no
classificatio
n label shall
be treated as
Unclassified
(PARAM-35),
and every
such
document
shall be
recorded so
the
population
can be
reviewed.
CRAFT shall
re-index a
document
when the
document
could
otherwise be
cited forever.
Chunk size is
separated
from the
request
context floor.
setting, RC-

---

<!-- PDF page 53 -->

ID Type Requirement Rationale V Note
source
version
changes,
and shall
remove it
from the
index and
stop citing it
when the
source is
deleted,
withdrawn or
superseded.
Chunk size
shall be a
configurable
setting
(PARAM-39).
Indexing
delay shall
be a
configurable
setting
(PARAM-28).
UMR-068 Mandatory
(new)
CRAFT shall
treat all
retrieved
document
content as
untrusted
data, not as
instructions.
CRAFT shall
detect and
neutralise
instruction-
like content
in retrieved
passages.
Defence
shall be
measured
An
instruction
hidden in a
document
can now
steer both
generated
code and the
choice of
search tool,
not only the
wording of
an answer.
T Test set
scope
widened in
P13

---

<!-- PDF page 54 -->

ID Type Requirement Rationale V Note
against the
approved
prompt-
injection test
set (PARAM-
29), which
shall include
cases
targeting
code
execution
under UMR-
093 and
retrieval tool
selection
under UMR-
094.
UMR-069 Mandatory
(new)
CRAFT shall
encrypt data
in transit and
at rest using
the approved
Azure
encryption
services and
algorithms,
at the
strength
required by
PBMM.
Secrets and
credentials
shall be held
in Azure Key
Vault or an
equivalent
approved
secret store,
and shall not
appear in
prompts,
logs, source
A Protected
B ceiling
raises the
assurance
level for
credential
handling.
T Session
workspace
included

---

<!-- PDF page 55 -->

ID Type Requirement Rationale V Note
code, or the
session
workspace.
UMR-070 Mandatory
(new)
CRAFT shall
be hosted on
Microsoft
Azure, in a
PBMM-
assessed
environment.
CRAFT shall
store and
process CSA
data only
within
Canadian
Azure
regions,
including
files
uploaded by
users and
files created
in a session
workspace.
Hosting in
Canadian
Azure
regions
under a
PBMM
authorization
satisfies the
residency
obligation.
I Session
workspace
included
UMR-071 Withdrawn Withdrawn
by CSA
decision. No
Algorithmic
Impact
Assessment
is required.
Identifier
retained. No
requirement
applies.
The Directive
was moved
to the
background
list.
— See OP-14
UMR-072 Mandatory
(new)
CRAFT shall
identify
personal
information
held in
memory,
Protected B
material
routinely
contains
personal
information.
T Session
workspace
included

---

<!-- PDF page 56 -->

ID Type Requirement Rationale V Note
prompts,
retrieved
content,
session
workspaces
and audit
records, and
shall provide
a way to find
and delete it
on request,
except
where a
record must
be kept
under UMR-
073.
UMR-073 Mandatory
(new)
CRAFT
records,
including
audit
records,
shall be
retained and
disposed of
according to
the
applicable
CSA records
retention
schedule.
The
schedule
and the
retention
period are
TBC.
Audit
records
cannot be
kept forever
without a
schedule.
I TBC, OP-07
UMR-074 Mandatory
(new)
CRAFT shall
be backed
up and
recoverable
within the
Nothing
covered data
loss or
recovery.
D From Azure
service tiers

---

<!-- PDF page 57 -->

ID Type Requirement Rationale V Note
approved
recovery
point and
recovery
time
objectives
(PARAM-30,
PARAM-31).
Recovery
shall be
demonstrate
d at the
approved
interval.
UMR-075 Goal (phase
2)
In phase 2,
CRAFT shall
answer in the
language of
the question
unless the
user asks for
another
language. In
phase 1,
CRAFT
answers in
English.
Kept as a
phase-2 goal
so the need
is not lost.
T Phase-2
Goal
UMR-076 Withdrawn Withdrawn
by CSA
decision. No
French-
language
quality
standard
applies at
this phase.
Identifier
retained.
CRAFT does
not generate
French
output in
phase 1.
— OP-10
closed
UMR-077 Mandatory
(new)
CRAFT shall
support
mission
planning by
Mission
planning
support is
named in the
T Traced to
UC-C8

---

<!-- PDF page 58 -->

ID Type Requirement Rationale V Note
retrieving
planning
evidence,
summarising
mission
parameters
and
constraints,
comparing
options
against
recorded
criteria, and
citing the
source of
every
parameter
used. CRAFT
shall not
change
mission
parameters.
A change to
a mission
parameter is
high-risk
under UMR-
082.
scope.
UMR-078 Mandatory
(new)
CRAFT shall
acquire
telemetry
and system
health data
from the
feeds listed
in the
approved
source
register, at
the
configured
interval
Anomaly
detection
needs data
CRAFT is
obliged to
acquire.
D Added

---

<!-- PDF page 59 -->

ID Type Requirement Rationale V Note
(PARAM-32).
UMR-079 Mandatory
(new)
CRAFT shall
deliver
approval
requests and
anomaly
reports
through the
approved
notification
channels,
route each to
the assigned
role, and
track
delivery and
acknowledge
ment.
Reports and
approval
requests
need a
delivery
channel.
T Added
UMR-080 Mandatory
(new)
CRAFT shall
monitor
answer
quality,
grounding,
confidence
calibration
and retrieval
quality over
time, and
raise an alert
when a
measure
falls below
its baseline
by more than
the
configured
margin
(PARAM-33).
Monitoring
shall cover
each
retrieval path
Quality
degrades
silently after
a model or
corpus
change. With
agent-
selected
retrieval, one
path can
degrade
while the
aggregate
looks
healthy.
T Per-path
monitoring
added in P13

---

<!-- PDF page 60 -->

ID Type Requirement Rationale V Note
separately.
UMR-081 Mandatory
(new)
CRAFT shall
allow the
language
model to be
replaced
without
changing
application
code. CRAFT
shall re-run
the
acceptance
set after any
model
change,
including a
change
made by the
model
provider, and
record the
result.
Providers
update
models
without
CSA's
involvement.
The
confidence
method in
UMR-007 no
longer
constrains
this,
because it
does not
need token
probabilities.
T Constraint
removed by
the UMR-007
decision
UMR-082 Mandatory
(new)
CRAFT shall
use one
classificatio
n scheme for
actions and
findings,
covering: (a)
action
reversibility
— read-only,
reversible,
irreversible;
(b) action
risk tier—
low,
medium,
high; (c)
finding
severity—
Every
human-
approval
trigger
depends on
this.
I Workspace
export added
in P13
<!-- PDF page 61 -->

ID Type Requirement Rationale V Note
low,
medium,
high, critical.
The scheme
shall state
which
combination
s require
human
approval.
High-risk
actions shall
include, at
minimum:
spending
commitment
s, changes to
the official
risk list,
changes to
mission
parameters,
code
execution
that writes
outside the
session
workspace,
export of
session
workspace
content
outside
CRAFT, and
any
irreversible
action. The
scheme
shall be held
under
change
control.

---

<!-- PDF page 62 -->

ID Type Requirement Rationale V Note
UMR-083 Mandatory
(new)
CRAFT shall
have read-
only access
to the CSA
financial
system of
record.
CRAFT shall
not write to
it.
Read-only
matters
more now
the source is
confirmed in
scope at
Protected B.
T Confirmed
applicable
UMR-084 Mandatory
(new)
CRAFT shall
provide user
guidance in
English,
covering
what CRAFT
can and
cannot do,
how to read
a citation,
how
confidence
scores
should be
interpreted,
the limits of
agent-
generated
analysis
code, and
how to read
the retrieval
path shown
with an
answer.
Users who
do not
understand
the limits of
the tool will
over-trust it.
I Retrieval
path
guidance
added in P13
UMR-085 Mandatory
(new)
The first
operational
release shall
support 50
active
requests
being
Both figures
are fixed
requirement
s, one per
phase.
T From
assumption
OA-04

---

<!-- PDF page 63 -->

ID Type Requirement Rationale V Note
processed at
the same
time, under
the approved
load profile.
This is a fixed
target.
UMR-086 Mandatory
(new, split
from UMR-
010)
If CRAFT
does not
hold enough
retrieved
evidence to
answer, it
shall say so,
ask a
clarifying
question, or
decline to
answer.
CRAFT shall
not answer
from the
model's own
knowledge
alone.
A distinct
behaviour
from
measuring
grounding.
T Split from
UMR-010
UMR-087 Mandatory
(new, split
from UMR-
029)
For an
irreversible
action,
CRAFT shall
first obtain
explicit
approval
from an
authorized
person.
Before the
action runs,
CRAFT shall
show what
will change
and what the
effect will
Some
actions
cannot be
undone.
T Split from
UMR-029

---

<!-- PDF page 64 -->

ID Type Requirement Rationale V Note
be.
UMR-088 Mandatory
(new, split
from UMR-
029)
Any change
CRAFT
makes to a
database, a
system
setting or
program
code shall
use version
control, a
backup or an
equivalent
method, so
the
previously
approved
state can be
restored.
This control
was dropped
from its
mirror and is
important
enough to
carry its own
identifier.
T Split from
UMR-029
UMR-089 Mandatory
(new, split
from UMR-
041)
Every
anomaly
report shall
state the
affected
system, the
time, the
severity
under UMR-
082, the
supporting
evidence
and the
recommend
ed next step.
Report
content is a
separate,
testable rule
from
detection.
D Split from
UMR-041
UMR-090 Mandatory
(revised)
A long-
running task
may run in
the
background.
Report
generation is
a
Naming
report
generation
and its scope
makes the
on-demand
decision
testable
D Report
scope stated

---

<!-- PDF page 65 -->

ID Type Requirement Rationale V Note
background
task and
runs on
demand,
covering
costing
reports and
reports
answering
engineering
questions or
reasoning
requests. For
every
background
task, CRAFT
shall show
progress,
allow the
user to
cancel it,
and report
when it is
finished.
without a
time figure.
UMR-091 Mandatory
(new)
The
approved
source
register shall
record, for
every
source,
whether it
holds real
CSA data or
simulated
data. CRAFT
shall label
every
retrieved
passage and
every
citation that
Phase 1 runs
on a
controlled
simulated
corpus. A
simulated
cost
estimate
mistaken for
a real one is
a direct route
to a bad
decision.
T Verification
owner TBD,
OP-21

---

<!-- PDF page 66 -->

ID Type Requirement Rationale V Note
comes from
a simulated
source, and
shall not
present
simulated
data as real
mission
evidence.
Before any
source
holding real
CSA data is
added, the
controls in
UMR-051
and the
classificatio
n controls in
UMR-058,
UMR-066
and UMR-
067 shall be
verified as
working. The
owner of that
verification
and the
review at
which it is
held are
TBD.
UMR-092 Mandatory
(revised)
CRAFT shall
give each
session an
isolated
workspace in
which the
agent may
create files,
such as
charts,
The review
asked
whether
each session
gets its own
filespace.
The
response
sets the
default to
T Ephemeral
default and
export
control
added inV3
from RC-10

---

<!-- PDF page 67 -->

ID Type Requirement Rationale V Note
scripts,
tables and
draft
documents.
The
workspace
shall be
ephemeral
by default: it
shall be
destroyed
when the
session
closes.
Persistence
beyond a
session shall
require an
approved
reason and
shall follow
the retention
period in
PARAM-41. A
workspace
shall be
isolated from
every other
session,
shall inherit
the data
classificatio
n of the
material
placed in it,
and shall be
held in Azure
within
Canadian
regions. A
user shall be
able to list,
ephemeral
and requires
export
control. An
indefinitely
retained
workspace
becomes an
uncontrolled
data store
holding
Protected B
derivatives,
and an
uncontrolled
export is the
shortest
path from a
classified
corpus to
somewhere
it should not
be.

---

<!-- PDF page 68 -->

ID Type Requirement Rationale V Note
download
and delete
the contents
of their own
workspace.
Export of
workspace
content
outside
CRAFT shall
be
controlled,
recorded in
the audit
record, and
subject to
the limits in
PARAM-46.
Files in a
workspace
shall not be
treated as
approved
sources and
shall not be
indexed for
retrieval
unless
added to the
approved
source
register.
UMR-093 Mandatory
(new)
CRAFT may
generate and
run analysis
code, such
as a script
for statistical
inference
over tabular
data, to
answer a
The review
proposed
that agents
write and run
scripts for
data
analysis.
This is a
genuine
capability
T See ASG-011

---

<!-- PDF page 69 -->

ID Type Requirement Rationale V Note
user request.
All generated
code shall
run inside
the
containment
described in
ASG-011.
CRAFT shall
record the
code, its
inputs, its
outputs and
its exit status
in the audit
record, and
shall present
the code to
the user
alongside
any result
derived from
it. A result
produced by
generated
code shall
carry the
same
citation and
confidence
obligations
as any other
answer.
Code that
would write
outside the
session
workspace is
a high-risk
action under
UMR-082.
gain and the
highest-risk
item in the
commentary
, so its
containment
is specified
rather than
assumed.
UMR-094 Mandatory The primary The review T Added in

---

<!-- PDF page 70 -->

ID Type Requirement Rationale V Note
(new) agent may
select
among
authorized
retrieval
tools to
answer a
request, and
may iterate.
The
authorized
tool set shall
be held in
the tool
registry
under UMR-
012 and shall
include, at
minimum:
meaning-
based
search,
keyword
search,
metadata
filtering, and
a
parameteris
ed file-
search
interface.
The file-
search
interface
shall accept
a fixed set of
named
inputs such
as path
scope,
filename
pattern and
proposed
that the
agent
choose how
to search,
including
constructing
commands
such as grep
or find. The
capability is
useful: a
traceability
question and
a definition
lookup want
different
strategies,
and a single
fixed pipeline
serves one of
them badly.
Free-form
shell strings
are not
acceptable,
because the
command
space is
unbounded,
unauditable,
and open to
injection
from
ingested
content. A
parameteris
ed interface
preserves
the
capability
and keeps
P13. Gap 1
closed, RC-
<!-- PDF page 71 -->

ID Type Requirement Rationale V Note
content
pattern.
CRAFT shall
not permit
an agent to
compose or
execute free-
form shell or
command-
line strings.
The
normalised,
fused default
path in UMR-
004 shall
remain
available and
shall be the
default
where the
agent
expresses no
preference.
The number
of retrieval
iterations per
request shall
be a
configurable
setting
(PARAM-43).
Every tool
selection
shall be
recorded in
the retrieval
path under
ARR-010,
and every
path shall be
subject to
UMR-066.
the
boundary.

---

<!-- PDF page 72 -->

ID Type Requirement Rationale V Note
UMR-095 Mandatory
(new)
CRAFT shall
provide a
conversation
al interface.
Each session
shall have
one primary
agent that
persists for
the life of the
session,
holds the
episodic
memory
defined in
UMR-014,
and is bound
to the
session
workspace
defined in
UMR-092.
The session,
its agent
context, and
its
workspace
shall end
together.
Session
lifetime and
idle timeout
shall be
configurable
settings
(PARAM-44).
A session
shall be tied
to one
authenticate
d user under
UMR-065,
The review's
stated
direction
was a chat
interface
with a
persistent
agent rather
than one-
shot model
calls
augmented
with
retrieval. V2
covered free-
text
questions
and
workspaces
but never
stated the
interaction
model, so
the
persistence,
ownership
and lifetime
of a session
were
undefined.
Ending the
session, the
agent
context and
the
workspace
together
prevents
orphaned
state holding
Protected B
derivatives.
T Added in
P13. Gap 2
closed, RC-

---

<!-- PDF page 73 -->

ID Type Requirement Rationale V Note
and session
state shall
not be
readable by
any other
session.
### 4.2 Agent requirements (detail)
Every tag mirrors one or more requirements in Section 4.1. Where the two appear to differ,
Section 4.1 governs.
#### 4.2.1 How agents are built
Tag Type Requirement Mirrors V
AAR-001 Mandatory
(revised)
Each session
shall have one
accountable
primary agent.
Fixed agent
roles shall not
be imposed,
and multiple
agents shall not
be used by
default.
UMR-011, UMR-
095
I
AAR-002 Mandatory
(revised)
An agent shall
use only the
tools listed in
the approved
tool registry for
its task,
including
retrieval tools.
UMR-012 T
AAR-003 Mandatory
(revised)
Agents shall run
within a
configurable
budget covering
time, tokens,
tool calls,
reasoning
steps, retrieval
iterations,
UMR-013, UMR-
030
T

---

<!-- PDF page 74 -->

Tag Type Requirement Mirrors V
delegated
subtasks,
estimated cost,
and code
execution
resources.
When the
budget is used
up, the agent
shall stop
safely, return
any useful
partial result,
record the
reason, and ask
the user what to
do next.
AAR-004 Mandatory
(revised)
Agents shall
have episodic,
semantic and
procedural
memory as
defined in UMR-
014, each with a
defined
retention period
and deletion
path. Semantic
memory entries
shall be source-
backed.
Procedural
memory shall
be approved
and version-
controlled.
UMR-014 I, T
AAR-005 Mandatory Agent-to-agent
messages shall
include the
agent identifier,
the action, the
input, the
UMR-015 I

---

<!-- PDF page 75 -->

Tag Type Requirement Mirrors V
output, a
confidence
score and a
timestamp.
AAR-006 Mandatory
(revised)
An agent shall
be able to be
started or
stopped while
the platform
continues to
serve requests.
Requests
running
elsewhere shall
not fail.
UMR-016 D
AAR-007 Mandatory
(revised)
An agent shall
not read,
change or
delete data,
system
functions or
system settings
outside its
registered tool
permissions.
UMR-017 T
AAR-008 Mandatory
(new)
Agent memory
shall be isolated
per user and per
data
classification.
One session's
memory shall
not be readable
in another
session.
UMR-014, UMR-
058, UMR-095
T
AAR-009 Mandatory
(new)
An agent shall
not modify its
own
instructions,
prompts, tool
permissions,
code, or
UMR-028 T

---

<!-- PDF page 76 -->

Tag Type Requirement Mirrors V
procedural
memory.
Changes go
through UMR-
028.
AAR-010 Mandatory
(new)
Where the
primary agent
delegates a
subtask, it shall
record the
reason and the
bounds, shall
validate the
returned result
before use, and
shall integrate it
into the final
response. The
primary agent
remains
accountable for
the response
given to the
user.
UMR-011 T
#### 4.2.2 How agents plan, search and answer
Tag Type Requirement Mirrors V
ARR-001 Mandatory CRAFT shall
break a
complex
request into
steps and
record the plan.
UMR-018 T
ARR-002 Mandatory
(revised)
CRAFT shall
retrieve using
keyword and
vector search
behind a
common
interface,
normalising,
fusing and
UMR-004, UMR-
005
I, T

---

<!-- PDF page 77 -->

Tag Type Requirement Mirrors V
deduplicating
the results.
Appending the
raw top results
of each method
is prohibited.
Weights shall
be configurable
and version-
controlled.
Phase 1
baseline: 0.7
semantic, 0.3
lexical.
ARR-003 Mandatory
(revised)
Every answer
shall name, for
each fact used,
the source
document, its
version and the
page or section.
Where the
format has no
such markers,
the passage
locator shall be
given.
UMR-006 D
ARR-004 Mandatory
(revised)
Every answer
shall carry a
confidence
score between
0 and 1,
computed from
evidence
coverage,
citations,
source
traceability,
source
agreement,
retrieval quality
and
UMR-007 D

---

<!-- PDF page 78 -->

Tag Type Requirement Mirrors V
unsupported-
claim detection.
Token-
probability
scoring shall
not be used.
ARR-005 Mandatory
(revised)
An output with a
confidence
score below the
approved
threshold for its
risk tier shall be
routed to the
Reviewer role.
Interim baseline
value: 0.6.
UMR-008, UMR-
065
T
ARR-006 Mandatory
(revised)
If the first
search does not
meet the
sufficiency
condition, the
agent shall
search again
with adjusted
terms or
another
authorized
retrieval tool, up
to the
configured
iteration limit.
UMR-009, UMR-
094
T
ARR-007 Mandatory
(revised)
All generated
content shall be
based on
retrieved
evidence. The
pass score, test
method and
checking tool
shall be written
down before
acceptance
UMR-010 T

---

<!-- PDF page 79 -->

Tag Type Requirement Mirrors V
testing.
ARR-008 Mandatory
(new)
If the evidence
is not sufficient,
the agent shall
say so, ask a
clarifying
question, or
decline to
answer. It shall
not answer from
the model's
own knowledge
alone.
UMR-086 T
ARR-009 Mandatory
(new)
Where an agent
derives a result
by running
generated code,
the answer shall
state that code
was used, show
the code, and
cite the data the
code read.
UMR-093, UMR-
006
D
ARR-010 Mandatory
(new)
CRAFT shall
record the
retrieval path
for every
answer: which
retrieval tools
were used, in
what order, with
what
parameters,
and how many
iterations were
run. The
retrieval path
shall be
available to the
user on request,
shall
accompany
UMR-094, UMR-
027, UMR-061
T

---

<!-- PDF page 80 -->

Tag Type Requirement Mirrors V
every approval
request, and
shall be written
to the audit
record.
4.2.3 Human review and approval
Tag Type Requirement Mirrors V
HITL-001 Mandatory
(revised)
CRAFT shall
obtain approval
from an
authorized
person before
any action
classified as
high-risk under
UMR-082.
UMR-021, UMR-
082
T
HITL-002 Mandatory
(revised)
High-risk
actions are
those listed in
the scheme
under UMR-082,
including
spending
commitments,
changes to the
official risk list,
changes to
mission
parameters,
code execution
writing outside
the session
workspace,
workspace
export outside
CRAFT, and any
irreversible
action.
UMR-082 I
HITL-003 Mandatory
(revised)
Every approval
request shall
show the
UMR-022, ARR-
010
D
<!-- PDF page 81 -->

Tag Type Requirement Mirrors V
reasoning, the
confidence
score, the
source
documents
used and the
retrieval path.
HITL-004 Mandatory
(revised)
A person
holding the
Approver role
shall be able to
approve, reject
or edit a
recommendatio
n before it
becomes final.
UMR-023, UMR-
065
D
HITL-005 Mandatory
(revised)
If a
recommendatio
n is rejected,
the agent may
try again using
the reviewer's
correction, up
to the
configured retry
limit.
UMR-024 T
HITL-006 Mandatory
(revised)
If no decision is
recorded within
the configured
timeout, the
request shall be
escalated to the
Backup
approver, then
cancelled and
flagged if still
undecided. If no
Backup
approver is
named, the
request shall
stay open and
UMR-025 T

---

<!-- PDF page 82 -->

Tag Type Requirement Mirrors V
be flagged, not
cancelled.
Interim baseline
timeout: 24
hours.
HITL-007 Mandatory Every approval,
rejection or edit
shall be logged
with who did it,
what was
decided, when
and why.
UMR-026 I
HITL-008 Mandatory
(new)
A request
reporting a high-
severity
operational
anomaly shall
not be
cancelled by
timeout. It shall
remain open
until a person
closes it.
UMR-025, UMR-
044
T
#### 4.2.4 Safety and oversight
Tag Type Requirement Mirrors V
ASG-001 Mandatory
(revised)
CRAFT shall
filter generated
content against
the approved
content policy
list, measured
against the
approved
adversarial test
set.
UMR-020 T
ASG-002 Mandatory
(revised)
Every agent
action shall be
classified as
read-only,
reversible or
irreversible
UMR-029, UMR-
087, UMR-088
T

---

<!-- PDF page 83 -->

Tag Type Requirement Mirrors V
under UMR-082.
A reversible
action shall be
checked before
it runs, shall
save the earlier
state or a
version marker,
shall be logged,
and shall be
undoable. An
irreversible
action shall
require explicit
human approval
first, with a
preview of what
will change.
ASG-003 Mandatory
(revised)
CRAFT shall
write every
agent decision
and action to
append-only
storage,
including
retrieval paths,
delegations,
workspace
exports and
code execution.
No platform
role, including
administrator,
shall be able to
change or
delete a record.
UMR-027 T
ASG-004 Mandatory
(revised)
CRAFT shall
limit resource
use per user,
per session, per
task and per
agent, covering
UMR-030 T

---

<!-- PDF page 84 -->

Tag Type Requirement Mirrors V
tokens,
concurrent
tasks,
estimated cost,
tool calls, call
rate, retrieval
iterations,
delegated
subtasks, and
code execution
time and
memory. Soft
limits shall warn
and slow new
work. Hard
limits shall stop
the task safely.
ASG-005 Mandatory
(revised)
If an agent
repeats an
action matching
the approved
repetition test
with no new
information,
CRAFT shall
stop the task
and escalate.
Interim baseline
value: 3.
UMR-019 T
ASG-006 Mandatory
(revised)
Every version of
an agent's
model settings,
prompts, tool
permissions
and procedural
memory shall
be version-
controlled,
reviewed and
approved
before
operational use.
UMR-028 I

---

<!-- PDF page 85 -->

Tag Type Requirement Mirrors V
ASG-007 Mandatory
(new)
Retrieved
content shall be
treated as data,
never as
instructions.
Instruction-like
content shall be
detected and
neutralised,
measured
against the
approved
prompt-
injection test
set, including
cases targeting
code execution
and retrieval
tool selection.
UMR-068 T
ASG-008 Mandatory
(new)
The audit store
shall be held in
an Azure service
configured with
immutable,
time-based
retention, so
that no role,
including the
administrator
role, can
change or
delete a record.
UMR-027, UMR-
065
T
ASG-009 Mandatory
(new)
CRAFT shall
refuse to index
any document
whose
classification is
above the
Protected B
ceiling, shall not
retain the
content of a
UMR-058, UMR-
067
T

---

<!-- PDF page 86 -->

Tag Type Requirement Mirrors V
refused
document, and
shall write the
refusal to the
audit record.
ASG-010 Mandatory
(new)
CRAFT shall
apply the
controls
required by the
PBMM profile
for Protected B
information,
and shall record
the mapping
between each
PBMM control
and the
requirement
that
implements it.
UMR-058, UMR-
069, UMR-070
I
ASG-011 Mandatory
(new)
Generated code
shall run in a
contained
environment
that: (a) has no
network access
by default; (b)
can read only
the data
explicitly
passed to it; (c)
can write only
inside the
session
workspace; (d)
runs under the
limits in
PARAM-42; (e)
has no access
to secrets,
credentials or
the audit store;
UMR-093, UMR-
069, UMR-082
T

---

<!-- PDF page 87 -->

Tag Type Requirement Mirrors V
(f) is destroyed
after the task.
Every execution
shall be
recorded with
its code, inputs,
outputs and exit
status. An
attempt to act
outside the
containment
shall be
stopped and
flagged to the
Security
authority role.
ASG-012 Mandatory
(new)
Agent retrieval
shall be
constrained at
the tool
boundary.
CRAFT shall
expose only the
retrieval tools
listed in the
approved tool
registry. CRAFT
shall not expose
a shell, a
command-line
interpreter, or
any interface
accepting a
free-form
command
string. The file-
search tool
shall accept
only named
parameters and
shall be
confined to the
UMR-094, UMR-
012, UMR-066
T

---

<!-- PDF page 88 -->

Tag Type Requirement Mirrors V
path scope of
sources in the
approved
source register.
Permission
trimming under
UMR-066 shall
apply to every
retrieval tool,
including direct
file search.
Every tool
selection, its
parameters,
and every
blocked
attempt shall be
written to the
audit record
and made
available to the
Security
authority role.
5. Architecture
### 5.1 Status
No Architecture Design Document exists. CSA-CRAFT-AD-0001 Draft A1 contains a cover
page and two framing paragraphs, with no interfaces, data flow, trust boundaries,
deployment view or decision records. RD-01 is treated as not available. Section 5.2 is an
allocation view only, not an architecture, and nothing in it is approved for procurement.
### 5.2 Building blocks implied by the requirements
Block Purpose Requirements it must satisfy
Ingestion and parsing Imports documents,
extracts text and metadata,
chunks, checks
classification
UMR-051, UMR-058, UMR-
067, ASG-009
Knowledge store Search index for meaning-
based search, and a
UMR-004, UMR-067

---

<!-- PDF page 89 -->

Block Purpose Requirements it must satisfy
knowledge graph
Retrieval engine Keyword and vector retrieval
behind one interface,
normalisation, fusion,
deduplication, permission
trimming
UMR-004, UMR-005, UMR-
066
Retrieval tool layer Authorized retrieval tools
exposed to the agent,
including parameterised file
search
UMR-094, UMR-012, ASG-
012
Primary agent and
delegation
Plans tasks, calls tools,
writes answers, delegates
bounded subtasks, validates
results
UMR-011 to UMR-019, UMR-
095, all AAR
Memory services Episodic, semantic and
procedural memory, with
curation, approval, retention
and isolation
UMR-014, UMR-072, UMR-
073, AAR-004, AAR-008
Session workspace Ephemeral per-session
filespace for agent-created
files, with controlled export
UMR-092, UMR-069, UMR-
070, UMR-072
Code execution sandbox Contained environment for
generated analysis code
UMR-093, ASG-011, UMR-
030
Grounding and confidence
service
Binds answers to evidence,
computes confidence from
six named inputs, detects
unsupported claims
UMR-006 to UMR-010, UMR-
086
Human review workflow Shows evidence and
retrieval path, records
decisions, handles timeout
and escalation
UMR-021 to UMR-026, all
HITL
Audit and logging Append-only record
covering actions, retrieval
paths, delegations, exports
and code execution
UMR-015, UMR-027, UMR-
061, UMR-062, ASG-008
Safety services Content filtering, action
classification, injection
defence, resource governor,
tool and code containment
UMR-020, UMR-029, UMR-
030, UMR-068, UMR-082, all
ASG
Integration layer Controlled connections to UMR-052 to UMR-055, UMR-

---

<!-- PDF page 90 -->

Block Purpose Requirements it must satisfy
the financial system, STK,
MATLAB, data feeds, and
later repositories
078, UMR-083
Identity and access Azure identity, user role
model, Protected B ceiling
enforcement, session
ownership
UMR-058, UMR-065, UMR-
065.1, UMR-066, UMR-095
Interface layer Conversational session
interface, progress,
cancellation, guidance
UMR-001, UMR-055, UMR-
079, UMR-084, UMR-090,
UMR-095
Monitoring Availability, performance,
per-path retrieval quality,
drift, recovery
UMR-056, UMR-057, UMR-
074, UMR-080
Deployment infrastructure
Azure is the deployment infrastructure for CRAFT. The on-premises infrastructure estimate
in Appendix A is withdrawn in full. Those figures do not convert: an on-premises estimate
counts machines, uplinks and disks; an Azure deployment is specified by service tiers,
instance families, regional capacity and consumption. Azure sizing shall be derived from
first principles in RD-01.
Workload assumptions retained from Appendix A:
Assumption Value Where it is carried
Phase-1 concurrency 50 active requests at the
same time
UMR-085
Target concurrency 500 active requests at the
same time
UMR-059
Availability 99.5 percent during CSA
operating hours
PARAM-25, UMR-057
Azure service classes implied by the requirements. An allocation list, not a design. No tier,
size, quantity or cost is stated, because none has been derived.
Building block Azure service class needed Driven by
Ingestion and parsing Compute for background
workers; document parsing
service
UMR-067
Knowledge store Managed vector index;
managed graph or relational
store
UMR-004, UMR-067
<!-- PDF page 91 -->

Building block Azure service class needed Driven by
Retrieval engine and tool
layer
Search service supporting
keyword and vector
retrieval, with permission
trimming and a constrained
file-search facility
UMR-004, UMR-005, UMR-
066, UMR-094
Model inference Managed model endpoint in
a Canadian region, with a
substitution path
UMR-070, UMR-081
Primary agent runtime Application compute with
autoscale and session
affinity
UMR-095, UMR-059, UMR-
085
Memory services Cache and persistent store,
isolated per user and per
classification
UMR-014, AAR-008
Session workspace Isolated ephemeral file
storage with lifecycle policy
and export control
UMR-092
Code execution sandbox Isolated container runtime
with no default network
egress
UMR-093, ASG-011
Human review workflow Workflow or queue service
with state persistence
UMR-021 to UMR-026
Audit and logging Immutable storage with
time-based retention
UMR-027, UMR-073, ASG-
008
Identity and access Azure identity, role-based
access control
UMR-065, UMR-065.1
Secrets and encryption Key Vault or approved
equivalent; platform
encryption at PBMM
strength
UMR-069
Backup and recovery Geo-redundant backup
within Canadian regions
UMR-074, UMR-070
Monitoring Platform monitoring, log
analytics, per-path quality
alerting
UMR-057, UMR-080
All of these shall sit inside a PBMM-assessed Azure landing zone in Canadian regions only,
as required by UMR-070. The definitive topology, service tiers, redundancy model, scaling
policy and cost position shall be fixed in RD-01 under ADR-08 and ADR-18.

---

<!-- PDF page 92 -->

### 5.3 Required content of the Architecture Design Document
Every architecture decision shall be recorded as an Architecture Decision Record (ADR),
with a Satisfies field naming the requirement identifiers it implements and a Sets baseline
for field naming the Annex B parameters it fixes. A DESIGN DECISIONwithout both fields is
not complete.
§ Section Minimum content Traces to
1 Introduction and
definitions
Purpose, readership,
acronym table,
relationship to CSA-
CRAFT-RD-0001
—
2 Applicable
documents
AD-01 to AD-08, plus
hosting and security
standards
AD-01 to AD-08
3 Architecture drivers The constraints that
shape the design
UMR-058, UMR-065
to UMR-073
4 Context view External systems,
users, data in and
out, trust boundaries
UMR-051 to UMR-
055, UMR-078
5 Functional view Allocation of every
requirement
identifier to a
component
all
6 Information view Document model,
chunking, metadata,
classification labels,
graph schema
UMR-058, UMR-067,
UMR-073
7 Retrieval design Keyword and vector
retrieval, common
interface,
normalisation,
fusion,
deduplication,
threshold validation,
reranking,
permission
trimming, evaluation
harness
UMR-004, UMR-005,
UMR-064, UMR-066
8 Agent design and
delegation
Primary agent
model, tool registry,
delegation criteria
UMR-011 to UMR-
019, UMR-095, AAR-
001 to AAR-010

---

<!-- PDF page 93 -->

§ Section Minimum content Traces to
and bounds,
validation and
integration, planner,
budget
enforcement, loop
breaker
9 Retrieval tool design Authorized tool set,
parameterised file-
search interface,
iteration control,
path recording
UMR-094, ARR-010,
ASG-012
10 Memory design Episodic, semantic
and procedural
implementation,
curation and
approval workflow,
isolation, retention,
deletion
UMR-014, UMR-072,
UMR-073, AAR-004
11 Grounding and
confidence design
Evidence binding,
citation generation,
six-input confidence
model, source
agreement,
unsupported-claim
detection,
calibration
UMR-006 to UMR-
010, UMR-086, ARR-
003 to ARR-008
12 Human review
workflow engine
State model,
queues, roles,
timeout, backup
approver, preview
rendering
UMR-021 to UMR-
026, HITL-001 to
HITL-008
13 Audit and logging
mechanism
Record schema,
append-only store,
integrity proof,
export, retention,
retrieval path and
delegation records
UMR-015, UMR-027,
UMR-061, UMR-062,
ASG-003, ASG-008
14 Safety architecture Action classification,
reversibility, content
filter, injection
defence, resource
UMR-020, UMR-029,
UMR-030, UMR-068,
UMR-082, ASG-001
to ASG-012

---

<!-- PDF page 94 -->

§ Section Minimum content Traces to
governor, tool and
code containment
15 Integration
architecture
Connector pattern,
authentication, rate
limits, read-only
enforcement,
source-onboarding
controls
UMR-051 to UMR-
055, UMR-078, UMR-
083
16 Deployment
topology
Azure environments
in a PBMM-assessed
landing zone,
Canadian regions,
service tiers, sizing,
scaling, backup,
cost position
UMR-057, UMR-059,
UMR-070, UMR-074,
UMR-085
17 Performance and
capacity design
Interactive request
classes, background
execution, session
affinity, queueing,
load model
UMR-056, UMR-059,
UMR-090, UMR-095
18 Security architecture Azure identity, user
role model,
separation of duties,
encryption, Key
Vault, Protected B
enforcement,
sandbox and tool
threat model, PBMM
control mapping
UMR-017, UMR-058,
UMR-065, UMR-066,
UMR-069, UMR-093,
UMR-094, ASG-010
to ASG-012
19 Operability Monitoring, per-path
drift detection,
model change
management,
incident handling
UMR-080, UMR-081
20 Architecture
Decision Records
One per decision,
with Satisfies, Sets
baseline for,
Alternatives,
Evidence
all
21 Requirement-to-
component
Every UMR, AAR,
ARR, HITL and ASG
all

---

<!-- PDF page 95 -->

§ Section Minimum content Traces to
traceability matrix mapped to a
component and an
ADR
A Annex A Baseline parameter
values with
supporting evidence
Annex B of this
document
B Annex B Open design
decisions still to be
tested
Annex E of this
document
Minimum set of Architecture Decision Records:
ADR Decision Satisfies
ADR-01 Retrieval methods, common
interface, normalisation,
fusion and deduplication
UMR-004, UMR-005, ARR-
002
ADR-02 Permission trimming across
every retrieval path
UMR-066, UMR-058, ASG-
012
ADR-03 Primary agent model,
delegation criteria and
accountability. Records the
decision that closed OP-30
UMR-011, UMR-012, AAR-
001, AAR-010
ADR-04 Budget enforcement point
and stop behaviour
UMR-013, UMR-030, AAR-
003, ASG-004
ADR-05 Memory tier
implementation, curation
workflow and retention
UMR-014, UMR-073, AAR-
004
ADR-06 Human review workflow
engine and approval state
model
UMR-021 to UMR-026, HITL-
001 to HITL-008
ADR-07 Audit logging mechanism
and integrity proof
UMR-027, UMR-062, ASG-
003
ADR-08 Azure PBMM landing zone,
Canadian region selection
and residency
UMR-057, UMR-070, UMR-
074, UMR-085
ADR-09 Language model sourcing
and substitution path
UMR-028, UMR-081
ADR-10 Confidence computation
from the six named inputs,
and its calibration
UMR-007, UMR-010, ARR-

---

<!-- PDF page 96 -->

ADR Decision Satisfies
ADR-11 Prompt-injection defence,
including code and tool-
selection cases
UMR-068, ASG-007
ADR-12 Anomaly detection method
and trigger tuning
UMR-041, UMR-042, UMR-
078
ADR-13 Azure immutable audit
store, binding on the
Administrator role
UMR-027, UMR-065, ASG-
008
ADR-14 Classification detection at
ingestion, and handling of
unlabelled documents
UMR-058, UMR-067, ASG-
009
ADR-15 User role model, separation
of duties, and Azure identity
integration
UMR-065, UMR-065.1
ADR-16 PBMM control
implementation and the
control-to-requirement
mapping
UMR-058, UMR-069, UMR-
070, ASG-010
ADR-17 Background task execution,
progress reporting and
cancellation
UMR-056, UMR-090
ADR-18 Azure sizing derived from the
workload assumptions,
service tiers and cost
position
UMR-059, UMR-070, UMR-
074, UMR-085
ADR-19 Session workspace
implementation, ephemeral
default, isolation, export
control
UMR-092, UMR-069, UMR-
072
ADR-20 Code execution sandbox:
runtime, containment
boundary, resource limits
and audit
UMR-093, ASG-011, UMR-
082
ADR-21 Chunking strategy and its
relationship to the request
context floor
UMR-003, UMR-067,
PARAM-39
ADR-22 Retrieval tool set,
parameterised file-search
interface, and iteration
control
UMR-094, ARR-010, ASG-

---

<!-- PDF page 97 -->

ADR Decision Satisfies
ADR-23 Session lifecycle: creation,
persistence, idle timeout,
and joint termination of
agent context and
workspace
UMR-095, UMR-092,
PARAM-44
Annex A—Identifier mapping
Old identifier New identifier Reason
UMR-010 UMR-010 + UMR-086 Insufficient-evidence
behaviour separated
UMR-029 UMR-029 + UMR-087 + UMR-
088
Irreversible-action approval
and change control
separated
UMR-041 UMR-041 + UMR-089 Anomaly report content
separated
UMR-056 UMR-056 + UMR-090 Background task behaviour
separated
UMR-051, UMR-052 UMR-051 (reissued), UMR-
052
Source register separated
from connectors
UMR-060 merged into UMR-006 Weaker duplicate. Identifier
retained as a pointer
UMR-065 UMR-065 + UMR-065.1 Separation of duties
separated
UMR-071, UMR-076 withdrawn Identifiers retained as
pointers
UC-C1 (Dublin Core) UC-C7 Identifier collision resolved
— UC-C8, UC-C9 Written to give orphaned
requirements a stated
demand
UMR-014 tier names episodic, semantic,
procedural
Renamed in V2, definitions
tightened in P13. Identifier
unchanged
— UMR-092, UMR-093, ASG-
011
V2: session workspace,
code execution,
containment
— UMR-094 (new) Agent-selected retrieval, V3
Gap 1

---

<!-- PDF page 98 -->

Old identifier New identifier Reason
— UMR-095 (new) Session-scoped primary
agent, V3Gap 2
— AAR-010 (new) Delegation accountability
— ARR-010 (new) Retrieval path recording and
disclosure
— ASG-012 (new) Retrieval tool containment
All other identifiers are unchanged. No identifier was deleted.
Annex B —Configurable Parameter Baseline Register
Required by UMR-063.
Parameter Setting Requirement Evidence status
PARAM-01 Language
detection
accuracy
UMR-001 Phase 1 answers in English only
PARAM-02 Minimum total
request context
UMR-003 A floor for model compatibility,
not a target. Larger windows
permitted; retrieval stays
selective
PARAM-03 Result count,
filter threshold,
fusion method,
primary quality
measure
UMR-004 0.72 may be adopted only once
measured against the
acceptance set
PARAM-04 Retrieval
method weights
UMR-005 Set by review decision.
Configurable in later phases
behind the common interface
PARAM-05 Retry limit after
insufficient
retrieval
UMR-009 Engineering judgement
PARAM-06 Confidence
gate per risk tier
UMR-008, ARR-
005
Untested
PARAM-07 Grounding pass
score per risk
tier
UMR-010 Untested
PARAM-08 Content filter
block rate and
false-block rate
UMR-020 Requires an adversarial test set

---

<!-- PDF page 99 -->

Parameter Setting Requirement Evidence status
PARAM-09 to
PARAM-13
Budget limits:
time, tokens,
tool calls,
reasoning
steps, cost
UMR-013, UMR-
030
Carried from the original draft
PARAM-14 Repetition limit UMR-019, ASG-
005
Untested
PARAM-15 Retry limit after
rejection
UMR-024, HITL-
005
Engineering judgement
PARAM-16 Approval
timeout per risk
tier
UMR-025, HITL-
006
Untested
PARAM-17 Cost estimate
accuracy
UMR-031 Requires a back-test
PARAM-18 Mission
comparison
method and
weights
UMR-032 Appendix B, UC-C4
PARAM-19 Comparison
mission count
and cutoff
UMR-033 Untested
PARAM-20 Anomaly
statistical
trigger, per
source
UMR-042 Untested
PARAM-21 Similar past
anomaly count
and cutoff
UMR-043 Engineering judgement
PARAM-22 to
PARAM-24
Withdrawn.
Response-time
targets are fixed
in UMR-056
UMR-056 Withdrawn, OP-12
PARAM-25 Availability
target
UMR-057 Assumption OA-03. Consistent
with PBMM Medium availability
PARAM-26 Withdrawn.
Concurrency is
fixed in UMR-
059
UMR-059 Withdrawn, OP-12
PARAM-27 Memory UMR-014 Waiting on the records schedule,

---

<!-- PDF page 100 -->

Parameter Setting Requirement Evidence status
retention per
tier
OP-07
PARAM-28 Indexing delay UMR-067 Requires sizing analysis
PARAM-29 Prompt-
injection
defence rate
UMR-068 Test set must include code and
tool-selection cases
PARAM-30,
PARAM-31
Recovery point
and recovery
time objectives
UMR-074 From Azure service tiers and
PBMM Medium availability
PARAM-32 Telemetry
acquisition
interval
UMR-078 Per data feed
PARAM-33 Quality drift
alert margin
UMR-080 Requires a quality baseline, per
retrieval path
PARAM-34 Withdrawn.
Phase-1
concurrency is
fixed in UMR-
085
UMR-085 Withdrawn, OP-12
PARAM-35 Default
handling of an
unlabelled
document
UMR-058, UMR-
067
Proof of concept only. Review
before production authorization,
OP-17
PARAM-36 Role
assignment
review interval
UMR-065 Engineering judgement
PARAM-37 Named Backup
approver for
each Approver
UMR-025, HITL-
006
Not assigned at the proof-of-
concept stage, OP-19
PARAM-38 Source data
type: real or
simulated, per
source
UMR-091 Set by CSA decision
PARAM-39 Document
chunk size and
overlap
UMR-067, UMR-
003
Separated from the request
context floor. Must be set by
retrieval testing
PARAM-40 Procedural
memory
implementation
UMR-014 Agents may not write to these
<!-- PDF page 101 -->

Parameter Setting Requirement Evidence status
PARAM-41 Session
workspace
retention where
persistence is
approved
UMR-092 Default set in P13. A persistence
value is needed only if
persistence is approved
PARAM-42 Code execution
time and
memory limits
UMR-093, ASG-
011
Must be set before code
execution is enabled, OP-31
PARAM-43 Retrieval
iterations per
request
UMR-094, ARR-
006
New in P13. Without a limit,
agent-chosen retrieval can loop
at cost
PARAM-44 Session lifetime
and idle timeout
UMR-095 New in P13. Governs when the
agent context and workspace are
destroyed
PARAM-45 Delegation
criteria and
thresholds
UMR-011, AAR-
010
New in P13. Makes
"demonstrably improves quality,
speed, isolation or capability"
measurable rather than asserted
PARAM-46 Session
workspace
export limits
UMR-092, UMR-
082
New in P13. Size, format and
approval threshold for taking
content out of CRAFT
Annex C— Traceability
Method. Requirements serving a user demand trace to a use case. Requirements that are
cross-cutting controls trace to an architecture component, aDESIGN DECISION and a
verification procedure, in the register at C.5.
### C.1 Use cases
Use case Title Actor
UC-A1 Systems engineering
documentation ingestion
and concept deduction
Systems engineer
UC-B1 Global space technology
benchmarking and horizon
scanning
Systems engineer
UC-C1 Natural language technical
query
CSA engineer
UC-C2 Verifiable question
answering with deep
Finance engineer, systems
engineer

---

<!-- PDF page 102 -->

Use case Title Actor
citations, and cost
estimation
UC-C3 Tabular data transformation
to SQL, and risk
identification and flagging
Systems engineer, risk
manager
UC-C4 Parametric mission distance
calculation, and anomaly
detection
Operations engineer,
mission control
UC-C5 Automated report
compilation
Systems engineer, project
manager
UC-C6 Enterprise cognitive
synthesis layer for the
engineering lifecycle
Systems engineer, cost
analyst, scientist, data
governance officer
UC-C7 Dublin Core metadata
extraction
Systems engineer
UC-C8 Mission planning support Systems engineer, mission
analyst
UC-C9 Governance and audit
reporting
Auditor, security authority,
technical authority
### C.2 Requirement to use case coverage
Requirement group Traced to
UMR-001, UMR-002, UMR-009 UC-C1
UMR-004 UC-C1, UC-C2, UC-C3, UC-C4, UC-C6, UC-
C7
UMR-005 to UMR-008, UMR-010, UMR-011,
UMR-018
UC-C1 to UC-C4, UC-C6
UMR-013 to UMR-017, UMR-019, UMR-020 UC-C1 to UC-C4
UMR-021 to UMR-030 UC-C2 to UC-C5, UC-C8
UMR-031 to UMR-035 UC-C2
UMR-036 to UMR-040 UC-C3
UMR-041 to UMR-045 UC-C4
UMR-046 to UMR-050 UC-C5
UMR-052, UMR-053 UC-C5
UMR-054, UMR-077 UC-C8
UMR-055 to UMR-059 UC-C1 to UC-C5
UMR-061, UMR-062, UMR-026, UMR-027, UC-C9

---

<!-- PDF page 103 -->

Requirement group Traced to
UMR-045, UMR-050
UMR-062, UMR-065, UMR-066, UMR-075 UC-C6
UMR-002, UMR-006, UMR-067 UC-C7
UMR-051, UMR-067, UMR-068 UC-A1
UMR-051, UMR-068, UMR-086, UMR-091 UC-B1
UMR-092, UMR-093 UC-C3, UC-C4
UMR-094 UC-A1, UC-B1, UC-C1, UC-C3, UC-C7—
documentation ingestion, horizon scanning,
free-text query and metadata extraction
each need a different search strategy, which
is the demand behind agent-selected
retrieval
UMR-095 UC-C1, UC-C6— the natural language
query and cognitive synthesis use cases
both describe multi-turn interaction, which
requires a persistent session
### C.5 Cross-cutting requirements register
Requirement
Component (Section
5.2) ADR V
UMR-003 Grounding and
confidence service;
ingestion
ADR-10, ADR-21 T
UMR-012 Retrieval tool layer;
primary agent; safety
services
ADR-03, ADR-22 T
UMR-063 Configuration
control, Annex B
ADR-04 I
UMR-064 Retrieval and
grounding evaluation
harness
ADR-01, ADR-10 I
UMR-065, UMR-
065.1
Identity and access ADR-15 T
UMR-066 Retrieval engine;
retrieval tool layer
ADR-02 T
UMR-067 Ingestion and
parsing
ADR-14, ADR-21 T
UMR-068 Safety services ADR-11 T

---

<!-- PDF page 104 -->

Requirement
Component (Section
5.2) ADR V
UMR-069 Secrets and
encryption
ADR-08, ADR-16 T
UMR-070 Deployment
topology
ADR-08 I
UMR-072 Memory services;
session workspace;
audit
ADR-05, ADR-19 T
UMR-073 Audit and logging ADR-07 I
UMR-074 Backup and recovery ADR-08, ADR-18 D
UMR-078 Integration layer ADR-12 D
UMR-079 Interface layer;
human review
workflow
ADR-06 T
UMR-080 Monitoring ADR-10 T
UMR-081 Model inference ADR-09 T
UMR-082 Safety services ADR-06, ADR-19,
ADR-20
I
UMR-083 Integration layer ADR-14 T
UMR-084 Interface layer — I
UMR-085, UMR-059 Deployment
topology; agent
runtime
ADR-18 T
UMR-088 Safety services ADR-04 T
UMR-091 Ingestion; approved
source register
ADR-14 T
UMR-092 Session workspace ADR-19 T
UMR-093 Code execution
sandbox
ADR-20 T
UMR-094 Retrieval tool layer ADR-22 T
UMR-095 Primary agent
runtime; interface
layer
ADR-23 T
AAR-008 Memory services ADR-05 T
AAR-009 Primary agent;
memory services
ADR-03, ADR-05 T
AAR-010 Primary agent and ADR-03 T

---

<!-- PDF page 105 -->

Requirement
Component (Section
5.2) ADR V
delegation
ARR-009 Interface layer;
grounding service
ADR-20 D
ARR-010 Retrieval tool layer;
audit and logging
ADR-22, ADR-07 T
ASG-008 Audit and logging ADR-13 T
ASG-009 Ingestion and
parsing
ADR-14 T
ASG-010 Security architecture ADR-16 I
ASG-011 Code execution
sandbox
ADR-20 T
ASG-012 Retrieval tool layer;
safety services
ADR-22, ADR-02 T
### C.6 Completeness check
Every requirement identifier in Section 4 traces to either a use case or the cross-cutting
register. No mandatory requirement is orphaned. UMR-060, UMR-071 and UMR-076 are
withdrawn and require no trace.
Completeness is not correctness. Whether each mapping is right is confirmed at the
Requirements Review by the people who own each use case. UC-C8 and UC-C9 were
written by this review rather than by the engineers who will use them (OP-29).
Annex D— Verification
Every requirement carries a verification method in the V column. The verification plan shall
record, for each requirement: the method, the test procedure identifier, the acceptance
criterion, the parameter identifiers involved, and the responsible role.
Five requirements need verification procedures that do not yet exist anywhere:
- UMR-092 session workspace isolation and ephemeral destruction.
- UMR-093 code execution behaviour.
- ASG-011 code containment. This needs an adversarial procedure: a containment
boundary is only proven by trying to break it.
- UMR-094 and ASG-012 retrieval tool containment. Also adversarial: the procedure
must attempt free-form command injection through the parameterised interface,
and must attempt to read a document the requesting user cannot open in the
source system.

---

<!-- PDF page 106 -->

- UMR-004 retrieval quality across every path, not only the default pipeline. The
acceptance set under UMR-064 must exercise agent-selected retrieval, or it will
measure a path production rarely takes.
Annex E—Open points
OP Question Status Blocks
OP-01 Parent document Closed. Arch and
Design document
will not be used as a
parent
Section 2.1
OP-02, OP-03, OP-
09
Missing appendices Closed. Will use as
RD-04, RD-05, RD-
07
Annex C
OP-04 Security profile and
ceiling
Closed. PBMM,
Protected B
UMR-058
OP-05, OP-18, OP-
22
Hosting platform
and region
Closed. Azure,
Canadian regions
UMR-070
OP-06, OP-13 Identity and
separation of duties
Closed. Azure
identity, role list in
Section 3.4
UMR-065
OP-07 Records retention
schedule
TBC by CSA decision UMR-073, PARAM-27
OP-08 Risk standard TBC by CSA decision UMR-036
OP-10 French-language
quality standard
Closed. Not needed
at this phase
UMR-046, UMR-075
OP-11 Algorithmic Impact
Assessment
Closed by CSA
decision.
UMR-071
OP-12 Fixed or configurable
targets
Closed. Both stay
fixed
UMR-056, UMR-059
OP-14 CRAFT does not
claim compliance
with the Directive on
Automated
Decision-Making,
but holds Protected
B data, reads the
financial system of
record, runs
generated code
under UMR-093, and
now selects its own
Phase 1 UC.
Recommend review
at the PBMM
authorization
UMR-071, UMR-093,
UMR-094

---

<!-- PDF page 107 -->

OP Question Status Blocks
retrieval strategy
under UMR-094.
Confirm the position
still holds, and name
the owner
OP-15 Report generation
target
Closed. Runs on
demand under UMR-
090
UMR-056
OP-16 Ceiling conflict Closed. Resolved by
the Protected B
ceiling
UMR-047, UMR-053
OP-17 Unlabelled
documents treated
as Unclassified
Decided, carried as
a residual risk.
Review before
production
authorization
UMR-058, UMR-067
OP-19 Named Backup
approver
TBC by CSA decision UMR-025, PARAM-37
OP-20 SharePoint migration
timing
Closed by CSA
decision. Deferred to
phase 2
UMR-052
OP-21 Owner of the
simulated-to-real
verification gate
TBD by CSA decision UMR-091
OP-23 Traceability
coverage
Closed in P11 Annex C
OP-24 Use case identifier
collision
Closed in P10 Annex C
OP-25 Appendix A conflict Closed in P10,
superseded by OP-
27
Section 5.2
OP-26 Document number
and approval block
Closed. CSA-CRAFT-
RD-0001; "CIO?"
removed
Section 2.1, 2.4
OP-27 On-premises figures
versus Azure
Closed. Azure; on-
premises sizing
withdrawn
Section 5.2
OP-28 No costed
infrastructure
position exists until
Section 5.2, ADR-18

---

<!-- PDF page 108 -->

OP Question Status Blocks
RD-01 derives Azure
sizing. Confirm who
owns the Azure
costing exercise
5K$ from SSC. Then
MB to assume the
cost
OP-29 UC-C8 and UC-C9
were written by this
review. Confirm both
at the Requirements
Review
Confirmed. Both UC
were modified as per
MB and JFC approval
email.
Annex C
OP-30 Agent architecture:
registered roles, on-
the-fly roles, or
something else
TBC UMR-011, UMR-012
OP-31 Code execution
needs PARAM-42
limits and an
approved library list.
Neither exists. Code
execution cannot be
enabled without
both
Postponed for a
future decision.
UMR-093, ASG-011
OP-32 Session workspace
retention
Ephemeral by
default.
UMR-092
OP-33 Who builds and
owns the Phase 1
Engineering Costing
corpus, how is it
version-controlled,
and is it varied
enough to support
the acceptance data
set in UMR-064?
TBC UMR-051, UMR-064
OP-34 The authorized
retrieval tool set
under UMR-094
must be defined and
approved before
agent-selected
retrieval is enabled.
PARAM-43 iteration
limit is also unset
TBC UMR-094, PARAM-
43, ADR-22

---

<!-- PDF page 109 -->

OP Question Status Blocks
OP-35 Session lifetime and
idle timeout
(PARAM-44) are
unset. Without
them, sessions,
agent contexts and
workspaces have no
defined end, which
conflicts with the
ephemeral default in
UMR-092
TBC UMR-095, PARAM-44
OP-36 The delegation
criteria in PARAM-45
must be defined
before delegation is
enabled, or
"demonstrably
improves quality,
speed, isolation or
capability" cannot
be tested and
delegation becomes
discretionary in
practice
TBC UMR-011, AAR-010,
PARAM-45
Annex F —Reconciliation of the technical review
Source: RD-08, requirements-analysis&#46;docx, with the CRAFT analysis responses. Adopted
means the requirement now says what the response says. Adopted with control means the
capability is admitted and bounded. Clarified means the requirement meant this already
and now says so. Reversed means said something the response rules out.
RC(Review
Comments) Point Affects Disposition
RC-01 Document sources.
Phase 1 should use
only a controlled
Engineering Costing
corpus. Personal
devices, individual
OneDrive accounts
and production CSA
repositories require
UMR-051, UMR-052,
UMR-091, Section
1.3
Adopted. UMR-051
names the Phase 1
scope and the five
onboarding controls.
Connectors
deferred. OP-33 asks
who owns the
corpus

---

<!-- PDF page 110 -->

RC(Review
Comments) Point Affects Disposition
a separately
approved
onboarding process
with ownership,
permissions,
classification,
retention and audit
controls
RC-02 8,192 tokens is the
minimum total
request context, not
the size of an
embedding chunk
UMR-003, UMR-067,
PARAM-02, PARAM-
39
Clarified. UMR-003
states the scope of
the figure. Chunk
size separated into
PARAM-39
RC-03 Larger-context
models are
permitted, but
retrieval must
remain selective and
relevant rather than
filling available
context
indiscriminately
UMR-003, UMR-010 Adopted. The
selectivity rule is
now in UMR-003.
This matters for
grounding: filling a
long window with
weakly relevant
passages lowers
answer quality and
weakens the UMR-
010 measure
RC-04 Do not blindly
append the top
results from each
method. Normalise,
fuse, deduplicate
UMR-004, ARR-002,
PARAM-03
Adopted, and this
reverses V2. V2
recorded "top 5 of
each and append"
as an acceptable
Phase 1 fallback.
UMR-004 now
requires
normalisation,
fusion and
deduplication, and
prohibits appending
RC-05 Validate thresholds
such as 0.72 against
measured retrieval
performance
UMR-004, PARAM-03 Adopted, and this
partly reverses V2.
P9 removed 0.72
outright. It returns in
PARAM-03 as a
<!-- PDF page 111 -->

RC(Review
Comments) Point Affects Disposition
candidate to
validate, not as a
fixed rule
RC-06 Hybrid retrieval
through a common
interface, initially 0.7
semantic and 0.3
lexical
UMR-005, ARR-002,
PARAM-04
Adopted. Fixed
Phase 1 weights
behind a common
interface
RC-07 Do not use
multiplied token
probabilities. They
do not indicate
correctness and are
often unavailable
from hosted models
UMR-007, ARR-004 Adopted. Explicitly
prohibited
RC-08 Base confidence on
evidence coverage,
citations,
traceability, source
agreement, retrieval
quality, and
identification of
unsupported claims
UMR-007, ARR-004,
UMR-081
Adopted. All six
inputs are named in
UMR-007. Also
removes a hidden
constraint on UMR-
081, which requires
a replaceable model
RC-09 "Agent spawning
and termination
without interruption"
implies persistent
agents tied to a
session
UMR-016, UMR-095 Clarified. UMR-016
concerns platform
availability. Session
persistence is UMR-
095
RC-10 Provide a session-
scoped primary
agent with an
isolated, ephemeral
workspace by
default. It may use
authorized retrieval
and analysis tools
and generate
artifacts, but all
actions,
UMR-092, UMR-093,
UMR-094, UMR-095,
ASG-011, ASG-012,
UMR-030, UMR-082
Adopted with
control. The
workspace default
changes from
retention-TBC to
ephemeral. Export
control added.
Authorized-tools-
only is now the
governing rule for
both retrieval and

---

<!-- PDF page 112 -->

RC(Review
Comments) Point Affects Disposition
permissions,
exports, resource
use and retention
must be controlled
and auditable
code
RC-11 Episodic memory is
governed
conversation and
task history
UMR-014, AAR-004 Adopted. Definition
used verbatim
RC-12 Semantic memory is
curated, source-
backed durable
knowledge
UMR-014, Section
1.8
Adopted. "Curated"
and "source-
backed" are now
requirements: an
entry must cite its
source and be
reviewable
RC-13 Procedural memory
is approved
guidance such as
instruction files,
runbooks and
templates
UMR-014, PARAM-40 Adopted.
"Approved" is the
operative word:
procedural memory
is version-controlled
and changed only
through the
approved process
RC-14 Do not permit
uncontrolled self-
modification of
procedures
UMR-028, AAR-009,
Section 1.3
Adopted. Prohibition
extended from
settings, prompts
and code to
procedural memory
RC-15 Do not impose fixed
roles or use multiple
agents by default
UMR-011, UMR-012,
AAR-001
Adopted, and this
reverses V2. The
registered-role-per-
agent rule is
withdrawn. Control
moves to the tool
boundary in UMR-
012
RC-16 Use one
accountable primary
agent that delegates
UMR-011, AAR-010,
PARAM-45, ADR-03
Adopted. OP-30
closed. UMR-011
rewritten. AAR-010

---

<!-- PDF page 113 -->

RC(Review
Comments) Point Affects Disposition
bounded subtasks
only where this
demonstrably
improves quality,
speed, isolation or
capability. It remains
responsible for
validating and
integrating the final
response
added for validation
and accountability.
PARAM-45 makes
"demonstrably"
measurable
RC-17 Gap 1. The agent
should choose how
to search, including
dense retrieval,
sparse retrieval, or
constructing
commands such as
grep or find
UMR-094, ARR-010,
ASG-012, UMR-066,
UMR-064, UMR-080
Adopted with
control. The agent
selects among
authorized retrieval
tools and may
iterate. File search is
parameterised.
Free-form shell
strings are
prohibited, because
the command space
is unbounded,
unauditable and
open to injection
from ingested
content. Permission
trimming applies to
every path
RC-18 Gap 2. Expose a chat
interface with a
persistent agent to
the user
UMR-095, UMR-001,
UMR-014, UMR-092
Adopted. One
primary agent per
session, persisting
for the session,
holding episodic
memory, bound to
the workspace.
Session, agent
context and
workspace end
together
RC-19 Gap 3. The response
text embedded in
Annex F Closed. The
responses were

---

<!-- PDF page 114 -->

RC(Review
Comments) Point Affects Disposition
RD-08 is truncated
mid-sentence
supplied separately
and are reconciled
above as RC-01 to
RC-18. The
reconciliation is now
complete against
both the comments
and the responses
