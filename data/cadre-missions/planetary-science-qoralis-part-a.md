<!-- PDF page 1 -->

Qoralis Interior and Surface Explorer (QISE) -
CADRe Part A
# Office of Mission Cost Analysis (OMCA)
Cost Analysis Data Requirements (CADRe)
PART A
Mission : Qoralis Interior and Surface Explorer
Design Reference : EDA
Key Decision Point : CDR
EPMO Gate : Gate-R3
Draft 1.0 (Integrated mission architecture baseline)
September 22, 2026

---

<!-- PDF page 2 -->

This Page Intentionally Left Blank

---

<!-- PDF page 3 -->

REVISION HISTORY
Rev. Description Prepared by Date
Draft 1.0 Initial synthesized mission baseline Avery Chen 22 Sept 2026

---

<!-- PDF page 4 -->

This Page Intentionally Left Blank

---

<!-- PDF page 5 -->

Table of Contents
1 INTRODUCTION....................................................................................................................7
1.1 PURPOSE OF THIS DOCUMENT.............................................................................................................................7
1.2 PURPOSE AND SCOPE OF MISSION........................................................................................................................7
2 GENERAL DESCRIPTIVE INFORMATION.......................................................................................9
2.1 MISSION OVERVIEW..........................................................................................................................................9
2.2 CONTEXT.......................................................................................................................................................11
2.3 STRATEGIC OBJECTIVES....................................................................................................................................12
2.4 SELECTED MISSION REQUIREMENTS...................................................................................................................12
2.5 HIGH-LEVEL MISSION ARCHITECTURE.................................................................................................................14
3 SPACE SEGMENT DESCRIPTION...............................................................................................16
3.1 SPACECRAFT BUS............................................................................................................................................16
3.2 PAYLOAD.......................................................................................................................................................24
4 LAUNCH SEGMENT DESCRIPTION............................................................................................28
5 GROUND SEGMENT AND MISSION OPERATIONS........................................................................29
6 SYSTEMS ENGINEERING AND PROJECT MANAGEMENT APPROACH..................................................30
6.1 TRL LEVELS AND HERITAGE..............................................................................................................................30
6.2 PHASING LOGIC AND NAMING CONVENTIONS......................................................................................................30
6.3 NSEO PROJECT MILESTONES............................................................................................................................31
6.4 SAFETY AND MISSION ASSURANCE.....................................................................................................................32
6.5 QUALIFICATION AND ACCEPTANCE STRATEGY, MODEL PHILOSOPHY........................................................................32
6.6 RISK ASSESSMENT...........................................................................................................................................33
6.7 ORGANIZATIONAL BREAKDOWN STRUCTURE........................................................................................................33
APPENDICES..............................................................................................................................35
A ACRONYM LIST....................................................................................................................................................36

---

<!-- PDF page 6 -->

LIST OF FIGURES
FIGURE PAGE
FIGURE 1 – QISE MISSION CONCEPT.......................................................................................................................10
FIGURE 2 – NOTIONAL QISE POWER-SYSTEM ARCHITECTURE..........................................................................19
FIGURE 3 – NOTIONAL QISE ADCS COMPONENTS................................................................................................23
FIGURE 4 – LAUNCH CONFIGURATION............................................................................................................28
FIGURE 5 – GROUND MISSION NETWORK......................................................................................................29
LIST OF TABLES
TABLE 1 – STRATEGIC ALIGNMENT..........................................................................................................................12
TABLE 2 – SELECTED MISSION REQUIREMENTS...................................................................................................12
TABLE 3 – PRELIMINARY QISE SPACECRAFT ALLOCATION AND REFERENCE DATA.......................................18
TABLE 4 – NSEO PROJECT MILESTONES................................................................................................................31

---

<!-- PDF page 7 -->

A-7
1 INTRODUCTION
1.1 PURPOSE OF THIS DOCUMENT
CADRe Part A provides a concise, standardized synopsis of the mission or project to support
costing and analysis activities. Its primary purpose is to consolidate technical, programmatic,
operational, and schedule information into a single normalized reference.
Specifically, CADRe Part A:
 Summarizes key mission characteristics in a consistent and structured format
 Aggregates information from the QISE mission concept, preliminary requirements,
architecture, schedule, and procurement assumptions
 Reduces the need for analysts to repeatedly consult disparate source material when
constructing cost and risk estimates
 Ensures a common baseline description is used across cost, schedule, technical, and risk
analyses
 Improves traceability between quantitative mission drivers and downstream cost-
estimating assumptions
In practical terms, CADRe Part A functions as a time-saving reference document that enables
analysts to understand the mission without re-interpreting the architecture or reconciling
multiple preliminary sources.
1.2 PURPOSE AND SCOPE OF MISSION
Qoralis Interior and Surface Explorer (QISE) is a fictitious deep-space planetary science mission
intended to determine the internal structure, shallow subsurface properties, and surface
thermal behaviour of Qoralis, a synthesized 410 km-diameter icy dwarf body in the outer solar
system. The mission is sponsored, owned, and operated by the National Space Exploration
Office (NSEO), with scientific direction from the fictitious Planetary Geophysics Directorate
(PGD).
QISE responds to a defined science need: determine whether Qoralis contains a mechanically
distinct interior layer or long-lived subsurface liquid reservoir, quantify the thickness and
dielectric properties of the upper 5 km of crust, and establish the relationship between surface
fractures and internal heat transport.
The mission uses two coordinated spacecraft with deliberately different functions: an Orbiter
(QO-1) performs global geophysics and remote sensing from a polar orbit, while a Surface
Geophysics Lander (QS-1) performs local seismic, thermal, and near-surface measurements.
The two-spacecraft architecture separates global orbital measurements from long-duration
surface measurements while retaining a common mission operations and data system.
The project is entirely synthesized for cost-analysis purposes. No existing spacecraft, launch
vehicle, instrument, company, government agency, or previously flown mission is assumed as
the technical baseline. Generic engineering practices are used only to make the architecture
internally consistent; all organization names, spacecraft names, target-body properties,
performance allocations, and program dates in this CADRe are fictional.

---

<!-- PDF page 8 -->

A-8

---

<!-- PDF page 9 -->

A-9
2 GENERAL DESCRIPTIVE INFORMATION
2.1 MISSION OVERVIEW
The Qoralis Interior and Surface Explorer (QISE) is a proposed two-spacecraft deep-space
mission designed to characterize the interior and surface of the fictional icy body Qoralis.
Qoralis is defined for the QISE reference case as a 410 km mean-diameter body with a bulk
density of 1.25 g/cm³, a nominal rotation period of 19.6 hours, and a heliocentric orbit with a
semi-major axis of 3.35 AU and eccentricity of 0.07. The reference body model is synthetic and
exists only to provide stable mission-analysis inputs.
The QISE spacecraft will travel together during cruise and separate approximately 45 days
before target arrival. QO-1 will enter a 100 × 1,500 km polar elliptical science orbit around
Qoralis; QS-1 will perform a controlled descent to a surface landing site between 65°S and 70°S
latitude selected for high fracture density and communications visibility.
The mission's broad science objectives include:
 Global gravity-field mapping and determination of mass distribution;
 Measurement of surface topography and long-wavelength shape;
 Detection and characterization of subsurface dielectric interfaces to a depth of at least 5
km;
 Measurement of local seismic activity and elastic-wave propagation;
 Mapping of thermal anomalies with a target sensitivity of 0.8 K at the instrument level;
and
 Correlation of orbital observations with long-duration surface measurements.
The system consists of one orbital geophysics spacecraft, one surface geophysics lander, a
combined launch service, government and contractor-provided ground infrastructure, mission-
control and planning systems, deep-space communications, science-data processing and
archive capability, and associated project-management, assurance, and sustainment activities.

---

<!-- PDF page 10 -->

A-10
FIGURE 1 – QISE MISSION CONCEPT

---

<!-- PDF page 11 -->

A-11
2.2 CONTEXT
The QISE concept is not derived from a named real mission. Its programmatic context is a
notional national planetary-science initiative requiring a flight system capable of operating
beyond 3 AU with a surface asset and an independently navigable orbiter.
The target body is intentionally defined as a fictional object so that the cost baseline is not
constrained by an existing mission design, real spacecraft heritage, or commercial provider. The
synthetic environment nevertheless imposes realistic engineering drivers: approximately 4.2
years of cruise, low solar flux, a 7.5-year total program duration from launch through nominal
disposal, deep-space communications, radiation exposure, autonomous fault management, and
a precision landing sequence.
 QISE retains no procurement baseline from real industry responses. The reference
organizations used in this CADRe are fictitious: Heliox Orbital Systems for the orbiter
bus, Cinderline Surface Systems for the lander, Blue Meridian Instruments for the
science payloads, Quarry Mission Data for the ground system, and Vantor Launch
Services for the launch service.
 The QISE CADRe baseline in this document is the controlling Part A reference for the
cost estimate. Any change to the target-body model, spacecraft architecture, transfer
trajectory, payload allocation, schedule, or organizational baseline shall be reconciled
across the later CADRe products.
 Reference Industry Responses – Not QISE Procurement Baseline
 Reference supplier / configuration observations are intentionally generic and fictional.
They are retained only as placeholders for cost-estimating structure and do not
represent actual supplier quotations.
 mission assurance and long-duration spacecraft operations are not inherited from any
real mission; all QISE architecture and program assumptions are synthetic.
 No external mission is treated as a technical or cost analogue. Quantitative values are
generated from the QISE reference-body model and internal mission trades.

---

<!-- PDF page 12 -->

A-12
Reference Industry Responses – Not QISE Procurement Baseline
Prime Architecture Bus / Element Payload /
Role
Heliox Orbital
Systems
2 spacecraft QO-1 orbital bus Orbiter
avionics
integration
Cinderline Surface
Systems
1 lander QS-1 surface bus Landing and
surface
systems
Blue Meridian
Instruments
Orbiter + lander
payloads
Instrument
packages
Radar,
thermal,
seismic
Quarry Mission Data Ground segment Mission data
infrastructure
Processing /
archive /
comms
integration
Vantor Launch
Services
Launch service Combined launch
stack
Launch and
separation
### 2.3 STRATEGIC OBJECTIVES
Consistent with the NSEO Exploration Strategy, QISE is intended to obtain quantitative
geophysical measurements of Qoralis that cannot be obtained from Earth-based observations
alone, establish a traceable relationship between orbital and surface datasets, and demonstrate
autonomous deep-space operations for a multi-spacecraft planetary mission.
TABLE 1 – STRATEGIC ALIGNMENT
Strategic Goals Exploration Strategy
1 MEASURE QISE will establish quantitative measurements of the interior, subsurface,
and surface thermal state of the fictional body Qoralis, linking orbital and
surface observations.
### 2.4 SELECTED MISSION REQUIREMENTS
The following table consolidates the quantitative mission parameters that are significant drivers
of QISE cost, schedule, risk, and technical complexity. Values are a preliminary estimating
baseline; unresolved items are intended to close through the design reviews identified in
Section 6.

---

<!-- PDF page 13 -->

A-13
TABLE 2 – SELECTED MISSION REQUIREMENTS
Area Key requirement
Target body
Synthetic 410 km-diameter icy body; reference density 1.25 g/cm³ and
rotation period 19.6 h.
Cruise
Launch-to-arrival planning duration of approximately 4.2 years; trajectory
correction campaign allocated 360 m/s.
Orbiter orbit
QO-1 polar elliptical science orbit of 100 × 1,500 km around Qoralis; final
orbit insertion profile TBD by navigation analysis.
Lander landing
QS-1 shall land within a designated 20 km × 20 km science ellipse with
terminal horizontal velocity ≤1.5 m/s.
Mission duration
Nominal science operations of 24 months after commissioning; total
launch-to-disposal mission duration approximately 7.5 years.
Combined launch
mass
≤1,460 kg including flight hardware, propellant, adapter allocation and
growth margin.
QO-1 mass ≤720 kg at launch; preliminary target 650 kg including propellant.
QS-1 mass
≤430 kg at separation; preliminary target 400 kg including landing
propellant.
Payload mass QO-1 payload ≤95 kg; QS-1 payload ≤42 kg.
QO-1 power
≥1.05 kW end-of-life solar generation at 3.35 AU; ≥25% continuous power
margin.
QS-1 power ≥180 W end-of-life surface generation; ≥30% survival-mode margin.
Radar sounding
8–20 MHz operating band; minimum investigation depth 5 km; nominal
vertical resolution ≤50 m.
Thermal mapping
7–14 μm band; instrument NETD ≤0.15 K at 250 K; ≤250 m ground
sampling at reference orbit.
Seismic
measurement
Broadband surface seismometer with timing accuracy ≤1 ms and
continuous nominal sampling.
Altimetry
QO-1 laser altimeter range precision ≤0.5 m for 1 km–1,500 km slant range
under reference conditions.
Pointing
QO-1 absolute pointing error ≤0.015° during radar mapping; ≤0.03° during
thermal mapping.
Orbit knowledge
QO-1 3-sigma position knowledge target ≤250 m during nominal science
operations.

---

<!-- PDF page 14 -->

A-14
Area Key requirement
Onboard storage QO-1 ≥512 GB usable; QS-1 ≥128 GB usable non-volatile storage.
Science data Planning case of 8 GB/day QO-1 and 1.2 GB/day QS-1 before compression.
Downlink
Ka-band science downlink target ≥2 Mbps peak with ≥3 dB end-to-end link
margin.
Priority latency
Priority science products available within 72 hours of receipt by the ground
segment.
Autonomy
QO-1 ≥24 h autonomous operation; QS-1 ≥72 h autonomous surface
operation.
Ground
availability
Deep-space ground system ≥98% availability during scheduled
communications periods.
Navigation
Radiometric plus optical navigation; final arrival solution shall close before
first science orbit.
Reliability
Preliminary 7.5-year mission-success probability target ≥0.75 for cost/risk
analysis.
Mass margin ≥15% nominal mass margin at system preliminary design baseline.
Power margin
≥25% QO-1 nominal continuous margin and ≥30% QS-1 survival-mode
margin.
Technology
readiness
Major bus components TRL ≥8 before qualification; critical payload
technologies TRL ≥5 at B2 start and ≥7 before spacecraft-level
qualification.
Landing readiness
Landing system shall complete a representative end-to-end descent
rehearsal before launch.
End of life QO-1 shall be placed in a non-interfering disposal orbit or controlled
trajectory; QS-1 remains on the surface after completion.
### 2.5 HIGH-LEVEL MISSION ARCHITECTURE
Owned and operated by NSEO, in collaboration with the Planetary Geophysics Directorate, the
mission consists of:
 A Program Segment: NSEO project management, systems engineering, science
management, mission assurance, configuration control, mission planning, and
government technical authority.

---

<!-- PDF page 15 -->

A-15
 A Space Segment: one orbital spacecraft (QO-1) and one surface geophysics lander
(QS-1), launched as a combined stack and separated before target arrival.
 A Launch Segment: a commercial launch service procured for the combined QISE stack;
Vantor Launch Services is the current fictional launch-service organization in the baseline.
 A Ground Segment: contractor-provided deep-space communications, navigation
support, mission planning, command, science-data processing, calibration, archive, and
secure distribution. Quarry Mission Data provides and integrates these elements.
 An Operations Segment: NSEO mission operators supported by contractor flight-dynamics
and engineering teams. Nominal operations require 16-hour daily staffed coverage with
on-call anomaly response outside staffed periods.
 A Science Segment: the PGD science team and fictional university laboratories supporting
instrument calibration, geophysical inversion, landing-site analysis, data validation, and
scientific exploitation.

---

<!-- PDF page 16 -->

A-16
3 SPACE SEGMENT DESCRIPTION
The space segment consists of 2 spacecraft: one orbiter and one surface geophysics lander,
each with a dedicated bus and payload complement.
### 3.1 SPACECRAFT BUS
The QISE spacecraft bus architecture provides the structural, electrical, thermal, computational,
communications, attitude-control, navigation, and propulsion functions required for a 3.35 AU-
class heliocentric cruise and subsequent operations around Qoralis. The orbiter and lander use
different mechanical and thermal configurations but share a common command/data protocol,
time system, fault-management philosophy, and ground interface.
The orbiter and lander are intentionally not identical. QO-1 is optimized for low-propellant
orbital operations, precision pointing, high-rate science downlink, and global mapping. QS-1 is
optimized for entry/descent/landing survivability, surface stability, thermal endurance, and
continuous low-rate geophysical measurements. A single Engineering Qualification Unit (EQU) is
used for the highest-risk common avionics and communications interfaces; each flight vehicle
then undergoes independent acceptance.
Key functions of the spacecraft buses include:
 Structural subsystem
 Electrical power generation and distribution
 Command and Data Handling (C&DH)
 Thermal subsystem
 Attitude Determination and Control System (ADCS)
 Propulsion and navigation subsystem
 Telemetry, Tracking and Command (TT&C)
All component examples in this section are fictional notional hardware used only for first-order
costing. No real spacecraft, instrument, or commercial product is treated as QISE flight heritage.

---

<!-- PDF page 17 -->

A-17
3.1.1 Structural Subsystem
The QO-1 primary structure uses a machined aluminum-lithium frame with carbon-fibre
instrument decks and local titanium fittings. QS-1 uses a low-centre-of-gravity landing frame
with crushable load paths and four deployable landing legs. Structural sizing shall demonstrate
a minimum 1.25 ultimate factor on limit loads and a first-mode frequency above 28 Hz for the
integrated launch configuration.

---

<!-- PDF page 18 -->

A-18
The preliminary structure allocation is 92 kg for QO-1 and 68 kg for QS-1, including primary
structure, secondary panels, fasteners, launch restraints, landing hardware, and 20% design
mass margin at the applicable baseline.
Parameter Preliminary QISE allocation / target
QO-1 launch mass ≤720 kg; target 650 kg
QS-1 separation mass ≤430 kg; target 400 kg
Combined flight-system mass ≤1,150 kg before launch adapter; target ~1,050 kg
Launch-stack allocation ≤1,460 kg including adapter and growth margin
QO-1 payload allocation ≤95 kg
QS-1 payload allocation ≤42 kg
QO-1 usable science storage ≥512 GB
QS-1 usable science storage ≥128 GB
QO-1 pointing ≤0.015° radar / ≤0.03° thermal
QS-1 landing ellipse 20 km × 20 km
QO-1 total ΔV 780 m/s preliminary budget
QS-1 total ΔV 420 m/s preliminary budget
QO-1 EOL power ≥1.05 kW at 3.35 AU
QS-1 EOL power ≥180 W surface generation
Qoralis reference orbit 100 × 1,500 km polar science orbit
3.1.2 The electrical-power systems shall close the end-of-life power budget with
at least 25% continuous power margin for QO-1 cruise/science modes and
at least 30% margin for QS-1 surface survival mode. The design shall
account for solar-distance degradation, battery ageing, heater duty cycle,
communications loads, instrument duty cycle, and peak landing loads.
Solar Array Panels
- QO-1 will use two body-deployed solar wings sized for operation at 3.35 AU. Preliminary
array area is 38 m² with an end-of-life generation target of 1.05 kW at the reference
heliocentric distance. QS-1 will use a 5.5 m² fixed deployable array with a 180 W end-of-
life target during the surface science phase.
- End-of-life power generation shall be sufficient to meet the verified mission power
budget with the specified design margin. Solar-cell degradation is preliminarily allocated
at 3.0% per year for QO-1 and 2.0% per year for QS-1 after landing.

---

<!-- PDF page 19 -->

A-19
- The power system shall be sized for deep-space communications, thermal control,
instrument operation, battery recharge, avionics, propulsion valves, and landing-event
peak loads.
Battery
- QO-1 uses a 2.4 kWh lithium-ion battery with a preliminary 80% usable-depth-of-
discharge limit. QS-1 uses a 0.9 kWh battery sized for 18 hours of surface survival
without solar input. Final capacities are TBD pending thermal and power-budget closure.
- Power Control Unit
The power-control and distribution architecture shall provide regulated power, protection, load
shedding, telemetry, and autonomous load management. Peak bus voltage is nominally 50 VDC
on QO-1 and 28 VDC on QS-1.
- The power-control and distribution architecture shall provide regulated power,
protection, telemetry, load shedding, and autonomous load management for all
spacecraft and payload functions.
QO-1 Solar Wings
38 m² reference area
QO-1 Power Control Unit
50 V regulated bus
Battery Pack
2.4 kWh usable allocation
FIGURE 2 – NOTIONAL SPACECRAFT POWER-SYSTEM EXAMPLES
3.1.3 The Command and Data Handling (C&DH) subsystem provides central
computing, timekeeping, fault management, data storage, instrument
control, and communications-interface functions for each spacecraft.
The C&DH subsystem will:
Receive and execute time-tagged commands;
Collect and compress engineering telemetry;
 Control payload interfaces and instrument modes;
 Manage onboard science-data storage;
 Execute fault-detection, isolation, and recovery;
 Maintain spacecraft configuration and software versions;
 Support autonomous operation during communication outages; and
 Maintain synchronized mission time across QO-1 and QS-1.
 QO-1 shall provide ≥512 GB usable non-volatile science storage; QS-1 shall provide ≥128
GB, for 640 GB combined.
 Fault Management

---

<!-- PDF page 20 -->

A-20
 The C&DH architecture will provide watchdogs, health monitoring, fault isolation, safe-
mode entry, redundant-unit selection, autonomous load shedding, command validation,
and recovery after loss of ground contact.
 Data Management
 The C&DH subsystem will buffer radar, thermal, altimetry, seismic, and surface-
monitoring data before transmission. Design inputs include generation rate,
compression, storage, communication windows, priority data, and round-trip latency.
Because the two spacecraft will operate as a coordinated constellation, configuration and
software management shall ensure that both spacecraft remain compatible with the common
mission architecture, software baseline, time reference, operational procedures, and mission-
planning interfaces.
#### 3.1.4 Thermal Control Subsystem
The Thermal Control Subsystem will maintain spacecraft and payload components within
qualified temperature limits throughout cruise, Qoralis orbit operations, and the surface phase.
Thermal design is dominated by low solar flux, long eclipse periods around the target, internal
heater loads, and the need to keep the radar electronics and surface seismometer within stable
operating ranges.
Thermal analysis will therefore consider:
Solar radiation
 Planetary/body infrared radiation
 Albedo
 Eclipse duration
 Orbital position
 Spacecraft attitude
 Instrument dissipation
 Communications equipment
 Battery temperature
 Propulsion components
 Lander surface-contact thermal conductance
 The thermal architecture will use passive thermal-control techniques wherever
practical. Potential components include multi-layer insulation, optical coatings,
radiators, thermal straps, heat pipes, heaters, thermostats, and temperature sensors.
Thermal Analysis

---

<!-- PDF page 21 -->

A-21
The spacecraft will undergo hot-case and cold-case thermal analyses for cruise, target arrival,
orbital operations, and the surface phase. The analysis will establish component temperature
ranges, heater requirements, radiator sizing, thermal gradients, instrument stability, battery
limits, and landing-leg thermal constraints.
Cost Drivers
 Thermal-system cost will be affected by payload heat dissipation, radiator area, heater
power, thermal stability requirements, low-flux environmental analysis, instrument duty
cycle, and environmental testing duration.
#### 3.1.5 Attitude Determination & Control
QO-1 coarse attitude determination will use sun sensors and rate gyros; fine attitude
determination will use two star trackers. Three-axis control will use four reaction wheels with
magnetic torquers for momentum management during cruise and target operations.
 QS-1 uses redundant inertial measurement units, sun sensors, and a radar altimeter
during descent. After landing, attitude knowledge is established from inertial sensors
and horizon/solar observations; active attitude control is limited to controlled
instrument pointing and lander health management.
 QO-1 absolute pointing accuracy target is ≤0.015° during radar mapping and ≤0.03°
during thermal imaging. QS-1 instrument deck pointing knowledge shall be ≤1.0° after
landing.
 Orbit determination for QO-1 will use optical navigation observations plus radiometric
tracking. A preliminary 3-sigma position-knowledge target of ≤250 m at Qoralis is
retained for science operations.
 Orbit Determination
 QO-1 orbit determination shall combine two-way range, Doppler, onboard time, and
optical landmark measurements. The final navigation filter shall close before the first
science orbit.
 Navigation sensors
QO-1 will carry a star tracker pair, sun sensors, inertial measurement unit, and optical
navigation camera. QS-1 will use an inertial measurement unit, descent radar, and redundant
altimeter channels during landing.
 Control actuators
 QO-1 will use four reaction wheels and redundant hydrazine-equivalent fictional
monopropellant thrusters; QS-1 will use twelve landing/descent thrusters arranged in
four functional clusters.
Star tracker Sun sensor
Inertial measurement unit Reaction wheel

---

<!-- PDF page 22 -->

A-22
Optical navigation camera Magnetorquer
Laser altimeter Descent radar / altimeter
#### 3.1.6 Propulsion subsystem
QISE propulsion is sized for a 4.2-year cruise correction campaign, QO-1 orbit insertion and
shaping, and QS-1 descent and landing. The preliminary propellant budget includes 20%
contingency.
Parameter QO-1
Value
QS-1
Valu
e
Propellant Type Fictio
nal
high-
densit
y
mono
prope
llant
Ficti
onal
stora
ble
mon
opro
pella
nt
Vacuum Specific Impulse (Isp) 228 s 225 s
Nominal Thrust 22 N 18 N
Tank capacity 185
kg
96 kg
kg 20%
Propulsion System Characteristics
Item Value
Cruise correction 360 m/s
Qoralis orbit insertion /
shaping
290 m/s
Station keeping 70 m/s
Disposal contingency 60 m/s
Required QO-1 ΔV 780 m/s
QS-1 descent / landing
reserve
420 m/s
Notes
 QO-1 total mission delta-V is 780 m/s, including 360 m/s cruise correction, 290 m/s
target orbit insertion and shaping, 70 m/s station keeping, and 60 m/s disposal

---

<!-- PDF page 23 -->

A-23
contingency. QS-1 requires 420 m/s for deorbit, descent, terminal hazard avoidance,
and landing reserve.
 QO-1 trajectory corrections are designed from the synthetic Qoralis reference orbit; no
real-body station-keeping or launch-window heritage is assumed.
FIGURE 3 – NOTIONAL ADCS AND PROPULSION COMPONENTS
#### 3.1.7 TT&C
The Telemetry, Tracking and Command subsystem shall provide command, telemetry,
navigation tracking, time synchronization, and science-data communications over the
interplanetary cruise and Qoralis operational phases.
o QO-1 uses an electrically steered high-gain antenna with a 1.6 m aperture and a
redundant low-gain antenna pair. QS-1 uses a fixed 0.55 m patch/reflector
assembly for surface-to-orbiter relay and a low-gain antenna for direct
emergency communications.
 Reference deep-space communications parameters
o Ka-band science downlink peak target: ≥2 Mbps at 3.35 AU equivalent range,
with adaptive coding and an end-to-end link margin target of ≥3 dB.
o X-band command/telemetry link: 8 kbps minimum command rate and 32 kbps
minimum engineering telemetry rate under nominal cruise geometry.
 QO-1 shall provide at least 4 hours/day of scheduled communications
opportunity during nominal target operations. QS-1 shall maintain at
least 6 relay contacts per Qoralis rotation, each ≥12 minutes, during the
nominal surface phase.
 Ground communications are assumed to use three fictional deep-space
antenna sites operated under a common service contract; final antenna
count and allocation are to be closed by the link budget.
o A pair of low-gain antennas on QO-1 provide broad coverage during safe mode.
The high-gain antenna is used for science-data transmission and precision
radiometric tracking.
 The QISE data link budget shall be reconciled with the science-data generation case of
approximately 8 GB/day for QO-1 and 1.2 GB/day for QS-1 before compression.

---

<!-- PDF page 24 -->

A-24
3.2 PAYLOAD
Source: QISE synthesized mission architecture and fictional instrument trade study
Each payload complement consists of:
- A low-frequency radar sounder
- A thermal-infrared radiometer
- A laser altimeter / optical navigation package
- A surface geophysical instrument suite including a broadband seismometer and heat-
flow package
#### 3.2.1 Radar Sounder
The radar sounder provides the primary subsurface-observation capability for QISE. It transmits
chirped RF pulses toward Qoralis and measures returned echoes to identify dielectric
interfaces, buried fractures, and layer boundaries.
The preliminary radar operates at 8–20 MHz with 100 kHz–2 MHz selectable chirps. Target
vertical resolution is ≤50 m in low-loss ice and ≤150 m in high-loss material; reference orbital
swath is ~120 km.
Synthetic reference radar instrument
Parameter Synthetic Radar Reference
Frequency range 8–20 MHz
Chirp bandwidth 100 kHz–2 MHz
Vertical resolution ≤50 m nominal; ≤150 m high-loss case
Investigation depth ≥5 km target
Mass 34 kg
Average power 95 W
Peak transmit
power
180 W

---

<!-- PDF page 25 -->

A-25
Antenna Dual deployable nadir-facing panels
Data rate Up to 6 Mbps raw; compressed science
stream TBD
Operating mode Global mapping / targeted fracture transects
Qualification Flight qualification required
The fictional radar has a preliminary mass of 34 kg, average power of 95 W, and peak transmit
power of 180 W. Final antenna geometry and thermal design remain subject to payload trade.
The final radar architecture shall close the 5 km investigation-depth target, ≤50 m nominal
vertical resolution, pointing, electromagnetic compatibility, mass, power, and data-rate
constraints.
3.2.2 The thermal-infrared radiometer measures surface-temperature gradients
and localized thermal anomalies associated with internal heat flow.
The radiometer covers a synthetic 7–14 μm band with ≤0.15 K NETD at 250 K and ≤250 m
ground sampling from the reference science orbit.
The fictional radiometer has a preliminary mass of 18 kg, average power of 42 W, and peak
power of 60 W; calibration uses an onboard reference and deep-space views.
Parameter Preliminary QISE Requirement / Target
Spectral range 7–14 μm
Detector
technology
Fictional cooled microbolometer array
NETD ≤0.15 K at 250 K
Ground sampling ≤250 m at reference orbit
Field of view 4.0° cross-track
Frame rate 1–10 Hz selectable
Interface QO-1 payload-data interface
Mass 18 kg

---

<!-- PDF page 26 -->

A-26
Power
consumption
42 W average / 60 W peak
Data rate ≤1.5 Mbps after onboard selection
Qualification Flight qualification required
3.2.3 Payload electronics interface the instruments with spacecraft C&DH and
provide control, readout, timing, formatting, compression, buffering, health
monitoring, and science-packet transfer.
Parameter Preliminary QISE Requirement / Target
Primary function Instrument control and science-data handling
Detector interface Instrument dependent
Spacecraft interface C&DH payload-data interface
Data processing Formatting, compression and event selection
Data buffering Required; ≥32 GB dedicated payload buffer on
QO-1
Timing ≤1 ms synchronization for surface geophysics data
Health monitoring Required
Mass ≤12 kg QO-1 payload electronics; ≤8 kg QS-1
Power consumption ≤35 W QO-1 average; ≤20 W QS-1 average
Data throughput ≥10 Mbps internal payload interface
Radiation tolerance Suitable for 3.35 AU cruise and Qoralis orbit
#### 3.2.4 Onboard Calibration and Timing
The payload complement includes internal calibration references and mission time transfer to
maintain traceability between orbiter and lander datasets.
Radar receiver/timing calibration occurs at least once per 24 h science cycle; radiometer
reference observations every 48 h; the lander seismometer time-tag accuracy is ≤1 ms.
Parameter Preliminary QISE Requirement / Target
Calibration type Radiometric, geometric, timing and navigation
Radar calibration Internal receiver/timing calibration every 24 h science
cycle

---

<!-- PDF page 27 -->

A-27
Thermal calibration Reference observations every 48 h
Seismometer calibration Instrument self-test every 7 days; ≤1 ms time-base
verification
Altimeter calibration Deep-space / target-body reference observations
before mapping
Calibration frequency Mode-dependent; minimum frequencies above
Instrument monitoring Required
Long-term degradation monitoring Required
Ground-processing interface Calibration metadata incorporated into product
generation
Mass Included in instrument allocations
4 LAUNCH SEGMENT DESCRIPTION
The preliminary combined QISE launch-stack mass is 1,460 kg, including 1,050 kg flight
hardware, 170 kg propellant, 90 kg launch adapter and separation hardware, and 150 kg
allocation for mass growth and late configuration margin. Final launch-vehicle sizing shall use
verified flight mass properties plus the launch provider's required performance margin.
The QISE orbiter and lander will be launched as a single combined stack on a fictional
commercial launch service and injected onto the reference heliocentric transfer. Vantor Launch
Services is the current fictional launch-service organization in the baseline; final launch-vehicle
selection remains subject to trajectory, fairing, separation, performance, and schedule analysis.
Launch insurance, if purchased, shall be treated as a separate cost element. The reference
estimate shall also separate launch-site processing, range services, spacecraft transportation,
and mission-specific separation hardware.

---

<!-- PDF page 28 -->

A-28
FIGURE 4 – QISE LAUNCH CONFIGURATION
Alternate fictional launch services may be considered if required by availability, injection
energy, schedule, cost, or technical compatibility.
- The launch-service down-select shall preserve compatibility with the 1,460 kg combined
stack, 4.8 m-class fairing envelope, launch-site environmental constraints, spacecraft
separation interfaces, and the required heliocentric injection energy.
- The launch campaign is planned to begin after flight hardware acceptance and shall be
completed within 7 months. The baseline launch-readiness date is 1 February 2031.
- Launch preparation shall include transportation, launch-site inspection, final functional
checks, battery conditioning, software configuration verification, propellant servicing if
applicable, integrated stack testing, and readiness reviews.
- Post-launch operations shall transition into a 30-day early-cruise checkout followed by
long-duration cruise operations and scheduled trajectory-correction campaigns.

---

<!-- PDF page 29 -->

A-29
5 GROUND SEGMENT AND MISSION OPERATIONS
The proposed baseline solution is for NSEO to provide mission authority and flight operations
while Quarry Mission Data provides and integrates the deep-space communications interfaces,
mission planning tools, navigation support, science-data processing, calibration pipelines,
archive, and secure dissemination.
Ground Segment
Element
Description
Mission Planning
System
Generates time-tagged spacecraft and instrument sequences using
ephemeris, power, thermal, communications, navigation and
science constraints.
Spacecraft Control
System
Command, telemetry, health monitoring, software configuration
and autonomous-sequence management for QO-1 and QS-1.
Deep-Space Receiving
Stations
Three fictional antenna sites supporting command, telemetry,
radiometric tracking and Ka-band science-data reception.
Flight Dynamics Trajectory determination, orbit propagation, target-body
navigation, manoeuvre design and landing-event support.
Data Processing,
Archiving and
Dissemination
Science packets are reconstructed, calibrated, quality-checked,
archived and distributed to authorized NSEO/PGD users.
Data Volume /
Availability
Planning case 9.2 GB/day combined; processing ≥100 GB/day;
scheduled ground availability ≥98%.
FIGURE 5 – QISE GROUND MISSION NETWORK
At a nominal combined science-data generation rate of 9.2 GB/day, a 30-day communication
outage would generate up to 276 GB before compression and prioritization. A preliminary 1 TB
mission archive per spacecraft therefore provides more than 3.6 times the 30-day
uncompressed outage volume for QO-1 and QS-1 combined.
The current planning case is 8 GB/day from QO-1 and 1.2 GB/day from QS-1. Ground processing
is sized at ≥100 GB/day of raw-equivalent science-data processing capacity to support
reprocessing, calibration, navigation updates, and product generation. Priority science products
shall be available within 72 hours of receipt.

---

<!-- PDF page 30 -->

A-30
6 SYSTEMS ENGINEERING AND PROJECT MANAGEMENT
APPROACH
6.1 QISE WILL USE HERITAGE EVIDENCE WHERE APPLICABLE, BUT THE
FINALIZED BASELINE IS NOT ASSUMED TO INHERIT THE TRL OF ANY
REFERENCE SPACECRAFT OR INSTRUMENT. MAJOR SPACECRAFT-BUS
COMPONENTS ARE TARGETED TO REACH TRL ≥8 BEFORE FLIGHT
QUALIFICATION. CRITICAL PAYLOAD TECHNOLOGIES SHOULD BE AT
LEAST TRL 5 AT THE START OF B2 DEVELOPMENT AND TRL ≥7 BEFORE
THE START OF SPACECRAFT-LEVEL QUALIFICATION. ANY REUSED TEST
EVIDENCE MUST BE DEMONSTRATED APPLICABLE TO THE QISE
CONFIGURATION, ENVIRONMENT, INTERFACES, AND OPERATING
ASSUMPTIONS.
6.2 PHASING LOGIC AND NAMING CONVENTIONS
For the QISE cost baseline, the PM nomenclature is B1, B2, C, D, E, and F. The nominal schedule
is: B1 = 13 months (September 2026–October 2027); B2 = 9 months (October 2027–July 2028);
C = 12 months (July 2028–July 2029); D = 19 months (July 2029–February 2031, including
manufacturing, integration, test, launch and commissioning); E = 30 months (April 2031–
October 2033, including the 4.2-year cruise that began after launch is treated within D/E
transition assumptions); F = approximately 2 months for disposal/close-out. For cost modelling,
the total program window from B1 start through nominal science completion is 85 months,
followed by a separate approximately 2-month Phase F close-out period.
PREP 1 Prototyping Activities (before Gate 1)
PREP 2 Prototyping Activities (during Phase 0/A)
Phase 0 Concept & Feasibility Studies
Phase A System Definition
Phase B Preliminary Design
Phase C Detailed Design
MAIT Manufacturing, Assembly, Integration and Test (of Systems, Subsystems
and Components)
SAIT Segment Level Assembly, Integration and Test
LEOP Launch and Early Operations (including deployment and commissioning)
Phase E Cruise and Nominal Science Operations
Phase X Extended Science Operations

---

<!-- PDF page 31 -->

A-31
Phase F Decommissioning and disposal
### 6.3 NSEO PROJECT MILESTONES
The finalized PM schedule is the nominal baseline for this CADRe Part A. It establishes payload,
orbiter, lander, and launch milestones used to determine NSEO need dates and is consistent
with the current QISE phase-duration and PM scenario baseline.
Instrument
/ PM Phase
Gate /
Milest
one
Major Milestone Milestone Date
B1 MCR Mission Concept Review 29 March 2027
B1 CA Contract Award 1 October 2027
B2 PAY-
PDR
Payload Preliminary Design Review 1 April 2028
B2 BUS-
PDR
Bus Preliminary Design Review 1 July 2028
B2 PDR Overall Preliminary Design Review 1 July 2028
C PAY-
CDR
Payload Critical Design Review 1 January 2029
C BUS-
CDR
Bus Critical Design Review 1 April 2029
C CDR Overall Critical Design Review 1 April 2029
D MRR Manufacturing Readiness Review 1 June 2029
D LT-
READ
Y
Long-Lead Hardware Ready 1 October 2029
D FLATS
AT
Integrated Avionics Flatsat Test 1 February 2030
D FH Flight Hardware Complete 1 September 2030
D ETRR Environmental Test Readiness Review 1 October 2030
D AR/
SAR
Acceptance Review 1 December 2030
D LRR Launch Readiness Review / Flight Stack
Complete
1 January 2031
D L Launch 1 February 2031
D ECO Early Cruise Checkout Complete 1 March 2031

---

<!-- PDF page 32 -->

A-32
Instrument
/ PM Phase
Gate /
Milest
one
Major Milestone Milestone Date
D ARR Arrival Readiness Review 1 November 2034
D OI QO-1 Orbit Insertion 1 December 2034
D LAND QS-1 Surface Landing 19 December 2034
E SCI-
START
Nominal Science Operations Start 1 January 2035
E EOM End of Nominal Science Operations 1 January 2037
F EOL Phase F disposal / close-out end 1 March 2037
6.4 SAFETY AND MISSION ASSURANCE
Initial assessment: Mission Class B. The program requires formal mission assurance,
qualification, acceptance, verification, configuration control, navigation validation, landing
readiness reviews, and independent science-data quality checks. Safety and mission-assurance
effort is a direct cost and schedule driver because QO-1 and QS-1 have different environmental
and operational verification profiles.
6.5 QUALIFICATION AND ACCEPTANCE STRATEGY, MODEL PHILOSOPHY
The QISE qualification and acceptance strategy will verify that QO-1 and QS-1 are capable of
surviving launch and performing their required functions throughout cruise, target operations,
and the planned surface mission. The approach uses one Engineering Qualification Unit for
common avionics and communications interfaces, followed by two flight vehicles with
independent acceptance verification.
The qualification unit will represent the flight avionics and communications configuration as
closely as practical and will undergo functional, vibration, thermal-vacuum, electromagnetic
compatibility, radiation-screening, and end-to-end command/data testing. The landing
subsystem will also use a dedicated structural/landing test article for descent and touchdown
verification. Existing qualification evidence may be reused only where the QISE configuration
and environment are demonstrated equivalent.
Following successful qualification, QO-1 and QS-1 will be manufactured using the controlled
design baseline. Each flight vehicle will undergo its own functional, electrical, communications,
software, payload, and applicable environmental acceptance testing. QS-1 will additionally
complete a representative landing-sequence rehearsal and surface deployment test.
The qualification and acceptance program also accounts for the logistics of a multi-year deep-
space mission. The two flight vehicles will be integrated as a launch stack, transported under

---

<!-- PDF page 33 -->

A-33
controlled environmental conditions, tested at the launch site, and maintained in a controlled
configuration through final readiness activities. Cruise support will include scheduled trajectory-
correction windows and independent command-load validation.
Following launch, the combined stack will undergo a 30-day early-cruise checkout. Target-
arrival operations begin approximately 45 days before Qoralis encounter. QO-1 orbit insertion
and QS-1 landing will be separated by approximately 18 days to allow navigation and health
assessments between critical events.
All qualification and acceptance results will be documented through the QISE verification and
configuration-management process. Any anomaly identified during testing, transportation,
launch-site processing, cruise, arrival, or commissioning will be assessed and resolved or
dispositioned before the affected mission phase proceeds. Final approval for launch and science
operations will be based on completion of required verification and successful Launch
Readiness, Arrival Readiness, and Operations Readiness Reviews.
6.6 THE CURRENT QISE PROGRAM RISK REGISTER AND RISK BREAKDOWN
STRUCTURE ARE THE CONTROLLING PROGRAMMATIC RISK
REFERENCES. COST AND SCHEDULE RISKS OF PARTICULAR
IMPORTANCE TO PART A ARE LONG-LEAD AVIONICS AND RADAR
DEVELOPMENT, PAYLOAD-TO-BUS ELECTROMAGNETIC COMPATIBILITY,
DEEP-SPACE COMMUNICATIONS PERFORMANCE, TRAJECTORY
CORRECTION REQUIREMENTS, PRECISION LANDING, TARGET-BODY
NAVIGATION UNCERTAINTY, THERMAL-CONTROL PERFORMANCE,
RADIATION EXPOSURE, GROUND-NETWORK AVAILABILITY, AND
EXTENDED CRUISE STAFFING.
The project team shall produce a risk register (ref CADRe Part C).
6.7 ORGANIZATIONAL BREAKDOWN STRUCTURE
NSEO Project Team: mission authority and program manager; responsible for systems
engineering, payload authority, program management, mission integration, mission planning,
mission assurance, and government flight operations.
 PGD: principal science authority and operational science user; provides measurement
priorities, geophysical models, calibration requirements, and science-product
acceptance criteria.
 Payload: Blue Meridian Instruments; payload electronics and instrument integration:
Heliox Orbital Systems / Cinderline Surface Systems as applicable.
 Radar and thermal instruments: Blue Meridian Instruments.
 Orbiter bus: Heliox Orbital Systems, selected fictional spacecraft contractor.
 Ground segment: Quarry Mission Data, responsible for provision and integration of the
deep-space communications interfaces, mission-planning tools, navigation support,
processing, and archive.

---

<!-- PDF page 34 -->

A-34
 Launch: Vantor Launch Services. Surface lander: Cinderline Surface Systems. Science
Segment: fictional university laboratories contracted through PGD. No international
mission partner is assumed in the baseline.

---

<!-- PDF page 35 -->

A-35
APPENDICES

---

<!-- PDF page 36 -->

A-36
A ACRONYM LIST
Acronym Definition
CADRe Cost Analysis Data Requirement
NSEO National Space Exploration Office
PGD Planetary Geophysics Directorate
QISE Qoralis Interior and Surface Explorer
QO-1 Qoralis Orbiter 1
QS-1 Qoralis Surface Geophysics Lander 1
C&DH Command and Data Handling
ADCS Attitude Determination and Control System
TT&C Telemetry, Tracking and Command
MPS Mission Planning System
SCS Spacecraft Control System
MCR Mission Concept Review
PDR Preliminary Design Review
CDR Critical Design Review
MRR Manufacturing Readiness Review
ETRR Environmental Test Readiness Review
AR/SAR Acceptance Review / System Acceptance Review
LRR Launch Readiness Review
ARR Arrival Readiness Review
LEOP Launch and Early Operations Phase
MAIT Manufacturing, Assembly, Integration and Test
SAIT Spacecraft/Segment Assembly, Integration and Test
TRL Technology Readiness Level
EQU Engineering Qualification Unit
FM Flight Model
NETD Noise-Equivalent Temperature Difference
GSD Ground Sample Distance
ΔV Change in velocity

---

<!-- PDF page 37 -->

A-37

---

<!-- PDF page 38 -->

A-38
