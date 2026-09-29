CADRe Part A • OADO

Mission Cost Analysis Directorate

Cost Analysis Data Requirements

PART A

Orastra Auroral Dynamics Observatory

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

Figure 1 -- Orastra Auroral Dynamics Observatory mission architecture

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

The reference configuration is two phased polar imaging spacecraft. Its
operational environment is Two spacecraft in a 760 ±20 km near-circular
orbit at 90° ±2° inclination; relative phase 180° ±10°. The nominal
duration is Three-year nominal science after three-month commissioning;
four-year flight design life. The flight or installed unit is sized at
260 kg and uses 720 W power generation or host allocation as stated in
the subsystem budget.

The design carries far-ultraviolet auroral imager, visible narrowband
auroral imager and energetic particle context sensor. Each produces a
separately calibrated record with common time, configuration and quality
metadata. The science objectives are quantified in the requirement
matrix below.

![Figure 1 -- Orastra Auroral Dynamics Observatory mission architecture.
Labeled boxes identify responsibility boundaries; dimensions are
schematic.](media/image5.png){width="6.4in"
height="1.8529407261592301in"}

## Strategic Objectives

The mission aligns the measurement or service objectives with the
sponsoring authority's stated science, capability and operations
priorities.

  -------------------------------------------------------------------------
  **Priority**   **Strategic goal**    **Mission contribution**
  -------------- --------------------- ------------------------------------
  1              Primary mission       Map 65°--80° magnetic-latitude
                 outcome               auroral emissions at ≤10 km
                                       projected sampling and ≤60 min
                                       median revisit during qualifying
                                       darkness; identify 20% brightness
                                       changes over two successive visits
                                       above the calibrated detection
                                       threshold.

  2              Operational           Deliver Three-year nominal science
                 sustainability        after three-month commissioning;
                                       four-year flight design life. with
                                       independently accepted baseline
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
  Mission         Two phased polar imaging           Flight hardware
  architecture    spacecraft; 2 unit(s).             allocation,
                                                     interface control
                                                     and acceptance
                                                     testing.

  Operating       Two spacecraft in a 760 ±20 km     Propellant,
  environment     near-circular orbit at 90° ±2°     navigation, flight
                  inclination; relative phase 180°   dynamics and
                  ±10°.                              delivery accuracy.

  Mission         Three-year nominal science after   Parts screening,
  duration        three-month commissioning;         redundancy, spares
                  four-year flight design life.      and operations
                                                     staffing.

  Unit mass       ≤260 kg as delivered or at launch, Launch capacity,
                  including the budgeted contents.   structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.

  Payload         ≤40 kg, with definitions           Launch capacity,
  allocation      controlled by the mass table.      structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.

  Power           720 W at specified reference;      Generation,
  generation /    nominal 410 W and peak 600 W.      storage, power
  provision                                          distribution,
                                                     thermal rejection
                                                     and eclipse margin.

  Primary         Map 65°--80° magnetic-latitude     Flight hardware
  measurement     auroral emissions at ≤10 km        allocation,
                  projected sampling and ≤60 min     interface control
                  median revisit during qualifying   and acceptance
                  darkness; identify 20% brightness  testing.
                  changes over two successive visits 
                  above the calibrated detection     
                  threshold.                         

  Instrument 1    20 kg / 105 W; 130--170 nm         Flight hardware
                  passband; ≤10 km mapped sampling   allocation,
                  at reference view; 30 s frames     interface control
                  with dayglow rejection.            and acceptance
                                                     testing.

  Instrument 2    12 kg / 65 W; 557.7 nm line with   Flight hardware
                  ≤2 nm passband; ≤10 km mapped      allocation,
                  sampling in darkness; 5 s exposure interface control
                  target.                            and acceptance
                                                     testing.

  Instrument 3    8 kg / 35 W; 1--100 keV particles  Generation,
                  in 16 energy bins with 1 s burst   storage, power
                  sampling and 10 s nominal          distribution,
                  sampling.                          thermal rejection
                                                     and eclipse margin.

  Pointing or     Two star trackers, four wheels,    Flight hardware
  positioning     magnetic torquers and GNSS;        allocation,
                  pointing knowledge ≤0.03° and      interface control
                  stability ≤0.01° over 30 s frame.  and acceptance
                                                     testing.

  Mission-data    6 GB/day per spacecraft after      Launch capacity,
  volume          onboard screening                  structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.
  ----------------------------------------------------------------------

  : Table 2 -- Selected System Requirements

## High-Level Mission Architecture

The architecture separates oversight, space or deployed hardware, launch
or delivery, ground services, operations and science or user
exploitation.

Iverune Polar Science Office owns system requirements, procurement, risk
and mission acceptance.

Nerovian Satellite Works owns the integrated unit, interfaces and
system-level verification.

Kelvori Optical Instruments delivers the measurement equipment and
calibration evidence.

Orivane Launch Cooperative delivers the unit to its destination and
verifies interface conditions.

Darellis Polar Ground Services supplies receiving, networking and
ground-service capacity.

Yalveran Geospace Institute produces, validates and archives the
calibrated mission products.

# Space Segment Description

The reference configuration is two phased polar imaging spacecraft. Its
operational environment is Two spacecraft in a 760 ±20 km near-circular
orbit at 90° ±2° inclination; relative phase 180° ±10°. The nominal
duration is Three-year nominal science after three-month commissioning;
four-year flight design life. The flight or installed unit is sized at
260 kg and uses 720 W power generation or host allocation as stated in
the subsystem budget. The segment boundary includes the integrated unit
and its mission-specific payload, interfaces, spares and verification
articles.

## Spacecraft Bus

The integrated unit provides structural restraint, power, command and
data handling, thermal protection, equipment control and the
communication interface appropriate to Two spacecraft in a 760 ±20 km
near-circular orbit at 90° ±2° inclination; relative phase 180° ±10°.
The design shall carry configuration identifiers and independent
acceptance records for every delivered unit.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary allocation / target**
  ------------------------ -------------------------------------------
  Unit mass                260 kg

  Mass composition         210 kg dry bus + 40 kg payload + 10 kg
                           propellant = 260 kg

  Payload / experiment     40 kg
  allocation               

  Generation / provision   720 W reference

  Nominal / peak demand    410 W / 600 W

  Storage                  256 GB usable

  Autonomy                 ≥72 h safe configuration with applicable
                           external power

  Maneuver / mobility      ≥70 m/s each; 10 kg monopropellant at 220 s
                           yields \~85 m/s ideal at 260 kg initial
                           mass

  Delivery                 Two × 260 kg flight units + 100 kg
                           dispenser/adaptor = 620 kg to reference 760
                           km orbit; service capacity ≥750 kg

  Design life              Three-year nominal science after
                           three-month commissioning; four-year flight
                           design life.
  --------------------------------------------------------------------

### Structural Subsystem

The structural design is sized for 260 kg delivery mass and the
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

Nominal allocation: 720 W generation or host provision, 410 W operating
demand, 600 W short-duration peak. These values describe distinct
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
  720 W baseline          Regulated bus,          410 W nominal / 600 W
                          protected battery/host  peak
                          service                 

  -----------------------------------------------------------------------

### Command and Data Handling

A redundant or monitored controller executes time-tagged operations,
instrument interlocks, fault detection and protected storage. The local
allocation is 256 GB usable. A storage analysis includes the worst
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

manage 256 GB usable storage and priority records;

switch to a safe mode after undervoltage, overtemperature or watchdog
failure;

retain the last accepted software and configuration baseline;

reacquire the ground or host link after a missed contact; and

report data quality and calibration status with each product.

A mission-data model checks the 6 GB/day per spacecraft after onboard
screening planning case against memory capacity, contact availability
and the required processing latency. Raw records are retained until
integrity checks and ingest acknowledgement complete.

### Thermal Subsystem

760 km eclipse season and auroral instrument duty-cycle cases; payload
optical bench 5--25 °C and UV detector −10--10 °C.

The thermal design shall close with numerical hot and cold cases and
shall separately report radiator, insulation, heater and sensor
allocations. Instrument calibration is repeated across the qualified
operating temperature range. Safe-mode heating and peak-mode waste heat
are independently assessed.

Thermal verification considers heat from 600 W peak electrical input,
the nominal 410 W mode, external heat flux, enclosure conduction and the
passive or active rejection path. The final instrument uncertainty
budget includes temperature-driven bias and gradients.

The thermal test programme shall establish:

steady and transient operating limits of each component;

heater and cooler demand in cold and hot cases;

radiator or host heat-rejection sizing;

calibration stability across the qualified temperature range; and

safe survival during a commanded outage.

### Attitude Determination and Control Subsystem

Two star trackers, four wheels, magnetic torquers and GNSS; pointing
knowledge ≤0.03° and stability ≤0.01° over 30 s frame.

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

10 kg monopropellant at 220 s effective Isp provides \~85 m/s ideal Δv;
70 m/s requirement leaves 15 m/s for performance dispersion.

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

  Initial unit mass       260                     kg

  Reference performance   ≥70 m/s each; 10 kg     m/s or N/A
                          monopropellant at 220 s 
                          yields \~85 m/s ideal   
                          at 260 kg initial mass  

  Fuel / propellant       10 kg monopropellant at kg / description
  allocation              220 s effective Isp     
                          provides \~85 m/s ideal 
                          Δv                      

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

  Operational maintenance  Near-polar 760 km circular reference orbit,
                           180° along-track phasing, about 100-minute
                           period.

  Navigation and           ≥70 m/s each; 10 kg monopropellant at 220 s
  correction               yields \~85 m/s ideal at 260 kg initial
                           mass

  Contingency and          Explicit reserve controlled in Part B /
  residuals                Part C

  Total capability         Reconcile with 10 kg monopropellant at 220
                           s effective Isp provides \~85 m/s ideal Δv;
                           70 m/s requirement leave
  --------------------------------------------------------------------

### Telemetry, Tracking and Command

At 100 Mb/s, two 12-minute contacts yield 18 GB gross; 6 GB/day requires
≥33% effective payload fraction, leaving outage/replay margin.

The final link assessment shall include transmitter power, antenna gain
or host data-service rate, geometry, coding, weather where relevant and
a minimum allocated margin. Distinguish command/control packets, health
telemetry, raw measurements and user or science products. A link outage
analysis is required before ground-service capacity is baselined.

The communications baseline includes 100 Mb/s X-band downlink to 7
m-class stations; S-band contingency command. The contact budget carries
acquisition, engineering telemetry, protocol framing, retransmission and
unavailable weather or host periods. The sizing check compares usable
transferred bytes per contact with 6 GB/day per spacecraft after onboard
screening and any higher burst case.

A separate low-rate command path or host maintenance interface shall
support diagnosis after the prime mission-data path becomes unavailable.
No unauthenticated measurement data can alter safety-critical command
parameters.

## Payload

The payload or process equipment is divided into far-ultraviolet auroral
imager, visible narrowband auroral imager and energetic particle context
sensor. Each element has a separate delivered mass, operating load, mode
list, failure assessment and calibration requirement.

### Far-ultraviolet auroral imager

20 kg / 105 W; 130--170 nm passband; ≤10 km mapped sampling at reference
view; 30 s frames with dayglow rejection.

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
  Primary function         Far-ultraviolet auroral imager

  Measured performance     20 kg / 105 W; 130--170 nm passband; ≤10 km
                           mapped sampling at reference view; 30 s
                           frames with dayglow rejection.

  Unit-level calibration   Before integration and after environmental
                           qualification

  Electrical interface     Protected distribution and commanded safe
                           state

  Data interface           Time-tagged raw records plus status and
                           quality flags

  Environmental tolerance  760 km eclipse season and auroral
                           instrument duty-cycle cases; payload
                           optical bench 5--25 °C and UV detector
                           −10--10 °C.

  Mass accounting          Within 40 kg payload or experiment
                           allocation

  Verification             Test against mission-level success
                           criterion

  Operations mode          Only when power, thermal and link margins
                           permit

  Fault response           Isolate and report without affecting
                           safe-mode command
  --------------------------------------------------------------------

### Visible narrowband auroral imager

12 kg / 65 W; 557.7 nm line with ≤2 nm passband; ≤10 km mapped sampling
in darkness; 5 s exposure target.

This measurement or process provides an independent check on the primary
result. The ground model shall retain geometric, thermal and
instrumental uncertainty, including changes caused by the spacecraft or
host.

For Orastra Auroral Dynamics Observatory, complementarity is
intentional: one channel measures a different physical quantity or
provides a contextual state. Processing shall preserve the raw evidence,
identify retrieval assumptions and reject inconsistent cross-calibration
before product release.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary requirement / target**
  ------------------------ -------------------------------------------
  Function                 Visible narrowband auroral imager

  Performance              12 kg / 65 W; 557.7 nm line with ≤2 nm
                           passband; ≤10 km mapped sampling in
                           darkness; 5 s exposure target.

  Mass                     Included in payload/experiment allocation

  Power                    Mode specific; close against peak load

  Field / process geometry Two spacecraft in a 760 ±20 km
                           near-circular orbit at 90° ±2° inclination;
                           relative phase 180° ±10°.

  Timing                   Synchronized to system command clock

  Calibration              At acceptance and by scheduled in-operation
                           reference

  Data volume              6 GB/day per spacecraft after onboard
                           screening

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

  Sensor interfaces        Far-ultraviolet auroral imager; Visible
                           narrowband auroral imager; Energetic
                           particle context sensor

  System interface         Protected command and local data bus

  Buffering                256 GB usable system allocation

  Processing               Lossless event flags and reversible
                           screening where practical

  Timing                   Absolute reference and monotonically
                           numbered records

  Health monitoring        Voltage, temperature, current, reset count
                           and status

  Mass                     Within 40 kg allocation

  Peak electrical power    Included in 600 W integrated peak

  Radiation / environment  Qualified for Two spacecraft in a 760 ±20
                           km near-circular orbit at 90° ±2°
                           inclination;
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

  Primary reference        Energetic particle context sensor

  Frequency                At commissioning, after anomaly and on a
                           scheduled monthly cadence

  Environmental dependency 760 km eclipse season and auroral
                           instrument duty-cycle cases; payload
                           optical bench 5--25 °C and UV detector
                           −10--10 °C.

  Long-term drift          Trend against accepted reference and flag
                           \>2% unexplained change

  Data linkage             100% released products identify applicable
                           calibration version

  Independent verification Recheck with Visible narrowband auroral
                           imager

  Instrument monitoring    On each operating cycle

  Mass / power             Within payload and system allocations
  --------------------------------------------------------------------

![Figure 2 -- Payload measurement and data path. Components and output
interfaces are explicitly labeled.](media/image6.png){width="6.4in"
height="1.8529407261592301in"}

# Launch Segment Description

Two × 260 kg flight units + 100 kg dispenser/adaptor = 620 kg to
reference 760 km orbit; service capacity ≥750 kg

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

Two polar 7 m sites plus one temperate backup; ≥30 GB/day combined
ingest; 80 TB multi-version archive.

At 100 Mb/s, two 12-minute contacts yield 18 GB gross; 6 GB/day requires
≥33% effective payload fraction, leaving outage/replay margin.

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

  Receiving Stations /     Two polar 7 m sites plus one temperate
  Host Link                backup; ≥30 GB/day combined ingest; 80 TB
                           multi-version archive.

  Operations Team          Staffed planned operations with automated
                           alarm and on-call response.

  Processing and Archive   Level 0 packet retention; Level 1
                           calibration; Level 2 products with
                           preserved lineage.

  Data Volume /            6 GB/day per spacecraft after onboard
  Availability             screening; scheduled ground service
                           availability ≥99%.
  --------------------------------------------------------------------

The daily return is 6 GB/day per spacecraft after onboard screening.
Downlink capacity and stored-data volume shall close under a minimum
48-hour missed-contact case, except where host operations impose a
different approved case. Science release depends on validation, access
permissions and a documented reprocessing path.

Mission operations include daily planning, health trending, commands,
flight dynamics or host status, calibrated processing, anomaly
resolution and archive integrity. Nominal staffing is a planned shift
with continuous alarm routing; time-critical encounters or crew
procedures require separate surge coverage.

The data archive retains source packets, released products, calibration
files, algorithm version and exceptions. Capacity in Two polar 7 m sites
plus one temperate backup; ≥30 GB/day combined ingest; 80 TB
multi-version archive. is a planning provision that shall be verified
against years of operation, replication and reprocessing.

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
D2 9 months; LEOP/commissioning 3 months; E 36 months. Activities with
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

  D1             EVT           UV qualification                Feb 2031

  D1             EVT           FM-1 complete                   Oct 2031

  D1             EVT           FM-2 complete                   Jan 2032

  D2             SIR           System Integration Review       Mar 2032

  D2             AR            Acceptance                      Jul 2032

  D2             LRR           Launch / Delivery Readiness     Oct 2032
                               Review                          

  D2             L             Launch                          Dec 2032

  E              EVT           Commissioning                   Mar 2033

  E              EVT           Nominal end                     Mar 2036
  --------------------------------------------------------------------------

  : Table 5 -- Major Milestones

## Safety and Mission Assurance

The project applies controlled requirements, hazard analysis,
independent quality oversight, parts and materials screening,
nonconformance disposition, serialized configuration and documented
readiness reviews. Hazards include stored energy, fluid containment,
high voltage, radiation, moving mechanisms, thermal surfaces and
potential loss of user service as applicable.

For Orastra Auroral Dynamics Observatory, the initial risk concentration
is Dayglow contamination, FUV detector gain drift, paired-orbit phasing,
radiation exposure in polar passes and viewing-geometry-dependent
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
exposure. Principal threats: Dayglow contamination, FUV detector gain
drift, paired-orbit phasing, radiation exposure in polar passes and
viewing-geometry-dependent coverage. Each has an owner, trigger, planned
mitigation and residual exposure. Design reserves on mass, power, data
and propellant or consumables are reported separately from financial
contingency.

## Organizational Breakdown Structure

### Space Agencies and Government Organizations

  ----------------------------------------------------------------------------
  **Partner**           **Jurisdiction**   **Proposed role**
  --------------------- ------------------ -----------------------------------
  Iverune Polar Science Mission            mission authority, procurement,
  Office                jurisdiction       project assurance and acceptance.

  ----------------------------------------------------------------------------

  : Table 6 -- Mission Organizations

### Industrial Partners

  -----------------------------------------------------------------------
  **Partner**           **Domain**    **Proposed role**
  --------------------- ------------- -----------------------------------
  Nerovian Satellite    Mission       integrated unit design, manufacture
  Works                 supply chain  and system verification.

  Kelvori Optical       Mission       payload/process equipment and
  Instruments           supply chain  acceptance calibration.

  Orivane Launch        Mission       delivery, campaign operations and
  Cooperative           supply chain  associated interfaces.

  Darellis Polar Ground Mission       ground network, receiving
  Services              supply chain  interfaces and operations support.
  -----------------------------------------------------------------------

  : Table 7 -- Industrial Partners

### Participating Academic Institutions

  -----------------------------------------------------------------------
  **Institution**       **Domain**    **Proposed contribution**
  --------------------- ------------- -----------------------------------
  Yalveran Geospace     Science       science or user requirements,
  Institute             consortium    calibration, data validation and
                                      exploitation.

  -----------------------------------------------------------------------

  : Table 8 -- Research Institutions

### Scientific Leadership (Principal Investigator)

  ----------------------------------------------------------------------
  **Position**          **Assigned      **Affiliation**
                        individual**    
  --------------------- --------------- --------------------------------
  Principal             Tavren Elovar   Yalveran Geospace Institute
  investigator                          

  Instrument scientist  Mirev Solanar   Kelvori Optical Instruments
  ----------------------------------------------------------------------

  : Table 9 -- Scientific Leadership
