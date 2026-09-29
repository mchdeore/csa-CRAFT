Office of Mission Cost Analysis

Cost Analysis Data Requirements (CADRe)

PART A

Mission: Myralis Dust Field Observatory

Design Reference: Preliminary integrated baseline

Key Decision Point: CDR

Project Gate: R3

Draft 1.0 \| 22 September 2026

This document describes one entirely synthesized mission, including its
organizations, spacecraft and data.

# Revision History

  -----------------------------------------------------------------------
  **Rev.**          **Description**   **Prepared by**   **Date**
  ----------------- ----------------- ----------------- -----------------
  Draft 1.0         Initial           Mission Analysis  22 Sept 2026
                    integrated        Office            
                    architecture and                    
                    cost-analysis                       
                    baseline                            

  -----------------------------------------------------------------------

# Table of Contents

1 Introduction

1.1 Purpose of this document

1.2 Purpose and scope of mission

2 General Descriptive Information

2.1 Mission Overview

2.2 Context

2.3 Strategic Objectives

2.4 Selected Mission Requirements

2.5 High-Level Mission Architecture

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

6.5 Qualification and Acceptance Strategy, Model Philosophy

6.6 Risk Assessment

6.7 Organizational Breakdown Structure

Appendices

A Acronym List

# List of Figures

Figure 1 -- Myralis mission concept and reference heliocentric geometry

Figure 2 -- Spacecraft power architecture and budget

Figure 3 -- Attitude control and observation modes

Figure 4 -- Three spacecraft launch configuration

Figure 5 -- Ground mission network and data flow

# List of Tables

Table 1 -- Strategic Alignment

Table 2 -- Selected Mission Requirements

Table 3 -- Preliminary Spacecraft Allocation and Reference Data

Table 4 -- Project Milestones

# 1 Introduction

## 1.1 Purpose of this document

CADRe Part A provides a standardized mission synopsis for cost
estimating. It brings the mission objectives, technical allocations,
operating concept, schedule and organizational responsibilities into a
single reference baseline. Quantities below are preliminary requirements
or estimating assumptions as marked; detailed design and verification
will refine them.

Specifically, CADRe Part A:

- summarizes the mission architecture and cost-driving quantities;

- collects technical and programmatic assumptions in one controlled
  record;

- sets common definitions for spacecraft, launch, ground and operations
  scope;

- identifies quantities to reconcile with schedule, risk and procurement
  records; and

- preserves a traceable starting point for independent cost analysis.

This Part A is a concept-level cost input. The corresponding Part B
technical parameter register, Part C schedule and risk baseline, and
Part D procurement record must carry the same controlled quantities
before an estimate is approved.

## 1.2 Purpose and scope of mission

The Myralis Dust Field Observatory (MDFO) measures the spatial and
temporal distribution of micrometre to millimetre particles across an
inner heliocentric annulus. Three identical spacecraft, D1--D3, leave
one launch vehicle and drift onto separated solar orbits. Each records
local impacts and optical dust brightness; time-correlated measurements
constrain a three-dimensional dust-density model. The reference science
region spans 0.97--1.03 astronomical units (AU), with useful spacecraft
separation of 0.04--0.20 AU after deployment.

The mission seeks to determine dust flux by size and direction, identify
transient dust enhancements, and produce a calibrated environmental
model for vehicle shielding and long-range mission planning. It does not
assume imaging of a celestial surface, landing, sampling, or a relay
satellite. The sponsor and owner is the Avelune Space Directorate (ASD),
with scientific leadership from the Ruvellan Data Institute (RDI).

# 2 General Descriptive Information

## 2.1 Mission Overview

MDFO comprises three 210 kg-class flight spacecraft launched together.
Differential separation impulses create modestly different heliocentric
periods. A daily spacecraft science return of 0.75 GB (2.25 GB for the
constellation) supports event counts, spectra, photometry and
housekeeping. A common flight design reduces recurring manufacture and
qualification effort. A five-year nominal science phase begins after a
six-month cruise and commissioning period.

The measurement strategy combines local impact counting with
line-of-sight optical photometry. Correlation of measurements at
multiple orbital longitudes constrains regional density changes;
individual dust grains are not tracked between spacecraft. A
simultaneous viewing window of at least 12 hours per week is planned
when geometry permits. Ground inversion is responsible for separating
dust brightness from background stars and stray light.

![Figure 1 -- Reference heliocentric geometry. Radial separation is
exaggerated; rings show the analysis region, not fixed operational
orbits; D1--D3 drift independently after
separation.](media/image1.png){width="6.6in"
height="4.153362860892388in"}

## 2.2 Context

Dust impact flux varies with particle size, heliocentric distance and
orbital direction. Single-point counts cannot distinguish local
enhancements from a spatial gradient without additional assumptions.
Three separated measurement stations improve the conditioning of the
inversion and provide spatially distributed evidence over a five-year
interval. The architecture trades larger flight-unit count and
deep-space communication capacity against a single-point observatory.

No existing supplier or instrument configuration is presumed. The
concept baseline includes one common bus, one common payload suite per
spacecraft, a three-unit launch dispenser, three ground antenna sites,
an operations center, an archive and five years of science processing.

## 2.3 Strategic Objectives

  -----------------------------------------------------------------------
  **Objective**           **Quantified outcome**  **Measurement basis**
  ----------------------- ----------------------- -----------------------
  Characterize dust       Flux from 10⁻¹³ to 10⁻⁶ Impact charge and
  environment             kg particles in ≥8      momentum proxies
                          logarithmic mass bins   

  Resolve heliocentric    Map 0.97--1.03 AU with  Distributed local
  gradients               ≤0.01 AU radial grid    counts + photometry
                          spacing where coverage  
                          supports it             

  Detect temporal change  Identify ≥30% flux      Time-binned event
                          changes sustained for   series
                          ≥48 h at 95% confidence 
                          in a defined count-rate 
                          regime                  

  Deliver reference       Monthly Level 2 flux    Calibrated archive and
  products                maps within 30 days of  inversion pipeline
                          month end               
  -----------------------------------------------------------------------

  : Table 1 -- Strategic Alignment

## 2.4 Selected Mission Requirements

The values below define the preliminary estimating baseline.
Requirements apply to each spacecraft unless stated otherwise.
Sensitivity and confidence claims are conditional on a minimum of 100
valid impacts in the relevant comparison bin; low-count regimes will
carry Poisson confidence intervals rather than a blanket detection
guarantee.

  -----------------------------------------------------------------------
  **Area**                            **Key requirement**
  ----------------------------------- -----------------------------------
  Flight architecture                 Three near-identical independent
                                      spacecraft; one launch and
                                      sequential separation.

  Science region                      Heliocentric radius 0.97--1.03 AU;
                                      operational solar elongation
                                      40°--140° for photometry.

  Nominal life                        Five years of science after
                                      six-month cruise/commissioning;
                                      propellant and reliability sized to
                                      six years after launch.

  Spacecraft mass                     ≤210 kg launch mass per flight
                                      unit; three-unit launch stack ≤790
                                      kg including 160 kg
                                      dispenser/adaptor allowance.

  Impact measurement                  10⁻¹³--10⁻⁶ kg particles; ≥0.10 m²
                                      effective sensitive area; dead time
                                      ≤2 ms per accepted event.

  Flux dynamic range                  10⁻⁶ to 10² impacts m⁻² s⁻¹ with
                                      selectable event threshold and
                                      saturation flagging.

  Optical photometry                  Three bands centered at 0.48, 0.72
                                      and 1.05 µm; ≥20° field; ≤1%
                                      relative repeatability for
                                      calibrated brightness \>100 nW m⁻²
                                      sr⁻¹.

  Pointing and knowledge              ≤0.20° absolute pointing error and
                                      ≤0.05° knowledge for photometric
                                      scans (95th percentile).

  Orbit knowledge                     ≤20 km position uncertainty (3σ)
                                      for science geolocation after
                                      ground solution.

  Autonomy                            ≥96 h safe-mode operation without a
                                      ground contact; ≥7 days autonomous
                                      stored-data retention.

  Storage                             ≥64 GB usable nonvolatile storage
                                      per spacecraft, with error
                                      correction.

  Data volume                         0.75 GB/day per spacecraft average;
                                      1.5 GB/day per spacecraft
                                      95th-percentile planning case.

  Communications                      X-band ≥2 Mb/s user data rate at
                                      1.5 AU range to 12 m-class antenna
                                      at ≥3 dB link margin; S-band
                                      command ≥2 kb/s.

  Science latency                     Priority event packet delivered ≤24
                                      h after ground receipt; routine L1
                                      ≤7 days; L2 ≤30 days.

  Power                               780 W end-of-life generation at 1
                                      AU; nominal science demand ≤410 W;
                                      maximum simultaneous peak ≤625 W.

  Thermal                             Bus avionics 0--40 °C operating;
                                      impact electronics −10--45 °C;
                                      detector surfaces calibrated over
                                      −20--50 °C.

  Reliability                         ≥0.80 probability of ≥2 functional
                                      spacecraft at end of year five, to
                                      be validated by reliability
                                      analysis.

  Ground capacity                     Three 12 m-class antenna sites; 15
                                      GB/day raw ingest capability; 120
                                      TB managed archive.

  Disposal                            Commanded passivation at end of
                                      operations; no Earth re-entry or
                                      planetary impact in the reference
                                      case.
  -----------------------------------------------------------------------

  : Table 2 -- Selected Mission Requirements

## 2.5 High-Level Mission Architecture

- Government Segment: ASD owns mission requirements, systems
  engineering, procurement, project controls and mission acceptance.

- Space Segment: D1, D2 and D3 share a bus and each carries an impact
  detector, a three-band photometer and a plasma/context package.

- Launch Segment: one launch, a three-port dispenser, sequential
  deployment and injection into a heliocentric transfer.

- Ground Segment: three geographically separated antennas, a
  mission-control center, flight dynamics, processing and archive.

- Operations Segment: one staffed daily operations shift with 24-hour
  automated monitoring and on-call anomaly response.

- Science Segment: RDI maintains the calibration/inversion pipeline and
  releases controlled Level 1 and Level 2 products.

# 3 Space Segment Description

The space segment consists of three flight units with common hardware
and software baselines. Each unit is independently power positive and
commandable after separation. Table 3 distinguishes mass allocations
from performance targets; the flight design must close against both.

## 3.1 Spacecraft Bus

  -----------------------------------------------------------------------
  **Parameter**                       **Per spacecraft allocation /
                                      target**
  ----------------------------------- -----------------------------------
  Dry bus including structure,        104 kg
  avionics, ADCS, propulsion hardware 

  Payload suite including electronics 38 kg
  and accommodation                   

  Propellant and pressurant           24 kg

  Harness, thermal and mechanical     14 kg
  provisions                          

  Allocated mass subtotal             180 kg

  Unallocated system mass reserve     30 kg (16.7% of allocated subtotal)

  Maximum launch mass                 210 kg

  Usable mission-data storage         64 GB minimum

  Δv capacity                         ≥180 m/s, including 25%
                                      propellant/dispersion reserve

  EOL power generation at 1 AU        780 W

  Nominal / peak loads                410 W / 625 W

  Maximum commanded autonomy          96 h safe mode
  -----------------------------------------------------------------------

  : Table 3 -- Preliminary Spacecraft Allocation and Reference Data

### Structural Subsystem

A central aluminum alloy shear structure transfers 210 kg maximum flight
mass into a standard separation ring. Two hinged array wings, a fixed
impact plate and an offset optical baffle fit inside a 1.55 m × 1.35 m ×
1.65 m allocated stowed envelope. The preliminary first-mode targets are
≥25 Hz lateral and ≥40 Hz axial, subject to launch-provider
coupled-loads analysis. A spacecraft-level finite-element model controls
local instrument interface accelerations and alignment drift.

Mass properties shall be measured for each unit before shipment. The bus
is sized for 6 g quasi-static axial loading and 2 g lateral loading at
concept level; final qualification levels and factors derive from the
selected launch service. A 210 kg unit at 6 g produces approximately
12.4 kN axial inertial load before factors of safety.

### Electrical Power Subsystem

Each spacecraft carries two deployable arrays with a combined 3.0 m²
active area. The estimating case assumes 30% end-of-life cell efficiency
and 1,361 W/m² irradiance at 1 AU, giving 1,225 W ideal normal-incidence
power. A combined incidence, wiring, thermal and conversion derating of
0.637 yields 780 W at 1 AU. At 1.03 AU, available power falls to
approximately 735 W by inverse-square scaling, before battery support.
The science timeline limits sustained deep-space demand to 430 W and
prohibits the 625 W peak mode without load shedding.

A 28 V regulated bus and 1.6 kWh usable lithium-ion battery cover
deployment, brief array off-pointing and transmitter peaks. With 150 W
safe-mode load, the battery provides approximately 10.7 h before reserve
constraints. The 96 h autonomy requirement assumes solar array
generation, not battery-only survival. A 20% minimum nominal power
margin applies at the 1.03 AU operating case: 735 / 430 − 1 = 71%.

![Figure 2 -- Per-spacecraft power distribution at 1 AU. Values are
end-of-life planning allocations; mode-specific loads and distance
scaling govern operation.](media/image2.png){width="6.6in"
height="2.093898731408574in"}

### Command and Data Handling

Dual redundant flight processors execute command sequences, onboard
event filtering, safe-mode logic and time-tagged instrument operations.
A radiation-tolerant 64 GB usable storage partition includes error
detection and correction; at the 1.5 GB/day planning peak it stores more
than 42 days of science data, subject to a 15% housekeeping and
file-system allowance reducing practical retention to approximately 36
days. The seven-day retention requirement therefore has substantial
headroom.

Impact records include time to ≤100 µs UTC-equivalent accuracy after
time correlation, detector charge, event classification, spacecraft
state and quality flags. The payload data interface sustains ≥5 MB/s
during burst acquisition. Daily average 0.75 GB is 69 kb/s over 24 h;
link sizing is driven by contact duration, range and outage, not the
average rate alone.

Fault protection detects processor watchdog expiry, battery
undervoltage, uncommanded attitude rates, thermal excursions and loss of
communications. It isolates a failed device, enters a Sun-safe attitude
and retains at least 96 h of time-tagged recovery instructions. All
three spacecraft carry separately uploaded command and software
baselines.

### Thermal Subsystem

Passive coatings, multilayer insulation, radiator panels, straps and
thermostatically controlled heaters maintain the bus limits. Solar input
at 0.97 AU is 1.063 times the 1 AU value; the radiator and baffle design
is sized for a 0.97 AU hot case with a 625 W peak load of no more than
20 minutes. A 1.03 AU cold case assumes safe mode, low instrument
dissipation and reduced incident flux. Preliminary radiator allocation
is 0.65 m² per spacecraft; detailed orbital thermal analysis shall
determine the final area.

Temperature sensors are distributed across the photometer bench, impact
front end, battery, propulsion lines and array hinges. Ground
calibration shall measure photometric responsivity across −20 to 50 °C
detector temperature and shall support temperature correction in Level 1
products.

### Attitude Determination and Control Subsystem

Two star trackers, six coarse Sun sensors, one inertial measurement unit
and four reaction wheels support three-axis control. Eight cold-gas
attitude thrusters provide wheel desaturation and safe recovery. The
science attitude keeps the optical axis within 40°--140° solar
elongation and rotates the impact detector toward the expected dust ram
direction when thermal limits allow. Photometric scans require ≤0.20°
95th-percentile absolute pointing error and ≤0.05° knowledge. Wheel
jitter allocation is ≤30 arcsec rms across a 10 s exposure.

![Figure 3 -- Instrument fields and attitude modes. The arrows indicate
functional interfaces; scan, impact and downlink modes are scheduled
separately.](media/image3.png){width="6.6in"
height="2.3776870078740155in"}

### Propulsion Subsystem

A monopropellant system with four 5 N thrusters provides separation
corrections and orbit trimming. An effective specific impulse of 225 s
and 24 kg propellant at 210 kg initial mass yield ideal Δv ≈267 m/s from
the rocket equation; after 20% unusable/contingency allowance, the
usable planning capability is approximately 214 m/s. The requirement is
180 m/s, leaving 34 m/s design headroom. This calculation is a reference
sizing check, not a final performance guarantee.

  -----------------------------------------------------------------------
  **Δv use**                          **Allocation**
  ----------------------------------- -----------------------------------
  Post-separation phasing             70 m/s

  Cruise trajectory corrections       35 m/s

  Five-year orbit maintenance and     25 m/s
  geometry control                    

  Momentum management / contingencies 14 m/s

  Navigation and performance reserve  36 m/s

  Total requirement                   180 m/s
  -----------------------------------------------------------------------

Orbit dispersion and fuel use will be propagated across the three units;
none requires a target-body insertion burn. A collision-avoidance
separation analysis is required through the first 72 h after release.
Commanded passivation vents residual propellant and discharges stored
energy at end of operations.

### Telemetry, Tracking and Command

A low-gain S-band link supports contingency commanding at ≥2 kb/s. A
two-axis pointed X-band high-gain antenna supports ≥2 Mb/s user data at
1.5 AU with ≥3 dB link margin to a 12 m-class receiving station,
assuming a 20 W RF transmitter; the final link budget must establish
antenna gain, weather allowance, coding loss and ground-equipment noise
temperature. The X-band downlink is scheduled for up to 60 minutes per
spacecraft per day on average.

At 2 Mb/s, one hour provides 0.9 GB before protocol overhead; a 0.75 GB
daily return requires ≥83.3% end-to-end payload efficiency for that
contact. The 95th-percentile case of 1.5 GB requires about 100 minutes
at the same efficiency, or a higher effective rate. Antenna time, range
variation and weather outages are direct operations-cost drivers.

## 3.2 Payload

Each spacecraft carries three coordinated measurement packages: an
impact ionization detector (IID), a three-band dust-scattered-light
photometer (DSP) and a compact plasma/context sensor (PCS). A common
electronics unit applies timestamps, onboard screening and data
compression. The total payload allocation is 38 kg and 270 W peak;
instrument simultaneous use is constrained by the spacecraft power case.

### Impact Ionization Detector

An exposed 0.12 m² impact target collects plasma generated by high-speed
particle impacts. The electronics digitize charge and rise time,
classify event amplitude and reject spacecraft-generated noise. The
measurement target is 10⁻¹³--10⁻⁶ kg over calibrated impact speeds of
5--70 km/s; mass inference is model dependent and must be reported as
probability bins, not exact mass. Effective area is ≥0.10 m² for
incidence within 60° of the normal.

  -----------------------------------------------------------------------
  **Parameter**                       **Preliminary requirement**
  ----------------------------------- -----------------------------------
  Mass / operating power              14 kg / 55 W

  Geometric / effective sensitive     0.12 / ≥0.10 m²
  area                                

  Mass range                          10⁻¹³--10⁻⁶ kg, speed dependent

  Maximum accepted event rate         500 events/s with ≤2 ms dead time

  Time-tag accuracy                   ≤100 µs after correlation

  Calibration                         Charge injection daily; impact
                                      analogues before flight
  -----------------------------------------------------------------------

### Dust Scattered-Light Photometer

The DSP observes diffuse sunlight scattered by dust in three spectral
bands centered at 0.48, 0.72 and 1.05 µm, with respective full widths of
0.08, 0.10 and 0.12 µm. A 20° × 20° instantaneous field is sampled in
0.1° angular bins by controlled spacecraft scanning. A deployable baffle
constrains direct solar stray light at elongation ≥40°. The primary
product is calibrated surface brightness by band, viewing geometry and
time.

  -----------------------------------------------------------------------
  **Parameter**                       **Preliminary requirement**
  ----------------------------------- -----------------------------------
  Mass / operating power              11 kg / 95 W

  Field and sampling                  20° × 20°; ≤0.1° output angular
                                      grid

  Spectral channels                   0.48 / 0.72 / 1.05 µm centers

  Relative repeatability              ≤1% for calibrated brightness above
                                      100 nW m⁻² sr⁻¹ band-integrated
                                      radiance

  Dark / flat calibration             Daily dark frames; monthly
                                      flat-field sequence

  Stray-light verification            Ground test and in-flight off-axis
                                      scans
  -----------------------------------------------------------------------

### Plasma and Context Sensor

The PCS measures local electron density and spacecraft charging state so
impact pulse classifications can be screened against plasma background.
Two short deployable sensors sample at 1 Hz nominally and 16 Hz in event
mode. The 7 kg / 35 W allocation includes sensor booms, electronics and
deployment. Its science value is contextual; the prime mission success
criterion relies on IID and DSP data.

### Payload Electronics and Calibration

The 6 kg / 85 W payload electronics unit distributes power, enforces
science mode interlocks and formats event records. The combined payload
masses are IID 14 kg, DSP 11 kg, PCS 7 kg and electronics 6 kg = 38 kg.
Combined operating allocations total 270 W; the peak case assumes
mutually compatible modes, while prolonged combined operation at 1.03 AU
is prohibited by the power budget.

IID gain shall be characterized at multiple impact energies and
incidence angles using laboratory analogues; in-flight charge injection
tracks electronics gain but cannot replicate an actual grain impact. DSP
dark correction occurs daily and its radiometric scale is checked
against internally controlled reference illumination and repeated sky
fields. A calibration register links raw parameters to released
products; monthly trending flags drift exceeding 2% from the accepted
reference.

# 4 Launch Segment Description

The reference launch purchases a single commercial service to a
near-Earth escape transfer with characteristic energy C3 ≥2 km²/s² and a
payload capacity of at least 950 kg for the required inclination and
injection window. Three flight spacecraft contribute 630 kg and the
dispenser/adaptor allowance contributes 160 kg, producing a 790 kg
reference stack and 160 kg, or 16.8%, capacity margin against the 950 kg
service requirement. The contract shall define injection dispersions,
separation sequence and collision avoidance.

![Figure 4 -- Reference three-port launch stack. Dimensions and mass
allocations are preliminary; the launch provider verifies fit, loads and
separation clearances.](media/image4.png){width="6.1in"
height="2.33451990376203in"}

The launch campaign includes shipment, battery conditioning, propellant
safety controls, combined electrical verification, dispenser integration
and a separation-system test. Insurance, launch-service price, dispenser
nonrecurring design and launch-site support are separately identified
cost elements. A 30-day launch window is the planning assumption;
monthly window sensitivity will be assessed in the schedule risk model.

# 5 Ground Segment and Mission Operations

Three geographically separated 12 m-class antenna sites provide
scheduled X-band contacts and S-band contingency support. An assumed
daily average of 60 minutes per spacecraft requires 3 antenna-hours/day
before setup and maintenance; the 95th-percentile data case requires
approximately 5 antenna-hours/day. A site outage shall be recoverable by
rescheduling within 48 h under nominal geometry. Antenna geographic
coordinates and visibility will be fixed at ground-network procurement.

![Figure 5 -- Ground and data-processing chain. The three ground sites
feed a common control and science system; labels state planning
capacities.](media/image5.png){width="6.6in"
height="1.8484601924759405in"}

  -----------------------------------------------------------------------
  **Ground element**                  **Planning scope**
  ----------------------------------- -----------------------------------
  Mission planning and flight         Daily contact plan; weekly
  dynamics                            trajectory solution; thrust
                                      screening before each maneuver.

  Spacecraft control                  Three independently configurable
                                      flight units; one staffed shift per
                                      day and continuous automated
                                      monitoring.

  Ground receiving                    Three 12 m-class antenna sites; ≥15
                                      GB/day raw ingest capacity.

  Processing                          Level 0 packets, calibrated Level 1
                                      events/brightness, monthly Level 2
                                      flux grids.

  Archive and dissemination           120 TB managed capacity with
                                      replicated metadata and controlled
                                      release; ≤24 h priority delivery
                                      after receipt.
  -----------------------------------------------------------------------

The average combined downlink is 2.25 GB/day; five years produces
approximately 4.1 TB raw science return before housekeeping and
reprocessing. The 120 TB archive allocation covers replicated raw
packets, calibration versions, intermediate products, sensitivity runs
and metadata, a roughly 29-fold multiplier over raw science alone. This
multiplier is an estimating allocation to validate through a
data-management plan.

# 6 Systems Engineering and Project Management Approach

## 6.1 TRL Levels and Heritage

The common bus uses mature component classes, but its integrated
three-unit deep-space configuration is a new qualification baseline. The
impact front end and baffle are treated as critical development items.
Critical payload elements shall demonstrate technology readiness level
(TRL) 6 at preliminary design review and TRL 8 before flight acceptance;
bus components target TRL 8 before spacecraft environmental
qualification. Claims of heritage require part numbers, operating
envelopes and qualification records, not resemblance of function.

## 6.2 Phasing Logic and Naming Conventions

  -----------------------------------------------------------------------
  **Phase**                           **Scope / nominal duration**
  ----------------------------------- -----------------------------------
  PREP 1 / PREP 2                     Measurement simulations and
                                      detector prototypes; 6 / 6 months.

  Phase 0 / A                         Concept trades and mission
                                      definition; 8 / 10 months.

  Phase B                             Preliminary design, instrument
                                      breadboards and PDR; 14 months.

  Phase C                             Detailed design, critical tests and
                                      CDR; 12 months.

  Phase D1                            Unit-level manufacture, assembly
                                      and environmental qualification; 18
                                      months.

  Phase D2                            System integration, acceptance,
                                      dispenser fit and launch campaign;
                                      10 months.

  LEOP                                Separation and spacecraft
                                      commissioning; 1 month.

  Phase E                             Six-month cruise/commissioning
                                      total, then five-year nominal
                                      science phase.

  Phase E EXT / F / G                 Optional extension; passivation;
                                      continuing archive exploitation.
  -----------------------------------------------------------------------

Dates in Table 4 are planning milestones, not contract commitments.
Phase boundaries are set by accepted review products; the phase
durations above overlap for long-lead procurement and unit builds and
must not be summed to infer the launch date.

## 6.3 Project Milestones

  -----------------------------------------------------------------------
  **Phase**         **Gate /          **Major           **Date**
                    milestone**       milestone**       
  ----------------- ----------------- ----------------- -----------------
  0                 MCR               Mission Concept   Mar 2027
                                      Review            

  A                 SRR               System            Jan 2028
                                      Requirements      
                                      Review            

  B                 PDR               Preliminary       Mar 2029
                                      Design Review     

  C                 PL-CDR            Payload Critical  Feb 2030
                                      Design Review     

  C                 CDR               System Critical   Mar 2030
                                      Design Review     

  D1                MRR               Manufacturing     Jun 2030
                                      Readiness Review  

  D1                DET-Q             Detector          May 2031
                                      qualification     
                                      complete          

  D1                FM-1              First flight unit Oct 2031
                                      assembled         

  D1                FM-3              Third flight unit Feb 2032
                                      assembled         

  D2                SIR               System            Mar 2032
                                      Integration       
                                      Review            

  D2                ETRR              Environmental     May 2032
                                      Test Readiness    
                                      Review            

  D2                AR                Flight-unit       Sep 2032
                                      acceptance        

  D2                LRR               Launch Readiness  Nov 2032
                                      Review            

  D2                L                 Launch            Jan 2033

  LEOP              SEP               All three units   Jan 2033
                                      separated and     
                                      acquired          

  E                 CCR               Commissioning     Jul 2033
                                      Complete Review   

  E                 EOM               End nominal       Jul 2038
                                      science           
                                      operations        

  F                 EOL               Passivation       Sep 2038
                                      complete          
  -----------------------------------------------------------------------

  : Table 4 -- Project Milestones

## 6.4 Safety and Mission Assurance

The preliminary mission assurance posture requires traceable
requirements, independent quality oversight of flight hardware,
serialized configuration, formal nonconformance control, parts screening
and supplier surveillance. Launch-site propellant handling and
deployment hazards require approved procedures. The three-unit design is
assessed for common-cause failure: one defective batch, flight-software
defect or calibration error can affect all units, so unit-to-unit
similarity alone does not establish independence.

## 6.5 Qualification and Acceptance Strategy, Model Philosophy

The model set comprises one electrical integration model, one
structural/thermal qualification article for the common bus and three
flight units. The detector front end receives a separate instrument
qualification campaign with representative high-speed impact tests; the
photometer baffle is qualified for stray light and thermal distortion.
The qualification article undergoes vibration, shock, thermal-vacuum and
electromagnetic compatibility tests. Each flight unit receives
workmanship-level environmental acceptance, deployment tests, end-to-end
contact demonstrations and calibrated payload acceptance.

Flight software is exercised against all three flight-unit
configurations, including lost-contact, invalid time, low-power and
wheel-failure cases. A 30-day post-launch checkout confirms each
spacecraft independently; the remaining cruise interval establishes
geometry and photometric reference fields. Acceptance evidence is
archived by serial number and test configuration.

## 6.6 Risk Assessment

The Part C risk register controls probability, cost and schedule
exposure. The highest concept-level drivers are detector calibration
extrapolation to natural grains; photometer stray light at 40°
elongation; ground-network coverage during unfavorable geometry;
propulsion dispersion across the three drift trajectories;
radiation-induced data corruption; and a common flight-software fault.
Each risk requires an owner, quantitative trigger, mitigation and
residual estimate. A technical reserve of 30 kg per unit and 34 m/s
usable Δv headroom are design allocations, not substitutes for cost
contingency.

## 6.7 Organizational Breakdown Structure

- Avelune Space Directorate: mission owner, systems authority,
  procurement, project controls and acceptance.

- Veylora Orbital Works: common spacecraft bus design, manufacturing and
  three flight-unit integrations.

- Kyntharel Instrument Works: impact detector, photometer, context
  package and payload calibration.

- Sorevian Launch Services: launch, dispenser integration and injection
  verification.

- Tavrel Ground Networks: three receiving sites and antenna scheduling.

- Ruvellan Data Institute: science calibration, inversion, product
  validation and archive stewardship.

A single interface-control register governs supplier boundaries. The
prime spacecraft contractor integrates payload and bus and owns
spacecraft-level verification; ASD owns mission-level acceptance.
Subcontract pricing, long-lead orders and government labor allocations
are defined in Part D and the associated cost breakdown structure.

# Appendices

## A Acronym List

  -----------------------------------------------------------------------
  **Acronym**                         **Definition**
  ----------------------------------- -----------------------------------
  ADCS                                Attitude Determination and Control
                                      System

  ASD                                 Avelune Space Directorate

  AU                                  Astronomical unit

  CADRe                               Cost Analysis Data Requirements

  CDR                                 Critical Design Review

  DSP                                 Dust Scattered-Light Photometer

  EOL                                 End of Life

  FM                                  Flight Model

  IID                                 Impact Ionization Detector

  LEOP                                Launch and Early Operations

  MDFO                                Myralis Dust Field Observatory

  PCS                                 Plasma and Context Sensor

  PDR                                 Preliminary Design Review

  RDI                                 Ruvellan Data Institute

  SIR                                 System Integration Review

  TRL                                 Technology Readiness Level

  TT&C                                Telemetry, Tracking and Command
  -----------------------------------------------------------------------
