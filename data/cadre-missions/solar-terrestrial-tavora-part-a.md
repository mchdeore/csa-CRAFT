CADRe Part A • TME

Mission Cost Analysis Directorate

Cost Analysis Data Requirements

PART A

Tavora Mesosphere Explorer

Planning baseline • Revision 1.0 • 23 September 2026

This mission and all named organizations and individuals are fictional.

Revision History

  --------------------------------------------------------------------------
  **Rev.**   **Description**                    **Prepared by**  **Date**
  ---------- ---------------------------------- ---------------- -----------
  1.0        Template aligned mission concept   Mission Cost     23 Sep 2026
                                                Analysis         
                                                Directorate      

  --------------------------------------------------------------------------

Table of Contents

1 Introduction

1.1 Purpose of this document

2 General Descriptive Information

2.1 Mission Overview

2.2 Strategic Objectives

2.3 Selected Mission Requirements

2.4 High-Level Mission Architecture

3 Space Segment Description

3.1 Spacecraft Bus

3.2 Payload

4 Launch Segment Description

5 Ground Segment and Mission Operations

6 Systems Engineering and Project Management Approach

6.1 TRL Levels and Heritage

6.2 Phasing Logic and Naming Conventions

6.3 Project Milestones

6.4 Safety and Mission Assurance

6.5 Prototyping Model Philosophy Qualification and Verification Strategy

6.6 Sparing Strategy

6.7 Risk Assessment

6.8 Organizational Breakdown Structure

List of Figures

Figure 1 -- Tavora Mesosphere Explorer mission architecture

Figure 2 -- Payload measurement and data path

List of Tables

Table 1 -- Strategic Alignment

Table 2 -- Selected System Requirements

Table 3 -- Costing Phase Crosswalk

Table 4 -- Planning Phase Dates

Table 5 -- Major Milestones

Table 6 -- Mission Organizations

Table 7 -- Industrial Partners

Table 8 -- Research Institutions

Table 9 -- Scientific Leadership

# Introduction

## Purpose of this document

CADRe Part A provides a concise, standardized synopsis of the mission to
support cost analysis. It consolidates the mission objectives, system
requirements, architecture, delivery boundaries, operations,
verification strategy, schedule and participating organizations.

The quantitative values are planning requirements or preliminary
allocations. CADRe Part B records cost element parameters, Part C
controls the phase schedule and risk register, and Part D records
programmatic evidence.

# General Descriptive Information

## Mission Overview

The reference configuration is two imaging spacecraft. Its operational
environment is 520 ±15 km near-circular altitude; two orbital planes
with target 45-minute local-time separation. The nominal duration is
Three-year nominal operations; six-month commissioning; four-year
spacecraft design life. The flight or installed unit is sized at 180 kg
and uses 520 W power generation or host allocation as stated in the
subsystem budget.

The design carries ultraviolet limb spectrometer, thermal infrared limb
radiometer and occultation timing receiver. Each produces a separately
calibrated record with common time, configuration and quality metadata.
The science objectives are quantified in the requirement matrix below.

![Figure 1 -- Tavora Mesosphere Explorer mission architecture. Labeled
boxes identify responsibility boundaries; dimensions are
schematic.](media/image5.png){width="6.4in"
height="1.8529407261592301in"}

## Strategic Objectives

The mission aligns the measurement or service objectives with the
sponsoring authority's stated science, capability and operations
priorities.

  -------------------------------------------------------------------------
  **Priority**   **Strategic goal**    **Mission contribution**
  -------------- --------------------- ------------------------------------
  1              Primary mission       Retrieve daily ozone and
                 outcome               water-vapour profiles at 2 km
                                       vertical sampling from 45--95 km
                                       altitude, with ≤10% relative
                                       precision where radiance exceeds
                                       sensitivity threshold.

  2              Operational           Deliver Three-year nominal
                 sustainability        operations; six-month commissioning;
                                       four-year spacecraft design life.
                                       with independently accepted baseline
                                       products and contingency procedures.
  -------------------------------------------------------------------------

  : Table 1 -- Strategic Alignment

## Selected Mission Requirements

The following selected requirements control the major cost and
complexity drivers. Their verification methods and approved values
belong in the controlled requirements baseline.

  ----------------------------------------------------------------------
  **Cost and      **Preliminary requirement**        **Principal cost or
  complexity                                         complexity effect**
  driver**                                           
  --------------- ---------------------------------- -------------------
  Mission         Two imaging spacecraft; 2 unit(s). Flight hardware
  architecture                                       allocation,
                                                     interface control
                                                     and acceptance
                                                     testing.

  Operating       520 ±15 km near-circular altitude; Propellant,
  environment     two orbital planes with target     navigation, flight
                  45-minute local-time separation.   dynamics and
                                                     delivery accuracy.

  Mission         Three-year nominal operations;     Parts screening,
  duration        six-month commissioning; four-year redundancy, spares
                  spacecraft design life.            and operations
                                                     staffing.

  Unit mass       ≤180 kg as delivered or at launch, Launch capacity,
                  including the budgeted contents.   structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.

  Payload         ≤43 kg, with definitions           Launch capacity,
  allocation      controlled by the mass table.      structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.

  Power           520 W at specified reference;      Generation,
  generation /    nominal 310 W and peak 445 W.      storage, power
  provision                                          distribution,
                                                     thermal rejection
                                                     and eclipse margin.

  Primary         Retrieve daily ozone and           Detector
  measurement     water-vapour profiles at 2 km      performance,
                  vertical sampling from 45--95 km   calibration,
                  altitude, with ≤10% relative       metrology and
                  precision where radiance exceeds   end-to-end
                  sensitivity threshold.             verification.

  Instrument 1    25 kg / 105 W; 250--340 nm; 0.5 nm Flight hardware
                  spectral sampling; 2 km vertical   allocation,
                  bins over 45--95 km.               interface control
                                                     and acceptance
                                                     testing.

  Instrument 2    12 kg / 85 W; 6.3--12 µm in 4      Flight hardware
                  bands; 0.15 K noise-equivalent     allocation,
                  delta-T at 250 K reference scene.  interface control
                                                     and acceptance
                                                     testing.

  Instrument 3    6 kg / 22 W; dual-frequency        Flight hardware
                  occultation signal tracking at 1   allocation,
                  Hz for profile registration and    interface control
                  retrieval screening.               and acceptance
                                                     testing.

  Pointing or     Dual star trackers, four wheels,   Flight hardware
  positioning     magnetic torquers and GNSS         allocation,
                  receiver; limb pointing error      interface control
                  ≤0.05° and knowledge ≤0.01° at 95% and acceptance
                  confidence.                        testing.

  Mission-data    20 GB/day per spacecraft           Launch capacity,
  volume                                             structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.
  ----------------------------------------------------------------------

  : Table 2 -- Selected System Requirements

## High-Level Mission Architecture

The architecture separates oversight, space or deployed hardware, launch
or delivery, ground services, operations and science or user
exploitation.

Neraval Atmospheric Directorate owns system requirements, procurement,
risk and mission acceptance.

Oryvex Orbital Manufacturing owns the integrated unit, interfaces and
system-level verification.

Selrith Optical Works delivers the measurement equipment and calibration
evidence.

Daverin Launch Collective delivers the unit to its destination and
verifies interface conditions.

Mirevan Receiving Services supplies receiving, networking and
ground-service capacity.

Istralen Atmospheric Institute produces, validates and archives the
calibrated mission products.

# Space Segment Description

The reference configuration is two imaging spacecraft. Its operational
environment is 520 ±15 km near-circular altitude; two orbital planes
with target 45-minute local-time separation. The nominal duration is
Three-year nominal operations; six-month commissioning; four-year
spacecraft design life. The flight or installed unit is sized at 180 kg
and uses 520 W power generation or host allocation as stated in the
subsystem budget. The segment boundary includes the integrated unit and
its mission-specific payload, interfaces, spares and verification
articles.

## Spacecraft Bus

The integrated unit provides structural restraint, power, command and
data handling, thermal protection, equipment control and the
communication interface appropriate to 520 ±15 km near-circular
altitude; two orbital planes with target 45-minute local-time
separation. The design shall carry configuration identifiers and
independent acceptance records for every delivered unit.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary allocation / target**
  ------------------------ -------------------------------------------
  Unit mass                180 kg

  Mass composition         125 kg dry bus + 43 kg payload + 12 kg
                           propellant = 180 kg

  Payload / experiment     43 kg
  allocation               

  Generation / provision   520 W reference

  Nominal / peak demand    310 W / 445 W

  Storage                  512 GB usable

  Autonomy                 ≥72 h safe configuration with applicable
                           external power

  Maneuver / mobility      ≥95 m/s per spacecraft; 12 kg
                           monopropellant at 220 s yields \~149 m/s
                           ideal at 180 kg initial mass

  Delivery                 Two contracted launches into separate
                           planes; each carries one 180 kg
                           spacecraft + 50 kg adaptor = 230 kg, with
                           ≥275 kg capacity to the reference orbit

  Design life              Three-year nominal operations; six-month
                           commissioning; four-year spacecraft design
                           life.
  --------------------------------------------------------------------

### Structural Subsystem

The structural design is sized for 180 kg delivery mass and the
qualified interface loads. The launch or cargo provider controls final
vibration, shock and handling cases; a 6 g axial and 2 g lateral
quasi-static concept check is retained until that interface is defined.
Enclosures, hinges, restraints and contained fluids receive separate
local load paths.

The configuration model records mass properties, lifting points,
contamination boundaries, access envelopes and center of gravity before
acceptance. Instrument alignment and enclosure sealing are measured
before and after environmental testing. The project shall document
whether the delivery carrier, lander or host provides final restraint
hardware.

### Electrical Power Subsystem

Nominal allocation: 520 W generation or host provision, 310 W operating
demand, 445 W short-duration peak. These values describe distinct
operating cases. The system power margin is assessed at the worst
insolation, eclipse or host-service case, not by comparing only
nameplate generation and nominal demand.

Power distribution uses protected 28 V or the host-qualified equivalent.
Independent current telemetry and latching protection isolate a failed
load. Battery or host reserve is sized from the longest commanded
safe-mode, transfer, eclipse or night interval rather than from an
arbitrary percentage of nominal energy.

  -----------------------------------------------------------------------
  **Reference             **Distribution and      **Protected loads**
  generation**            storage**               
  ----------------------- ----------------------- -----------------------
  520 W baseline          Regulated bus,          310 W nominal / 445 W
                          protected battery/host  peak
                          service                 

  -----------------------------------------------------------------------

### Command and Data Handling

A redundant or monitored controller executes time-tagged operations,
instrument interlocks, fault detection and protected storage. The local
allocation is 512 GB usable. A storage analysis includes the worst
observation burst, delayed contact, software overhead, file-system
reserve and corrected-memory events.

Every science record carries absolute time, equipment serial number,
calibration-set ID, operating mode and validity flags. Loss of link
initiates a controlled safe state that preserves source data and
performs scheduled reacquisition. A corrupted parameter upload must not
silently change instrument calibration or safety limits.

Flight and process software controls the following functions:

receive and execute authorized commands;

collect health telemetry and time-correlated payload packets;

manage 512 GB usable storage and priority records;

switch to a safe mode after undervoltage, overtemperature or watchdog
failure;

retain the last accepted software and configuration baseline;

reacquire the ground or host link after a missed contact; and

report data quality and calibration status with each product.

A mission-data model checks the 20 GB/day per spacecraft planning case
against memory capacity, contact availability and the required
processing latency. Raw records are retained until integrity checks and
ingest acknowledgement complete.

### Thermal Subsystem

520 km eclipse and albedo hot/cold cases; payload bench 15--25 °C ±1
°C/orbit; radiator planning area 0.55 m².

The thermal design shall close with numerical hot and cold cases and
shall separately report radiator, insulation, heater and sensor
allocations. Instrument calibration is repeated across the qualified
operating temperature range. Safe-mode heating and peak-mode waste heat
are independently assessed.

Thermal verification considers heat from 445 W peak electrical input,
the nominal 310 W mode, external heat flux, enclosure conduction and the
passive or active rejection path. The final instrument uncertainty
budget includes temperature-driven bias and gradients.

The thermal test programme shall establish:

steady and transient operating limits of each component;

heater and cooler demand in cold and hot cases;

radiator or host heat-rejection sizing;

calibration stability across the qualified temperature range; and

safe survival during a commanded outage.

### Attitude Determination and Control Subsystem

Dual star trackers, four wheels, magnetic torquers and GNSS receiver;
limb pointing error ≤0.05° and knowledge ≤0.01° at 95% confidence.

The reference control architecture separates safe/recovery, measurement,
communications and maneuver or servicing modes. A commanded transition
requires validated sensor state and resource availability. For hosted
equipment, mechanical positioning takes the place of free-flight
attitude determination, while retaining an equivalent repeatability
verification requirement.

The control design maintains a mode and pointing error budget. It
distinguishes knowledge of where the instrument looked from closed-loop
control accuracy, including disturbance rejection and post-facto
reconstruction. Engineering tests separately verify sensor alignment,
actuator range and degraded operations after a failed sensor or wheel.

  --------------------------------------------------------------------
  **Control element A**    **Control element B**
  ------------------------ -------------------------------------------
  Primary                  Independent cross-check and health monitor
  position/attitude        
  reference                

  Science or process       Safe-mode or host restraint
  pointing                 

  Actuator / positioning   Feedback telemetry
  hardware                 

  Alignment calibration    Post-test acceptance evidence
  --------------------------------------------------------------------

### Propulsion Subsystem

12 kg monopropellant, 220 s Isp; ideal Δv \~149 m/s, leaving 54 m/s
before unusable propellant and performance allowances.

Any maneuver, descent or mobility not carried by the delivered unit is
assigned explicitly to the launch or cargo provider. If propulsion is
installed, the flight reserve includes residuals, thrust and
specific-impulse dispersion, navigation error and unusable propellant.
No requirement is treated as closed by nominal rocket-equation
capability alone.

  -----------------------------------------------------------------------
  **Parameter**           **Reference value**     **Units**
  ----------------------- ----------------------- -----------------------
  Propulsion type         Installed or external;  ---
                          see baseline            

  Initial unit mass       180                     kg

  Reference performance   ≥95 m/s per spacecraft; m/s or N/A
                          12 kg monopropellant at 
                          220 s yields \~149 m/s  
                          ideal at 180 kg initial 
                          mass                    

  Fuel / propellant       12 kg monopropellant,   kg / description
  allocation              220 s Isp               

  Performance reserve     Verify at PDR           m/s

  Residual accounting     Required in final mass  kg
                          budget                  
  -----------------------------------------------------------------------

  --------------------------------------------------------------------
  **Maneuver / mobility    **Allocation / assumption**
  element**                
  ------------------------ -------------------------------------------
  Initial injection or     Included in contracted service unless
  landing                  stated otherwise

  Operational maintenance  Two Sun-synchronous orbit planes; 45-minute
                           local-time spacing verified by trajectory
                           and launch analysis.

  Navigation and           ≥95 m/s per spacecraft; 12 kg
  correction               monopropellant at 220 s yields \~149 m/s
                           ideal at 180 kg initial mass

  Contingency and          Explicit reserve controlled in Part B /
  residuals                Part C

  Total capability         Reconcile with 12 kg monopropellant, 220 s
                           Isp; ideal Δv \~149 m/s, leaving 54 m/s
                           before unusable propellant a
  --------------------------------------------------------------------

### Telemetry, Tracking and Command

Two 12-minute contacts/day at 150 Mb/s yield 27 GB gross; 20 GB/day
requires 74% effective payload throughput.

The final link assessment shall include transmitter power, antenna gain
or host data-service rate, geometry, coding, weather where relevant and
a minimum allocated margin. Distinguish command/control packets, health
telemetry, raw measurements and user or science products. A link outage
analysis is required before ground-service capacity is baselined.

The communications baseline includes 150 Mb/s X-band to ≥7 m ground
antenna. The contact budget carries acquisition, engineering telemetry,
protocol framing, retransmission and unavailable weather or host
periods. The sizing check compares usable transferred bytes per contact
with 20 GB/day per spacecraft and any higher burst case.

A separate low-rate command path or host maintenance interface shall
support diagnosis after the prime mission-data path becomes unavailable.
No unauthenticated measurement data can alter safety-critical command
parameters.

## Payload

The payload or process equipment is divided into ultraviolet limb
spectrometer, thermal infrared limb radiometer and occultation timing
receiver. Each element has a separate delivered mass, operating load,
mode list, failure assessment and calibration requirement.

### Ultraviolet limb spectrometer

25 kg / 105 W; 250--340 nm; 0.5 nm spectral sampling; 2 km vertical bins
over 45--95 km.

The element is accepted by a traced performance test across the
specified environment. Detector or process response, temporal stability,
alignment and throughput are measured, not inferred from component
labels. Operational anomalies are flagged in the Level 1 record.

The technical budget traces the stated measurement scale to a physical
sampling process and detector or process limits. The performance model
shall state coverage, dynamic range, timing, throughput, noise,
calibration interval and data-rejection logic. Acceptance reports both
the verified central value and its uncertainty.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary requirement / target**
  ------------------------ -------------------------------------------
  Primary function         Ultraviolet limb spectrometer

  Measured performance     25 kg / 105 W; 250--340 nm; 0.5 nm spectral
                           sampling; 2 km vertical bins over 45--95
                           km.

  Unit-level calibration   Before integration and after environmental
                           qualification

  Electrical interface     Protected distribution and commanded safe
                           state

  Data interface           Time-tagged raw records plus status and
                           quality flags

  Environmental tolerance  520 km eclipse and albedo hot/cold cases;
                           payload bench 15--25 °C ±1 °C/orbit;
                           radiator planning area 0.55 m².

  Mass accounting          Within 43 kg payload or experiment
                           allocation

  Verification             Test against mission-level success
                           criterion

  Operations mode          Only when power, thermal and link margins
                           permit

  Fault response           Isolate and report without affecting
                           safe-mode command
  --------------------------------------------------------------------

### Thermal infrared limb radiometer

12 kg / 85 W; 6.3--12 µm in 4 bands; 0.15 K noise-equivalent delta-T at
250 K reference scene.

This measurement or process provides an independent check on the primary
result. The ground model shall retain geometric, thermal and
instrumental uncertainty, including changes caused by the spacecraft or
host.

For Tavora Mesosphere Explorer, complementarity is intentional: one
channel measures a different physical quantity or provides a contextual
state. Processing shall preserve the raw evidence, identify retrieval
assumptions and reject inconsistent cross-calibration before product
release.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary requirement / target**
  ------------------------ -------------------------------------------
  Function                 Thermal infrared limb radiometer

  Performance              12 kg / 85 W; 6.3--12 µm in 4 bands; 0.15 K
                           noise-equivalent delta-T at 250 K reference
                           scene.

  Mass                     Included in payload/experiment allocation

  Power                    Mode specific; close against peak load

  Field / process geometry 520 ±15 km near-circular altitude; two
                           orbital planes with target 45-minute
                           local-time separation.

  Timing                   Synchronized to system command clock

  Calibration              At acceptance and by scheduled in-operation
                           reference

  Data volume              20 GB/day per spacecraft

  Quality masks            Record saturation, missing packets and
                           calibration excursions

  Qualification            Relevant launch, host and operational
                           environment
  --------------------------------------------------------------------

### Payload Electronics

The payload electronics supervise instrument power, timing, detector
readout, process controls, data formatting and safe-mode interlocks.
Interfaces are controlled by released drawings and telemetry
dictionaries. Each unit supports configuration rollback after a failed
upload.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary requirement / target**
  ------------------------ -------------------------------------------
  Primary function         Instrument / process control and
                           time-tagging

  Sensor interfaces        Ultraviolet limb spectrometer; Thermal
                           infrared limb radiometer; Occultation
                           timing receiver

  System interface         Protected command and local data bus

  Buffering                512 GB usable system allocation

  Processing               Lossless event flags and reversible
                           screening where practical

  Timing                   Absolute reference and monotonically
                           numbered records

  Health monitoring        Voltage, temperature, current, reset count
                           and status

  Mass                     Within 43 kg allocation

  Peak electrical power    Included in 445 W integrated peak

  Radiation / environment  Qualified for 520 ±15 km near-circular
                           altitude; two orbital planes with target
                           45-minute
  --------------------------------------------------------------------

### Onboard Calibration

Calibration is designed around traceable reference states rather than a
generic check flag. A pre-deployment baseline, scheduled in-operation
reference and post-anomaly verification distinguish genuine environment
or biological changes from instrument drift.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary requirement / target**
  ------------------------ -------------------------------------------
  Calibration type         Radiometric, geometric, biological,
                           material or electrical as applicable

  Primary reference        Occultation timing receiver

  Frequency                At commissioning, after anomaly and on a
                           scheduled monthly cadence

  Environmental dependency 520 km eclipse and albedo hot/cold cases;
                           payload bench 15--25 °C ±1 °C/orbit;
                           radiator planning area 0.55 m².

  Long-term drift          Trend against accepted reference and flag
                           \>2% unexplained change

  Data linkage             100% released products identify applicable
                           calibration version

  Independent verification Recheck with Thermal infrared limb
                           radiometer

  Instrument monitoring    On each operating cycle

  Mass / power             Within payload and system allocations
  --------------------------------------------------------------------

![Figure 2 -- Payload measurement and data path. Components and output
interfaces are explicitly labeled.](media/image6.png){width="6.4in"
height="1.8529407261592301in"}

# Launch Segment Description

Two contracted launches into separate planes; each carries one 180 kg
spacecraft + 50 kg adaptor = 230 kg, with ≥275 kg capacity to the
reference orbit

Delivery pricing shall separately identify vehicle or carrier service,
packaging and adaptor, loading and contamination controls, integration
testing, range or landing support, insurance if applicable and
post-delivery transition. Any mass carried by a host rather than the
flight unit is shown as a separate line and is not double counted.

The final delivery contractor verifies mechanical fit, safety,
compatibility, deployment, insertion or landing dispersions and
acceptance criteria. The mission team performs final health checks
before the affected unit is declared operational.

Delivery preparation includes controlled packing, shipment and receiving
inspection, integrated electrical checkout, safety review, interface
sign-off and a final readiness decision. The handover record separates
damage observed before launch or cargo installation from anomalies in
early operation.

Any alternate provider must meet the same delivered mass, envelope,
power-on sequence, schedule and injection or landing accuracy. A
provider change triggers re-verification of coupled loads and
mission-specific interfaces.

# Ground Segment and Mission Operations

Four 7 m-class receive sites; ≥100 GB/day ingest; 180 TB multi-version
archive and processing.

Two 12-minute contacts/day at 150 Mb/s yield 27 GB gross; 20 GB/day
requires 74% effective payload throughput.

  --------------------------------------------------------------------
  **Ground Segment         **Description**
  Element**                
  ------------------------ -------------------------------------------
  Mission Planning System  Schedules commanded measurement, service or
                           observation periods and checks resource
                           constraints.

  Control System           Monitors status, authorizes command,
                           handles anomaly response and keeps
                           configuration history.

  Receiving Stations /     Four 7 m-class receive sites; ≥100 GB/day
  Host Link                ingest; 180 TB multi-version archive and
                           processing.

  Operations Team          Staffed planned operations with automated
                           alarm and on-call response.

  Processing and Archive   Level 0 packet retention; Level 1
                           calibration; Level 2 products with
                           preserved lineage.

  Data Volume /            20 GB/day per spacecraft; scheduled ground
  Availability             service availability ≥99%.
  --------------------------------------------------------------------

The daily return is 20 GB/day per spacecraft. Downlink capacity and
stored-data volume shall close under a minimum 48-hour missed-contact
case, except where host operations impose a different approved case.
Science release depends on validation, access permissions and a
documented reprocessing path.

Mission operations include daily planning, health trending, commands,
flight dynamics or host status, calibrated processing, anomaly
resolution and archive integrity. Nominal staffing is a planned shift
with continuous alarm routing; time-critical encounters or crew
procedures require separate surge coverage.

The data archive retains source packets, released products, calibration
files, algorithm version and exceptions. Capacity in Four 7 m-class
receive sites; ≥100 GB/day ingest; 180 TB multi-version archive and
processing. is a planning provision that shall be verified against years
of operation, replication and reprocessing.

# Systems Engineering and Project Management Approach

## TRL Levels and Heritage

A similar component class does not establish mission-specific
qualification. Critical payload, software, biological, medical or
manufacturing elements target TRL 6 at PDR and TRL 8 before acceptance.
The evidence register identifies the exact hardware/software
configuration, environment and remaining work for each claim.

## Phasing Logic and Naming Conventions

The costing convention separates early concept work, definition, design,
subsystem manufacture and test, system integration, delivery,
commissioning, nominal operations and closeout. Phase labels are mapped
to the project schedule in Part C.

  ------------------------------------------------------------------------
  **Costing        **Phase description**          **Project name**
  nomenclature**                                  
  ---------------- ------------------------------ ------------------------
  PREP 1           Pre-gate prototyping           Technology maturation

  PREP 2           Phase 0/A prototyping          Concept demonstrations

  Phase 0          Concept and feasibility        Concept

  Phase A          System definition              Definition

  Phase B          Preliminary design             Preliminary design

  Phase C          Detailed design                Detailed design

  Phase D1         Subsystem manufacture and test Unit AIT

  Phase D2         System assembly, integration   System AIT
                   and test                       

  LEOP             Delivery and commissioning     Commissioning

  Phase E          Nominal operations             Operations

  Phase E EXT      Extended operations            Extension

  Phase F          Closeout and disposal          Closeout

  Phase G          Data exploitation              Science use
  ------------------------------------------------------------------------

  : Table 3 -- Costing Phase Crosswalk

The schedule planning basis is B 15 months; C 12 months; D1 16 months;
D2 9 months; LEOP/commissioning 6 months; E 36 months. Activities with
long-lead procurement and parallel unit builds overlap; durations should
not be arithmetically summed to infer a delivery date.

  ----------------------------------------------------------------------------------------
  **Phase**   **0**      **A**      **B**      **C**      **D1**     **D2**     **E**
  ----------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
  Duration,   TBD        TBD        15         12         16         9          36
  months                                                                        

  Status      planning   planning   planning   planning   planning   planning   planning
  ----------------------------------------------------------------------------------------

  : Table 4 -- Planning Phase Dates and Durations

## Project Milestones

  --------------------------------------------------------------------------
  **Instrument / **Gate /      **Major Milestone**             **Milestone
  PM Phase**     Milestone**                                   Date**
  -------------- ------------- ------------------------------- -------------
  0              MCR           Mission Concept Review          Apr 2027

  A              SRR           System Requirements Review      Feb 2028

  B              PDR           Preliminary Design Review       Apr 2029

  C              CDR           Critical Design Review          Apr 2030

  D1             MRR           Manufacturing Readiness Review  Jul 2030

  D1             EVT           Instrument qualification        Feb 2031

  D1             EVT           FM-1 complete                   Oct 2031

  D1             EVT           FM-2 complete                   Jan 2032

  D2             SIR           System Integration Review       Mar 2032

  D2             AR            Acceptance                      Jul 2032

  D2             LRR           Launch / Delivery Readiness     Oct 2032
                               Review                          

  D2             L1--L3        Launch sequence                 Dec 2032

  E              EVT           Commissioning                   Jun 2033

  E              EVT           Nominal end                     Jun 2036
  --------------------------------------------------------------------------

  : Table 5 -- Major Milestones

## Safety and Mission Assurance

The project applies controlled requirements, hazard analysis,
independent quality oversight, parts and materials screening,
nonconformance disposition, serialized configuration and documented
readiness reviews. Hazards include stored energy, fluid containment,
high voltage, radiation, moving mechanisms, thermal surfaces and
potential loss of user service as applicable.

For Tavora Mesosphere Explorer, the initial risk concentration is
Detector stray light at twilight, spectral calibration drift,
orbital-plane separation, drag-driven propellant growth and downlink
coverage. Safety-related controls receive independent verification;
mission success and medical or food-use claims require separate
acceptance evidence.

## Prototyping Model Philosophy Qualification and Verification Strategy

The reference model philosophy comprises an electrical integration
article, engineering or breadboard articles for novel functions, a
structural/thermal qualification article and 2 flight or delivered
unit(s). Every unit receives end-to-end functional, environmental
workmanship, communications, safety and calibration testing.
Qualification of a representative article does not waive acceptance of
later units.

Verification records state the exact serial number, software version,
procedures, environmental settings, anomalies and concessions. The
commissioning review compares as-delivered performance to the reference
allocation before operations begin.

## Sparing Strategy

Flight spares are allocated for critical, long lead and failure-prone
units. A maintained engineering article and ground support equipment
support anomaly reproduction and software validation. The final spare
quantities and holding costs belong in Part B.

## Risk Assessment

The Part C risk register controls risk probability, cost and schedule
exposure. Principal threats: Detector stray light at twilight, spectral
calibration drift, orbital-plane separation, drag-driven propellant
growth and downlink coverage. Each has an owner, trigger, planned
mitigation and residual exposure. Design reserves on mass, power, data
and propellant or consumables are reported separately from financial
contingency.

## Organizational Breakdown Structure

### Space Agencies and Government Organizations

  ----------------------------------------------------------------------------
  **Partner**           **Jurisdiction**   **Proposed role**
  --------------------- ------------------ -----------------------------------
  Neraval Atmospheric   Mission            mission authority, procurement,
  Directorate           jurisdiction       project assurance and acceptance.

  ----------------------------------------------------------------------------

  : Table 6 -- Mission Organizations

### Industrial Partners

  -----------------------------------------------------------------------
  **Partner**           **Domain**    **Proposed role**
  --------------------- ------------- -----------------------------------
  Oryvex Orbital        Mission       integrated unit design, manufacture
  Manufacturing         supply chain  and system verification.

  Selrith Optical Works Mission       payload/process equipment and
                        supply chain  acceptance calibration.

  Daverin Launch        Mission       delivery, campaign operations and
  Collective            supply chain  associated interfaces.

  Mirevan Receiving     Mission       ground network, receiving
  Services              supply chain  interfaces and operations support.
  -----------------------------------------------------------------------

  : Table 7 -- Industrial Partners

### Participating Academic Institutions

  -----------------------------------------------------------------------
  **Institution**       **Domain**    **Proposed contribution**
  --------------------- ------------- -----------------------------------
  Istralen Atmospheric  Science       science or user requirements,
  Institute             consortium    calibration, data validation and
                                      exploitation.

  -----------------------------------------------------------------------

  : Table 8 -- Research Institutions

### Scientific Leadership (Principal Investigator)

  ----------------------------------------------------------------------
  **Position**          **Assigned      **Affiliation**
                        individual**    
  --------------------- --------------- --------------------------------
  Principal             Tavren Elovar   Istralen Atmospheric Institute
  investigator                          

  Instrument scientist  Mirev Solanar   Selrith Optical Works
  ----------------------------------------------------------------------

  : Table 9 -- Scientific Leadership
