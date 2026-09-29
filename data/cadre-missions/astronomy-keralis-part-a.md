CADRe Part A • KAR

Mission Cost Analysis Directorate

Cost Analysis Data Requirements

PART A

Keralis Binary Interior Survey

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

Figure 1 -- Keralis Binary Interior Survey mission architecture

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

The reference configuration is one carrier and two beacons. Its
operational environment is Reference binary target on preliminary a =
1.24 AU, e = 0.18, i = 3.2° orbit; trajectory is an estimating
reference. The nominal duration is 20-month cruise; 14-month survey; 36
months launch-to-closeout. The flight or installed unit is sized at 340
kg and uses 630 W power generation or host allocation as stated in the
subsystem budget.

The design carries low-frequency bistatic radar, laser altimeter and
optical navigation camera and dual surface beacons. Each produces a
separately calibrated record with common time, configuration and quality
metadata. The science objectives are quantified in the requirement
matrix below.

![Figure 1 -- Keralis Binary Interior Survey mission architecture.
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
  1              Primary mission       Determine bulk density to ±8%,
                 outcome               characterize the primary interior to
                                       30 m radial cells where geometry
                                       permits, and map the binary mutual
                                       orbit to ±5 m range accuracy.

  2              Operational           Deliver 20-month cruise; 14-month
                 sustainability        survey; 36 months
                                       launch-to-closeout. with
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
  Mission         One carrier and two beacons; 1     Flight hardware
  architecture    unit(s).                           allocation,
                                                     interface control
                                                     and acceptance
                                                     testing.

  Operating       Reference binary target on         Propellant,
  environment     preliminary a = 1.24 AU, e = 0.18, navigation, flight
                  i = 3.2° orbit; trajectory is an   dynamics and
                  estimating reference.              delivery accuracy.

  Mission         20-month cruise; 14-month survey;  Launch capacity,
  duration        36 months launch-to-closeout.      structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.

  Unit mass       ≤340 kg as delivered or at launch, Launch capacity,
                  including the budgeted contents.   structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.

  Payload         ≤64 kg, with definitions           Launch capacity,
  allocation      controlled by the mass table.      structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.

  Power           630 W at specified reference;      Generation,
  generation /    nominal 320 W and peak 500 W.      storage, power
  provision                                          distribution,
                                                     thermal rejection
                                                     and eclipse margin.

  Primary         Determine bulk density to ±8%,     Detector
  measurement     characterize the primary interior  performance,
                  to 30 m radial cells where         calibration,
                  geometry permits, and map the      metrology and
                  binary mutual orbit to ±5 m range  end-to-end
                  accuracy.                          verification.

  Instrument 1    18 kg / 120 W; 15--30 MHz stepped  Flight hardware
                  radar with 2 MHz useful bandwidth; allocation,
                  \~40 m equivalent range cell in    interface control
                  material of dielectric constant 4, and acceptance
                  subject to inversion and geometry. testing.

  Instrument 2    21 kg / 65 W; 5 cm ranging         Detector
                  precision at 5 km and ≤0.5 m/pixel performance,
                  optical mapping at 3 km under      calibration,
                  illuminated geometry.              metrology and
                                                     end-to-end
                                                     verification.

  Instrument 3    Two 9 kg beacons; 2 W transmitters Flight hardware
                  and 3-year primary-cell capacity   allocation,
                  with duty cycled operation;        interface control
                  survivability after deployment is  and acceptance
                  a mission risk.                    testing.

  Pointing or     Two star trackers, four reaction   Flight hardware
  positioning     wheels, six Sun sensors and        allocation,
                  optical navigation. Radar baseline interface control
                  pointing ≤0.15°; imaging pointing  and acceptance
                  knowledge ≤0.03° (95th             testing.
                  percentile).                       

  Mission-data    2.0 GB/day during survey           Launch capacity,
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

Aderven Exploration Authority owns system requirements, procurement,
risk and mission acceptance.

Qevrion Flight Systems owns the integrated unit, interfaces and
system-level verification.

Mavellis Instrument Foundry delivers the measurement equipment and
calibration evidence.

Orthen Launch Cooperative delivers the unit to its destination and
verifies interface conditions.

Luroven Deep Space Network supplies receiving, networking and
ground-service capacity.

Telvaran Geophysics Institute produces, validates and archives the
calibrated mission products.

# Space Segment Description

The reference configuration is one carrier and two beacons. Its
operational environment is Reference binary target on preliminary a =
1.24 AU, e = 0.18, i = 3.2° orbit; trajectory is an estimating
reference. The nominal duration is 20-month cruise; 14-month survey; 36
months launch-to-closeout. The flight or installed unit is sized at 340
kg and uses 630 W power generation or host allocation as stated in the
subsystem budget. The segment boundary includes the integrated unit and
its mission-specific payload, interfaces, spares and verification
articles.

## Spacecraft Bus

The integrated unit provides structural restraint, power, command and
data handling, thermal protection, equipment control and the
communication interface appropriate to Reference binary target on
preliminary a = 1.24 AU, e = 0.18, i = 3.2° orbit; trajectory is an
estimating reference. The design shall carry configuration identifiers
and independent acceptance records for every delivered unit.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary allocation / target**
  ------------------------ -------------------------------------------
  Unit mass                340 kg

  Mass composition         196 kg dry bus, 64 kg hosted payload, 80 kg
                           propellant = 340 kg carrier

  Payload / experiment     64 kg
  allocation               

  Generation / provision   630 W reference

  Nominal / peak demand    320 W / 500 W

  Storage                  128 GB usable

  Autonomy                 ≥72 h safe configuration with applicable
                           external power

  Maneuver / mobility      550 m/s maneuver requirement; 80 kg
                           monopropellant at 230 s yields \~603 m/s
                           ideal at 340 kg initial mass

  Delivery                 C3 ≥8 km²/s²; 340 kg carrier including its
                           two beacons + 90 kg adaptor/dispenser = 430
                           kg; ≥550 kg service capability

  Design life              20-month cruise; 14-month survey; 36 months
                           launch-to-closeout.
  --------------------------------------------------------------------

### Structural Subsystem

The structural design is sized for 340 kg delivery mass and the
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

Nominal allocation: 630 W generation or host provision, 320 W operating
demand, 500 W short-duration peak. These values describe distinct
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
  630 W baseline          Regulated bus,          320 W nominal / 500 W
                          protected battery/host  peak
                          service                 

  -----------------------------------------------------------------------

### Command and Data Handling

A redundant or monitored controller executes time-tagged operations,
instrument interlocks, fault detection and protected storage. The local
allocation is 128 GB usable. A storage analysis includes the worst
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

manage 128 GB usable storage and priority records;

switch to a safe mode after undervoltage, overtemperature or watchdog
failure;

retain the last accepted software and configuration baseline;

reacquire the ground or host link after a missed contact; and

report data quality and calibration status with each product.

A mission-data model checks the 2.0 GB/day during survey planning case
against memory capacity, contact availability and the required
processing latency. Raw records are retained until integrity checks and
ingest acknowledgement complete.

### Thermal Subsystem

0.82--1.46 AU irradiance envelope; avionics 0--40 °C and radar front-end
−10--45 °C; 0.8 m² radiator planning area.

The thermal design shall close with numerical hot and cold cases and
shall separately report radiator, insulation, heater and sensor
allocations. Instrument calibration is repeated across the qualified
operating temperature range. Safe-mode heating and peak-mode waste heat
are independently assessed.

Thermal verification considers heat from 500 W peak electrical input,
the nominal 320 W mode, external heat flux, enclosure conduction and the
passive or active rejection path. The final instrument uncertainty
budget includes temperature-driven bias and gradients.

The thermal test programme shall establish:

steady and transient operating limits of each component;

heater and cooler demand in cold and hot cases;

radiator or host heat-rejection sizing;

calibration stability across the qualified temperature range; and

safe survival during a commanded outage.

### Attitude Determination and Control Subsystem

Two star trackers, four reaction wheels, six Sun sensors and optical
navigation. Radar baseline pointing ≤0.15°; imaging pointing knowledge
≤0.03° (95th percentile).

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

80 kg monopropellant, 230 s effective Isp, 4 × 20 N thrusters; ideal Δv
= 603 m/s by rocket equation.

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

  Initial unit mass       340                     kg

  Reference performance   550 m/s maneuver        m/s or N/A
                          requirement; 80 kg      
                          monopropellant at 230 s 
                          yields \~603 m/s ideal  
                          at 340 kg initial mass  

  Fuel / propellant       80 kg monopropellant,   kg / description
  allocation              230 s effective Isp, 4  
                          × 20 N thrusters        

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

  Operational maintenance  Repeated 3--8 km standoff arcs with
                           0.2--1.0 m/s corrections; no continuous
                           stable close orbit assumed.

  Navigation and           550 m/s maneuver requirement; 80 kg
  correction               monopropellant at 230 s yields \~603 m/s
                           ideal at 340 kg initial mass

  Contingency and          Explicit reserve controlled in Part B /
  residuals                Part C

  Total capability         Reconcile with 80 kg monopropellant, 230 s
                           effective Isp, 4 × 20 N thrusters; ideal Δv
                           = 603 m/s by rocket equ
  --------------------------------------------------------------------

### Telemetry, Tracking and Command

At 4 Mb/s, a 90-minute contact yields 2.7 GB gross, leaving 26%
protocol/retransmission allowance for 2.0 GB daily return. Schedule 2
h/day in survey.

The final link assessment shall include transmitter power, antenna gain
or host data-service rate, geometry, coding, weather where relevant and
a minimum allocated margin. Distinguish command/control packets, health
telemetry, raw measurements and user or science products. A link outage
analysis is required before ground-service capacity is baselined.

The communications baseline includes 4 Mb/s X-band at ≤1.6 AU to a 12
m-class station. The contact budget carries acquisition, engineering
telemetry, protocol framing, retransmission and unavailable weather or
host periods. The sizing check compares usable transferred bytes per
contact with 2.0 GB/day during survey and any higher burst case.

A separate low-rate command path or host maintenance interface shall
support diagnosis after the prime mission-data path becomes unavailable.
No unauthenticated measurement data can alter safety-critical command
parameters.

## Payload

The payload or process equipment is divided into low-frequency bistatic
radar, laser altimeter and optical navigation camera and dual surface
beacons. Each element has a separate delivered mass, operating load,
mode list, failure assessment and calibration requirement.

### Low-frequency bistatic radar

18 kg / 120 W; 15--30 MHz stepped radar with 2 MHz useful bandwidth;
\~40 m equivalent range cell in material of dielectric constant 4,
subject to inversion and geometry.

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
  Primary function         Low-frequency bistatic radar

  Measured performance     18 kg / 120 W; 15--30 MHz stepped radar
                           with 2 MHz useful bandwidth; \~40 m
                           equivalent range cell in material of
                           dielectric constant 4, subject to inversion
                           and geometry.

  Unit-level calibration   Before integration and after environmental
                           qualification

  Electrical interface     Protected distribution and commanded safe
                           state

  Data interface           Time-tagged raw records plus status and
                           quality flags

  Environmental tolerance  0.82--1.46 AU irradiance envelope; avionics
                           0--40 °C and radar front-end −10--45 °C;
                           0.8 m² radiator planning area.

  Mass accounting          Within 64 kg payload or experiment
                           allocation

  Verification             Test against mission-level success
                           criterion

  Operations mode          Only when power, thermal and link margins
                           permit

  Fault response           Isolate and report without affecting
                           safe-mode command
  --------------------------------------------------------------------

### Laser altimeter and optical navigation camera

21 kg / 65 W; 5 cm ranging precision at 5 km and ≤0.5 m/pixel optical
mapping at 3 km under illuminated geometry.

This measurement or process provides an independent check on the primary
result. The ground model shall retain geometric, thermal and
instrumental uncertainty, including changes caused by the spacecraft or
host.

For Keralis Binary Interior Survey, complementarity is intentional: one
channel measures a different physical quantity or provides a contextual
state. Processing shall preserve the raw evidence, identify retrieval
assumptions and reject inconsistent cross-calibration before product
release.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary requirement / target**
  ------------------------ -------------------------------------------
  Function                 Laser altimeter and optical navigation
                           camera

  Performance              21 kg / 65 W; 5 cm ranging precision at 5
                           km and ≤0.5 m/pixel optical mapping at 3 km
                           under illuminated geometry.

  Mass                     Included in payload/experiment allocation

  Power                    Mode specific; close against peak load

  Field / process geometry Reference binary target on preliminary a =
                           1.24 AU, e = 0.18, i = 3.2° orbit;
                           trajectory is an estimating reference.

  Timing                   Synchronized to system command clock

  Calibration              At acceptance and by scheduled in-operation
                           reference

  Data volume              2.0 GB/day during survey

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

  Sensor interfaces        Low-frequency bistatic radar; Laser
                           altimeter and optical navigation camera;
                           Dual surface beacons

  System interface         Protected command and local data bus

  Buffering                128 GB usable system allocation

  Processing               Lossless event flags and reversible
                           screening where practical

  Timing                   Absolute reference and monotonically
                           numbered records

  Health monitoring        Voltage, temperature, current, reset count
                           and status

  Mass                     Within 64 kg allocation

  Peak electrical power    Included in 500 W integrated peak

  Radiation / environment  Qualified for Reference binary target on
                           preliminary a = 1.24 AU, e = 0.18, i = 3.2°
                           orbi
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

  Primary reference        Dual surface beacons

  Frequency                At commissioning, after anomaly and on a
                           scheduled monthly cadence

  Environmental dependency 0.82--1.46 AU irradiance envelope; avionics
                           0--40 °C and radar front-end −10--45 °C;
                           0.8 m² radiator planning area.

  Long-term drift          Trend against accepted reference and flag
                           \>2% unexplained change

  Data linkage             100% released products identify applicable
                           calibration version

  Independent verification Recheck with Laser altimeter and optical
                           navigation camera

  Instrument monitoring    On each operating cycle

  Mass / power             Within payload and system allocations
  --------------------------------------------------------------------

![Figure 2 -- Payload measurement and data path. Components and output
interfaces are explicitly labeled.](media/image6.png){width="6.4in"
height="1.8529407261592301in"}

# Launch Segment Description

C3 ≥8 km²/s²; 340 kg carrier including its two beacons + 90 kg
adaptor/dispenser = 430 kg; ≥550 kg service capability

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

Two 12 m-class sites plus one contingency site; ≥8 GB/day ingestion; 60
TB controlled archive.

At 4 Mb/s, a 90-minute contact yields 2.7 GB gross, leaving 26%
protocol/retransmission allowance for 2.0 GB daily return. Schedule 2
h/day in survey.

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

  Receiving Stations /     Two 12 m-class sites plus one contingency
  Host Link                site; ≥8 GB/day ingestion; 60 TB controlled
                           archive.

  Operations Team          Staffed planned operations with automated
                           alarm and on-call response.

  Processing and Archive   Level 0 packet retention; Level 1
                           calibration; Level 2 products with
                           preserved lineage.

  Data Volume /            2.0 GB/day during survey; scheduled ground
  Availability             service availability ≥99%.
  --------------------------------------------------------------------

The daily return is 2.0 GB/day during survey. Downlink capacity and
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
files, algorithm version and exceptions. Capacity in Two 12 m-class
sites plus one contingency site; ≥8 GB/day ingestion; 60 TB controlled
archive. is a planning provision that shall be verified against years of
operation, replication and reprocessing.

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

The schedule planning basis is B 14 months; C 12 months; D1 16 months;
D2 8 months; cruise 20 months; survey 14 months. Activities with
long-lead procurement and parallel unit builds overlap; durations should
not be arithmetically summed to infer a delivery date.

  ----------------------------------------------------------------------------------------
  **Phase**   **0**      **A**      **B**      **C**      **D1**     **D2**     **E**
  ----------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
  Duration,   TBD        TBD        14         12         16         8          TBD
  months                                                                        

  Status      planning   planning   planning   planning   planning   planning   planning
  ----------------------------------------------------------------------------------------

  : Table 4 -- Planning Phase Dates and Durations

## Project Milestones

  --------------------------------------------------------------------------
  **Instrument / **Gate /      **Major Milestone**             **Milestone
  PM Phase**     Milestone**                                   Date**
  -------------- ------------- ------------------------------- -------------
  0              MCR           Mission Concept Review          Mar 2027

  A              SRR           System Requirements Review      Jan 2028

  B              PDR           Preliminary Design Review       Mar 2029

  C              CDR           Critical Design Review          Mar 2030

  D1             MRR           Manufacturing Readiness Review  Jun 2030

  D1             EVT           First flight unit assembled     May 2031

  D2             SIR           System Integration Review       Oct 2031

  D2             AR            Environmental acceptance        Apr 2032

  D2             LRR           Launch / Delivery Readiness     Sep 2032
                               Review                          

  D2             L             Launch                          Nov 2032

  E              EVT           Encounter                       Jul 2034

  E              EVT           Nominal survey end              Sep 2035

  E              EVT           Closeout                        Nov 2035
  --------------------------------------------------------------------------

  : Table 5 -- Major Milestones

## Safety and Mission Assurance

The project applies controlled requirements, hazard analysis,
independent quality oversight, parts and materials screening,
nonconformance disposition, serialized configuration and documented
readiness reviews. Hazards include stored energy, fluid containment,
high voltage, radiation, moving mechanisms, thermal surfaces and
potential loss of user service as applicable.

For Keralis Binary Interior Survey, the initial risk concentration is
Beacon landing at \<0.25 m/s, uncertain dielectric attenuation, complex
binary gravity, repeated proximity maneuvers and dust hazard.
Safety-related controls receive independent verification; mission
success and medical or food-use claims require separate acceptance
evidence.

## Prototyping Model Philosophy Qualification and Verification Strategy

The reference model philosophy comprises an electrical integration
article, engineering or breadboard articles for novel functions, a
structural/thermal qualification article and 1 flight or delivered
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
exposure. Principal threats: Beacon landing at \<0.25 m/s, uncertain
dielectric attenuation, complex binary gravity, repeated proximity
maneuvers and dust hazard. Each has an owner, trigger, planned
mitigation and residual exposure. Design reserves on mass, power, data
and propellant or consumables are reported separately from financial
contingency.

## Organizational Breakdown Structure

### Space Agencies and Government Organizations

  ----------------------------------------------------------------------------
  **Partner**           **Jurisdiction**   **Proposed role**
  --------------------- ------------------ -----------------------------------
  Aderven Exploration   Mission            mission authority, procurement,
  Authority             jurisdiction       project assurance and acceptance.

  ----------------------------------------------------------------------------

  : Table 6 -- Mission Organizations

### Industrial Partners

  -----------------------------------------------------------------------
  **Partner**           **Domain**    **Proposed role**
  --------------------- ------------- -----------------------------------
  Qevrion Flight        Mission       integrated unit design, manufacture
  Systems               supply chain  and system verification.

  Mavellis Instrument   Mission       payload/process equipment and
  Foundry               supply chain  acceptance calibration.

  Orthen Launch         Mission       delivery, campaign operations and
  Cooperative           supply chain  associated interfaces.

  Luroven Deep Space    Mission       ground network, receiving
  Network               supply chain  interfaces and operations support.
  -----------------------------------------------------------------------

  : Table 7 -- Industrial Partners

### Participating Academic Institutions

  -----------------------------------------------------------------------
  **Institution**       **Domain**    **Proposed contribution**
  --------------------- ------------- -----------------------------------
  Telvaran Geophysics   Science       science or user requirements,
  Institute             consortium    calibration, data validation and
                                      exploitation.

  -----------------------------------------------------------------------

  : Table 8 -- Research Institutions

### Scientific Leadership (Principal Investigator)

  ----------------------------------------------------------------------
  **Position**          **Assigned      **Affiliation**
                        individual**    
  --------------------- --------------- --------------------------------
  Principal             Tavren Elovar   Telvaran Geophysics Institute
  investigator                          

  Instrument scientist  Mirev Solanar   Mavellis Instrument Foundry
  ----------------------------------------------------------------------

  : Table 9 -- Scientific Leadership
