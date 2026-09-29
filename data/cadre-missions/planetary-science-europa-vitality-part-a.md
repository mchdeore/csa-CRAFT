CSA-FIN-RD-1234

Canadian Space Agency

Office of the Chief Financial Officer (OCFO)

+--------------------------------------------------+
| Cost Analysis Data Requirements (CADRe)          |
|                                                  |
| (This data is definitely 100% real)              |
|                                                  |
| PART A                                           |
|                                                  |
| > Mission : Europa Vitality Exploration (EVE)    |
| >                                                |
| > Design Reference :                             |
| >                                                |
| > Key Decision Point : EDL-G4                    |
| >                                                |
| > EPMO Gate : GATE-4                             |
|                                                  |
| Draft 1 (Initial Release upon approval)          |
|                                                  |
| September 17, 2026                               |
+--------------------------------------------------+
|                                                  |
+--------------------------------------------------+

This Page Intentionally Left Blank

Revision History

  ------------------------------------------------------
  Rev.    Description             Prepared   Date
                                  by         
  ------- ----------------------- ---------- -----------
  Draft   Initial draft           SC         17
  1.0                                        September
                                             2026

                                             

                                             

                                             

                                             

                                             

                                             

                                             

                                             

                                             

                                             

                                             

                                             
  ------------------------------------------------------

This Page Intentionally Left Blank

Table of Contents

[1 Introduction [7](#introduction)](#introduction)

[1.1 Purpose of this document
[7](#purpose-of-this-document)](#purpose-of-this-document)

[2 General Descriptive Information
[7](#general-descriptive-information)](#general-descriptive-information)

[2.1 Mission Overview [7](#mission-overview)](#mission-overview)

[2.2 Context [8](#context)](#context)

[2.3 Strategic Objectives
[8](#strategic-objectives)](#strategic-objectives)

[2.4 Selected Mission Requirements
[8](#selected-mission-requirements)](#selected-mission-requirements)

[2.5 High-Level Mission Architecture
[9](#high-level-mission-architecture)](#high-level-mission-architecture)

[3 Space Segment Description
[11](#space-segment-description)](#space-segment-description)

[3.1 europa oRBITER [11](#europa-orbiter)](#europa-orbiter)

[3.2 Payload [18](#payload)](#payload)

[4 Ground Segment and Mission Operations
[33](#ground-segment-and-mission-operations)](#ground-segment-and-mission-operations)

[5 Systems Engineering and Project Management Approach
[34](#systems-engineering-and-project-management-approach)](#systems-engineering-and-project-management-approach)

[5.1 TRL Levels and Heritage
[34](#trl-levels-and-heritage)](#trl-levels-and-heritage)

[5.2 Phasing Logic and Naming conventions
[34](#phasing-logic-and-naming-conventions)](#phasing-logic-and-naming-conventions)

[5.3 CSA PRoject Milestones
[35](#csa-project-milestones)](#csa-project-milestones)

[5.4 Safety and Mission Assurance
[36](#safety-and-mission-assurance)](#safety-and-mission-assurance)

[5.5 Qualification and Acceptance Strategy, MODEL Philosophy
[36](#qualification-and-acceptance-strategy-model-philosophy)](#qualification-and-acceptance-strategy-model-philosophy)

[5.6 Risk Assessment [37](#risk-assessment)](#risk-assessment)

[5.7 Organizational Breakdown Structure
[37](#organizational-breakdown-structure)](#organizational-breakdown-structure)

List of Figures

FIGURE PAGE

Figure 1 -- LiteBIRD Space Telescope [7](#_Toc233178903)

Figure 2 -- Canadian Contribution to LiteBIRD Mission
[8](#_Toc233178904)

Figure 3 -- LiteBIRD: Exploring the very beginning of our Universe
[10](#_Toc233178905)

List of TABLES

[Table 1 -- Explanation of Science Requirements
[11](#_Toc233178906)](#_Toc233178906)

[Table 2 - Strategic Alignment [13](#_Toc233178907)](#_Toc233178907)

[Table 3 -- Select Mission Requirements
[14](#_Toc233178908)](#_Toc233178908)

[Table X4 -- Selected Mission Requirements [**Error! Bookmark not
defined.**](#_Toc233178909)](#_Toc233178909)

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

**EUROPA VITALITY EXPLORATION (EVE)** is a fictional robotic space
mission designed by the Canadian Space Agency (CSA) to investigate
Europa, one of Jupiter's largest moons, and search for potential signs
of extraterrestrial life. The mission will send a spacecraft to the
Jovian system, where an orbiter will enter orbit around Europa and
conduct detailed observations of its icy surface. Using imaging and
scientific instruments, the orbiter will study Europa's terrain and
identify a suitable location for a surface landing. After completing its
initial reconnaissance, the orbiter will deploy a lander toward the
selected site.

Once on the surface, the lander will release a small rover to begin
exploring Europa's ice. The rover will travel across the surface,
collect scientific measurements, and use a drill to penetrate the upper
layers of ice. Samples obtained from below the surface will be analyzed
for chemical or biological signatures that could indicate the presence
of life or environments capable of supporting it. The mission's overall
goal is to improve our understanding of Europa and determine whether its
hidden subsurface environment may contain evidence of biological
activity.

Figure 1 -- Mission Concept

Page 57

## Context

Different mission architectures have been proposed over the years. Each
Design Reference Mission has its own CADRe. Make sure you are using the
right file

[Industry
Response](https://livelink/livelink/llisapi.dll?func=ll&objId=298461394&objAction=browse)s

  -------------------------------------------------------
  **Prime**     **Constellation   **Bus**      **P/L**
                Size**                         
  ------------- ----------------- ------------ ----------
  SASH TECH     1 Sat             The Big Boy  SashTech
                                  Rev3         

  -------------------------------------------------------

## Strategic Objectives

Consistent with the Government of Canada\'s Space Policy Framework, the
WFS mission supports the following 2 main strategic goals:

+---+-------------+-------------------------------------------+
|   | **Strategic | **Space Strategy**                        |
|   | Goals**     |                                           |
+===+=============+===========================================+
| 1 | **EXPLORE** | **Advance scientific knowledge and        |
|   |             | exploration of the Solar System.**        |
|   |             |                                           |
|   |             | EUROPA VITALITY EXPLORATION supports the  |
|   |             | CSA's **Explore** strategy by advancing   |
|   |             | Canadian scientific and technological     |
|   |             | capabilities in deep-space exploration    |
|   |             | through the investigation of Europa's     |
|   |             | surface and subsurface environment. The   |
|   |             | mission would generate new scientific     |
|   |             | knowledge about Europa while              |
|   |             | demonstrating technologies for orbital    |
|   |             | reconnaissance, planetary landing,        |
|   |             | surface mobility, drilling, and in-situ   |
|   |             | sample analysis.                          |
+---+-------------+-------------------------------------------+
| 2 | **INSPIRE** | **Engage and inspire Canadians through    |
|   |             | space exploration.**                      |
|   |             |                                           |
|   |             | EUROPA VITALITY EXPLORATION supports the  |
|   |             | CSA's **Inspire** strategy by using a     |
|   |             | high-profile search for potential         |
|   |             | extraterrestrial life to engage Canadians |
|   |             | and promote interest in science,          |
|   |             | technology, engineering, and mathematics  |
|   |             | (STEM). The mission would provide         |
|   |             | opportunities for public outreach,        |
|   |             | education, and student participation,     |
|   |             | helping inspire the next generation of    |
|   |             | Canadian scientists and engineers.        |
+---+-------------+-------------------------------------------+

: []{#_Toc233178907 .anchor}Table 2 - Strategic Alignment

Additionally, EVE contributes to Space Diplomacy through international
partnerships.

## Selected Mission Requirements

The following table presents a summary of selected mission requirements
that are expected to be significant drivers of mission cost, risk, and
technical complexity. For clarity and accessibility, the requirements
have been consolidated, simplified, and reworded from their original
form. The complete and authoritative set of requirements is contained in
the Mission Requirements Document
([MRD](https://livelink/livelink/llisapi.dll?func=ll&objId=297999575&objAction=browse&viewType=1))

  -----------------------------------------------------------
  **Area**           **Key requirement**
  ------------------ ----------------------------------------
  **Europa           Characterize at least **90% of Europa\'s
  investigation**    accessible surface** and investigate its
                     subsurface environment to assess the
                     moon\'s geological, chemical, and
                     biological potential.

  **Jovian transit** Transport the mission spacecraft from
                     Earth to the Jovian system and arrive at
                     Jupiter within **7 years of launch**.

  **Europa orbit**   Establish and maintain a **100--500 km
                     circular polar orbit** around Europa for
                     a minimum of **180 days** of orbital
                     science operations.

  **Surface          Acquire imagery of at least **95% of
  reconnaissance**   Europa\'s accessible surface** at a
                     ground sampling distance of **≤10
                     m/pixel** prior to landing-site
                     selection.

  **Landing site**   Identify and select a landing site with
                     a horizontal landing uncertainty of
                     **≤500 m**, terrain slopes of **≤15°**,
                     and sufficient communication visibility
                     to support surface operations.

  **Surface          Deliver the lander to the selected site
  landing**          and achieve a successful soft landing
                     with a vertical velocity of **≤3 m/s**
                     and horizontal velocity of **≤1 m/s** at
                     touchdown.

  **Rover            Deploy a rover capable of traversing at
  exploration**      least **5 km** across Europa\'s surface
                     and conducting scientific observations
                     at a minimum of **10 distinct
                     investigation sites**.

  **Subsurface       Acquire at least **6 subsurface ice
  sampling**         samples** from depths of up to **3 m**
                     below the local surface during the
                     primary rover mission.

  **Sample           Analyze acquired samples for **organic
  analysis**         compounds, elemental composition,
                     mineralogy, and potential
                     biosignatures**, with a minimum of **4
                     distinct analytical techniques**.

  **Data return**    Return at least **95% of
                     mission-critical scientific and
                     engineering data** generated during the
                     mission to Earth, with all critical data
                     received within **30 days** of
                     acquisition.
  -----------------------------------------------------------

  : []{#_Toc233178908 .anchor}Table 3 -- Selected Mission Requirements

## High-Level Mission Architecture 

Owned and operated by CSA, the mission consists of

- **Government Segment:** consisting of CSA resources for mission
  oversight, program governance, science management, and associated
  management costs such as travel and logistics.

- **Space Segment:** consisting of an internationally provided **Europa
  orbiter and lander**, and a **Canadian-developed rover and scientific
  payload**. The orbiter will perform Europa reconnaissance and support
  communications, while the lander will deliver the Canadian rover to
  the selected surface location.

- **Launch Segment:** consisting of an internationally provided launch
  vehicle and launch service provider responsible for delivering the
  spacecraft to the required interplanetary trajectory.

- **Ground Segment:** consisting of facilities, equipment, software, and
  personnel required to plan and command mission activities, monitor
  spacecraft health, receive and process telemetry, and receive,
  archive, and distribute scientific data.

- **Operations Segment:** consisting of the resources required to
  conduct routine mission operations, including mission planning,
  spacecraft and rover commanding, flight dynamics, anomaly response,
  scheduling, communications operations, and operational support
  throughout the mission lifecycle.

- **Science Segment:** consisting of the scientific teams, facilities,
  analytical resources, and data-processing capabilities required to
  define scientific investigations, plan observations, analyze returned
  data and samples, and generate scientific products and mission
  findings.

- **Mission-Level SEITPM:** consisting of the **systems engineering,
  integration and test, and program management** activities required to
  coordinate the mission as an integrated space system. This includes
  requirements management, system architecture, interface management,
  verification and validation, configuration management, risk
  management, integration and test planning, and overall program/project
  management.

- **International Partner Segment:** consisting of partner-agency
  resources supporting the development, integration, operation, and
  maintenance of the internationally provided mission elements and their
  interfaces with the Canadian rover and ground systems.

# Space Segment Description

The EVE space segment consists of three primary spacecraft elements: a
**Europa Orbiter**, a **Europa Lander**, and a **Canadian Surface
Rover**. The orbiter provides Europa reconnaissance, communications
relay, and mission support; the lander provides controlled descent and
surface deployment; and the Canadian rover performs surface mobility,
subsurface sampling, and in-situ scientific investigation.

The three elements operate as an integrated system throughout the
mission. During the orbital phase, the Europa Orbiter surveys the
surface and identifies candidate landing sites. Following site
selection, the lander separates from the orbiter and performs its
descent to Europa. Once surface operations have been established, the
lander deploys the Canadian rover, which conducts the primary surface
and subsurface science campaign.

## europa oRBITER

The Europa Orbiter provides the primary remote-sensing and
communications platform for EVE. The spacecraft is responsible for
transporting the lander to the Europa vicinity, conducting orbital
reconnaissance, supporting landing-site selection, and providing a
communications relay between the surface assets and Earth.

Key functions of the orbiter include:

- Electrical power generation and distribution

- Three-axis attitude determination and control

- Orbital navigation and control

- Command and data handling

- High-gain communications with Earth

- Communications relay with the lander and rover

- Europa surface imaging and remote sensing

- Lander deployment

- Thermal control

- Fault management and autonomous spacecraft protection

### Structural Subsystem

The orbiter primary structure consists of a lightweight aluminum-lithium
frame with carbon-fibre-reinforced polymer secondary structures.
Honeycomb sandwich panels are used for equipment decks and instrument
mounting surfaces.

The structure is designed to withstand launch loads, interplanetary
cruise loads, Europa orbit insertion, and the mechanical loads
associated with lander separation.

  ---------------------------------
     **Subsystem /     **Notional
      Component**      Mass**
  -------------------- ------------
   Primary structural  185 kg
         frame         

  Equipment decks and  95 kg
         panels        

   High-gain antenna   32 kg
   support structure   

      Solar-array      28 kg
       deployment      
       mechanisms      

   Lander separation   46 kg
       mechanism       

  Instrument mounting  24 kg
       structures      

      Harness and      38 kg
  structural fittings  

      **Structural     **448 kg**
   subsystem total**   
  ---------------------------------

### Electrical power generation and distribution

The orbiter uses deployable solar arrays during the Earth-to-Jupiter
cruise and Europa orbital phases. Because solar intensity at Jupiter is
significantly lower than at Earth, the arrays are sized for end-of-life
operation at the Jovian distance.

Two large deployable solar wings provide approximately **9.5 kW of
beginning-of-life electrical power at 5.2 AU**. The spacecraft power
system distributes regulated power to the spacecraft bus, communications
system, instruments, propulsion system, and lander interface.

**Solar Array**

- Two deployable solar-array wings

- Triple-junction photovoltaic cells

- Approximately **72 m² total active solar-cell area**

- Beginning-of-life generation: **9.5 kW**

- End-of-life generation: **7.2 kW**

- Array operating voltage: approximately **120 V**

- Independent array strings provide fault tolerance

**Battery**

A rechargeable lithium-ion battery system provides energy storage during
periods of eclipse and high instantaneous power demand.

- Nominal capacity: **18 kWh**

- Operating voltage: **100--120 V**

- Two independent battery modules

- Battery thermal control through dedicated heaters and radiators

- Designed for approximately **2,500 equivalent deep-discharge cycles**

**Power Control and Distribution**

The Power Control and Distribution Unit (PCDU) regulates spacecraft
power and provides switched distribution to all major loads.

Functions include:

- Solar-array power regulation

- Battery charge/discharge control

- Primary and secondary power distribution

- Load switching

- Over-current protection

- Fault isolation

- Power telemetry

- Emergency load shedding

### Command an Data handling

The Command and Data Handling (CDH) subsystem provides centralized
spacecraft computing, data processing, storage, command execution, and
fault management.

The system consists of two redundant flight computers operating in a
cold-redundant configuration.

Each computer provides:

- 64-bit radiation-tolerant processor

- **16 GB radiation-tolerant non-volatile memory**

- **2 TB solid-state mass memory**

- Error detection and correction

- Time-tagged command execution

- Autonomous fault detection and recovery

- Instrument command and control

- Data compression and packetization

- Software and firmware upload capability

The CDH subsystem interfaces with the spacecraft through redundant
high-speed data buses. Critical spacecraft functions can continue
following the loss of one flight computer.

### Thermal Subsystem

The orbiter uses a combination of passive and active thermal-control
techniques to maintain spacecraft components within their allowable
temperature ranges.

Thermal-control methods include:

- Multi-layer insulation

- High-emissivity radiator surfaces

- Low-emissivity thermal coatings

- Heat pipes

- Conductive thermal straps

- Localized electrical heaters

- Thermostatically controlled heater circuits

Particular thermal attention is required for the spacecraft propulsion
system, batteries, instruments, and communications electronics.

The nominal spacecraft component operating range is approximately
**−30°C to +55°C**, with survival limits extending to approximately
**−60°C to +70°C**, depending on the individual component.

The thermal subsystem is designed to support spacecraft operations from
Earth departure through Europa orbital operations.

### Attitude Determination and Control Subsystem

The orbiter uses a redundant three-axis attitude-control system to
support high-resolution imaging, communications, propulsion maneuvers,
and lander deployment.

Attitude determination is provided by:

- Two star trackers

- Six sun sensors

- Two inertial measurement units

- Two rate gyroscope assemblies

- One magnetometer

Attitude control is provided by:

- Four reaction wheels

- Twelve hydrazine-compatible reaction-control thrusters

- Thruster-based momentum unloading

- Autonomous safe-mode sun acquisition

The spacecraft provides a nominal pointing accuracy of **≤0.05°** during
science operations and **≤0.01°** during high-resolution imaging.

Unlike an Earth-orbiting spacecraft, the orbiter does not use GPS for
navigation. Position and velocity are determined using ground-based
radiometric tracking combined with onboard optical navigation
observations of Europa and Jupiter.

### Propulsion subsystem

The orbiter propulsion subsystem provides the delta-V required for
interplanetary trajectory correction, Jupiter arrival, Europa orbit
insertion, orbit maintenance, collision avoidance, and lander deployment
operations.

The primary propulsion system uses a **bipropellant chemical propulsion
system** consisting of monomethylhydrazine (MMH) and nitrogen tetroxide
(NTO).

  -------------------------------
  **Parameter**      **Notional
                     Value**
  ------------------ ------------
  Propellant         MMH / NTO

  Main engine thrust 1.8 kN

  Specific impulse   320 s

  Propellant load    1,850 kg

  Main propulsion    2
  tanks              

  Reaction-control   12
  thrusters          

  Nominal mission ΔV 2.65 km/s

  ΔV reserve         15%
  -------------------------------

The propulsion system provides the primary maneuvering capability
required for Europa orbit insertion and subsequent orbital operations.

**Notional ΔV Budget**

  ------------------------
  **Maneuver**    **ΔV**
  --------------- --------
  Trajectory      180 m/s
  correction      

  Jupiter orbit   1,450
  insertion       m/s

  Europa orbit    720 m/s
  insertion       

  Orbit           160 m/s
  adjustment and  
  phasing         

  Lander          55 m/s
  deployment      
  maneuver        

  Collision       40 m/s
  avoidance       

  Mission reserve 395 m/s

  **Total ΔV      **3.00
  capability**    km/s**
  ------------------------

### TT&C

The orbiter Telemetry, Tracking and Command (TT&C) subsystem provides
communications between the spacecraft and Earth and acts as the primary
communications relay for the lander and rover.

The system consists of:

- One high-gain parabolic antenna

- Two medium-gain antennas

- Two low-gain antennas

- X-band command and telemetry system

- Ka-band high-rate science-data transmitter

- Redundant receivers

- Radio-frequency switching network

**Earth Communications**

  ------------------------------
  **Parameter**     **Notional
                    Value**
  ----------------- ------------
  Command frequency X-band

  Telemetry         X-band
  frequency         

  Science downlink  Ka-band

  Maximum science   4 Mbps
  downlink rate     

  Nominal science   1 Mbps
  downlink rate     

  Command uplink    128 kbps
  rate              

  High-gain antenna 3.5 m
  diameter          

  Maximum           150 W
  transmitter RF    
  power             
  ------------------------------

Communications with Earth are performed through NASA/ESA/CSA-compatible
deep-space ground-station infrastructure.

> **Surface Communications**

The orbiter provides a relay link between Europa\'s surface assets and
Earth.

- Lander ↔ Orbiter: UHF

- Rover ↔ Lander: UHF

- Rover ↔ Orbiter: UHF/S-band contingency link

- Nominal rover-to-lander data rate: **2 Mbps**

- Nominal lander-to-orbiter data rate: **8 Mbps**

The communications architecture allows the rover to continue collecting
scientific data during periods when direct communication with Earth is
unavailable.

## Payload

The **Europa Orbiter payload** consists of:

- One (1) high-resolution visible imaging system

- One (1) multispectral imaging system

- One (1) infrared spectrometer

- One (1) thermal infrared imager

- One (1) ice-penetrating radar

- One (1) magnetometer

- One (1) dust and particle analyzer

- One (1) payload electronics unit

The **Europa Lander payload** consists of:

- One (1) panoramic imaging system

- One (1) microscopic imaging system

- One (1) seismometer

- One (1) environmental sensor suite

- One (1) radiation detector

- One (1) sample-handling and analysis interface

- One (1) payload electronics unit

The **Canadian Europa Rover payload** consists of:

- One (1) panoramic stereo camera

- One (1) microscopic imager

- One (1) Raman spectrometer

- One (1) mass spectrometer

- One (1) X-ray spectrometer

- One (1) radiation detector

- One (1) thermal probe

- One (1) subsurface drilling and sample-acquisition system

- One (1) in-situ sample analysis chamber

- One (1) payload electronics unit

### Europa Multispectral Infrared Imagers

The proposed **Europa Multispectral Infrared Imager (EMII)** is a
cryogenic infrared imaging instrument designed to characterize Europa\'s
surface temperature, thermal properties, and compositional variations.
The instrument combines mid-wave infrared (MWIR) and long-wave infrared
(LWIR) detectors with a shared telescope assembly and selectable
spectral filters.

The EMII detector assembly uses two infrared focal plane arrays (FPAs):

- Each FPA provides **640 × 512 pixels**, corresponding to approximately
  **328,000 infrared-sensitive pixels**.

- The MWIR detector operates primarily between **3.0 and 5.5 µm**.

- The LWIR detector operates primarily between **7.5 and 14 µm**.

- Each detector has a nominal **25 µm pixel pitch**.

- The instrument provides a maximum frame rate of approximately **30
  frames/s**.

- A five-position filter wheel provides additional spectral
  discrimination within the instrument\'s broadband response.

- The instrument is designed for both high-resolution surface mapping
  and lower-resolution wide-area thermal surveys.

**Notional Instrument Specifications**

  -----------------------------------
  **Parameter**       **Notional
                      Value**
  ------------------- ---------------
  MWIR FPA resolution 640 × 512
                      pixels

  LWIR FPA resolution 640 × 512
                      pixels

  Pixel pitch         25 µm

  MWIR spectral range 3.0--5.5 µm

  LWIR spectral range 7.5--14 µm

  Spectral channels   8

  Maximum frame rate  30 Hz

  Telescope aperture  180 mm

  Instantaneous field 0.015°/pixel
  of view             

  Full detector field 9.6° × 7.7°
  of view             

  Nominal orbital     250 km
  altitude            

  Approximate nadir   65 m/pixel
  ground sampling     

  Wide-area mapping   42 km
  swath               

  Radiometric         ≤2 K
  accuracy            

  Operating           80--320 K scene
  temperature         temperature

  Detector operating  ≤70 K
  temperature         

  Instrument power    95 W nominal

  Peak instrument     125 W
  power               

  Data rate           82 Mbps raw

  Onboard data        3:1 nominal
  compression         
  -----------------------------------

The EMII is mounted on the Europa Orbiter\'s nadir-facing instrument
deck. A two-axis pointing mechanism provides fine instrument pointing
independent of the spacecraft body, allowing targeted observations of
scientifically significant surface features.

The instrument\'s primary functions are:

- Mapping Europa\'s surface temperature distribution

- Identifying thermal anomalies

- Characterizing variations in surface ice properties

- Supporting geological feature identification

- Detecting potential active or recently active surface regions

- Supporting landing-site characterization

- Providing contextual data for higher-resolution visible and
  spectroscopic observations

At the nominal **250 km orbital altitude**, the instrument provides an
approximate **65 m/pixel ground sampling distance at nadir**. The
instrument can operate in a wide-area mapping mode or a high-resolution
targeted-observation mode.

**Optical Assembly**

The optical system consists of an all-reflective telescope using
lightweight silicon-carbide mirrors. Reflective optics are used to
provide broadband infrared performance while minimizing chromatic
aberration.

  ---------------------------------------
  **Component**   **Notional
                  Specification**
  --------------- -----------------------
  Primary mirror  180 mm
  diameter        

  Optical         Three-mirror anastigmat
  configuration   

  Effective focal 950 mm
  length          

  F-number        f/5.3

  Optical         Silicon carbide
  material        

  Focal-plane     2
  assemblies      

  Filter          5-position filter wheel
  mechanism       

  Calibration     Internal blackbody +
  system          deep-space reference
  ---------------------------------------

An internal calibration blackbody is used to provide periodic
radiometric calibration. Deep-space observations are used as a secondary
cold reference.

**Mass Estimate**

For the preliminary EVE spacecraft mass model, the complete EMII
instrument is assigned the following notional mass:

  -----------------------------
  **Item**        **Estimated
                  Mass**
  --------------- -------------
  MWIR detector   1.8 kg
  assembly        

  LWIR detector   2.1 kg
  assembly        

  Telescope and   8.5 kg
  mirrors         

  Filter wheel    1.6 kg

  Cryogenic       5.2 kg
  detector        
  assembly        

  Instrument      3.8 kg
  electronics     

  Calibration     1.4 kg
  blackbody       

  Instrument      4.1 kg
  structure       

  Thermal         2.7 kg
  hardware        

  Harness and     1.3 kg
  connectors      

  **Instrument    **32.5 kg**
  dry mass**      

  Design margin   20%

  **Allocated     **39.0 kg**
  instrument      
  mass**          
  -----------------------------

**Power Estimate**

  -------------------------
  **Operating   **Power**
  Mode**        
  ------------- -----------
  Standby       18 W

  Calibration   72 W

  Normal        95 W
  imaging       

  High-rate     110 W
  imaging       

  Peak          125 W
  -------------------------

The EMII is expected to operate primarily during Europa orbital passes
where the spacecraft geometry provides suitable viewing conditions.
Observations will be scheduled alongside the visible and spectroscopic
instruments to produce co-located datasets.

**Data Generation**

At the maximum detector frame rate, the two FPAs can generate a
substantial volume of raw data. To reduce storage and downlink
requirements, the instrument electronics perform onboard:

- Bad-pixel correction

- Non-uniformity correction

- Radiometric calibration

- Image cropping

- Lossless compression

- Optional controlled-loss compression

A typical science observation is expected to generate approximately
**1.5--4.0 GB of processed data**, depending on observation duration and
operating mode.

This makes EMII a significant contributor to the EVE orbiter\'s **mass,
power, thermal, onboard storage, and communications budgets**, giving
you a useful instrument to trace through the rest of your CADRe.

### VNIR Imager

The proposed **Europa Visible and Near-Infrared Imager (EVNII)** is a
high-resolution optical imaging instrument designed to provide detailed
characterization of Europa\'s surface. The imager will support
geological mapping, landing-site characterization, identification of
surface features, and contextual observations for the orbiter\'s other
scientific instruments.

The instrument uses a radiation-tolerant CMOS focal plane coupled to a
compact, wide-field telescope. A filter wheel provides selectable
spectral bands across the visible and near-infrared portions of the
spectrum.

  --------------------------------------
  **Parameter**     **Notional
                    Specification**
  ----------------- --------------------
  Instrument type   VNIR multispectral
                    imager

  Spectral region   0.40--1.05 µm

  Detector          Radiation-tolerant
  technology        CMOS

  Detector          4096 × 3072 pixels
  resolution        

  Pixel pitch       5.5 µm

  Maximum frame     20 Hz
  rate              

  Shutter           Global shutter

  Spectral channels 7

  Telescope         150 mm
  aperture          

  Effective focal   1.8 m
  length            

  Field of view     7.2° × 5.4°

  Nominal orbital   250 km
  altitude          

  Nadir ground      \~25 m/pixel
  sampling distance 

  Nominal imaging   \~32 km
  swath             

  Radiometric       ≤5%
  accuracy          

  Instrument mass   24 kg

  Nominal power     65 W

  Peak power        90 W

  Raw data rate     \~1.5 Gbps

  Onboard           4:1 nominal
  compression       
  --------------------------------------

The detector provides approximately **12.6 million pixels** per image.
The relatively high pixel count allows the instrument to produce
detailed surface imagery while maintaining sufficient swath for regional
mapping.

The VNIR instrument includes seven selectable spectral bands centered
approximately at:

  --------------------------------------------
  **Band**   **Central      **Primary
             Wavelength**   Application**
  ---------- -------------- ------------------
  Violet     0.43 µm        Surface scattering

  Blue       0.48 µm        Ice
                            characterization

  Green      0.55 µm        Surface morphology

  Red        0.65 µm        Geological mapping

  Deep Red   0.75 µm        Ice/terrain
                            discrimination

  Near-IR 1  0.90 µm        Hydrated materials

  Near-IR 2  1.02 µm        Surface
                            composition
  --------------------------------------------

The seven bands are acquired using a motorized filter wheel located
between the telescope and detector assembly. The system can perform
sequential multispectral observations of the same surface region.

**Optical Assembly**

The EVNII telescope uses a compact reflective optical design optimized
for high-resolution imaging at visible and near-infrared wavelengths.

  ------------------------------
  **Parameter**   **Notional
                  Value**
  --------------- --------------
  Primary         150 mm
  aperture        

  Effective focal 1.8 m
  length          

  Optical         Three-mirror
  configuration   anastigmat

  F-number        f/12

  Telescope FOV   7.2° × 5.4°

  Optical         Silicon
  material        carbide

  Number of       3
  powered mirrors 

  Filter          7
  positions       

  Internal        Yes
  calibration     
  target          
  ------------------------------

At the nominal **250 km Europa orbit**, the instrument provides
approximately **25 m/pixel** resolution at nadir.

The instrument can operate in two primary modes:

**Regional Mapping Mode**

- Reduced spatial resolution

- Large-area surface coverage

- Multispectral imaging

- Used for geological and landing-site characterization

**Targeted Imaging Mode**

- Full detector resolution

- High-resolution observations of selected surface features

- Used for detailed examination of fractures, ridges, impact structures,
  and potential landing locations

**Mass Estimate**

The preliminary mass allocation for the complete VNIR instrument is:

  ------------------------------
  **Item**         **Estimated
                   Mass**
  ---------------- -------------
  CMOS detector    2.5 kg
  assembly         

  Detector         2.8 kg
  electronics      

  Telescope        7.0 kg
  mirrors and      
  optics           

  Filter wheel and 1.8 kg
  mechanism        

  Telescope        3.2 kg
  structure        

  Instrument       2.5 kg
  electronics      

  Calibration      1.0 kg
  assembly         

  Thermal hardware 1.4 kg

  Baffle and       1.2 kg
  stray-light      
  hardware         

  Harness and      0.8 kg
  connectors       

  **Instrument dry **24.2 kg**
  mass**           

  Design margin    20%

  **Allocated      **29.0 kg**
  instrument       
  mass**           
  ------------------------------

For preliminary spacecraft budgeting, **29 kg** is therefore allocated
to the EVNII instrument.

**Power Estimate**

  -----------------------------
  **Operating       **Power**
  Mode**            
  ----------------- -----------
  Standby           12 W

  Calibration       42 W

  Normal imaging    65 W

  High-resolution   78 W
  imaging           

  Peak              90 W
  -----------------------------

The instrument is expected to operate primarily during dedicated Europa
observation windows. During periods of high-rate imaging, the
instrument\'s data output is temporarily stored in the orbiter\'s
mass-memory system before being transmitted to Earth.

**Data Generation**

A single full-resolution monochromatic frame contains approximately
**12.6 million pixels**. Assuming 14-bit detector output, one
uncompressed frame produces approximately **22 MB of raw data** before
ancillary data and packet overhead.

At the maximum 20 Hz frame rate, the theoretical raw data generation
rate is approximately **440 MB/s**.

Continuous maximum-rate operation is not expected during normal mission
operations. Instead, the instrument will acquire short image sequences
and use onboard processing to reduce the volume of data requiring
transmission.

The onboard processing chain includes:

- Dark-current correction

- Bad-pixel correction

- Flat-field correction

- Radiometric calibration

- Image co-registration

- Spectral-band selection

- Lossless compression

- Controlled-loss compression when required

A typical **30-second multispectral observation** is expected to
generate approximately **300--500 MB of compressed science data**,
depending on the selected imaging mode.

The EVNII therefore represents a significant contributor to the EVE
orbiter\'s **science data volume and onboard storage requirements**,
while providing the high-resolution visible and near-infrared imagery
required for surface characterization and landing-site selection.

### Payload Electronics

The **Payload Electronics Unit (PEU)** provides the processing,
data-management, instrument-control, and communications interface for
the EVE scientific payload. The unit receives raw measurements from the
imaging and spectroscopic instruments, performs initial processing and
compression onboard, and transfers prioritized science products to the
spacecraft\'s central data-handling system.

The PEU is designed around a radiation-tolerant heterogeneous processing
architecture combining a multicore CPU with programmable logic. This
allows computationally intensive operations such as image correction,
spectral processing, compression, and instrument data fusion to be
performed before transmission.

The preliminary EVE PEU is a **notional, custom-developed flight
computer** rather than an existing commercial product.

  ------------------------------------------
  **Parameter**   **Notional Specification**
  --------------- --------------------------
  Product type    Radiation-tolerant payload
                  processing computer

  Primary         Quad-core 64-bit ARM
  processor       processor

  Real-time       Dual-core real-time
  processor       processor

  FPGA            Radiation-tolerant
                  programmable logic device

  CPU clock       Up to 1.5 GHz

  Programmable    \~350,000 logic cells
  logic           

  RAM             8 GB EDAC-protected memory

  Boot memory     2 × 256 MB
                  radiation-tolerant NOR
                  flash

  Local data      2 TB radiation-tolerant
  storage         solid-state memory

  Input voltage   24--32 VDC

  Nominal power   55 W

  Peak power      80 W

  Operating       −35°C to +55°C
  temperature     

  Radiation       ≥100 krad(Si) TID
  tolerance       

  Data interfaces SpaceWire, Ethernet, LVDS,
                  CAN-FD, GPIO

  Instrument      Up to 8 high-speed
  interfaces      instrument channels

  Mass            4.8 kg

  Dimensions      220 × 180 × 65 mm
  ------------------------------------------

**Onboard Processing**

A major function of the PEU is to reduce the amount of raw instrument
data that must be stored and transmitted by the orbiter.

The processing pipeline includes:

- Detector health monitoring

- Bad-pixel identification and correction

- Dark-current correction

- Flat-field correction

- Radiometric calibration

- Image filtering

- Image compression

- Spectral data processing

- Data prioritization

- Metadata generation

- Instrument health and performance monitoring

The PEU can operate different processing profiles depending on the
instrument and mission phase. High-priority observations can be retained
at full or near-full resolution, while routine survey observations can
undergo more aggressive compression.

A preliminary **4:1 average reduction in science data volume** is
assumed for imaging instruments, with higher reductions possible for
observations containing significant spatial redundancy.

**Data Storage**

The PEU includes approximately **2 TB of local solid-state storage**.
This provides temporary storage for high-rate instrument observations
during periods when the spacecraft is unable to immediately transfer
data to the central spacecraft computer.

The storage system uses redundant memory partitions and error-detection
and correction techniques. Science data are assigned priority levels so
that critical observations are retained if available storage approaches
capacity.

  --------------------------------------------------------
  **Data Type** **Priority**   **Example**
  ------------- -------------- ---------------------------
  Critical      1              Landing-site imagery and
  science                      unusual surface features

  Primary       2              Multispectral and infrared
  science                      observations

  Supporting    3              Calibration and contextual
  science                      imagery

  Engineering   4              Instrument temperatures and
                               health telemetry

  Diagnostic    5              Debug and maintenance
                               information
  --------------------------------------------------------

**Instrument Interfaces**

The PEU provides electrical and data interfaces between the scientific
instruments and the spacecraft Command and Data Handling subsystem.

The preliminary interface allocation is:

  ---------------------------------------------
  **Interface**   **Quantity**   **Nominal Data
                                 Rate**
  --------------- -------------- --------------
  High-speed      6              200
  SpaceWire                      Mbps/channel

  LVDS instrument 4              400
  interfaces                     Mbps/channel

  Gigabit         2              1 Gbps/channel
  Ethernet                       

  CAN-FD          4              5 Mbps/channel

  Discrete I/O    32             ---
  ---------------------------------------------

The PEU also distributes instrument timing signals to maintain
synchronization between observations from different payloads. This is
particularly important when combining visible, infrared, and
spectroscopic measurements of the same Europa surface feature.

**Fault Management**

The PEU incorporates hardware and software features intended to maintain
payload operations following individual component faults.

These include:

- EDAC-protected memory

- Watchdog timers

- Current monitoring

- Automatic processor reset

- FPGA configuration scrubbing

- Redundant power inputs

- Radiation-event detection

- Instrument isolation

- Safe-mode operation

- Dual boot images

If a payload instrument experiences a fault, the PEU can electrically
isolate the affected instrument while maintaining operation of the
remaining payload.

**Power Consumption**

  ---------------------------
  **Operating     **Power**
  Mode**          
  --------------- -----------
  Standby         12 W

  Instrument      28 W
  monitoring      

  Normal          55 W
  processing      

  High-rate       68 W
  processing      

  Peak            80 W
  computational   
  load            
  ---------------------------

The PEU is expected to operate whenever one or more primary science
instruments are active. During periods without science observations, the
unit enters a reduced-power monitoring state.

**Mass Allocation**

The preliminary mass allocation for the PEU is:

  ------------------------------
  **Item**         **Estimated
                   Mass**
  ---------------- -------------
  Processor and    1.1 kg
  FPGA board       

  Memory and       0.9 kg
  storage modules  

  Power            0.5 kg
  conditioning     

  Interface        0.6 kg
  electronics      

  Radiation        0.5 kg
  shielding        

  Structural       0.7 kg
  enclosure        

  Thermal hardware 0.3 kg

  Harness and      0.2 kg
  connectors       

  **Estimated dry  **4.8 kg**
  mass**           

  Design margin    20%

  **Allocated      **5.8 kg**
  mass**           
  ------------------------------

For the preliminary EVE mass budget, **5.8 kg** is allocated to the
Payload Electronics Unit.

The PEU therefore acts as the **primary processing hub for the EVE
scientific payload**, reducing raw science-data volume before downlink
while providing instrument control, synchronization, data storage, and
fault-management functions.

### Onboard blackbody calibration

Onboard The **Onboard Infrared Calibration System (OICS)** provides a
stable reference for maintaining the radiometric accuracy of the EVE
Europa Multispectral Infrared Imager (EMII) throughout the mission.

Infrared detectors can experience changes in sensitivity due to
radiation exposure, temperature variations, aging, and electronic drift.
The calibration system provides the instrument with a reference source
of known thermal emission, allowing the payload electronics to compare
the measured detector response against the expected response and apply
corrections to science observations.

The OICS consists of a small, high-emissivity calibration target
positioned within the EMII optical assembly. The target is maintained at
a monitored temperature using embedded heaters and temperature sensors.
During calibration activities, a motorized calibration shutter moves
into the optical path, allowing the detector to observe the calibration
target instead of Europa.

The calibration sequence is expected to be performed:

- Before the start of major science observation campaigns

- Following significant spacecraft thermal changes

- After extended periods of instrument inactivity

- At regular intervals during orbital operations

- Following detected changes in detector performance

The calibration target is observed by both the MWIR and LWIR detector
assemblies, allowing corrections to be applied independently to each
spectral channel.

A secondary **deep-space calibration view** is also incorporated into
the instrument. Observing the cold background of deep space provides an
additional reference point for detector offset and low-radiance
measurements.

The combination of the internal calibration target and deep-space
observations allows the EMII to compensate for long-term detector drift
and maintain consistent radiometric measurements over the planned
mission lifetime.

Launch Segment description

The 4 spacecraft will be launched into a 550km SSO using a single
dedicated Rocket Lab Electron launch.

Quoted price does not include launch insurance.

![Figure 7 - Launch
configuration](media/image3.png){width="4.770833333333333in"
height="4.492244094488189in"}

Alternate launch providers have been considered :

- Falcon 9 rideshare

- Starship

- Rocket Lab Neutron

- MaiaSpace

# Ground Segment and Mission Operations

The approach proposed for the baseline solution is for the Government of
Canada to provide the Mission Planning System and perform operations,
while EDA provided some ground segment elements.

+---------------+----------------------------------+
| Mission       | The Mission Planning System      |
| Planning      | (MPS) will be developed and      |
| System        | provided by the CSA.             |
|               |                                  |
|               | The MPS will incorporate         |
|               | spacecraft, lander, and rover    |
|               | functional requirements,         |
|               | operational constraints, command |
|               | and telemetry databases, and     |
|               | science objectives. The MPS will |
|               | generate mission timelines,      |
|               | activity schedules, and command  |
|               | sequences for uplink to the      |
|               | spacecraft.                      |
+===============+==================================+
| Spacecraft    | The Spacecraft Control System    |
| Control       | (SCS) will be provided by the    |
| System        | CSA and will provide the primary |
|               | interface for spacecraft         |
|               | operations.                      |
|               |                                  |
|               | The SCS will support command     |
|               | uplink, telemetry reception,     |
|               | spacecraft health monitoring,    |
|               | alarm management, data           |
|               | processing, and communications   |
|               | with the international orbiter   |
|               | and lander.                      |
+---------------+----------------------------------+
| Receiving     | Government of Canada ground      |
| Stations      | stations will be used in         |
|               | combination with commercial and  |
|               | international deep-space ground  |
|               | stations.                        |
|               |                                  |
|               | The ground-station network will  |
|               | support X-band command and       |
|               | telemetry, Ka-band science data  |
|               | reception, and spacecraft        |
|               | tracking. The CSA will           |
|               | coordinate ground-station        |
|               | scheduling and will be the       |
|               | primary operational interface.   |
+---------------+----------------------------------+
| Spacecraft    | Spacecraft operations will be    |
| Operations    | performed by the CSA in          |
|               | coordination with the            |
|               | international spacecraft         |
|               | providers.                       |
|               |                                  |
|               | The CSA will be responsible for  |
|               | mission planning, spacecraft and |
|               | rover commanding, health         |
|               | monitoring, anomaly response,    |
|               | communications scheduling, and   |
|               | coordination of orbital,         |
|               | landing, and surface operations. |
+---------------+----------------------------------+
| Science       | Science operations will be       |
| Operations    | performed by the CSA in          |
|               | coordination with Canadian and   |
|               | international science teams.     |
|               |                                  |
|               | The Science Operations Centre    |
|               | will support observation         |
|               | planning, rover investigation    |
|               | planning, instrument operations, |
|               | scientific data processing, and  |
|               | selection of surface             |
|               | investigation sites.             |
|               |                                  |
|               |   --                             |
|               |                                  |
|               |   --                             |
+---------------+----------------------------------+
| Data Archival | Mission and science data will be |
| and           | archived and disseminated        |
| Dissemination | through CSA-managed data         |
|               | systems.                         |
|               |                                  |
|               | Processed scientific data,       |
|               | including orbital imagery, rover |
|               | observations, drilling results,  |
|               | and sample-analysis data, will   |
|               | be made available to the EVE     |
|               | science team and, following      |
|               | validation and applicable        |
|               | release requirements, to the     |
|               | broader scientific community.    |
+---------------+----------------------------------+

# Systems Engineering and Project Management Approach

## TRL Levels and Heritage

SFL bus has high heritage (TRL-9)

## Phasing Logic and Naming conventions

The following are the phases in terms of costing:

+----------------+--------------------------+-----------------+
| **Costing      | **Phase Description      | **Corresponding |
| Nomenclature** | according to Costing     | Name for        |
|                | Standards**              | Project team**  |
+================+==========================+=================+
| PREP 1         | Prototyping Activities   | N/A             |
|                | (before Gate 1)          |                 |
+----------------+--------------------------+-----------------+
| PREP 2         | Prototyping Activities   | N/A             |
|                | (during Phase 0/A)       |                 |
+----------------+--------------------------+-----------------+
| Phase 0        | Concept & Feasibility    | Phase 0         |
|                | Studies                  |                 |
+----------------+--------------------------+-----------------+
| Phase A        | System Definition        | Phase A         |
+----------------+--------------------------+-----------------+
| Phase B        | Preliminary Design       | Phase B         |
+----------------+--------------------------+-----------------+
| Phase C        | Detailed Design          | Phase C         |
+----------------+--------------------------+-----------------+
| MAIT           | Manufacturing, Assembly, | Phase D         |
|                | Integration and Test (of |                 |
|                | Canadian Systems,        |                 |
|                | Subsystems and           |                 |
|                | Components)              |                 |
+----------------+--------------------------+                 |
| ATLO           | Mission Level Assembly,  |                 |
|                | Test, and Launch         |                 |
|                | Operations (ATLO)        |                 |
+----------------+--------------------------+                 |
| Cruise         | Outbound Cruise is the   |                 |
|                | interplanetary journey   |                 |
|                | ending with approach and |                 |
|                | orbit insertion at the   |                 |
|                | destination              |                 |
+----------------+--------------------------+                 |
| LEOP           | Launch and Early         |                 |
|                | Operations (incl.        |                 |
|                | commissioning)           |                 |
+----------------+--------------------------+-----------------+
| EDL            | Entry Descent and        |                 |
|                | Landing                  |                 |
+----------------+--------------------------+-----------------+
| Early Ops      | For surface operations,  |                 |
|                | early operations might   |                 |
|                | include commissioning    |                 |
+----------------+--------------------------+-----------------+
| Phase E        | Nominal Operations (per  | Phase E         |
|                | design life)             |                 |
+----------------+--------------------------+-----------------+
| Phase X        | Extended operations      | Extended ops    |
|                | (mission extension)      |                 |
+----------------+--------------------------+-----------------+
| Return and     | Inbound cruise is the    |                 |
| Re-Entry       | return to Earth and      |                 |
|                | re-entry                 |                 |
+----------------+--------------------------+-----------------+
| Phase F        | Disposal (audit)         | Phase F         |
+----------------+--------------------------+-----------------+
| Phase G        | Post-Mortem data         | N/A             |
|                | utilization              |                 |
+----------------+--------------------------+-----------------+

## CSA PRoject Milestones

The project has not created a schedule baseline yet. Assuming instrument
level milestones will drive the CSA need dates.

+--------------+-----+----------------------+----------------+
| **Instrument |     | **Major Milestone**  | **Milestone    |
| Phases**     |     |                      | Date**         |
+==============+=====+======================+================+
| Phase 0      | MCR | Mission Concept      |                |
|              |     | Review               |                |
+--------------+-----+----------------------+----------------+
| Phase A      | SRR | System Requirements  |                |
|              |     | Review               |                |
+--------------+-----+----------------------+----------------+
|              |     | Mission Rebaseline   | Spring 2026    |
+--------------+-----+----------------------+----------------+
| Phase B      | PDR | Preliminary Design   |                |
|              |     | Review               |                |
+--------------+-----+----------------------+----------------+
| Phase C      | CDR | Critical Design      |                |
|              |     | Review               |                |
+--------------+-----+----------------------+----------------+
| MAIT         | MRR | Manufacturing        |                |
|              |     | readiness Review     |                |
|              +-----+----------------------+----------------+
|              | PSR | Pre-Ship Review of   |                |
|              |     | systems to Prime     |                |
+--------------+-----+----------------------+----------------+
| SAIT         | SIR | System Integration   |                |
|              |     | Review               |                |
|              +-----+----------------------+----------------+
|              | AR  | Acceptance Review    |                |
|              +-----+----------------------+----------------+
|              | PSR | Pre-Ship Review of   |                |
|              |     | S/C to Launch site   |                |
+--------------+-----+----------------------+----------------+
| ATLO         | AR  | Acceptance Review or |                |
|              |     | you could use the    |                |
|              |     | PSR to the launch    |                |
|              |     | site                 |                |
+--------------+-----+----------------------+----------------+
| LEOP         | L   | Launch               |                |
|              +-----+----------------------+----------------+
|              | CR  | Commissioning Review |                |
+--------------+-----+----------------------+----------------+
| Cruise and   |     | Entry descent        |                |
| EDL          |     | landing              |                |
+--------------+-----+----------------------+----------------+
| Phase E      |     | Start of Nominal Ops |                |
|              +-----+----------------------+----------------+
|              |     | End of Nominal Ops   |                |
+--------------+-----+----------------------+----------------+
| Phase X      |     | End of Life          |                |
+--------------+-----+----------------------+----------------+
| Sample       |     | When the sample      |                |
| Return phase |     | arrived on Earth     |                |
+--------------+-----+----------------------+----------------+

## Safety and Mission Assurance

Initial assessments is assumed to be Mission Class: D

## Qualification and Acceptance Strategy, MODEL Philosophy

**Project Specific Quality Assurance Approach and Model Philosophy**

For EVE, the qualification and acceptance approach will be tailored
according to the maturity, heritage, and risk of each subsystem.
Existing and previously qualified technologies will primarily follow an
acceptance-testing approach, while new or mission-critical technologies
will undergo qualification or protoflight testing.

Engineering models will be developed for selected high-risk elements,
including the **Canadian Europa Rover mobility system, drilling and
sample-acquisition system, and selected payload instruments**. These
models will be used for functional testing, software development,
operational validation, and environmental testing prior to flight
hardware delivery.

The **Europa Orbiter and Lander** will use a combination of
qualification and acceptance testing based on the international
partners' existing hardware heritage. Previously qualified units will
generally undergo acceptance testing at the unit level, while new or
significantly modified units will follow a qualification approach.

The Canadian rover will use a **protoflight approach** for the flight
unit, supported by engineering models for high-risk mechanical and
scientific functions. The rover drill and sample-handling system will
undergo additional qualification testing using representative Europa ice
simulants.

At the spacecraft level, the baseline approach will be **protoflight
testing** for the orbiter, lander, and rover. Environmental testing will
include vibration, shock, thermal-vacuum, electromagnetic compatibility,
and functional testing. Where practical, testing will be performed at
the integrated spacecraft level to verify interfaces between the mission
elements.

The qualification and acceptance program will focus on identifying
design and interface issues as early as possible while avoiding
unnecessary duplication of testing on flight hardware. Particular
emphasis will be placed on the rover drilling system, communications
interfaces, thermal performance, planetary protection requirements, and
long-duration autonomous operations.

The project will prioritize early development and testing of high-risk
systems so that sufficient time remains for corrective actions before
system-level integration. All qualification and acceptance activities
will be documented through configuration-controlled test plans,
procedures, results, and verification reports.

The baseline model philosophy is therefore:

  -------------------------------------------
  **Hardware**   **Model Philosophy**
  -------------- ----------------------------
  Europa Orbiter Protoflight

  Europa Lander  Qualification / Protoflight

  Canadian       Protoflight with Engineering
  Europa Rover   Models

  Rover Drill    Qualification

  Scientific     Qualification / Acceptance
  Payloads       

  Payload        Acceptance with
  Electronics    qualification testing of new
                 designs

  Ground Systems Engineering Models and
                 Acceptance Testing

  Mission        Engineering/Operational
  Software       Validation Models
  -------------------------------------------

## Risk Assessment

The project team shall produce a risk register (ref CADRe part C)

## Organizational Breakdown Structure

Earth Daily Analytics' supply chain

**Science Instruments:**\
Northern Optics Research (Ottawa, Canada) -- VNIR and infrared imaging
instruments

**Payload:**\
Laurentian Space Systems (Montreal, Canada) -- integrated scientific
payload and sample-analysis equipment

**Payload Electronics:**\
Orbital Electronics Canada (Toronto, Canada) -- payload electronics unit
and instrument interfaces

**Rover:**\
Canadian Planetary Robotics (Calgary, Canada) -- Europa surface rover,
mobility system, drilling and sample acquisition

**Lander:**\
European Planetary Systems Agency (Darmstadt, Germany) -- Europa lander
and descent system

**Orbiter:**\
Nordic Deep Space Systems (Kiruna, Sweden) -- Europa orbiter and
communications relay

**Launch:**\
International Launch Services (Florida, USA) -- heavy-lift launch
vehicle and launch services

**Ground Segment:**\
Canadian Space Operations Centre (Longueuil, Canada) -- mission
planning, spacecraft operations and data processing

**Prime:**\
Canadian Space Agency (Longueuil, Canada)

####### 
