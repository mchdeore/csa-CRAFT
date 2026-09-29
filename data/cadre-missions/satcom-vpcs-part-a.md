CADRe Part A • VPCS

Mission Cost Analysis Directorate

Cost Analysis Data Requirements

PART A

Virelan Protected Communications System

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

Figure 1 -- Virelan Protected Communications System mission architecture

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

The reference configuration is three geostationary relay satellites. Its
operational environment is Three geostationary slots at nominal
longitudes 40°, 160° and 280°E, each held within ±0.10° longitude and
±0.10° inclination box. The nominal duration is Seven years nominal
service after six-month transfer and commissioning; ten-year design
life. The flight or installed unit is sized at 1150 kg and uses 5400 W
power generation or host allocation as stated in the subsystem budget.

The design carries protected digital communications payload, steerable
multi-beam antenna assembly and cryptographic command boundary. Each
produces a separately calibrated record with common time, configuration
and quality metadata. The science objectives are quantified in the
requirement matrix below.

![Figure 1 -- Virelan Protected Communications System mission
architecture. Labeled boxes identify responsibility boundaries;
dimensions are schematic.](media/image5.png){width="6.4in"
height="1.8529407261592301in"}

## Strategic Objectives

The mission aligns the measurement or service objectives with the
sponsoring authority's stated science, capability and operations
priorities.

  -------------------------------------------------------------------------
  **Priority**   **Strategic goal**    **Mission contribution**
  -------------- --------------------- ------------------------------------
  1              Primary mission       Deliver ≥2.0 Gb/s aggregate usable
                 outcome               service per spacecraft across eight
                                       beams, ≥99.5% scheduled monthly
                                       network availability in each
                                       declared service region, and
                                       authenticated control of every
                                       protected user session.

  2              Operational           Deliver Seven years nominal service
                 sustainability        after six-month transfer and
                                       commissioning; ten-year design life.
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
  Mission         Three geostationary relay          Flight hardware
  architecture    satellites; 3 unit(s).             allocation,
                                                     interface control
                                                     and acceptance
                                                     testing.

  Operating       Three geostationary slots at       Flight hardware
  environment     nominal longitudes 40°, 160° and   allocation,
                  280°E, each held within ±0.10°     interface control
                  longitude and ±0.10° inclination   and acceptance
                  box.                               testing.

  Mission         Seven years nominal service after  Parts screening,
  duration        six-month transfer and             redundancy, spares
                  commissioning; ten-year design     and operations
                  life.                              staffing.

  Unit mass       ≤1150 kg as delivered or at        Launch capacity,
                  launch, including the budgeted     structure,
                  contents.                          separation hardware
                                                     and qualification
                                                     loads.

  Payload         ≤180 kg, with definitions          Launch capacity,
  allocation      controlled by the mass table.      structure,
                                                     separation hardware
                                                     and qualification
                                                     loads.

  Power           5400 W at specified reference;     Generation,
  generation /    nominal 3200 W and peak 4700 W.    storage, power
  provision                                          distribution,
                                                     thermal rejection
                                                     and eclipse margin.

  Primary         Deliver ≥2.0 Gb/s aggregate usable Parts screening,
  measurement     service per spacecraft across      redundancy, spares
                  eight beams, ≥99.5% scheduled      and operations
                  monthly network availability in    staffing.
                  each declared service region, and  
                  authenticated control of every     
                  protected user session.            

  Instrument 1    180 kg hosted communications       Recorder capacity,
                  allocation including               RF equipment,
                  channelization and authentication; ground contacts and
                  eight 125 MHz channels with 250    archive processing.
                  Mb/s usable throughput each.       

  Instrument 2    Two deployable reflectors per      Detector
                  spacecraft; eight steerable spot   performance,
                  beams with ≥0.2° commandable       calibration,
                  beam-centre placement accuracy     metrology and
                  after calibration.                 end-to-end
                                                     verification.

  Instrument 3    Two isolated security processors   Flight hardware
                  per spacecraft; 256-bit symmetric  allocation,
                  session key material; key rotation interface control
                  ≤24 h and immediate authenticated  and acceptance
                  revocation capability.             testing.

  Pointing or     Dual star trackers, four reaction  Flight hardware
  positioning     wheels, Sun sensors and thrusters; allocation,
                  antenna boresight knowledge ≤0.05° interface control
                  (95th percentile); longitude and   and acceptance
                  inclination each within ±0.10°.    testing.

  Mission-data    18 GB/day per spacecraft of        Launch capacity,
  volume          encrypted network logs and         structure,
                  housekeeping; user traffic is      separation hardware
                  relayed rather than archived       and qualification
                  onboard                            loads.
  ----------------------------------------------------------------------

  : Table 2 -- Selected System Requirements

## High-Level Mission Architecture

The architecture separates oversight, space or deployed hardware, launch
or delivery, ground services, operations and science or user
exploitation.

Avranel Space Communications Directorate owns system requirements,
procurement, risk and mission acceptance.

Qelvoria Orbital Systems owns the integrated unit, interfaces and
system-level verification.

Sorevex Signal Engineering delivers the measurement equipment and
calibration evidence.

Lundrith Launch Consortium delivers the unit to its destination and
verifies interface conditions.

Pervalin Gateway Services supplies receiving, networking and
ground-service capacity.

Tervalis Network Operations Institute produces, validates and archives
the calibrated mission products.

# Space Segment Description

The reference configuration is three geostationary relay satellites. Its
operational environment is Three geostationary slots at nominal
longitudes 40°, 160° and 280°E, each held within ±0.10° longitude and
±0.10° inclination box. The nominal duration is Seven years nominal
service after six-month transfer and commissioning; ten-year design
life. The flight or installed unit is sized at 1150 kg and uses 5400 W
power generation or host allocation as stated in the subsystem budget.
The segment boundary includes the integrated unit and its
mission-specific payload, interfaces, spares and verification articles.

## Spacecraft Bus

The integrated unit provides structural restraint, power, command and
data handling, thermal protection, equipment control and the
communication interface appropriate to Three geostationary slots at
nominal longitudes 40°, 160° and 280°E, each held within ±0.10°
longitude and ±0.10° inclination box. The design shall carry
configuration identifiers and independent acceptance records for every
delivered unit.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary allocation / target**
  ------------------------ -------------------------------------------
  Unit mass                1150 kg

  Mass composition         420 kg dry bus + 180 kg communications
                           payload + 550 kg bipropellant = 1,150 kg

  Payload / experiment     180 kg
  allocation               

  Generation / provision   5400 W reference

  Nominal / peak demand    3200 W / 4700 W

  Storage                  256 GB usable

  Autonomy                 ≥72 h safe configuration with applicable
                           external power

  Maneuver / mobility      ≥1,850 m/s orbit raising and station
                           keeping; 550 kg storable bipropellant at
                           320 s yields \~2,040 m/s ideal at 1,150 kg
                           initial mass

  Delivery                 Three separate launches; each 1,150 kg
                           spacecraft + 150 kg adaptor = 1,300 kg to
                           GTO, with service capability ≥1,500 kg per
                           launch

  Design life              Seven years nominal service after six-month
                           transfer and commissioning; ten-year design
                           life.
  --------------------------------------------------------------------

### Structural Subsystem

The structural design is sized for 1150 kg delivery mass and the
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

Nominal allocation: 5400 W generation or host provision, 3200 W
operating demand, 4700 W short-duration peak. These values describe
distinct operating cases. The system power margin is assessed at the
worst insolation, eclipse or host-service case, not by comparing only
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
  5400 W baseline         Regulated bus,          3200 W nominal / 4700 W
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

A mission-data model checks the 18 GB/day per spacecraft of encrypted
network logs and housekeeping; user traffic is relayed rather than
archived onboard planning case against memory capacity, contact
availability and the required processing latency. Raw records are
retained until integrity checks and ingest acknowledgement complete.

### Thermal Subsystem

Geostationary eclipse hot/cold cases; payload electronics maintained
5--40 °C; 2.8 m² radiator area reference with payload heat rejection
sized to ≥2.3 kW.

The thermal design shall close with numerical hot and cold cases and
shall separately report radiator, insulation, heater and sensor
allocations. Instrument calibration is repeated across the qualified
operating temperature range. Safe-mode heating and peak-mode waste heat
are independently assessed.

Thermal verification considers heat from 4700 W peak electrical input,
the nominal 3200 W mode, external heat flux, enclosure conduction and
the passive or active rejection path. The final instrument uncertainty
budget includes temperature-driven bias and gradients.

The thermal test programme shall establish:

steady and transient operating limits of each component;

heater and cooler demand in cold and hot cases;

radiator or host heat-rejection sizing;

calibration stability across the qualified temperature range; and

safe survival during a commanded outage.

### Attitude Determination and Control Subsystem

Dual star trackers, four reaction wheels, Sun sensors and thrusters;
antenna boresight knowledge ≤0.05° (95th percentile); longitude and
inclination each within ±0.10°.

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

550 kg storable bipropellant at 320 s effective Isp provides \~2,040 m/s
ideal Δv; 1,850 m/s allocation leaves \~190 m/s before performance and
residual allowances.

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

  Initial unit mass       1150                    kg

  Reference performance   ≥1,850 m/s orbit        m/s or N/A
                          raising and station     
                          keeping; 550 kg         
                          storable bipropellant   
                          at 320 s yields \~2,040 
                          m/s ideal at 1,150 kg   
                          initial mass            

  Fuel / propellant       550 kg storable         kg / description
  allocation              bipropellant at 320 s   
                          effective Isp provides  
                          \~2,040 m/s ideal Δv    

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

  Operational maintenance  GTO-to-geostationary transfer followed by
                           seven-year longitude/inclination control;
                           three slots separated by about 120°.

  Navigation and           ≥1,850 m/s orbit raising and station
  correction               keeping; 550 kg storable bipropellant at
                           320 s yields \~2,040 m/s ideal at 1,150 kg
                           initial mass

  Contingency and          Explicit reserve controlled in Part B /
  residuals                Part C

  Total capability         Reconcile with 550 kg storable bipropellant
                           at 320 s effective Isp provides \~2,040 m/s
                           ideal Δv; 1,850 m/s all
  --------------------------------------------------------------------

### Telemetry, Tracking and Command

Each of eight beams carries 125 MHz × 2.0 net bit/s/Hz = 250 Mb/s; eight
beams yield 2.0 Gb/s usable per spacecraft after coding allocation.
Gateway capacity is separately sized.

The final link assessment shall include transmitter power, antenna gain
or host data-service rate, geometry, coding, weather where relevant and
a minimum allocated margin. Distinguish command/control packets, health
telemetry, raw measurements and user or science products. A link outage
analysis is required before ground-service capacity is baselined.

The communications baseline includes Ka-class user links with eight 125
MHz beams at 250 Mb/s usable throughput each; 20/30 GHz class reference
frequencies subject to assignment. The contact budget carries
acquisition, engineering telemetry, protocol framing, retransmission and
unavailable weather or host periods. The sizing check compares usable
transferred bytes per contact with 18 GB/day per spacecraft of encrypted
network logs and housekeeping; user traffic is relayed rather than
archived onboard and any higher burst case.

A separate low-rate command path or host maintenance interface shall
support diagnosis after the prime mission-data path becomes unavailable.
No unauthenticated measurement data can alter safety-critical command
parameters.

## Payload

The payload or process equipment is divided into protected digital
communications payload, steerable multi-beam antenna assembly and
cryptographic command boundary. Each element has a separate delivered
mass, operating load, mode list, failure assessment and calibration
requirement.

### Protected digital communications payload

180 kg hosted communications allocation including channelization and
authentication; eight 125 MHz channels with 250 Mb/s usable throughput
each.

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
  Primary function         Protected digital communications payload

  Measured performance     180 kg hosted communications allocation
                           including channelization and
                           authentication; eight 125 MHz channels with
                           250 Mb/s usable throughput each.

  Unit-level calibration   Before integration and after environmental
                           qualification

  Electrical interface     Protected distribution and commanded safe
                           state

  Data interface           Time-tagged raw records plus status and
                           quality flags

  Environmental tolerance  Geostationary eclipse hot/cold cases;
                           payload electronics maintained 5--40 °C;
                           2.8 m² radiator area reference with payload
                           heat rejection sized to ≥2.3 kW.

  Mass accounting          Within 180 kg payload or experiment
                           allocation

  Verification             Test against mission-level success
                           criterion

  Operations mode          Only when power, thermal and link margins
                           permit

  Fault response           Isolate and report without affecting
                           safe-mode command
  --------------------------------------------------------------------

### Steerable multi-beam antenna assembly

Two deployable reflectors per spacecraft; eight steerable spot beams
with ≥0.2° commandable beam-centre placement accuracy after calibration.

This measurement or process provides an independent check on the primary
result. The ground model shall retain geometric, thermal and
instrumental uncertainty, including changes caused by the spacecraft or
host.

For Virelan Protected Communications System, complementarity is
intentional: one channel measures a different physical quantity or
provides a contextual state. Processing shall preserve the raw evidence,
identify retrieval assumptions and reject inconsistent cross-calibration
before product release.

  --------------------------------------------------------------------
  **Parameter**            **Preliminary requirement / target**
  ------------------------ -------------------------------------------
  Function                 Steerable multi-beam antenna assembly

  Performance              Two deployable reflectors per spacecraft;
                           eight steerable spot beams with ≥0.2°
                           commandable beam-centre placement accuracy
                           after calibration.

  Mass                     Included in payload/experiment allocation

  Power                    Mode specific; close against peak load

  Field / process geometry Three geostationary slots at nominal
                           longitudes 40°, 160° and 280°E, each held
                           within ±0.10° longitude and ±0.10°
                           inclination box.

  Timing                   Synchronized to system command clock

  Calibration              At acceptance and by scheduled in-operation
                           reference

  Data volume              18 GB/day per spacecraft of encrypted
                           network logs and housekeeping; user traffic
                           is relayed rather than archived onboard

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

  Sensor interfaces        Protected digital communications payload;
                           Steerable multi-beam antenna assembly;
                           Cryptographic command boundary

  System interface         Protected command and local data bus

  Buffering                256 GB usable system allocation

  Processing               Lossless event flags and reversible
                           screening where practical

  Timing                   Absolute reference and monotonically
                           numbered records

  Health monitoring        Voltage, temperature, current, reset count
                           and status

  Mass                     Within 180 kg allocation

  Peak electrical power    Included in 4700 W integrated peak

  Radiation / environment  Qualified for Three geostationary slots at
                           nominal longitudes 40°, 160° and 280°E,
                           each h
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

  Primary reference        Cryptographic command boundary

  Frequency                At commissioning, after anomaly and on a
                           scheduled monthly cadence

  Environmental dependency Geostationary eclipse hot/cold cases;
                           payload electronics maintained 5--40 °C;
                           2.8 m² radiator area reference with payload
                           heat rejection sized to ≥2.3 kW.

  Long-term drift          Trend against accepted reference and flag
                           \>2% unexplained change

  Data linkage             100% released products identify applicable
                           calibration version

  Independent verification Recheck with Steerable multi-beam antenna
                           assembly

  Instrument monitoring    On each operating cycle

  Mass / power             Within payload and system allocations
  --------------------------------------------------------------------

![Figure 2 -- Payload measurement and data path. Components and output
interfaces are explicitly labeled.](media/image6.png){width="6.4in"
height="1.8529407261592301in"}

# Launch Segment Description

Three separate launches; each 1,150 kg spacecraft + 150 kg adaptor =
1,300 kg to GTO, with service capability ≥1,500 kg per launch

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

Three protected gateways plus one backup gateway; ≥7 Gb/s aggregate
terrestrial backhaul; dual network-control sites; 150 TB audit/archive
capacity.

Each of eight beams carries 125 MHz × 2.0 net bit/s/Hz = 250 Mb/s; eight
beams yield 2.0 Gb/s usable per spacecraft after coding allocation.
Gateway capacity is separately sized.

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

  Receiving Stations /     Three protected gateways plus one backup
  Host Link                gateway; ≥7 Gb/s aggregate terrestrial
                           backhaul; dual network-control sites; 150
                           TB audit/archive capacity.

  Operations Team          Staffed planned operations with automated
                           alarm and on-call response.

  Processing and Archive   Level 0 packet retention; Level 1
                           calibration; Level 2 products with
                           preserved lineage.

  Data Volume /            18 GB/day per spacecraft of encrypted
  Availability             network logs and housekeeping; user traffic
                           is relayed rather than archived onboard;
                           scheduled ground service availability ≥99%.
  --------------------------------------------------------------------

The daily return is 18 GB/day per spacecraft of encrypted network logs
and housekeeping; user traffic is relayed rather than archived onboard.
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
files, algorithm version and exceptions. Capacity in Three protected
gateways plus one backup gateway; ≥7 Gb/s aggregate terrestrial
backhaul; dual network-control sites; 150 TB audit/archive capacity. is
a planning provision that shall be verified against years of operation,
replication and reprocessing.

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

The schedule planning basis is B 14 months; C 12 months; D1 18 months;
D2 10 months; three launches and six-month commissioning; E 84 months.
Activities with long-lead procurement and parallel unit builds overlap;
durations should not be arithmetically summed to infer a delivery date.

  ----------------------------------------------------------------------------------------
  **Phase**   **0**      **A**      **B**      **C**      **D1**     **D2**     **E**
  ----------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
  Duration,   TBD        TBD        14         12         18         10         84
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

  D1             EVT           Payload qualification           Apr 2031

  D1             EVT           FM-1 complete                   Sep 2031

  D1             EVT           FM-3 complete                   Mar 2032

  D2             SIR           System Integration Review       May 2032

  D2             AR            Acceptance                      Sep 2032

  D2             LRR           Launch / Delivery Readiness     Nov 2032
                               Review                          

  D2             L1--L3        Launch sequence                 Jan 2033

  E              EVT           Commissioning                   Jul 2033

  E              EVT           Nominal end                     Jul 2040
  --------------------------------------------------------------------------

  : Table 5 -- Major Milestones

## Safety and Mission Assurance

The project applies controlled requirements, hazard analysis,
independent quality oversight, parts and materials screening,
nonconformance disposition, serialized configuration and documented
readiness reviews. Hazards include stored energy, fluid containment,
high voltage, radiation, moving mechanisms, thermal surfaces and
potential loss of user service as applicable.

For Virelan Protected Communications System, the initial risk
concentration is Spectrum coordination, reflector deployment, key
management and recovery, radiation-induced processor upset, high-duty
payload thermal rejection and common-mode ground software.
Safety-related controls receive independent verification; mission
success and medical or food-use claims require separate acceptance
evidence.

## Prototyping Model Philosophy Qualification and Verification Strategy

The reference model philosophy comprises an electrical integration
article, engineering or breadboard articles for novel functions, a
structural/thermal qualification article and 3 flight or delivered
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
exposure. Principal threats: Spectrum coordination, reflector
deployment, key management and recovery, radiation-induced processor
upset, high-duty payload thermal rejection and common-mode ground
software. Each has an owner, trigger, planned mitigation and residual
exposure. Design reserves on mass, power, data and propellant or
consumables are reported separately from financial contingency.

## Organizational Breakdown Structure

### Space Agencies and Government Organizations

  ----------------------------------------------------------------------------
  **Partner**           **Jurisdiction**   **Proposed role**
  --------------------- ------------------ -----------------------------------
  Avranel Space         Mission            mission authority, procurement,
  Communications        jurisdiction       project assurance and acceptance.
  Directorate                              

  ----------------------------------------------------------------------------

  : Table 6 -- Mission Organizations

### Industrial Partners

  -----------------------------------------------------------------------
  **Partner**           **Domain**    **Proposed role**
  --------------------- ------------- -----------------------------------
  Qelvoria Orbital      Mission       integrated unit design, manufacture
  Systems               supply chain  and system verification.

  Sorevex Signal        Mission       payload/process equipment and
  Engineering           supply chain  acceptance calibration.

  Lundrith Launch       Mission       delivery, campaign operations and
  Consortium            supply chain  associated interfaces.

  Pervalin Gateway      Mission       ground network, receiving
  Services              supply chain  interfaces and operations support.
  -----------------------------------------------------------------------

  : Table 7 -- Industrial Partners

### Participating Academic Institutions

  -----------------------------------------------------------------------
  **Institution**       **Domain**    **Proposed contribution**
  --------------------- ------------- -----------------------------------
  Tervalis Network      Science       science or user requirements,
  Operations Institute  consortium    calibration, data validation and
                                      exploitation.

  -----------------------------------------------------------------------

  : Table 8 -- Research Institutions

### Scientific Leadership (Principal Investigator)

  ----------------------------------------------------------------------
  **Position**          **Assigned      **Affiliation**
                        individual**    
  --------------------- --------------- --------------------------------
  Principal             Tavren Elovar   Tervalis Network Operations
  investigator                          Institute

  Instrument scientist  Mirev Solanar   Sorevex Signal Engineering
  ----------------------------------------------------------------------

  : Table 9 -- Scientific Leadership
