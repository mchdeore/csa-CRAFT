CSA-FIN-RD-0743

Canadian Space Agency

Office of the Chief Financial Officer (OCFO)

+----------------------------------------------------------------------+
| Cost Analysis Data Requirements (CADRe)                              |
|                                                                      |
| PART A                                                               |
|                                                                      |
| > Mission : ZELVORA                                                  |
| >                                                                    |
| > Key Decision Point : KDP-E                                         |
| >                                                                    |
| > EPMO Gate : G4                                                     |
|                                                                      |
| Daft 1.0                                                             |
|                                                                      |
| September 18, 2026                                                   |
+----------------------------------------------------------------------+
|                                                                      |
+----------------------------------------------------------------------+

This Page Intentionally Left Blank

Revision History

  ------------------------------------------------------------------------
  Rev.      Description                      Prepared by    Date
  --------- -------------------------------- -------------- --------------
  Draft 1.0 Initial draft                    MB             19 Sept 2026

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            
  ------------------------------------------------------------------------

This Page Intentionally Left Blank

Table of Contents

[1 Introduction [7](#introduction)](#introduction)

[1.1 Purpose of this document
[7](#purpose-of-this-document)](#purpose-of-this-document)

[2 General Descriptive Information
[7](#general-descriptive-information)](#general-descriptive-information)

[2.1 Mission Overview [7](#mission-overview)](#mission-overview)

[2.2 Strategic Objectives
[8](#strategic-objectives)](#strategic-objectives)

[2.3 Selected Mission Requirements
[9](#selected-mission-requirements)](#selected-mission-requirements)

[2.4 High-Level Mission Architecture
[10](#high-level-mission-architecture)](#high-level-mission-architecture)

[3 Space Segment Description
[11](#space-segment-description)](#space-segment-description)

[3.1 Spacecraft Bus [11](#spacecraft-bus)](#spacecraft-bus)

[3.2 Payload [13](#payload)](#payload)

[4 Launch Segment description
[17](#launch-segment-description)](#launch-segment-description)

[5 Ground Segment and Mission Operations
[17](#ground-segment-and-mission-operations)](#ground-segment-and-mission-operations)

[6 Systems Engineering and Project Management Approach
[18](#systems-engineering-and-project-management-approach)](#systems-engineering-and-project-management-approach)

[6.1 TRL Levels and Heritage
[18](#trl-levels-and-heritage)](#trl-levels-and-heritage)

[6.2 Phasing Logic and Naming conventions
[18](#phasing-logic-and-naming-conventions)](#phasing-logic-and-naming-conventions)

[6.3 CSA PRoject Milestones
[19](#csa-project-milestones)](#csa-project-milestones)

[6.4 Safety and Mission Assurance
[19](#safety-and-mission-assurance)](#safety-and-mission-assurance)

[6.5 Qualification and Acceptance Strategy, MODEL Philosophy
[19](#qualification-and-acceptance-strategy-model-philosophy)](#qualification-and-acceptance-strategy-model-philosophy)

[6.6 Sparing Strategies [20](#sparing-strategies)](#sparing-strategies)

[6.7 Risk Assessment [20](#risk-assessment)](#risk-assessment)

[6.8 Organizational Breakdown Structure
[20](#organizational-breakdown-structure)](#organizational-breakdown-structure)

List of Figures

FIGURE PAGE

Figure 1 -- Mission Concept [8](#_Toc240961235)

FIGURE 2 - KARVIX BUS 13

Figure 3 -- Robotic Capture Arm 17

List of TABLES

[Table 2 - Strategic Alignment [8](#_Toc240608386)](#_Toc240608386)

[Table 3 -- Selected SysteM Requirements
[9](#_Toc240608387)](#_Toc240608387)

# Introduction

## Purpose of this document

CADRE Part A provides a concise, standardized synopsis of the mission or
project to support costing and analysis activities. Its primary purpose
is to consolidate information from multiple technical and programmatic
source documents into a single, normalized reference.

Specifically, CADRE Part A:

- Summarizes key mission characteristics in a consistent and structured
  format

- Aggregates information drawn from multiple authoritative technical
  documents

- Reduces the need for analysts to repeatedly consult disparate source
  materials

- Ensures a common baseline description is used across analyses

- Improves efficiency, traceability, and consistency in downstream
  costing work

In practical terms, CADRE Part A functions as a time-saving reference
document that enables analysts to quickly understand the mission context
without re-interpreting or reconciling multiple source documents.

# General Descriptive Information

## Mission Overview

**Project ZELVORA** is an active debris-removal mission designed to
reduce the number of inactive satellites and large pieces of debris in
Low Earth Orbit (LEO). The mission will launch an advanced servicing
spacecraft, known as the ZELVORA **Orbital Spacecraft**, which will
travel to selected non-operational satellites, safely rendezvous with
them, capture them, and lower their orbits. Once placed into a
sufficiently low orbit, atmospheric drag will gradually pull the
captured satellite toward Earth for re-entry.

The ZELVORA Orbital Spacecraft is designed to service multiple targets
during a single mission. After completing the removal of one satellite,
the spacecraft will use its propulsion system to transfer to another
target and repeat the process. This approach allows one servicing
vehicle to address several pieces of debris rather than requiring a
separate launch for every object.

The mission builds on technologies demonstrated by previous orbital
debris-removal efforts, including **Astroscale\'s ELSA-d**, which
demonstrated rendezvous and capture operations, and **ESA\'s
ClearSpace-1**, which is designed to capture and remove an inactive
object from orbit. ZELVORA advances these concepts by combining
rendezvous, robotic capture, orbital maneuvering, and multi-target
operations into one integrated mission.

The primary objective of Project ZELVORA is to demonstrate a practical
method for removing large inactive objects from Earth\'s increasingly
congested orbital environment. By safely lowering the orbits of selected
satellites and allowing atmospheric drag to complete their removal,
ZELVORA will demonstrate how future servicing spacecraft could help
maintain a safer and more sustainable space environment.

![[]{#_Toc240961235 .anchor}Figure 1 -- Mission
Concept](media/image3.jpeg){width="6.5in" height="4.333333333333333in"}

## Strategic Objectives

Consistent with the Government of Canada\'s Space Policy Framework, the
WFS mission supports the following 2 main strategic goals:

+---+-------------+--------------------------------------------------------------+
|   | **Strategic | **Space Strategy**                                           |
|   | Goals**     |                                                              |
+===+=============+==============================================================+
| 1 | **SOLVE**   | **Harness space to solve everyday challenges for             |
|   |             | Canadians.**                                                 |
|   |             |                                                              |
|   |             | ZELVORA addresses the practical problem of **space debris    |
|   |             | and inactive satellites**. Removing debris can help make     |
|   |             | orbital space safer and more sustainable for future          |
|   |             | satellite operations.                                        |
+---+-------------+--------------------------------------------------------------+
| 2 | **ENABLE**  | **Position the space sector to help grow the economy**       |
|   |             |                                                              |
|   |             |   --                                                         |
|   |             |                                                              |
|   |             |   --                                                         |
|   |             |                                                              |
|   |             |   ---------------------------------------------------------- |
|   |             |   The mission develops in-orbit servicing and debris-removal |
|   |             |   technology, which could support the growth of Canada\'s    |
|   |             |   space industry and create future commercial opportunities  |
|   |             |   for satellite servicing.                                   |
|   |             |   ---------------------------------------------------------- |
|   |             |                                                              |
|   |             |   ---------------------------------------------------------- |
+---+-------------+--------------------------------------------------------------+

: []{#_Toc240608386 .anchor}Table 2 - Strategic Alignment

Additionally, Project ZELVORA contributes to Stewardship, Management and
Accountability through international partnerships.

## Selected Mission Requirements

The following represents a summary of selected mission requirements. The
complete and authoritative set of requirements is contained in the
Mission Requirements Document.

1.  **Launch and deploy** the ZELVORA Orbital Bus into its designated
    Low Earth Orbit.

2.  **Rendezvous and safely capture** selected inactive satellites using
    the spacecraft\'s navigation and robotic systems.

3.  **Deorbit captured satellites** by lowering their orbits to a
    trajectory that results in controlled atmospheric re-entry.

4.  **Service multiple targets** during a single mission while
    maintaining safe operations and sufficient spacecraft resources.

5.  **Demonstrate reliable and sustainable debris removal** without
    creating additional orbital debris or unacceptable risks to other
    spacecraft and people on Earth.

  ---------------------------------------------------------------------------------
  **\#**   **Requirement    **Requirement Description**
           Name**           
  -------- ---------------- -------------------------------------------------------
  **1**    **Multi-Target   ZELVORA shall be capable of capturing and deorbiting
           Removal**        **at least 5 inactive satellites** during one mission.

  **2**    **Orbital        ZELVORA shall be capable of safely rendezvousing with
           Rendezvous**     selected inactive satellites in **Low Earth Orbit
                            (LEO)**.

  **3**    **Satellite      ZELVORA shall be capable of securely capturing
           Capture**        **non-cooperative satellites** using its robotic
                            capture system.

  **4**    **Deorbit        ZELVORA shall be capable of lowering the orbit of each
           Capability**     captured satellite to a **planned disposal trajectory**
                            that results in atmospheric re-entry.

  **5**    **Orbital        ZELVORA shall have sufficient propulsion capability to
           Maneuvering**    **transfer between multiple targets and perform
                            required deorbit maneuvers**.

  **6**    **Precision      ZELVORA shall be capable of determining the **position
           Navigation**     and relative motion of target satellites** during
                            rendezvous and capture operations.

  **7**    **Mission        ZELVORA shall have sufficient **power, propellant,
           Lifetime**       communications, and thermal-control resources** to
                            complete its planned mission.

  **8**    **Debris         ZELVORA shall conduct capture and disposal operations
           Prevention**     without intentionally creating **additional long-lived
                            orbital debris**.
  ---------------------------------------------------------------------------------

  : []{#_Toc240608387 .anchor}Table 3 -- Selected SysteM Requirements

## High-Level Mission Architecture 

Owned and operated by CSA, the mission consists of

- A **Government Segment**: consisting of government resources for
  oversight and their associated management costs such as T&L

- A **Space Segment**: consisting of four spacecrafts with a
  platform/bus and an infrared instrument.

- A **Launch Segment**: consisting of the launcher and launch service
  provider.

- A **Ground Segment**: consisting of facilities and equipment to plan
  and command acquisitions, as well as, to receive, archive and process
  data acquired by the satellite.

- An **Ops Segment**: consisting of personnel to handle real-time
  operations and some O&M costs

- A **Science Segment**: consisting of scientific leadership, research
  teams, and supporting infrastructure responsible for mission science
  planning, calibration and validation, data analysis, scientific data
  products, user support, and the maximization of scientific return from
  the mission.

# Space Segment Description

The space segment consists of a bus and a payload.

## Spacecraft Bus 

The **KARVIX Orbital Bus** provides the common spacecraft platform
required to support the ZELVORA active debris-removal mission. The bus
supplies the power, control, communications, propulsion, thermal
management, and autonomous capabilities necessary for the spacecraft to
operate in Low Earth Orbit and perform repeated rendezvous and deorbit
operations.

Key functions of the bus include:

- Electrical power generation and distribution

- Spacecraft pointing and attitude control

- Data handling and storage

- Communications with Earth

- Propulsion and orbit maintenance

- Thermal control

- Fault management and autonomy

### Spacecraft pointing and attitude control

The attitude control system maintains the orientation and stability of
the KARVIX spacecraft during all phases of the mission. Sensors
determine the spacecraft\'s orientation, while reaction wheels and
attitude-control thrusters provide the necessary control. Precise
pointing is particularly important during rendezvous and satellite
capture, where the spacecraft must maintain a controlled position and
orientation relative to an inactive satellite. The system also supports
accurate pointing of communications antennas and navigation sensors.

### Data handling and storage

The KARVIX data-handling system acts as the spacecraft\'s central
computing and information-management system. It receives commands from
mission control, monitors the status of onboard systems, and processes
information collected by sensors and cameras. Mission data and
spacecraft health information are stored onboard before being
transmitted to Earth. The system also supports autonomous operations by
allowing KARVIX to process navigation and spacecraft-status information
without requiring continuous instructions from ground operators.

### Communications with Earth

The communications system provides the connection between KARVIX and
ground stations on Earth. It allows mission controllers to send commands
to the spacecraft and receive telemetry concerning spacecraft health,
position, power, temperature, and mission progress. Communications are
maintained throughout normal spacecraft operations and provide a means
of monitoring critical rendezvous and deorbit activities. The system
also supports communication during contingency and safe-mode operations.

### Propulsion and orbit maintenance

The propulsion system provides the changes in velocity required for
KARVIX to travel between selected target satellites and perform deorbit
operations. Propulsion manoeuvres allow the spacecraft to adjust its
orbital altitude and trajectory, rendezvous with inactive satellites,
and move between multiple targets during the mission. Following capture,
the propulsion system lowers the orbit of the combined spacecraft and
target until atmospheric drag can cause the target to re-enter Earth\'s
atmosphere. Propulsion also provides orbit-maintenance and
collision-avoidance capabilities when required.

### Thermal control

The thermal-control system maintains the KARVIX spacecraft and its
equipment within acceptable operating temperatures. The spacecraft
experiences changing thermal conditions as it moves between sunlight and
Earth\'s shadow, while onboard electronics and other equipment generate
heat during operation. Insulation, heat-transfer paths, and radiators
are used to manage these temperature variations. Maintaining appropriate
temperatures protects sensitive electronics, batteries, propulsion
components, and the robotic capture equipment throughout the mission.

### Fault management and autonomy

The fault-management and autonomy system monitors the health and
performance of KARVIX\'s major subsystems. It can identify abnormal
conditions and take predefined actions to protect the spacecraft without
waiting for instructions from Earth. If a serious fault occurs, the
spacecraft can enter a safe operating mode, reduce non-essential
activities, and maintain critical functions until the problem can be
assessed. Autonomous capabilities are also used during rendezvous and
close-proximity operations, allowing KARVIX to respond to changing
conditions while approaching and capturing an inactive satellite.

### Overall Bus Function

Together, these seven bus systems provide the infrastructure required
for **KARVIX to operate as an autonomous orbital servicing spacecraft**.
The electrical, attitude-control, computing, communications, propulsion,
thermal, and fault-management systems work together to support the
ZELVORA mission from launch through satellite rendezvous, capture,
deorbit, and completion of the mission.

![Figure 2 -- Karvix Bus](media/image4.png){width="6.765625546806649in"
height="4.510416666666667in"}

## Payload

###  Payload System Overview

The **ZELVORA payload system** contains the mission-specific equipment
required to locate, approach, capture, and assist in the disposal of
inactive satellites in Low Earth Orbit (LEO). The **KARVIX Orbital Bus**
provides the spacecraft with power, propulsion, communications, attitude
control, thermal control, and data handling, while the payload performs
the direct interaction with the target.

The payload is designed to work with non-operational satellites that may
no longer be able to control their own position or orientation. It
combines imaging sensors, relative-navigation equipment, a robotic
capture mechanism, payload electronics, and structural support systems.

The major payload elements are:

- Target detection and imaging system

- Relative-navigation and proximity sensors

- Robotic capture system

- Target interface and capture mechanism

- Payload electronics and control

- Payload structural support

- Payload safety system

Together, these systems allow ZELVORA to safely approach and establish a
physical connection with selected orbital debris.

### Target Detection and Imaging System

The target detection and imaging system provides the spacecraft with
visual information about the selected satellite. Cameras mounted on the
spacecraft are used during the approach to identify the target and
determine its position and orientation.

As the spacecraft gets closer, higher-resolution imaging is used to
monitor the target\'s movement and rotation. This is important because
an inactive satellite may be tumbling or slowly changing orientation.

The imaging system supports:

- Target identification

- Relative-position determination

- Monitoring of target movement

- Final approach

- Capture verification

- Post-capture inspection

Information from the cameras is provided to the spacecraft\'s onboard
computer and can also be transmitted to ground operators.

### Relative Navigation and Proximity Sensors

The relative-navigation system determines the position and movement of
the target relative to ZELVORA. It combines information from cameras and
proximity sensors to provide accurate measurements during close-range
operations.

The system monitors:

- Distance to the target

- Relative direction

- Closing speed

- Target orientation

- Target rotation

- Capture-interface position

This information is supplied to the spacecraft\'s guidance and
attitude-control systems. As ZELVORA approaches the target, navigation
measurements become increasingly important for maintaining a controlled
position and preventing accidental contact.

Using multiple sensors also provides additional reliability if one
sensor produces poor-quality information because of lighting, target
orientation, or other conditions.

### Robotic Capture System

The **robotic capture system** is the primary mechanical component of
the ZELVORA payload. Its purpose is to establish a secure physical
connection with an inactive satellite.

The system consists of a robotic arm or articulated mechanism,
actuators, an end-effector, position sensors, and a capture mechanism.
The robotic arm allows the capture device to be moved toward a suitable
structural region of the target.

During capture, the arm moves at controlled speeds to reduce unwanted
forces. The end-effector establishes contact with the target and secures
the connection.

The capture system must also account for target movement. If the
inactive satellite is rotating or moving slightly during the approach,
the robotic mechanism must accommodate this motion while maintaining a
stable connection.

### Target Interface and Capture Mechanism

The target interface is the part of the payload that makes direct
contact with the inactive satellite. Before a mission, the target would
be analyzed to identify an appropriate structural region for capture.

During the final approach, navigation sensors guide the robotic system
toward this region. Once contact is established, the capture mechanism
secures the target so that the spacecraft can control the combined
system during orbital maneuvers.

Sensors within the capture mechanism confirm that the connection has
been successfully established. If the capture conditions are outside the
expected limits, the spacecraft can stop the operation rather than
continuing an unsafe maneuver.

The target interface is therefore designed to provide a controlled and
secure connection between ZELVORA and the captured satellite.

### Payload Electronics and Control

The payload electronics control the sensors and robotic capture
equipment and provide the interface between the payload and the KARVIX
Orbital Bus.

The electronics collect information from the cameras, navigation
sensors, robotic-arm sensors, and capture mechanism. This information is
processed by the spacecraft\'s computing system and used to support
navigation and capture operations.

The system can control functions such as:

- Robotic-arm movement

- Capture-head positioning

- Capture activation

- Actuator monitoring

- Capture confirmation

- Payload health monitoring

The payload electronics work together with the spacecraft\'s power,
communications, attitude-control, and fault-management systems to ensure
that the capture system operates only when the spacecraft is in an
appropriate state.

### Payload Structural Support

The payload structural system provides the mounting points for the
cameras, sensors, robotic arm, and other mission equipment.

The structure must withstand launch loads as well as forces generated
during orbital operations and target capture. Particular attention is
given to the robotic capture system because forces produced during
contact with a target can be transferred into the spacecraft structure.

The payload structure also positions the cameras and sensors so that
they have appropriate views of the target while providing the robotic
arm with sufficient range of motion.

###  Payload Safety System

The payload safety system is designed to reduce the possibility of
accidental contact or an unsuccessful capture creating additional
orbital debris.

Before the robotic system is deployed, ZELVORA verifies that conditions
such as spacecraft attitude, relative distance, navigation accuracy,
power availability, and system health are suitable for the operation.

During capture, the spacecraft continuously monitors the target and
robotic mechanism. If an unexpected condition occurs, the capture
operation can be paused or aborted and the robotic system returned to a
safe configuration.

Following successful capture, the spacecraft confirms that the target is
securely attached before performing major orbital maneuvers.

![](media/image5.png){width="6.375in" height="4.25in"} Figure 3 --
Robotic capture arm

# Launch Segment description

The **ZELVORA launch segment** begins with the spacecraft being
integrated with its launch vehicle and prepared for deployment into Low
Earth Orbit (LEO). Following launch, the spacecraft is released at its
designated orbit and begins initial system checks. The KARVIX Orbital
Bus then deploys its solar arrays, establishes communication with ground
control, and verifies the health of its major systems. Once
commissioning is complete, ZELVORA transitions into its operational
orbit and prepares for its first debris-removal operation.

# Ground Segment and Mission Operations

The **ZELVORA ground segment** provides the communication, monitoring,
planning, and control functions required to operate the spacecraft
throughout its mission. Ground stations maintain communication with
ZELVORA and receive telemetry containing information about the
spacecraft\'s health, position, power levels, propulsion system,
payload, and other critical systems. Commands and mission updates are
transmitted from the ground to the spacecraft through these
communication links.

Mission operations are managed by a ground control team responsible for
planning orbital maneuvers, monitoring spacecraft performance, and
coordinating debris-removal activities. Before each target encounter,
operators review the target\'s orbital position and prepare the required
rendezvous and capture sequence. During critical operations, such as
final approach and satellite capture, the ground team monitors telemetry
and sensor data while ZELVORA\'s onboard autonomous systems handle rapid
responses that cannot depend on continuous communication with Earth.

After a successful capture, mission operators verify spacecraft and
target status before authorizing the deorbit maneuver. The ground
segment also maintains mission records and evaluates system performance
after each operation. This combination of **ground-based planning and
onboard autonomy** allows ZELVORA to safely conduct repeated
debris-removal operations while maintaining continuous oversight from
Earth.

# Systems Engineering and Project Management Approach

## TRL Levels and Heritage

ZELVORA has an estimated overall **TRL of 6**, using mature spacecraft
technologies combined with less-proven robotic capture and autonomous
rendezvous systems. Its technology heritage is based on previous orbital
servicing and debris-removal missions, including demonstrated rendezvous
and capture technologies.

## Phasing Logic and Naming conventions

The following are the phases in terms of costing:

+----------------+-------------------------------------+---------------------+
| **Costing      | **Phase Description according to    | **Corresponding     |
| Nomenclature** | Costing Standards**                 | Name for Project    |
|                |                                     | team**              |
+================+=====================================+=====================+
| PREP 1         | Prototyping Activities (before Gate | N/A                 |
|                | 1)                                  |                     |
+----------------+-------------------------------------+---------------------+
| PREP 2         | Prototyping Activities (during      | N/A                 |
|                | Phase 0/A)                          |                     |
+----------------+-------------------------------------+---------------------+
| Phase 0        | Concept & Feasibility Studies       | Phase 0             |
+----------------+-------------------------------------+---------------------+
| Phase A        | System Definition                   | Phase A             |
+----------------+-------------------------------------+---------------------+
| Phase B        | Preliminary Design                  | Phase B             |
+----------------+-------------------------------------+---------------------+
| Phase C        | Detailed Design                     | Phase C             |
+----------------+-------------------------------------+---------------------+
| MAIT           | Manufacturing, Assembly,            | Phase D             |
|                | Integration and Test (of Canadian   |                     |
|                | Systems, Subsystems and Components) |                     |
+----------------+-------------------------------------+                     |
| SAIT           | Segment Level Assembly, Integration |                     |
|                | and Test (begins with System        |                     |
|                | Integration review)                 |                     |
+----------------+-------------------------------------+                     |
| LEOP           | Launch and Early Operations (incl.  |                     |
|                | commissioning)                      |                     |
+----------------+-------------------------------------+---------------------+
| Phase E        | Nominal Operations (per design      | Phase E             |
|                | life)                               |                     |
+----------------+-------------------------------------+---------------------+
| Phase X        | Extended operations (mission        | Extended ops        |
|                | extension)                          |                     |
+----------------+-------------------------------------+---------------------+
| Phase F        | Disposal                            | Phase F             |
+----------------+-------------------------------------+---------------------+

## CSA PRoject Milestones

The project has not created a schedule baseline yet. Assuming instrument
level milestones will drive the CSA need dates.

+--------------+-----+-------------------------------+----------------------+
| **Instrument |     | **Major Milestone**           | **Milestone Date**   |
| Phases**     |     |                               |                      |
+==============+=====+===============================+======================+
| Phase 0      | MCR | Mission Concept Review        | 10/20/2020           |
+--------------+-----+-------------------------------+----------------------+
| Phase A      | SRR | System Requirements Review    | 07/15/2022           |
+--------------+-----+-------------------------------+----------------------+
|              |     | Mission Rebaseline            |   --                 |
|              |     |                               |                      |
|              |     |                               |   --                 |
|              |     |                               |                      |
|              |     |                               | 09/19/2022           |
+--------------+-----+-------------------------------+----------------------+
| Phase B      | PDR | Preliminary Design Review     | 10/18/2023           |
+--------------+-----+-------------------------------+----------------------+
| Phase C      | CDR | Critical Design Review        | 12/12/2024           |
+--------------+-----+-------------------------------+----------------------+
| MAIT         | MRR | Manufacturing readiness       | 06/24/2025           |
|              |     | Review                        |                      |
|              +-----+-------------------------------+----------------------+
|              | PSR | Pre-Ship Review of systems to | 10/14/2025           |
|              |     | Prime                         |                      |
+--------------+-----+-------------------------------+----------------------+
| SAIT         | SIR | System Integration Review     | 06/23/2026           |
|              +-----+-------------------------------+----------------------+
|              | AR  | Acceptance Review             | 09/24/2026           |
|              +-----+-------------------------------+----------------------+
|              | PSR | Pre-Ship Review of S/C to     | 01/15/2027           |
|              |     | Launch site                   |                      |
+--------------+-----+-------------------------------+----------------------+
| LEOP         | L   | Launch                        | 03/01/2027           |
|              +-----+-------------------------------+----------------------+
|              | CR  | Commissioning Review          | 03/14/2027           |
+--------------+-----+-------------------------------+----------------------+
| Phase E      |     | Start of Nominal Ops          | 04/13/2027           |
|              +-----+-------------------------------+----------------------+
|              |     | End of Nominal Ops            | 05/04/2028           |
+--------------+-----+-------------------------------+----------------------+
| Phase X      |     | End of Life                   | 10/27/2031           |
+--------------+-----+-------------------------------+----------------------+

## Safety and Mission Assurance

Initial assessments is assumed to be Mission Class: B

## Qualification and Acceptance Strategy, MODEL Philosophy

ZELVORA will follow a **Class B development and verification approach**
based on the GSFC GOLD Rules, using progressive testing from individual
units through subsystem and full spacecraft levels. Engineering Models
(EM) will be used to verify interfaces and system functionality, while
Qualification Models (QM) will be used for higher-risk hardware such as
the robotic capture system. The Protoflight/Flight Model (PFM) will
undergo functional, environmental, and flight-acceptance testing before
launch.

Testing will progress from **unit and subsystem testing to
spacecraft-level testing**, including vibration, thermal-vacuum,
functional, and end-to-end mission testing. Critical functions such as
rendezvous, capture, communications, propulsion, and fault management
will be tested using flight software where practical.

A **Structural-Thermal-Optical Performance (STOP) analysis** will also
be performed to evaluate how structural deformation and thermal
conditions could affect spacecraft and payload performance. This
analysis will be particularly important for ZELVORA\'s cameras,
navigation sensors, and robotic capture mechanism, ensuring that thermal
and structural changes do not compromise alignment or capture
performance.

ZELVORA will use **selective redundancy and fault tolerance** for
mission-critical systems such as power, communications, command and data
handling, and attitude control. Less critical components may remain
single-string to reduce mass and complexity, with the final redundancy
approach determined through system-level risk and reliability analysis.

## Sparing Strategies

ZELVORA will use a **selective sparing and redundancy strategy** to
improve mission reliability while controlling spacecraft mass, cost, and
complexity. Not every subsystem will require a complete backup; instead,
redundancy will be applied to functions where a single failure could
significantly affect spacecraft safety or mission success. Critical
systems such as command and data handling, electrical power,
communications, and attitude control will be designed with appropriate
backup capabilities where practical. For example, backup communication
paths or redundant processing capabilities could allow the spacecraft to
continue operating if a primary component fails.

For the payload, redundancy will focus on the most important functions
required for target detection, navigation, and capture. Multiple sensors
can provide overlapping measurements so that the loss or degradation of
one sensor does not immediately end a mission operation. The robotic
capture system will also incorporate fault detection and safe
configurations to reduce the consequences of actuator or mechanism
failures. Less critical equipment may remain single-string to avoid
unnecessary mass and hardware.

Sparing will also be supported through **fault detection, isolation, and
recovery (FDIR)**. The spacecraft will monitor system health and
automatically transition affected equipment to backup or safe modes when
required. This approach allows ZELVORA to maintain useful functionality
following individual failures while keeping the overall spacecraft
design practical for a Class B mission.

## Risk Assessment

The project team shall produce a risk register (ref CADRe part C).

## Organizational Breakdown Structure

Canada has established cooperation with both **EOSA and JSRA**,
including collaboration in robotics, Earth observation, space
technology, and sustainable space activities.

### ZELVORA Project Partners: Space Agencies and Government Organizations

  ---------------------------------------------------------------------------
  **Partner**           **Type**        **Role in ZELVORA**
  --------------------- --------------- -------------------------------------
  **Canadian Space      Government /    Leads ZELVORA and is responsible for
  Agency (CSA)**        Prime           spacecraft design, construction,
                                        integration, testing, and mission
                                        operations.

  **European Orbital    International   Provides fictional international
  Systems Agency        Agency          expertise in orbital debris removal
  (EOSA)**                              and spacecraft servicing.

  **Japan Space         International   Supports fictional research in
  Robotics Agency       Agency          robotic capture and autonomous
  (JSRA)**                              rendezvous technologies.

  **Northstar Orbital   Industrial      Develops propulsion and orbital
  Technologies**        Vendor          maneuvering hardware.

  **Aetheris Space      Industrial      Develops the robotic capture arm and
  Robotics**            Vendor          capture mechanism.

  **Polarion Avionics   Industrial      Supplies avionics, flight computers,
  Corporation**         Vendor          and payload electronics.

  **Borealis Vision     Industrial      Develops cameras and optical
  Systems**             Vendor          navigation sensors.

  **Canterra Space      Industrial      Supports spacecraft communication
  Communications**      Vendor          hardware and ground interfaces.

  **Northern Institute  University      Researches autonomous rendezvous,
  of Space                              guidance, and navigation.
  Engineering**                         

  **Laurentia           University      Supports robotic capture research and
  University of                         spacecraft testing.
  Aerospace                             
  Technology**                          

  **Boreal Technical    University      Conducts structural, thermal, and
  University**                          spacecraft-environment research.

  **Canadian Orbital    Canadian OGD    Provides fictional orbital tracking
  Safety Directorate                    and conjunction-monitoring support.
  (COSD)**                              

  **Canadian Space      Canadian OGD    Provides fictional space-weather and
  Environment Office                    orbital-environment information.
  (CSEO)**                              

  **National Aerospace  Canadian OGD    Provides independent engineering
  Research Directorate                  analysis, testing support, and
  (NARD)**                              technical review.
  ---------------------------------------------------------------------------

### Principal Investigators

  ------------------------------------------------------------------------
  **Principal      **Area of Responsibility**  **Affiliated International
  Investigator**                               Agency**
  ---------------- --------------------------- ---------------------------
  **Dr. Maya       Autonomous Rendezvous &     European Orbital Systems
  Laurent**        Navigation                  Agency (EOSA)

  **Dr. Daniel     Robotic Capture Systems     Japan Space Robotics Agency
  Okafor**                                     (JSRA)

  **Dr. Elise      Orbital Debris & Space      European Orbital Systems
  Tremblay**       Sustainability              Agency (EOSA)

  **Dr. Nathan     Spacecraft Structures &     Japan Space Robotics Agency
  Chen**           Thermal Systems             (JSRA)

  **Dr. Sofia      Propulsion & Orbital        European Orbital Systems
  Moreau**         Maneuvering                 Agency (EOSA)

  **Dr. Marcus     Flight Software & Autonomy  Japan Space Robotics Agency
  Bennett**                                    (JSRA)

  **Dr. Amélie     Spacecraft Power & Avionics European Orbital Systems
  Rousseau**                                   Agency (EOSA)

  **Dr. Liam       Mission Operations & Ground Japan Space Robotics Agency
  Carter**         Systems                     (JSRA)
  ------------------------------------------------------------------------

####### 
