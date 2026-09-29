CSA-FIN-RD-0765

Canadian Space Agency

Office of the Chief Financial Officer (OCFO)

+----------------------------------------------------------------------+
| Cost Analysis Data Requirements (CADRe)                              |
|                                                                      |
| PART A                                                               |
|                                                                      |
| > Mission : LUMEN Exoplanet Observatory                              |
| >                                                                    |
| > Key Decision Point : CDR                                           |
| >                                                                    |
| > EPMO Gate : Gate R3                                                |
|                                                                      |
| Draft 3.0                                                            |
|                                                                      |
| August 19, 2026                                                      |
+----------------------------------------------------------------------+
|                                                                      |
+----------------------------------------------------------------------+

This Page Intentionally Left Blank

Revision History

  ------------------------------------------------------------------------
  Rev.      Description                      Prepared by    Date
  --------- -------------------------------- -------------- --------------
  Draft 1.0 Initial draft                    MB             19 Aug 2026

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            

                                                            
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
[11](#high-level-mission-architecture)](#high-level-mission-architecture)

[3 Space Segment Description
[12](#space-segment-description)](#space-segment-description)

[3.1 Spacecraft Bus [12](#spacecraft-bus)](#spacecraft-bus)

[4.1 CEAM Payload [12](#ceam-payload)](#ceam-payload)

[5 Launch Segment description
[14](#launch-segment-description)](#launch-segment-description)

[6 Ground Segment and Mission Operations
[14](#ground-segment-and-mission-operations)](#ground-segment-and-mission-operations)

[7 Ground Segment and Mission Operations
[14](#science-segment)](#science-segment)

[8 Systems Engineering and Project Management Approach
[15](#systems-engineering-and-project-management-approach)](#systems-engineering-and-project-management-approach)

[8.1 TRL Levels and Heritage
[15](#trl-levels-and-heritage)](#trl-levels-and-heritage)

[8.2 Phasing Logic and Naming conventions
[15](#phasing-logic-and-naming-conventions)](#phasing-logic-and-naming-conventions)

[8.3 CSA PRoject Milestones
[16](#csa-project-milestones)](#csa-project-milestones)

[8.4 Safety and Mission Assurance
[17](#safety-and-mission-assurance)](#safety-and-mission-assurance)

[8.5 Prototyping (MODEL Philosophy), Qualification and Verification
Strategy
[17](#prototyping-model-philosophy-qualification-and-verification-strategy)](#prototyping-model-philosophy-qualification-and-verification-strategy)

[8.6 Sparing Straegy [17](#sparing-straegy)](#sparing-straegy)

[8.7 Risk Assessment [18](#risk-assessment)](#risk-assessment)

[8.8 Organizational Breakdown Structure
[18](#organizational-breakdown-structure)](#organizational-breakdown-structure)

List of Figures

FIGURE PAGE

Figure 1 -- CEAM instrument on the LUMEN Observatory\]
[8](#_Toc240546292)

Figure 2 -- Simplified optical path from Telescope to Focal Plane Array
[13](#_Toc240546293)

List of TABLES

[Table 1 - Strategic Alignment [8](#_Toc240546294)](#_Toc240546294)

[Table 2 -- Selected SYSTEM Requirements
[9](#_Toc240546295)](#_Toc240546295)

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

The **LUMEN Exoplanet Observatory** is a proposed European-led space
science mission dedicated to discovering and characterizing planets
orbiting nearby stars. Its primary objective is to identify potentially
habitable worlds and examine the physical and chemical properties of
their atmospheres. The mission would study planets of different sizes
and temperatures, ranging from hot gas giants to small rocky planets
located within the habitable zones of their host stars.

The observatory would be placed in a stable orbit near the Sun--Earth L2
region, where it could conduct long-duration observations with limited
interruptions from Earth. A medium-aperture telescope would collect
visible and infrared light from selected planetary systems. LUMEN would
use several complementary observing techniques, including transit
photometry, transit spectroscopy and direct measurement of changes in a
star's light as a planet moves through its orbit. These observations
would help determine planetary size, orbital characteristics,
atmospheric composition and temperature.

Canada would contribute the **Canadian Exoplanet Atmospheric Mapper
(CEAM)**, a specialized scientific instrument designed to separate
incoming light into multiple spectral bands. CEAM would search for
atmospheric signatures associated with water vapour, carbon dioxide,
methane, clouds and other compounds. Canada would also provide elements
of the instrument electronics, calibration system, data-processing
software and scientific analysis capability.

The European mission partner would be responsible for the spacecraft
platform, telescope, launch service, mission operations and overall
system integration. Canadian scientists and engineers would participate
in instrument development, mission planning, commissioning and
scientific operations. In return for its contribution, Canada would
receive guaranteed access to mission observations and opportunities for
Canadian researchers and students.

LUMEN is envisioned as a five-year mission, with the possibility of an
extended operational phase. Its results would provide a catalogue of
characterized exoplanets, identify high-priority targets for future
missions and improve scientific understanding of how planetary systems
form and evolve.

The diagram now shows the **Canadian Exoplanet Atmospheric Mapper
(CEAM)** as the red internal module, with a prominent arrow pointing
directly to its location inside the observatory.

![[]{#_Toc240546292 .anchor}Figure 1 -- CEAM instrument on the LUMEN
Observatory\]](media/image3.png){width="6.496527777777778in"
height="3.65625in"}

## Strategic Objectives

Consistent with the Government of Canada\'s Space Policy Framework, the
WFS mission supports the following 2 main strategic goals:

+---+--------------+----------------------------------------------------------+
|   | **Strategic  | **Space Strategy**                                       |
|   | Goals**      |                                                          |
+===+==============+==========================================================+
| 5 | **DISCOVER** | Expand human knowledge through scientific discoveries.   |
|   |              |                                                          |
|   |              | The investment will expand human knowledge by enabling   |
|   |              | Canadian scientists to detect and characterize           |
|   |              | exoplanets and study the composition of their            |
|   |              | atmospheres.                                             |
+---+--------------+----------------------------------------------------------+
| 4 | **ENABLE**   | Position the space sector to help grow the economy       |
|   |              |                                                          |
|   |              | The investment will strengthen Canada's space sector by  |
|   |              | advancing domestic expertise and technologies in space   |
|   |              | instrumentation, data processing and exoplanet science   |
|   |              | through an international partnership.                    |
+---+--------------+----------------------------------------------------------+
| 2 | **INSPIRE**  | Inspire Canadians to reach for the stars.                |
|   |              |                                                          |
|   |              | The mission's search for potentially habitable worlds    |
|   |              | will engage Canadians and inspire students and           |
|   |              | researchers to pursue careers in science, technology,    |
|   |              | engineering and space exploration.                       |
+---+--------------+----------------------------------------------------------+

: []{#_Toc240546294 .anchor}Table 1 - Strategic Alignment

Additionally, LUMEN contributes to Space Diplomacy through international
partnerships.

## Selected Mission Requirements

The following presents a summary of selected mission requirements. The
complete and authoritative set of requirements is contained in the
Mission Requirements Document (link MRD)

**Level 1 Scientific Requirements**

- **Exoplanet Discovery:** Detect exoplanets orbiting nearby stars and
  determine their basic orbital characteristics.

- **Planetary Characterization:** Measure the size, temperature and
  other physical properties of selected exoplanets.

- **Atmospheric Composition:** Identify and characterize gases, clouds
  and aerosols present in exoplanet atmospheres.

- **Planetary Habitability:** Assess the environmental conditions of
  rocky exoplanets and identify promising candidates for future studies
  of habitability and potential biosignatures.

[]{#_Toc240546295 .anchor}Table 2 -- Selected SYSTEM Requirements

The following are suitable **preliminary system-level requirements** for
the fictional LUMEN mission. The numerical values are intentionally
conceptual and would need confirmation through mission trade studies.

  ---------------------------------------------------------------------------
  **Cost- and          **Preliminary requirement**   **Principal cost and
  complexity-driving                                 complexity effects**
  system requirement**                               
  -------------------- ----------------------------- ------------------------
  Telescope aperture   The observatory shall provide Drives telescope size,
                       a telescope with an effective mirror manufacturing,
                       aperture of at least **2.0    structural stability,
                       m**.                          launch volume,
                                                     spacecraft mass and
                                                     launch-vehicle
                                                     selection.

  Spectral coverage    The observatory shall measure Requires multiple
                       exoplanet spectra over a      detector technologies,
                       wavelength range of           optical channels,
                       approximately **0.6--5.0      filters, calibration
                       μm**.                         equipment and thermal
                                                     control.

  Spectral resolution  CEAM shall provide selectable Drives optical design,
                       spectral resolving power of   detector count,
                       approximately **R =           instrument calibration,
                       100--1,000**, depending on    data volume and
                       the observing mode.           processing complexity.

  Measurement          The observatory shall         Drives detector
  stability            maintain the photometric and  performance, thermal
                       spectroscopic stability       stability, calibration,
                       required to detect variations contamination control
                       in stellar brightness of      and systematic-error
                       approximately **20 parts per  correction.
                       million** during a transit    
                       observation.                  

  Pointing performance The spacecraft shall maintain Drives attitude-control
                       line-of-sight stability       sensors and actuators,
                       within approximately **20     structural stability,
                       milliarcseconds** during      vibration isolation and
                       science observations.         guidance software.

  Thermal environment  CEAM detectors shall operate  May require passive
                       at temperatures below         cooling, mechanical
                       approximately **70 K**, with  cryocoolers, thermal
                       temperature variations        shielding, specialized
                       controlled during             materials and additional
                       observations.                 power.

  Operational orbit    The observatory shall operate Drives launch energy,
                       in a **Sun--Earth L2 halo or  propulsion, navigation,
                       Lissajous orbit** and support communications range,
                       station-keeping throughout    radiation design and
                       the mission.                  ground operations.

  Mission life         The observatory shall provide Drives redundancy,
                       at least **five years of      component quality, fuel
                       science operations**, with    capacity, reliability
                       consumables and reliability   analysis, testing and
                       provisions supporting a goal  obsolescence management.
                       of **eight years**.           

  Communications and   The observatory shall return  Drives antenna size,
  data                 at least **100 gigabits of    transmitter power,
                       science and engineering data  onboard storage,
                       per day** through the         communications
                       European ground segment.      scheduling and ground
                                                     infrastructure.

  Canadian instrument  The European observatory      Drives international
  interface            shall accommodate CEAM as a   coordination, interface
                       separately developed Canadian control, verification
                       instrument and provide        facilities, schedule
                       defined mechanical,           reserves and joint
                       electrical, thermal, optical, integration and testing.
                       software and data interfaces. 
  ---------------------------------------------------------------------------

## High-Level Mission Architecture 

Owned and operated by ESA, the mission consists of the following
segments, howere CSA is only responsible for the **Canadian Exoplanet
Atmospheric Mapper (CEAM)**.

- A **Government Segment**: consisting of government resources for
  oversight and their associated management costs such as T&L

- A **Space Segment**: consisting of four spacecrafts with a
  platform/bus and a infrared instrument.

- A **Launch Segment**: consisting of the launcher and launch service
  provider, provided by ESA.

- A **Ground Segment**: consisting of facilities and equipment to plan
  and command acquisitions, as well as, to receive, archive and process
  data acquired by the satellite, provided by ESA.

- An **Ops Segment**: consisting of personnel to handle real-time
  operations and some O&M costs, provided by ESA

- A **Science Segment**: consisting of scientific leadership, research
  teams, and supporting infrastructure responsible for mission science
  planning, calibration and validation, data analysis, scientific data
  products, user support, and the maximization of scientific return from
  the mission.

# Space Segment Description

The space segment consists of a constellation of 4 spacecrafts, each
with a bus and a payload. The 4^th^ spacecraft is an on-orbit spare.

## Spacecraft Bus 

4.  **Vespera-L2 Spacecraft Platform**

The **Vespera-L2** is a fictional European spacecraft platform proposed
as the service module for the LUMEN Exoplanet Observatory. It would be
developed by the fictional prime contractor **Elystria Orbital Systems**
and adapted specifically for long-duration astronomical observations
near the Sun--Earth L2 point. The platform would support the European
telescope and payload module, including Canada's **Canadian Exoplanet
Atmospheric Mapper (CEAM)**.

Vespera-L2 would provide the observatory's structural support,
electrical power, propulsion, communications, command and data handling,
attitude control and thermal-management services. A modular mechanical
interface would connect the relatively warm service module to the
cryogenic payload module while limiting the transfer of heat and
vibration to the telescope and scientific instruments. Deployable solar
arrays would generate electrical power, while rechargeable batteries
would maintain spacecraft functions during launch and contingency
operations.

A high-precision attitude-control system using star trackers, reaction
wheels and fine-guidance information from the payload would maintain the
stable pointing required for exoplanet transit observations. Small
electric-propulsion thrusters would perform trajectory corrections, L2
orbit insertion, station-keeping, momentum unloading and end-of-mission
disposal. The platform would also incorporate redundant flight
computers, fault-detection and recovery functions, and
radiation-tolerant electronics to support autonomous operations far from
Earth.

Science and engineering data would be stored in a redundant onboard
memory system and transmitted to the European ground segment through a
steerable high-gain antenna. The platform would be designed for a
minimum five-year operational mission, with sufficient consumables and
reliability provisions to support a possible extension to eight years.
Its modular payload interfaces would allow CEAM to be developed and
tested in Canada before delivery for integration with the European
observatory.

## CEAM Payload

The **Canadian Exoplanet Atmospheric Mapper (CEAM)** is the principal
Canadian contribution to the LUMEN Exoplanet Observatory. The instrument
receives light collected by the European telescope and measures small
variations in the spectrum of a star as an exoplanet passes in front of
it. These measurements are used to identify water vapour, carbon
dioxide, methane, clouds and other atmospheric characteristics.

CEAM is notionally developed by the fictional Canadian prime contractor
**Maple Arc Space Instruments**. The instrument has an estimated mass of
140 kg, requires approximately 300 W during science observations and
operates over a spectral range of 0.6--5.0 μm.

![[]{#_Toc240546293 .anchor}Figure 2 -- Simplified optical path from
Telescope to Focal Plane
Array](media/image4.png){width="6.486111111111111in"
height="2.2743055555555554in"}

### Optical Bench 

The optical components are mounted on a lightweight
**carbon-fibre-reinforced polymer (CFRP) optical bench** designed to
provide high stiffness and low thermal expansion. The bench incorporates
precision metallic or composite inserts for mounting and alignment of
the optical components. Its laminate configuration, joints and surface
treatments are selected to minimize moisture release, dimensional
changes and optical misalignment during launch, cooldown and operation
in the cryogenic space environment.

### Optical Subsystem

The **StarPath Optical Assembly**, supplied by the fictional company
**Northlight Precision Optics**, receives the telescope beam and directs
it toward CEAM's scientific channels. Mirrors, filters and beam
splitters divide the incoming light into visible, near-infrared and
mid-infrared wavelength bands.

The **SpectrumArc Spectrometer**, developed by **Maple Arc Space
Instruments**, separates the incoming light into its component
wavelengths. It provides multiple observing modes with spectral
resolving power between approximately R = 100 and R = 1,000. The
spectrometer contains diffraction gratings, precision mirrors and
selectable optical elements but has few moving parts to reduce
mechanical risk.

The **DeepView Focal Plane Detector Assembly**, supplied by the
fictional company **Redstone Photon Devices**, converts the dispersed
light into digital measurements. Separate visible and infrared detector
arrays provide sensitivity across CEAM's wavelength range. The detectors
are designed for low noise, high stability and repeated observations of
very small changes in stellar brightness.

### Cryogenic and Thermal-Control Subsystem

The **FrostLine Thermal System**, developed by the fictional company
**Cryovanta Space Technologies**, maintains the infrared detectors below
approximately 70 K. It combines passive radiators, thermal straps,
insulation, heaters and a miniature mechanical cryocooler. Precision
temperature sensors and control electronics minimize thermal variations
that could affect scientific measurements.

### Calibration Subsystem

The **TrueStar Calibration Unit**, supplied by **Northlight Precision
Optics**, provides stable internal light sources and reference signals.
It is used to measure detector response, identify instrument drift and
distinguish genuine exoplanet signatures from changes caused by the
instrument. Calibration observations are performed before, during and
after selected science campaigns.

### Instrument Electronics

The **PolarCore Electronics Unit**, developed by the fictional company
**Avenor Space Microsystems**, distributes electrical power, controls
the detectors and mechanisms, collects housekeeping telemetry and
digitizes scientific measurements. Redundant processing and power
channels allow the instrument to continue operating following selected
equipment failures.

### Instrument Data-Processing Unit

The **SpectraForge Processing Unit**, supplied by the fictional company
**Quanta Harbour Technologies**, performs initial processing,
compression and storage of CEAM data. It removes detector artefacts,
packages observations and transfers the resulting data to the European
spacecraft computer for transmission to Earth.

### Instrument Software

CEAM flight software commands the instrument, controls observing modes,
monitors health and safety, and coordinates detector readout and
calibration activities. Canadian-developed ground software converts raw
measurements into calibrated spectra and supports the identification of
atmospheric gases, clouds and aerosols.

# Launch Segment description

The LUMEN Observatory will be launched aboard the fictional **Aquila-6
launch vehicle** and injected into a transfer trajectory toward the
Sun--Earth L2 point. Following separation from the launch vehicle, the
observatory will use its onboard propulsion system to perform trajectory
corrections and enter its operational L2 orbit.

ESA is providing launch.

# Ground Segment and Mission Operations

The proposed approach is for the European Space Agency (ESA) to provide
the complete ground segment and assume responsibility for operating the
LUMEN Observatory and the Canadian Exoplanet Atmospheric Mapper (CEAM).
ESA would perform spacecraft and instrument command and control,
ground-station communications, mission planning, flight dynamics, L2
orbit maintenance, health monitoring and anomaly response. CEAM
observing modes, detector operations, calibration activities and
thermal-control functions would be incorporated into the overall
mission-operations plan and commanded through the European ground
segment.

The CEAM passive optical assembly would not require routine commanding.
ESA would nevertheless monitor its associated temperatures, alignment
indicators and instrument-performance telemetry as part of normal
observatory operations. Canadian instrument specialists would provide
technical documentation, operating constraints and expert support to
ESA, particularly during commissioning, calibration campaigns and the
investigation of instrument anomalies.

Observation data would be received through the European ground network
and transferred to a Canadian science data centre. The science data
centre would process, validate and archive CEAM observations and
associated engineering and calibration data. It would also generate
standardized scientific products and maintain the information required
to trace processed results back to the original observations and
calibration files.

Canadian researchers would access CEAM scientific products through the
**Canadian Astronomy Data Centre (CADC)**. The CADC would provide the
user-facing archive, search tools and data-access services required by
the Canadian astronomy community. Data-transfer arrangements, access
rights, proprietary periods, cybersecurity requirements, metadata
standards and long-term preservation responsibilities would be
established through agreements between Canada, ESA and the participating
science organizations.

# Science Segment

# Systems Engineering and Project Management Approach

## TRL Levels and Heritage

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
| ATLO           | and Test                            |                     |
+----------------+-------------------------------------+                     |
| ATLO           | Mission Level Assembly, Test, and   |                     |
|                | Launch Operations (ATLO)            |                     |
+----------------+-------------------------------------+---------------------+
| Outbound       | Outbound Cruise is the              | Cruise              |
| Cruise         | interplanetary journey ending with  |                     |
|                | approach and orbit insertion at the |                     |
|                | destination                         |                     |
+----------------+-------------------------------------+---------------------+
| Phase E        | Nominal Operations (per design      | Phase E             |
|                | life)                               |                     |
+----------------+-------------------------------------+---------------------+
| Phase X        | Extended operations (mission        | Extended ops        |
|                | extension)                          |                     |
+----------------+-------------------------------------+---------------------+
| Phase F        | Disposal (audit)                    | Phase F             |
+----------------+-------------------------------------+---------------------+
| Phase G        | Post-Mortem data utilization        | N/A                 |
+----------------+-------------------------------------+---------------------+

The Cadre part C has the most up-to date schedule, these dates are
notional.

  --------------------------------------------------------------------------------------------------------------
               Phase 0       Phase A       Phase B       Phase C       Phase D       Operations    Mission
                                                                                                   Extension
  ------------ ------------- ------------- ------------- ------------- ------------- ------------- -------------
  Start Date   2017-Aug-15   2021-Jul-15   2023-Nov-01   2025-Jul-01   2026-Nov-26   2028-Apr-26   2039-Apr-26

  End Date     2019-Jul-15   2023-Oct-31   2025-Jul-29   2026-Nov-01   2028-Apr-25   2039-Apr-26   2039-Jul-25

  Duration (m) 23.0 mo       27.6 mo       20.9 mo       16.0 mo       17.0 mo       132.1 mo      3.0 mo
  --------------------------------------------------------------------------------------------------------------

## CSA PRoject Milestones

The project has not created a schedule baseline yet. Assuming instrument
level milestones will drive the CSA need dates.

+--------------+-----+-------------------------------+----------------------+
| **Instrument |     | **Major Milestone**           | **Milestone Date**   |
| Phases**     |     |                               |                      |
+==============+=====+===============================+======================+
| Phase 0      | MCR | Mission Concept Review        |                      |
+--------------+-----+-------------------------------+----------------------+
| Phase A      | SRR | System Requirements Review    |                      |
+--------------+-----+-------------------------------+----------------------+
| Phase B      | PDR | Preliminary Design Review     |                      |
+--------------+-----+-------------------------------+----------------------+
| Phase C      | CDR | Critical Design Review        |                      |
+--------------+-----+-------------------------------+----------------------+
| MAIT         | PSR | Pre-Ship Review               |                      |
+--------------+-----+-------------------------------+----------------------+
| ATLO         |     |                               |                      |
|              +-----+-------------------------------+----------------------+
|              | AR  | Acceptance Review or you      |                      |
|              |     | could use the PSR to the      |                      |
|              |     | launch site                   |                      |
|              +-----+-------------------------------+----------------------+
|              | L   | Launch                        |                      |
+--------------+-----+-------------------------------+----------------------+
| Cruise and   |     | Orbit insertion at Europe     |                      |
| EDL          |     |                               |                      |
|              +-----+-------------------------------+----------------------+
|              |     | Entry descent landing         |                      |
|              +-----+-------------------------------+----------------------+
|              |     | Swimming begins               |                      |
+--------------+-----+-------------------------------+----------------------+
| Phase E      |     | Start of Nominal Ops          |                      |
|              +-----+-------------------------------+----------------------+
|              |     | End of Nominal Ops            |                      |
+--------------+-----+-------------------------------+----------------------+
| Phase X      |     | End of Life                   |                      |
+--------------+-----+-------------------------------+----------------------+
| Sample       |     | When the sample arrived on    |                      |
| Return phase |     | Earth                         |                      |
+--------------+-----+-------------------------------+----------------------+

## Safety and Mission Assurance

Mission Class B

## Prototyping (MODEL Philosophy), Qualification and Verification Strategy

Consistent with the intent of the GSFC GOLD Rules for a **Class B
mission**, CEAM would use a conservative development and verification
approach emphasizing design maturity, qualification margins, redundancy
and testing at progressively higher levels of assembly. An **Engineering
Model (EM)** would be produced early to validate the optical path,
detector performance, electronics, software, thermal behaviour and
spacecraft interfaces. A structurally representative model could also be
used to confirm mechanical interfaces and predict launch-load responses.

A coupled **Structural--Thermal--Optical Performance (STOP) analysis**
would be conducted and maintained throughout instrument development.
Structural and thermal models would predict how launch loads, spacecraft
pointing, equipment dissipation and changes in the operational thermal
environment could deform or misalign the CFRP optical bench, mirrors,
gratings and focal-plane assembly. The resulting distortions would be
transferred into the optical model to assess line-of-sight error, focus,
wavefront quality, spectral registration and overall scientific
performance. Analytical models would be correlated using structural,
thermal-vacuum and optical-alignment test results and updated as the
design matures.

New or significantly modified hardware would normally be verified using
a dedicated **Qualification Model (QM)** subjected to environmental
levels and durations exceeding those expected in flight. The Flight
Model would subsequently undergo acceptance testing to screen for
manufacturing and workmanship defects. A **Protoflight Model (PFM)**
approach, in which the flight unit is tested at qualification levels for
reduced durations, could be considered for mature, flight-proven
components; however, its use would require documented risk acceptance
and would not normally be preferred for new or mission-critical CEAM
assemblies.

Testing would begin at the component and unit levels and progress
through instrument-subsystem, complete-instrument and spacecraft-level
verification. Testing would include functional performance, vibration,
acoustic, shock, electromagnetic compatibility, thermal-vacuum, thermal
balance, optical alignment, calibration and end-to-end data-flow
testing. Environmental testing would be followed by functional checks to
identify degradation or latent failures.

Electrical, electronic and electromechanical parts would be selected
from approved space-qualified part families or supported by documented
screening, qualification and radiation analysis. Mission-critical
functions would incorporate fault detection, isolation and recovery,
together with selective redundancy in power supplies, instrument
electronics, heaters, sensors and data paths. Where redundancy is
impractical---particularly for passive optics---the design would rely on
adequate margins, STOP analysis, robust qualification, contamination
control and conservative workmanship standards.

## Sparing Straegy

CEAM would use a **subassembly-level sparing strategy** focused on
critical, long-lead and failure-prone hardware. Qualified flight spares
would be maintained for detector electronics, data-processing units,
mechanisms and communication interfaces. Common components would be used
where practical to reduce the number of unique spares.

Passive optical elements and the CFRP optical bench would not normally
have complete flight spares because of their cost and specialized
manufacturing. Instead, spare mirrors, filters, gratings, mounts and
interface hardware would be procured where practical and cost effective.

Engineering models and ground-support equipment would be retained after
launch to reproduce anomalies and validate software or operational
changes.

## Risk Assessment

The project team shall produce a risk register (ref CADRe part C)

## Organizational Breakdown Structure

The following is an illustrative partnership structure. **Industry,
university and investigator names are fictional**; government and
space-agency names are real.

### Space Agencies and Government Organizations

  -------------------------------------------------------------------------------
  **Partner**          **Country/region**   **Proposed role**
  -------------------- -------------------- -------------------------------------
  **European Space     Europe               Mission lead; spacecraft, telescope,
  Agency (ESA)**                            launch, ground segment, mission
                                            operations and command and control of
                                            CEAM.

  **Canadian Space     Canada               Sponsor and manager of the Canadian
  Agency (CSA)**                            contribution; responsible for CEAM
                                            development oversight, Canadian
                                            industrial contracts and
                                            international interfaces.

  **Japan Aerospace    Japan                Contributes infrared detector
  Exploration Agency                        technology, calibration support and
  (JAXA)**                                  scientific expertise in exoplanet
                                            atmospheric observations.

  **National Research  Canada               Provides the Canadian science-data
  Council Canada                            infrastructure and access to
  (NRC)**                                   observations through the Canadian
                                            Astronomy Data Centre.

  **Innovation,        Canada               Supports spectrum coordination,
  Science and Economic                      industrial participation and the
  Development Canada                        development of Canadian space
  (ISED)**                                  technologies.

  **Global Affairs     Canada               Supports international agreements,
  Canada (GAC)**                            technology-transfer arrangements and
                                            diplomatic coordination with
                                            European, Japanese and Slovenian
                                            partners.

  **Slovenian Space    Slovenia             Coordinates Slovenia's national
  Office**                                  contribution, industrial
                                            participation and relationship with
                                            ESA.

  **Slovenian Research Slovenia             Supports Slovenian scientific
  and Innovation                            participation, research grants and
  Agency**                                  university-led data analysis.
  -------------------------------------------------------------------------------

### Industrial Partners

  -----------------------------------------------------------------------------
  **Fictional       **Country**   **Proposed role**
  partner**                       
  ----------------- ------------- ---------------------------------------------
  **Elystria        Europe        European prime contractor responsible for the
  Orbital Systems**               LUMEN spacecraft, telescope integration and
                                  observatory-level verification.

  **Maple Arc Space Canada        Canadian prime contractor responsible for
  Instruments**                   CEAM design, assembly, integration and
                                  testing.

  **Northlight      Canada        CEAM mirrors, filters, diffraction gratings
  Precision                       and optical alignment equipment.
  Optics**                        

  **CarbonNorth     Canada        CFRP optical bench, precision inserts and
  Structures**                    instrument structural assembly.

  **Cryovanta Space Canada        Cryogenic cooling equipment, thermal straps,
  Technologies**                  radiators and temperature-control hardware.

  **Avenor Space    Canada        Instrument electronics, power-conditioning
  Microsystems**                  units and radiation-tolerant data-processing
                                  hardware.

  **Velora Photonic Slovenia      Optical-fibre assemblies, calibration light
  Systems**                       sources and optical-performance test
                                  equipment.

  **Karstline Space Slovenia      Detector readout electronics, temperature
  Electronics**                   sensors and instrument-support electronics.

  **Hinodeka        Japan         Visible and infrared focal-plane detector
  Detector                        arrays developed in cooperation with JAXA.
  Technologies**                  
  -----------------------------------------------------------------------------

### Participating Academic Institutions

  -----------------------------------------------------------------------------
  **Fictional institution**  **Country**   **Proposed scientific contribution**
  -------------------------- ------------- ------------------------------------
  **Starlake University --   Canada        Leads Canadian science planning,
  Centre for Exoplanet                     atmospheric retrieval and
  Science**                                interpretation of CEAM observations.

  **Northern Dominion        Canada        Develops calibration algorithms,
  Institute of                             observation simulations and
  Astrophysics**                           stellar-activity correction methods.

  **Adriatic University of   Slovenia      Studies atmospheric chemistry,
  Science and Technology**                 clouds and aerosols in rocky
                                           exoplanets.

  **Ljublana Institute for   Slovenia      Develops machine-learning tools and
  Computational Astronomy**                atmospheric-retrieval software.

  **Hoshikawa University --  Japan         Provides molecular spectroscopy,
  Laboratory for Planetary                 detector characterization and
  Spectroscopy**                           comparative planetary science.

  **European Institute for   Europe        Coordinates the international
  Distant Worlds**                         science team, target selection and
                                           scientific-product validation.
  -----------------------------------------------------------------------------

### Scientific Leadership (Principal Investigator)

  ------------------------------------------------------------------------
  **Fictional position**     **Fictional     **Affiliation**
                             individual**    
  -------------------------- --------------- -----------------------------
  LUMEN Principal            **Dr. Eliana    European Institute for
  Investigator               Vautrin**       Distant Worlds

  Canadian Principal         **Dr. Maya      Starlake University
  Investigator for CEAM      Desrosiers**    

  CEAM Instrument Scientist  **Dr. Adrian    Maple Arc Space Instruments
                             Kells**         

  Slovenian Science          **Dr. Talia     Adriatic University of
  Co-Investigator            Zoren**         Science and Technology

  Japanese Science           **Dr. Renji     Hoshikawa University
  Co-Investigator            Amahara**       

  Canadian Data-System Lead  **Dr. Noah      Northern Dominion Institute
                             Bellavance**    of Astrophysics
  ------------------------------------------------------------------------
