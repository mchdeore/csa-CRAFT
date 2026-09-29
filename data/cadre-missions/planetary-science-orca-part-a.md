CSA-FIN-RD-0589

Canadian Space Agency

Office of the Chief Financial Officer (OCFO)

+----------------------------------------------------------------------+
| Cost Analysis Data Requirements (CADRe)                              |
|                                                                      |
| PART A                                                               |
|                                                                      |
| > Mission : ORCA                                                     |
| >                                                                    |
| > Design Reference : EDA                                             |
| >                                                                    |
| > Key Decision Point : KDP-B                                         |
| >                                                                    |
| > EPMO Gate : G3^4^                                                  |
|                                                                      |
| September 17. 2026                                                   |
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

[1 Introduction](#introduction)

[1.1 Purpose of this document](#purpose-of-this-document)

[2 General Descriptive Information](#general-descriptive-information)

[2.1 Mission Overview](#mission-overview)

[2.2 Context](#context)

[2.3 Strategic Objectives](#_Toc238050557)

[2.4 Selected Mission Requirements](#selected-mission-requirements)

[2.5 High-Level Mission Architecture](#high-level-mission-architecture)

[3 Space Segment Description](#space-segment-description)

[3.1 Spacecraft Bus](#spacecraft-bus)

[3.2 Payload](#payload)

[4 Launch Segment description](#launch-segment-description)

[5 Ground Segment and Mission
Operations](#ground-segment-and-mission-operations)

[6 Systems Engineering and Project Management
Approach](#systems-engineering-and-project-management-approach)

[6.1 TRL Levels and Heritage](#trl-levels-and-heritage)

[6.2 Phasing Logic and Naming
conventions](#phasing-logic-and-naming-conventions)

[6.3 CSA PRoject Milestones](#csa-project-milestones)

[6.4 Safety and Mission Assurance](#safety-and-mission-assurance)

[6.5 Qualification and Acceptance Strategy, MODEL
Philosophy](#qualification-and-acceptance-strategy-model-philosophy)

[6.6 Risk Assessment](#risk-assessment)

[6.7 Organizational Breakdown
Structure](#organizational-breakdown-structure)

[Appendices](#appendices)

[A Acronym List](#acronym-list)

List of Figures

FIGURE PAGE

List of TABLES

[Table 1 -- Explanation of Science Requirements](#_Toc233178906)

[Table 2 - Strategic Alignment](#_Toc233178907)

[Table 3 -- Select Mission Requirements](#_Toc233178908)

[Table X4 -- Selected Mission Requirements**Error! Bookmark not
defined.**](#_Toc233178909)

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

ORCA (Ocean Reconnaissance and Chemistry Analyzer) is a proposed
Canadian instrument suite, led by the Canadian Space Agency (CSA) and
flown on a NASA flagship mission, to determine whether the subsurface
ocean of Saturn\'s moon Enceladus is habitable and shows signs of life.

The mission\'s primary objective is to characterize the ocean\'s
chemistry by repeatedly sampling the plumes of water vapour and ice
grains that erupt from the moon\'s south polar region. Measurements of
salts, organic molecules, dissolved gases, and isotope ratios will
reveal whether the ocean holds the energy sources and nutrients that
life requires. Canadian laser altimetry and ice-penetrating radar will
map the ice shell and show how the plumes connect to the ocean below.
Together, these data will help the international science community
decide where and how to search for life on ocean worlds, and will guide
the design of future life detection missions, including an optional
lander.

.

![1](media/image3.png){width="6.0625in" height="4.041666666666667in"}

![](media/image4.png){width="6.078125546806649in"
height="4.052083333333333in"}

![](media/image5.png){width="6.5in" height="4.333333333333333in"}

![](media/image6.png){width="6.5in" height="4.333333333333333in"}

![](media/image7.png){width="6.5in" height="4.333333333333333in"}

## Context

[]{#_Toc238050557 .anchor}Several mission architectures have been
considered for ORCA. Each has its own cost and risk analysis, so any
study must state which architecture it uses.

  ---------------------------------------------------------------------------
  Option       Configuration      Spacecraft          Canadian payload
  ------------ ------------------ ------------------- -----------------------
  A (baseline) 1 orbiter, no      NASA led flagship   Laser altimeter and
               lander                                 LIDAR, ice-penetrating
                                                      radar, plume particle
                                                      analyzer

  B            1 orbiter, no      ESA led flagship    Same three instruments
               lander                                 

  C            1 orbiter and 1    NASA or ESA led     Three instruments, plus
               small lander       flagship            sampling arm on the
                                                      lander

  D            1 orbiter and 1    NASA or ESA         Particle analyzer on
               CubeSat-class      flagship, Canadian  the probe, altimeter
               companion probe    built probe         and radar on the
                                                      orbiter

  E            1 small plume      Canadian prime,     Focused suite of plume
               flyby spacecraft   partner launch and  analyzer and altimeter
                                  deep space support  
  ---------------------------------------------------------------------------

These are internal concept options. No industry studies have been
carried out yet.

## Strategic Objectives

Consistent with the Government of Canada\'s Space Policy Framework, ORCA
supports two main strategic goals. The alignment is a working assumption
to confirm with CSA.

  --------------------------------------------------------------------------
  No.   Strategic   Space strategy
        goal        
  ----- ----------- --------------------------------------------------------
  1     DISCOVER    Advance knowledge of life in the universe. ORCA will
                    test whether Enceladus\'s ocean has the chemistry and
                    energy that life needs, and will guide the search for
                    life on other ocean worlds.

  2     ENABLE      Position the space sector to help grow the economy. ORCA
                    will develop advanced Canadian instruments and robotics,
                    build international partnerships, and train highly
                    qualified personnel who will lead future missions.
  --------------------------------------------------------------------------

Additionally, ORCA contributes to space diplomacy through its
partnership with NASA or ESA.

## Selected Mission Requirements

[]{#_Toc233178908 .anchor}The table summarizes selected requirements
expected to drive mission cost, risk, and technical complexity. All
values are notional, for the concept study to refine, and the complete
and authoritative set would be held in a future Mission Requirements
Document (MRD).

  -----------------------------------------------------------------------
  Area           Key requirement
  -------------- --------------------------------------------------------
  Plume sampling Complete at least 20 plume flythroughs at altitudes
                 between 25 and 200 km, with at least 10 at relative
                 speeds below 5 km/s.

  Ocean          Measure salts, organic molecules, and dissolved gases in
  chemistry      plume grains and vapor across a mass range of at least 1
                 to 1000 Da.

  Biosignature   Detect organic compound distributions and carbon isotope
  sensitivity    ratios at parts per billion concentrations, to support
                 tests of biological versus non-biological origin.

  Ice shell      Sound the ice shell to a depth of at least 10 km near
  sounding       the south pole, with vertical resolution of 100 m or
                 better.

  Topography     Map the south polar terrain with vertical accuracy of 1
                 m and horizontal resolution of 50 m or better.

  Coverage       Cover at least 90% of the terrain south of 60° S
                 latitude with both radar and laser altimetry.

  Planetary      Comply with COSPAR planetary protection requirements for
  protection     a possibly habitable world, including end of mission
                 disposal that avoids impact with Enceladus.

  Canadian suite Combined mass of no more than 90 kg and peak power of no
  allocation     more than 120 W for the Canadian instruments.

  Mission life   Prime science mission of at least 4 years at Saturn,
                 design life of at least 15 years including cruise, and
                 consumables for at least 17 years.

  Data delivery  Deliver calibrated Level 1 data to the Canadian Science
                 Operations Centre within 7 days of receipt on Earth.
                 One-way light time to Saturn is roughly 70 to 90
                 minutes, so real time operations are not possible.

  Operations     Support onboard storage for at least 2 flythroughs of
                 raw data, and integration with the partner agency\'s
                 deep space network, mission operations, and CSA science
                 operations.
  -----------------------------------------------------------------------

  : 3

## High-Level Mission Architecture 

ORCA is a partnership mission. The Canadian Space Agency (CSA) owns and
operates the Canadian instrument suite, and a partner agency (NASA or
ESA) owns and operates the spacecraft. The mission consists of:

- **Government segment:** Government resources for oversight and
  partnership management, and their associated management costs.

- **Space segment:** One partner flagship orbiter carrying the Canadian
  laser altimeter and LIDAR, ice-penetrating radar, and plume particle
  analyzer, plus an optional small lander with a Canadian sampling arm.

- **Launch segment:** The heavy launch vehicle and launch service
  provider, supplied by the partner agency.

- **Ground segment:** Facilities and equipment to plan and command
  instrument observations and to receive, archive, and process the data,
  including the partner\'s deep space network and a Canadian Science
  Operations Centre.

- **Ops segment:** Personnel to handle instrument operations, and the
  CSA share of operations and maintenance costs.

- **Science segment:** Scientific leadership, research teams, and
  supporting infrastructure responsible for science planning,
  calibration and validation, data analysis, science data products, user
  support, and maximizing the scientific return of the mission.

# Space Segment Description

This section describes the baseline single-orbiter, no-lander
architecture (Option A), the design reference noted on the cover page.
The optional small lander and sampling arm (Option C) are discussed
separately in 3.2.10 and are excluded from the mass, power and cost
figures below unless stated otherwise.

The space segment is a single orbiter carrying the Canadian instrument
suite. There is no on-orbit spare and no second spacecraft in the
baseline.

## Spacecraft Bus

The orbiter platform would be built by the Johns Hopkins Applied Physics
Laboratory (APL), which delivered Europa Clipper, New Horizons and
Parker Solar Probe. APL has flown more outer-planet and deep-space
missions than any other US integrator, and its heritage bus architecture
is the closest fit for a decade-long cruise to Saturn.

The bus carries the instrument suite on a dedicated nadir deck and
handles structure, propulsion, command and data handling, attitude
control and thermal management. Power comes from two radioisotope
thermoelectric generators rather than solar arrays: sunlight at Saturn
is about 1% of what Earth gets, so solar is not a practical option at
this range. Batteries cover peak loads and any eclipse periods.

Pointing during flythroughs and mapping passes is handled by star
trackers and reaction wheels. Chemical thrusters handle trajectory
correction burns, the Jupiter gravity-assist flyby, Saturn orbit
insertion, Enceladus orbit insertion, momentum dumping and disposal at
end of mission. Flight computers are redundant and radiation-tolerant,
since the one-way light time to Saturn runs 70 to 90 minutes and the
spacecraft has to manage most anomalies on its own.

Onboard storage holds at least two flythroughs of raw data, downlinked
through a steerable high-gain antenna. Design life is at least 15 years
including cruise, with consumables sized for 17. The payload interface
is modular, so the instrument suite can be built and tested in Canada,
then shipped for integration with the orbiter.

## Payload

The ORCA (Ocean Reconnaissance and Chemistry Analyzer) instrument suite
is Canada\'s contribution to the mission. MDA Space would lead
integration of the three instruments, with a combined mass around 85 kg
and peak power draw around 110 W during flythroughs, in line with the
suite-level allocation in the requirements table above.

### Instrument Accommodation Structure

The three instruments and their shared electronics sit on an aluminum
and composite deck built for stiffness and low thermal drift. Mounting
inserts and alignment features keep the altimeter, radar antennas and
particle analyzer inlet boresighted through launch loads, a decade of
cruise and the thermal swings of Saturn-system operations.

### Laser Altimeter and LIDAR

Teledyne Optech, which built the laser altimeter that flew on OSIRIS-REx
under Canadian Space Agency sponsorship, would develop the Nightingale
Laser Altimeter (NLA). It measures the south polar terrain and plume
structure by timing the return of a pulsed laser beam, adapted from the
OSIRIS-REx design for Saturn-system thermal conditions. Estimated mass
is 15 kg, peak power about 25 W.

### Ice-Penetrating Radar

MDA Space, which built the RADARSAT synthetic aperture radars, would
develop the Glacia Sounding Radar (GSR). Using two 10 m deployable
dipole booms, it sounds the ice shell and locates where liquid water
sits closest to the surface. Estimated mass is 30 kg, with about 40 W
needed during sounding passes.

### Plume Particle Analyzer

ABB Inc. in Quebec, which built the Fourier-transform spectrometer on
SCISAT and supplies the sensors flying on GHGSat, would develop the
Plume Composition Spectrometer (PCS): a time-of-flight mass spectrometer
covering 1 to 1000 Da to characterize the salts, organics and dissolved
gases in plume ice grains and vapor. Estimated mass is 25 kg, with about
35 W needed during science operations.

### Cryogenic and Thermal-Control Subsystem

Honeywell Aerospace would supply the thermal system that keeps the
particle analyzer\'s detectors and the radar electronics within their
operating range, using passive radiators, thermal straps, insulation and
heaters. Temperature sensors and control electronics limit the drift
that would otherwise show up as calibration error between flythroughs.

### Calibration Subsystem

The NRC Herzberg Astronomy and Astrophysics Research Centre would
provide the reference calibration sources used to characterize
instrument response and track drift, so genuine plume signatures can be
separated from instrument artifacts. Calibration runs happen before,
during and after each science campaign.

### Instrument Electronics

Honeywell Aerospace\'s Mississauga site would build the Instrument
Control and Power Unit (ICPU), which distributes power, sequences the
three instruments during flythroughs, collects housekeeping telemetry
and digitizes the science data. Power and processing channels are
redundant, so the suite keeps operating through selected component
failures.

### Instrument Data-Processing Unit

Neptec Technologies would supply the Plume Data Processing Unit (PDPU),
which handles initial processing, compression and storage of ORCA data:
stripping instrument artifacts, packaging observations by flythrough and
handing the result to the spacecraft computer for downlink.

### Instrument Software

Flight software commands the three instruments, runs the observing
sequences for flythroughs and mapping passes, and monitors instrument
health. Ground software, developed in Canada, converts the raw telemetry
into calibrated chemistry, topography and radar products.

### Sampling Arm (Option C, optional lander)

Under Option C, a small lander near one of the tiger-stripe fractures
would carry a sampling arm built by MDA Space, drawing on the Canadarm
and Canadarm2 heritage, to collect surface material and hand it to a
lander-mounted instrument for analysis. The lander and arm sit outside
the baseline mass, power and cost figures here and would need their own
CADRe Part A if Option C moves forward.

# Launch Segment description

ORCA would launch on a heavy-lift vehicle, most plausibly SLS Block 1B
or a Falcon Heavy-class commercial vehicle, and use a Jupiter gravity
assist to reach Saturn in roughly 10 years. After separation, the
orbiter\'s own propulsion handles trajectory correction, the Jupiter
flyby and Saturn orbit insertion.

Launch is provided by the partner agency.

# Ground Segment and Mission Operations

NASA would run the ground segment and operate both the orbiter and the
ORCA suite: command and control, Deep Space Network communications,
mission planning, flight dynamics, orbit maintenance at Saturn and
Enceladus, health monitoring and anomaly response. ORCA\'s observing
modes, flythrough sequencing and calibration activities would be folded
into the overall operations plan and commanded through the DSN.

With a one-way light time of 70 to 90 minutes, real-time control is not
possible. Flythrough sequences are uplinked ahead of time and run
autonomously, with onboard storage for at least two flythroughs of raw
data.

Data comes down through the partner\'s ground network and is handed off
to a Canadian Science Operations Centre, which processes, validates and
archives ORCA\'s science and calibration data within 7 days of receipt
on Earth, and builds the standardized data products while keeping the
trace back to raw observations.

Canadian researchers would reach ORCA\'s products through a Canadian
planetary science archive. The details, data-transfer arrangements,
access rights, proprietary periods, cybersecurity, metadata standards
and long-term preservation, get worked out in agreements between Canada,
NASA and the participating science teams.

# Systems Engineering and Project Management Approach

## TRL Levels and Heritage

Technology readiness varies across the suite. The laser altimeter draws
on flight-proven heritage, while the radar, particle analyzer and
sampling arm still need development work before a critical design
review.

  -----------------------------------------------------------------------
  **Instrument / element** **TRL**   **Heritage**
  ------------------------ --------- ------------------------------------
  Nightingale Laser        TRL 6-7   Adapted from the OSIRIS-REx laser
  Altimeter (NLA)                    altimeter (Teledyne Optech) for
                                     Saturn-system thermal conditions

  Glacia Sounding Radar    TRL 4     New development; draws on RADARSAT
  (GSR)                              SAR heritage and planetary
                                     ice-sounding radar concepts

  Plume Composition        TRL 4     New development; draws on ABB\'s
  Spectrometer (PCS)                 SCISAT and GHGSat spectrometer
                                     heritage and Cassini INMS/Europa
                                     Clipper MASPEX concepts

  Spacecraft bus (APL)     TRL 6     Adapted from prior APL deep-space
                                     orbiter designs (New Horizons,
                                     Europa Clipper)

  Sampling arm (Option C   TRL 3     Draws on Canadarm and Canadarm2
  only)                              heritage, not yet flown beyond Earth
                                     orbit
  -----------------------------------------------------------------------

## Phasing Logic and Naming conventions

The following are the phases in terms of costing, consistent with CSA
costing nomenclature:

  ---------------------------------------------------------------------------
  **Costing        **Phase Description**                    **Corresponding
  Nomenclature**                                            Name for Project
                                                            team**
  ---------------- ---------------------------------------- -----------------
  PREP 1           Prototyping activities (before Gate 1)   N/A

  PREP 2           Prototyping activities (during Phase     N/A
                   0/A)                                     

  Phase 0          Concept and feasibility studies          Phase 0

  Phase A          System definition                        Phase A

  Phase B          Preliminary design                       Phase B

  Phase C          Detailed design                          Phase C

  MAIT             Manufacturing, assembly, integration and Phase D
                   test (Canadian systems, subsystems and   
                   components)                              

  ATLO             Mission-level assembly, test and launch  Phase D
                   operations                               

  Outbound Cruise  Interplanetary journey (Jupiter gravity  Cruise
                   assist) ending with Saturn orbit         
                   insertion                                

  Phase E          Nominal operations (per design life)     Phase E

  Phase X          Extended operations (mission extension)  Extended ops

  Phase F          Disposal (audit)                         Phase F

  Phase G          Post-mission data utilization            N/A
  ---------------------------------------------------------------------------

CADRe Part C carries the most current schedule; the dates below are
notional:

  ------------------------------------------------------------------------
  **Phase**                **Start Date**  **End Date**    **Duration**
  ------------------------ --------------- --------------- ---------------
  Phase 0                  2026-Jan        2027-Dec        24 mo

  Phase A                  2028-Jan        2029-Dec        24 mo

  Phase B                  2030-Jan        2031-Dec        24 mo

  Phase C                  2032-Jan        2033-Dec        24 mo

  Phase D (MAIT/ATLO)      2034-Jan        2040-Dec        84 mo

  Outbound Cruise          2041-Jan        2050-Dec        120 mo

  Phase E (Nominal Ops)    2051-Jan        2055-Dec        60 mo

  Phase X (Extension,      2056-Jan        2058-Dec        36 mo
  optional)                                                
  ------------------------------------------------------------------------

## CSA PRoject Milestones

With the project now at Gate 4, the major reviews through Critical
Design Review have been completed. The dates below reflect the current
schedule baseline and remain notional pending confirmation in CADRe Part
C.

  -------------------------------------------------------------------------
  **Instrument   **Major Milestone**                   **Milestone Date**
  Phase**                                              
  -------------- ------------------------------------- --------------------
  Phase 0        MCR - Mission Concept Review          Dec 2027 (notional)

  Phase A        SRR - System Requirements Review      Dec 2029 (notional)

  Phase B        PDR - Preliminary Design Review       Dec 2031 (notional)

  Phase C        CDR - Critical Design Review          Dec 2033 (notional)

  MAIT           PSR - Pre-Ship Review                 Jun 2040 (notional)

  ATLO           AR - Acceptance Review (or PSR to     Nov 2040 (notional)
                 launch site)                          

  ATLO           L - Launch                            2041 (notional)

  Cruise         Jupiter gravity-assist flyby          \~2043 (notional)

  Cruise         Saturn Orbit Insertion (SOI)          \~2051 (notional)

  Cruise         Enceladus orbit insertion (Phase 2    \~2052 (notional)
                 start)                                

  Phase E        Start of Nominal Ops                  \~2051 (notional)

  Phase E        End of Nominal Ops                    \~2055 (notional)

  Phase X        End of Life / disposal                2058 (notional)
  -------------------------------------------------------------------------

## Safety and Mission Assurance

Mission Class B.

The overall observatory-level classification is set by the partner
agency. Class B is assumed here for the Canadian instrument suite,
pending confirmation through the partnership agreement.

## Qualification and Acceptance Strategy, MODEL Philosophy

Consistent with the intent of the GSFC GOLD Rules for a Class B mission,
the ORCA suite would follow a conservative development and verification
approach: design maturity, qualification margins, redundancy, and
testing at progressively higher levels of assembly. An Engineering Model
would come first, to validate the optical, radar and mass spectrometer
measurement chains, electronics, software and spacecraft interfaces.

New or significantly modified hardware would normally go through a
dedicated Qualification Model, tested at environmental levels and
durations that exceed flight conditions. The flight model then undergoes
acceptance testing to screen for manufacturing and workmanship defects.
A protoflight approach, testing the flight unit itself at qualification
levels for shorter durations, could work for mature components such as
parts of the laser altimeter, but would need documented risk acceptance
and would not normally suit the radar, particle analyzer or sampling
arm.

Testing starts at the component and unit level and works up through
instrument-subsystem, complete-suite and spacecraft-level verification:
functional performance, vibration, acoustic, shock, electromagnetic
compatibility, thermal-vacuum, thermal balance, deployment testing for
the radar booms, and end-to-end data-flow checks.

Sparing would focus at the subassembly level, on critical, long-lead and
failure-prone hardware, with flight spares kept for instrument
electronics, the data-processing unit and mechanisms such as the radar
boom deployment mechanism. Engineering models and ground support
equipment stay in Canada after launch to reproduce anomalies and
validate software or operational changes.

## Risk Assessment

The project team shall produce a risk register (ref CADRe part C).

## Organizational Breakdown Structure

The table below sets out a plausible partnership structure for costing
purposes.

### Space Agencies and Government Organizations

  -------------------------------------------------------------------------------
  **Partner**              **Country/region**   **Proposed role**
  ------------------------ -------------------- ---------------------------------
  National Aeronautics and United States        Mission lead (assumed);
  Space Administration                          spacecraft, launch, deep space
  (NASA)                                        network, mission operations and
                                                command and control of ORCA

  Canadian Space Agency    Canada               Sponsor and manager of the
  (CSA)                                         Canadian contribution;
                                                responsible for ORCA development
                                                oversight, Canadian industrial
                                                contracts and international
                                                interfaces

  National Research        Canada               Provides Canadian science-data
  Council Canada (NRC)                          infrastructure and access to
                                                observations through a Canadian
                                                planetary science archive

  Innovation, Science and  Canada               Supports industrial participation
  Economic Development                          and the development of Canadian
  Canada (ISED)                                 space technologies

  Global Affairs Canada    Canada               Supports international agreements
  (GAC)                                         and diplomatic coordination with
                                                the partner agency
  -------------------------------------------------------------------------------

### Industrial Partners

  --------------------------------------------------------------------------
  **Partner**                 **Country**   **Proposed role**
  --------------------------- ------------- --------------------------------
  Johns Hopkins Applied       United States Orbiter prime; spacecraft
  Physics Laboratory (APL)                  integration and
                                            observatory-level verification

  MDA Space                   Canada        ORCA suite integration; Glacia
                                            Sounding Radar; sampling arm
                                            (Option C)

  Teledyne Optech             Canada        Nightingale Laser Altimeter

  ABB Inc.                    Canada        Plume Composition Spectrometer

  Honeywell Aerospace         Canada        Instrument Control and Power
                                            Unit; thermal control system

  Neptec Technologies         Canada        Plume Data Processing Unit

  NRC Herzberg Astronomy and  Canada        Calibration subsystem
  Astrophysics Research                     
  Centre                                    
  --------------------------------------------------------------------------

### Participating Academic Institutions

  --------------------------------------------------------------------------
  **Institution**               **Country**   **Proposed scientific
                                              contribution**
  ----------------------------- ------------- ------------------------------
  University of Waterloo,       Canada        Leads Canadian science
  Centre for Planetary Science                planning and interpretation of
  and Exploration                             ORCA observations

  Western University, Institute Canada        Ice-shell and radar sounding
  for Earth and Space                         data products; biosignature
  Exploration                                 detection criteria

  York University, Centre for   Canada        Calibration algorithms and
  Research in Earth and Space                 observation simulations
  Science                                     

  McGill University, space      Canada        Sampling arm design support
  robotics group                              and lander operations concept,
                                              Option C
  --------------------------------------------------------------------------

### Scientific Leadership (Principal Investigator)

  -----------------------------------------------------------------------
  **Position**              **Name**            **Affiliation**
  ------------------------- ------------------- -------------------------
  ORCA Principal            Dr. Elena Kowalski  University of Waterloo
  Investigator                                  

  ORCA Deputy Principal     Dr. Michael Osei    Western University
  Investigator                                  

  ORCA Instrument Scientist Dr. Sarah Lindqvist MDA Space

  Canadian Data-System Lead Dr. James Whitfield York University
  -----------------------------------------------------------------------

# Appendices

## Acronym List

  -----------------------------------------------------------------------
  **Acronym**      **Definition**
  ---------------- ------------------------------------------------------
  ATLO             Assembly, Test, and Launch Operations

  CADRe            Cost Analysis Data Requirements

  COSPAR           Committee on Space Research

  CSA              Canadian Space Agency

  Da               Dalton (unit of atomic mass)

  DSN              Deep Space Network

  EM               Engineering Model

  EPMO             Enterprise Project Management Office

  ESA              European Space Agency

  GSR              Glacia Sounding Radar

  ICPU             Instrument Control and Power Unit

  IGMF             Investment Governance and Monitoring Framework

  KDP              Key Decision Point

  LIDAR            Light Detection and Ranging

  MAIT             Manufacturing, Assembly, Integration and Test

  MCR              Mission Concept Review

  MRD              Mission Requirements Document

  NASA             National Aeronautics and Space Administration

  NLA              Nightingale Laser Altimeter

  ORCA             Ocean Reconnaissance and Chemistry Analyzer

  PCS              Plume Composition Spectrometer

  PDPU             Plume Data Processing Unit

  PDR              Preliminary Design Review

  PFM              Protoflight Model

  PSR              Pre-Ship Review

  QM               Qualification Model

  S&MA             Safety and Mission Assurance

  SOI              Saturn Orbit Insertion

  SRR              System Requirements Review

  TRL              Technology Readiness Level
  -----------------------------------------------------------------------
