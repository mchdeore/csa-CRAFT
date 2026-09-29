## Cover Page

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
|  | CSA-FIN-RD-0589 |  |  |  |  |  |
|  | Version Draft 1.0 |  |  |  |  |  |
|  | 2026-09-21 00:00:00 |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  | Cost Analysis Data Requirement (CADRe) |  |  |  |  |  |
|  |  |  | CADRe Part C - Essential Programmatic Inputs |  |  |  |
|  |  |  | ORCA (Ocean Reconnaissance and Chemistry Analyzer) |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  | Prepared by ORCA Project Team |  |  |  |  |
|  |  | Reviewed by [TBD] | TBD |  |  |  |

## Table of Contents

| ORCA CADRe Part C - Table of Contents |  |
| --- | --- |
|  |  |
| # | Sheet |
| 1 | Cover Page |
| 2 | 1 - Change History |
| 3 | 4d - CBS in JS format |
| 4 | 2 - Phasing Nomenclature |
| 5 | 3 - Phase Durations |
| 6 | PM's sched Scenarios |
| 7 | GR&A |
| 8 | 4 - RAM LoE |
| 9 | 5 - Risk Register |
| 10 | Risk Breakdown Structure |
| 11 | Raw Labour Rates |
| 12 | Labour Rates lookup |
| 13 | Rolodex |
| 14 | Inflation Rate |

## 1 - Change History

| ` Table of Contents |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |
| 2. Version Control - Baseline Tracker |  |  |  |  |  |  |  |  |  |  |
| Purpose: | To track the baseline across time |  |  |  |  |  |  |  |  |  |
|  | hold the major and minor releases of the baseline |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  | Change history and associated files that contain the relevant data |  |  |  |  | Reserved |  |  |  |  |
|  | File Number | Date | File Version | Author | Changes | Parent Baseline Name | Baseline ID |  |  |  |
|  |  |  |  |  |  | ORCA @ PREP1 | 1 |  |  |  |
|  |  |  |  |  |  | ORCA @ KDP-0 | 2 |  |  |  |
|  |  |  |  | MB | Rebaseline: cruise duration increased following updated Jupiter gravity-assist trajectory analysis. | ORCA @ MDR#2 | 3 |  |  |  |
|  |  |  |  |  |  | ORCA @ PREP2 | 4 |  |  |  |
|  |  |  |  |  |  | ORCA @ KDP-A | 5 |  |  |  |
|  | CSA-FIN-RD-0587 | 2033-12-20 00:00:00 | Draft 1 | MB | Initial document ahead of Phase B | ORCA @ KDP-B | 6 |  |  |  |
|  |  |  |  |  |  | ORCA @ PDR | 7 |  |  |  |
|  |  |  |  |  |  | ORCA @ CDR | 8 |  |  |  |
|  | CSA-FIN-RD-0590 | 2026-09-21 00:00:00 | Draft 1 | MB | Update ahead of Gate 4: PDR and CDR complete, System Integration Review baseline. | ORCA @ SIR | 9 | <<--- We are here now |  |  |
|  |  |  |  |  |  | ORCA @ Launch (as flown) | 10 |  |  |  |
|  |  |  |  |  |  | ORCA @ CR | 11 |  |  |  |
|  |  |  |  |  |  | ORCA @ KDP-X | 12 |  |  |  |
|  |  |  |  |  |  | ORCA @ end of life | 13 |  |  |  |

## 4d - CBS in JS format

| ` Table of Contents |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4d. CBS (as self referencing list) for use as a javascript array |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Why we we asking: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | this page is auto-generated and used for drawing it out |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Self referencing list for dtree |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| UID | Parent ID | Level | Node Name | CBS Code | Depth | Icon | Notes |  | Javascript Code |  |  |  | Depth |  |
| 1 | -1 | 1 | Space Missions |  | Taxon 1 | Box.png |  |  | datatable[0] = new Array("1","-1","Space Missions","1","Box.png"); |  |  |  | Taxon 1 |  |
| 2 | 1 | 2 | EO SAR Missions |  | Taxon 2 | EO.png |  |  | datatable[1] = new Array("2","1","EO SAR Missions","2","EO.png"); |  |  |  | Taxon 2 |  |
| 3 | 2 | 3 | Radarsat Portfolio |  | Phylum | Pouch.png |  |  | datatable[2] = new Array("3","2","Radarsat Portfolio","3","Pouch.png"); |  |  |  | Phylum |  |
| 4 | 0 | 4 | Radarsat 1 |  | Mission | Satellite.png |  |  | datatable[3] = new Array("4","0","Radarsat 1","4","Satellite.png"); |  |  |  | Mission |  |
| 5 | 0 | 4 | Radarsat 2 |  | Mission | Satellite.png |  |  | datatable[4] = new Array("5","0","Radarsat 2","4","Satellite.png"); |  |  |  | Design Reference Mission |  |
| 6 | 0 | 4 | Radarsat Constellation Mission |  | Mission | Satellite.png |  |  | datatable[5] = new Array("6","0","Radarsat Constellation Mission","4","Satellite.png"); |  |  |  | Segment |  |
| 7 | 0 | 4 | Radarsat+ Replenishment | 1 | Mission | Satellite.png |  |  | datatable[6] = new Array("7","0","Radarsat+ Replenishment","4","Satellite.png"); |  |  |  | System of Systems |  |
| 8 | 0 | 4 | Radarsat+ Next Generation |  | Mission | Satellite.png |  |  | datatable[7] = new Array("8","0","Radarsat+ Next Generation","4","Satellite.png"); |  |  |  | System |  |
| 9 | 2 | 5 | Analysis Scenario 1: RCM Proxy |  | Design Reference Mission | Scenario.png |  |  | datatable[8] = new Array("9","2","Analysis Scenario 1: RCM Proxy","5","Scenario.png"); |  |  |  | Subsystem |  |
| 10 | 2 | 5 | Analysis Scenario 2: RCM+ |  | Design Reference Mission | Scenario.png |  |  | datatable[9] = new Array("10","2","Analysis Scenario 2: RCM+","5","Scenario.png"); |  |  |  | Assembly |  |
| 11 | 2 | 5 | Analysis Scenario 3: Airbus concept |  | Design Reference Mission | Scenario.png |  |  | datatable[10] = new Array("11","2","Analysis Scenario 3: Airbus concept","5","Scenario.png"); |  |  |  | Component |  |
| 12 | 2 | 5 | Analysis Scenario 4: MDA Chorus Data Buy |  | Design Reference Mission | Scenario.png |  |  | datatable[11] = new Array("12","2","Analysis Scenario 4: MDA Chorus Data Buy","5","Scenario.png"); |  |  |  |  |  |
| 13 | 2 | 5 | Analysis Scenario 5: MDA Chorus+ |  | Design Reference Mission | Scenario.png |  |  | datatable[12] = new Array("13","2","Analysis Scenario 5: MDA Chorus+","5","Scenario.png"); |  |  |  |  |  |
| 14 | 2 | 5 | Analysis Scenario 6: Airbus Sentinel 2 |  | Design Reference Mission | Scenario.png |  |  | datatable[13] = new Array("14","2","Analysis Scenario 6: Airbus Sentinel 2","5","Scenario.png"); |  |  |  |  |  |
| 15 | 8 | 6 | Government Overhead and Oversight | 1.1 | Segment | Government.png | This WBS includes all CSA Oversight, OGD salaries, and basic overhead for the care and maintenance of CSA staff |  | datatable[14] = new Array("15","8","Government Overhead and Oversight","6","Government.png"); |  |  |  |  |  |
| 16 | 8 | 6 | Space Segment | 1.2 | Segment | Satellite.png | The Space Segment includes things we launch into space |  | datatable[15] = new Array("16","8","Space Segment","6","Satellite.png"); |  |  |  |  |  |
| 17 | 8 | 6 | Launch Segment | 1.3 | Segment | Rocket.png | The launch segment includes the launch vehicle and seom support services |  | datatable[16] = new Array("17","8","Launch Segment","6","Rocket.png"); |  |  |  |  |  |
| 18 | 8 | 6 | Ground Segment | 1.4 | Segment | Facility.png | The ground segment includes the planning desgin and development of the GS, but not the Ops |  | datatable[17] = new Array("18","8","Ground Segment","6","Facility.png"); |  |  |  |  |  |
| 19 | 8 | 6 | Ops Segment | 1.5 | Segment | Ops.png | Ops includes SatOps, Mission Ops, Science Ops - typically contracts |  | datatable[18] = new Array("19","8","Ops Segment","6","Ops.png"); |  |  |  |  |  |
| 20 | 8 | 6 | Science Segment | 1.6 | Segment | Science.png | Typically G&C |  | datatable[19] = new Array("20","8","Science Segment","6","Science.png"); |  |  |  |  |  |
| 21 | 10 | 7 | Gov't Oversight (Salaries and EBP) | 1.1.1 | System of Systems | Government.png |  |  | datatable[20] = new Array("21","10","Gov't Oversight (Salaries and EBP)","7","Government.png"); |  |  |  |  |  |
| 22 | 10 | 7 | Government Overhead | 1.1.2 | System of Systems | Government.png |  |  | datatable[21] = new Array("22","10","Government Overhead","7","Government.png"); |  |  |  |  |  |
| 23 | 21 | 8 | CSA Oversight | 1.1.1.1 | System | Government.png |  |  | datatable[22] = new Array("23","21","CSA Oversight","8","Government.png"); |  |  |  |  |  |
| 24 | 21 | 8 | OGD Oversight | 1.1.1.2 | System | Government.png |  |  | datatable[23] = new Array("24","21","OGD Oversight","8","Government.png"); |  |  |  |  |  |
| 25 | 23 | 9 | CSA Project Team | 1.1.1.1.1 | Subsystem | Government.png | This CBS contains all salaries associated with the RAM of the Project team |  | datatable[24] = new Array("25","23","CSA Project Team","9","Government.png"); |  |  |  |  |  |
| 26 | 23 | 9 | CSA Internal Services | 1.1.1.1.2 | Subsystem | Government.png | This CBS contains all salaries associated with CSA internal services (finance, HR, audit, eval, policy, Executives, IM, IT, contracts, shipping, etc) |  | datatable[25] = new Array("26","23","CSA Internal Services","9","Government.png"); |  |  |  |  |  |
| 27 | 24 | 9 | OGD Internal Services by MOU | 1.1.1.2.1 | Subsystem | Government.png |  |  | datatable[26] = new Array("27","24","OGD Internal Services by MOU","9","Government.png"); |  |  |  |  |  |
| 28 | 24 | 9 | OGD User Departments by MOU (RAM portion) | 1.1.1.2.2 | Subsystem | Government.png |  |  | datatable[27] = new Array("28","24","OGD User Departments by MOU (RAM portion)","9","Government.png"); |  |  |  |  |  |
| 29 | 21 | 10 | Shared Services | 1.1.1.2.1.1 | Assembly | Government.png |  |  | datatable[28] = new Array("29","21","Shared Services","10","Government.png"); |  |  |  |  |  |
| 30 | 21 | 10 | SPAC | 1.1.1.2.1.2 | Assembly | Government.png |  |  | datatable[29] = new Array("30","21","SPAC","10","Government.png"); |  |  |  |  |  |
| 31 | 21 | 10 | Justice Canada | 1.1.1.2.1.3 | Assembly | Government.png |  |  | datatable[30] = new Array("31","21","Justice Canada","10","Government.png"); |  |  |  |  |  |
| 32 | 23 | 10 | ECCC | 1.1.1.2.2.1 | Assembly | Government.png |  |  | datatable[31] = new Array("32","23","ECCC","10","Government.png"); |  |  |  |  |  |
| 33 | 23 | 10 | NRCAN | 1.1.1.2.2.2 | Assembly | Government.png |  |  | datatable[32] = new Array("33","23","NRCAN","10","Government.png"); |  |  |  |  |  |
| 34 | 23 | 10 | DND | 1.1.1.2.2.3 | Assembly | Government.png |  |  | datatable[33] = new Array("34","23","DND","10","Government.png"); |  |  |  |  |  |
| 35 | 25 | 11 | RAM per Person per FY and Phase | 1.1.1.1.1.1 | Component | Government.png |  |  | datatable[34] = new Array("35","25","RAM per Person per FY and Phase","11","Government.png"); |  |  |  |  |  |
| 36 | 25 | 11 | PSPC Procurement Services | 1.1.1.2.1.2.1 | Component | Government.png |  |  | datatable[35] = new Array("36","25","PSPC Procurement Services","11","Government.png"); |  |  |  |  |  |
| 37 | 25 | 11 | PSPC Fairness Monitor | 1.1.1.2.1.2.2 | Component | Government.png |  |  | datatable[36] = new Array("37","25","PSPC Fairness Monitor","11","Government.png"); |  |  |  |  |  |
| 38 | 31 | 11 | Legal Services | 1.1.1.2.1.3.1 | Component | Government.png |  |  | datatable[37] = new Array("38","31","Legal Services","11","Government.png"); |  |  |  |  |  |
| 39 | 22 | 8 | CSA Overhead | 1.1.2.1 | System | Government.png |  |  | datatable[38] = new Array("39","22","CSA Overhead","8","Government.png"); |  |  |  |  |  |
| 40 | 34 | 9 | IS Management Overhead  | 1.1.2.1.1 | Subsystem | Government.png |  |  | datatable[39] = new Array("40","34","IS Management Overhead ","9","Government.png"); |  |  |  |  |  |
| 41 | 34 | 9 | Management Consulting Services | 1.1.2.1.2 | Subsystem | Government.png |  |  | datatable[40] = new Array("41","34","Management Consulting Services","9","Government.png"); |  |  |  |  |  |
| 42 | 34 | 9 | Temporary Help | 1.1.2.1.3 | Subsystem | Government.png |  |  | datatable[41] = new Array("42","34","Temporary Help","9","Government.png"); |  |  |  |  |  |
| 43 | 34 | 9 | Students | 1.1.2.1.4 | Subsystem | Government.png | This CBS  includes any students, FSWEP or PDF assisint Csa project team |  | datatable[42] = new Array("43","34","Students","9","Government.png"); |  |  |  |  |  |
| 44 | 34 | 9 | Government Travel & Living | 1.1.2.1.5 | Subsystem | Government.png | This CBS includes any government Travel and Living expenses |  | datatable[43] = new Array("44","34","Government Travel & Living","9","Government.png"); |  |  |  |  |  |
| 45 | 34 | 9 | Translation | 1.1.2.1.6 | Subsystem | Government.png | This CBS includes any translation costs |  | datatable[44] = new Array("45","34","Translation","9","Government.png"); |  |  |  |  |  |
| 46 | 34 | 9 | Shipping | 1.1.2.1.7 | Subsystem | Government.png | This CBs includes any shipping cost, but not shipping flight HW which is under space segment |  | datatable[45] = new Array("46","34","Shipping","9","Government.png"); |  |  |  |  |  |
| 47 | 34 | 9 | Software Licenses | 1.1.2.1.8 | Subsystem | Government.png | This CBS includes any COTs SW not flight Sw or ground SW |  | datatable[46] = new Array("47","34","Software Licenses","9","Government.png"); |  |  |  |  |  |
| 48 | 34 | 9 | Public Outreach and STEM initiatives | 1.1.2.1.9 | Subsystem | Government.png | This CBS includes any public relations and STEM |  | datatable[47] = new Array("48","34","Public Outreach and STEM initiatives","9","Government.png"); |  |  |  |  |  |
| 49 | 34 | 9 | Other Overhead (Specify) | 1.1.2.1.10 | Subsystem | Government.png | This CBS includes any other misc fees  |  | datatable[48] = new Array("49","34","Other Overhead (Specify)","9","Government.png"); |  |  |  |  |  |
| 50 | 36 | 10 | Consultants - Industrial Space Experts | 1.1.2.1.2.1 | Assembly | Government.png |  |  | datatable[49] = new Array("50","36","Consultants - Industrial Space Experts","10","Government.png"); |  |  |  |  |  |
| 51 | 36 | 10 | Consultants - Academia | 1.1.2.1.2.2 | Assembly | Government.png |  |  | datatable[50] = new Array("51","36","Consultants - Academia","10","Government.png"); |  |  |  |  |  |
| 52 | 36 | 10 | Consultants - Non-Space Experts | 1.1.2.1.2.3 | Assembly | Government.png |  |  | datatable[51] = new Array("52","36","Consultants - Non-Space Experts","10","Government.png"); |  |  |  |  |  |
| 53 | 12 | 6 | Mission SEITPM and Support Equipment |  | Segment | SEITPM.png |  |  | datatable[52] = new Array("53","12","Mission SEITPM and Support Equipment","6","SEITPM.png"); |  |  |  |  |  |
| 54 | 48 | 7 | Project Management |  | System of Systems | SEITPM.png |  |  | datatable[53] = new Array("54","48","Project Management","7","SEITPM.png"); |  |  |  |  |  |
| 55 | 48 | 7 | Systems Engineering |  | System of Systems | SEITPM.png |  |  | datatable[54] = new Array("55","48","Systems Engineering","7","SEITPM.png"); |  |  |  |  |  |
| 56 | 48 | 7 | Mission Assurance |  | System of Systems | SEITPM.png |  |  | datatable[55] = new Array("56","48","Mission Assurance","7","SEITPM.png"); |  |  |  |  |  |
| 57 | 48 | 7 | Assembly, Integration and Testing |  | System of Systems | SEITPM.png |  |  | datatable[56] = new Array("57","48","Assembly, Integration and Testing","7","SEITPM.png"); |  |  |  |  |  |
| 58 | 48 | 7 | Support Equipment |  | System of Systems | SEITPM.png |  |  | datatable[57] = new Array("58","48","Support Equipment","7","SEITPM.png"); |  |  |  |  |  |
| 59 | 16 | 7 | Space Vehicle 1 … i |  | System of Systems | Satellite.png |  |  | datatable[58] = new Array("59","16","Space Vehicle 1 … i","7","Satellite.png"); |  |  |  |  |  |
| 60 | 59 | 8 | Spacecraft SEITPM and Support Equipment |  | System | SEITPM.png |  |  | datatable[59] = new Array("60","59","Spacecraft SEITPM and Support Equipment","8","SEITPM.png"); |  |  |  |  |  |
| 61 | 55 | 9 | Project Management |  | Subsystem | SEITPM.png |  |  | datatable[60] = new Array("61","55","Project Management","9","SEITPM.png"); |  |  |  |  |  |
| 62 | 55 | 9 | Systems Engineering |  | Subsystem | SEITPM.png |  |  | datatable[61] = new Array("62","55","Systems Engineering","9","SEITPM.png"); |  |  |  |  |  |
| 63 | 55 | 9 | Mission Assurance |  | Subsystem | SEITPM.png |  |  | datatable[62] = new Array("63","55","Mission Assurance","9","SEITPM.png"); |  |  |  |  |  |
| 64 | 55 | 9 | Assembly, Integration and Testing |  | Subsystem | SEITPM.png |  |  | datatable[63] = new Array("64","55","Assembly, Integration and Testing","9","SEITPM.png"); |  |  |  |  |  |
| 65 | 55 | 9 | Support Equipment |  | Subsystem | SEITPM.png |  |  | datatable[64] = new Array("65","55","Support Equipment","9","SEITPM.png"); |  |  |  |  |  |
| 66 | 59 | 8 | Bus/Platform |  | System | Widget.png |  |  | datatable[65] = new Array("66","59","Bus/Platform","8","Widget.png"); |  |  |  |  |  |
| 67 | 66 | 9 | Platform SEITPM and Support Equipment |  | Subsystem | SEITPM.png |  |  | datatable[66] = new Array("67","66","Platform SEITPM and Support Equipment","9","SEITPM.png"); |  |  |  |  |  |
| 68 | 62 | 10 | Project Management |  | Assembly | SEITPM.png |  |  | datatable[67] = new Array("68","62","Project Management","10","SEITPM.png"); |  |  |  |  |  |
| 69 | 62 | 10 | Systems Engineering |  | Assembly | SEITPM.png |  |  | datatable[68] = new Array("69","62","Systems Engineering","10","SEITPM.png"); |  |  |  |  |  |
| 70 | 62 | 10 | Mission Assurance |  | Assembly | SEITPM.png |  |  | datatable[69] = new Array("70","62","Mission Assurance","10","SEITPM.png"); |  |  |  |  |  |
| 71 | 62 | 10 | Assembly, Integration and Testing |  | Assembly | SEITPM.png |  |  | datatable[70] = new Array("71","62","Assembly, Integration and Testing","10","SEITPM.png"); |  |  |  |  |  |
| 72 | 62 | 10 | Support Equipment |  | Assembly | SEITPM.png |  |  | datatable[71] = new Array("72","62","Support Equipment","10","SEITPM.png"); |  |  |  |  |  |
| 73 | 61 | 9 | Structures and Mechanisms Subsystem (SMS) |  | Subsystem | Widget.png |  |  | datatable[72] = new Array("73","61","Structures and Mechanisms Subsystem (SMS)","9","Widget.png"); |  |  |  |  |  |
| 74 | 68 | 10 | Structures and Mechanisms Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[73] = new Array("74","68","Structures and Mechanisms Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 75 | 69 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[74] = new Array("75","69","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 76 | 69 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[75] = new Array("76","69","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 77 | 69 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[76] = new Array("77","69","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 78 | 69 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[77] = new Array("78","69","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 79 | 69 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[78] = new Array("79","69","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 80 | 68 | 10 | Primary Structures |  | Assembly | Widget.png |  |  | datatable[79] = new Array("80","68","Primary Structures","10","Widget.png"); |  |  |  |  |  |
| 81 | 75 | 11 | Load Carrying Shell/Truss |  | Component | Widget.png |  |  | datatable[80] = new Array("81","75","Load Carrying Shell/Truss","11","Widget.png"); |  |  |  |  |  |
| 82 | 75 | 11 | Equipment Compartments |  | Component | Widget.png |  |  | datatable[81] = new Array("82","75","Equipment Compartments","11","Widget.png"); |  |  |  |  |  |
| 83 | 75 | 11 | Booms |  | Component | Widget.png |  |  | datatable[82] = new Array("83","75","Booms","11","Widget.png"); |  |  |  |  |  |
| 84 | 75 | 11 | Adapters |  | Component | Widget.png |  |  | datatable[83] = new Array("84","75","Adapters","11","Widget.png"); |  |  |  |  |  |
| 85 | 75 | 11 | Other Structures (Specify) |  | Component | Widget.png |  |  | datatable[84] = new Array("85","75","Other Structures (Specify)","11","Widget.png"); |  |  |  |  |  |
| 86 | 68 | 10 | Secondary Structures |  | Assembly | Widget.png |  |  | datatable[85] = new Array("86","68","Secondary Structures","10","Widget.png"); |  |  |  |  |  |
| 87 | 81 | 11 | Equipment (Instrument) Mountings |  | Component | Widget.png |  |  | datatable[86] = new Array("87","81","Equipment (Instrument) Mountings","11","Widget.png"); |  |  |  |  |  |
| 88 | 81 | 11 | Ballast Mass |  | Component | Widget.png |  |  | datatable[87] = new Array("88","81","Ballast Mass","11","Widget.png"); |  |  |  |  |  |
| 89 | 81 | 11 | Other Secondary Structures (Specify) |  | Component | Widget.png |  |  | datatable[88] = new Array("89","81","Other Secondary Structures (Specify)","11","Widget.png"); |  |  |  |  |  |
| 90 | 68 | 10 | Mechanisms and Pyrotechnics |  | Assembly | Widget.png |  |  | datatable[89] = new Array("90","68","Mechanisms and Pyrotechnics","10","Widget.png"); |  |  |  |  |  |
| 91 | 85 | 11 | Positioning |  | Component | Widget.png |  |  | datatable[90] = new Array("91","85","Positioning","11","Widget.png"); |  |  |  |  |  |
| 92 | 85 | 11 | Deployment and Storage Equipment |  | Component | Widget.png |  |  | datatable[91] = new Array("92","85","Deployment and Storage Equipment","11","Widget.png"); |  |  |  |  |  |
| 93 | 85 | 11 | Docking Mechanisms |  | Component | Widget.png |  |  | datatable[92] = new Array("93","85","Docking Mechanisms","11","Widget.png"); |  |  |  |  |  |
| 94 | 85 | 11 | Other Mechanisms (Specify) |  | Component | Widget.png |  |  | datatable[93] = new Array("94","85","Other Mechanisms (Specify)","11","Widget.png"); |  |  |  |  |  |
| 95 | 85 | 11 | Pyrotechnics |  | Component | Widget.png |  |  | datatable[94] = new Array("95","85","Pyrotechnics","11","Widget.png"); |  |  |  |  |  |
| 96 | 68 | 10 | SMS Other (Specify) |  | Assembly | Widget.png |  |  | datatable[95] = new Array("96","68","SMS Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 97 | 61 | 9 | Thermal Control Subsystem (TCS) |  | Subsystem | Widget.png |  |  | datatable[96] = new Array("97","61","Thermal Control Subsystem (TCS)","9","Widget.png"); |  |  |  |  |  |
| 98 | 92 | 10 | Thermal Control Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[97] = new Array("98","92","Thermal Control Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 99 | 93 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[98] = new Array("99","93","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 100 | 93 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[99] = new Array("100","93","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 101 | 93 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[100] = new Array("101","93","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 102 | 93 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[101] = new Array("102","93","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 103 | 93 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[102] = new Array("103","93","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 104 | 92 | 10 | Active Devices |  | Assembly | Widget.png |  |  | datatable[103] = new Array("104","92","Active Devices","10","Widget.png"); |  |  |  |  |  |
| 105 | 99 | 11 | Cryogenic Devices |  | Component | Widget.png |  |  | datatable[104] = new Array("105","99","Cryogenic Devices","11","Widget.png"); |  |  |  |  |  |
| 106 | 99 | 11 | Liquid Loops |  | Component | Widget.png |  |  | datatable[105] = new Array("106","99","Liquid Loops","11","Widget.png"); |  |  |  |  |  |
| 107 | 99 | 11 | Electric Coolers |  | Component | Widget.png |  |  | datatable[106] = new Array("107","99","Electric Coolers","11","Widget.png"); |  |  |  |  |  |
| 108 | 99 | 11 | Heaters, Thermistors, and Thermostats |  | Component | Widget.png |  |  | datatable[107] = new Array("108","99","Heaters, Thermistors, and Thermostats","11","Widget.png"); |  |  |  |  |  |
| 109 | 99 | 11 | Other Active Devices (Specify) |  | Component | Widget.png |  |  | datatable[108] = new Array("109","99","Other Active Devices (Specify)","11","Widget.png"); |  |  |  |  |  |
| 110 | 92 | 10 | Passive Devices |  | Assembly | Widget.png |  |  | datatable[109] = new Array("110","92","Passive Devices","10","Widget.png"); |  |  |  |  |  |
| 111 | 105 | 11 | Radiator Panel/Fins |  | Component | Widget.png |  |  | datatable[110] = new Array("111","105","Radiator Panel/Fins","11","Widget.png"); |  |  |  |  |  |
| 112 | 105 | 11 | Coatings |  | Component | Widget.png |  |  | datatable[111] = new Array("112","105","Coatings","11","Widget.png"); |  |  |  |  |  |
| 113 | 105 | 11 | Heat Pipes |  | Component | Widget.png |  |  | datatable[112] = new Array("113","105","Heat Pipes","11","Widget.png"); |  |  |  |  |  |
| 114 | 105 | 11 | Insulation |  | Component | Widget.png |  |  | datatable[113] = new Array("114","105","Insulation","11","Widget.png"); |  |  |  |  |  |
| 115 | 105 | 11 | Conductive Structures |  | Component | Widget.png |  |  | datatable[114] = new Array("115","105","Conductive Structures","11","Widget.png"); |  |  |  |  |  |
| 116 | 105 | 11 | Heat Activated Structures |  | Component | Widget.png |  |  | datatable[115] = new Array("116","105","Heat Activated Structures","11","Widget.png"); |  |  |  |  |  |
| 117 | 105 | 11 | Sun Shields |  | Component | Widget.png |  |  | datatable[116] = new Array("117","105","Sun Shields","11","Widget.png"); |  |  |  |  |  |
| 118 | 105 | 11 | Second Surface Mirrors |  | Component | Widget.png |  |  | datatable[117] = new Array("118","105","Second Surface Mirrors","11","Widget.png"); |  |  |  |  |  |
| 119 | 105 | 11 | Shutters and Louvers |  | Component | Widget.png |  |  | datatable[118] = new Array("119","105","Shutters and Louvers","11","Widget.png"); |  |  |  |  |  |
| 120 | 105 | 11 | Other Passive Devices (Specify) |  | Component | Widget.png |  |  | datatable[119] = new Array("120","105","Other Passive Devices (Specify)","11","Widget.png"); |  |  |  |  |  |
| 121 | 92 | 10 | TCS Other (Specify) |  | Assembly | Widget.png |  |  | datatable[120] = new Array("121","92","TCS Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 122 | 61 | 9 | Electric Power Subsystem (EPS) |  | Subsystem | Widget.png |  |  | datatable[121] = new Array("122","61","Electric Power Subsystem (EPS)","9","Widget.png"); |  |  |  |  |  |
| 123 | 117 | 10 | Electric Power Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[122] = new Array("123","117","Electric Power Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 124 | 118 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[123] = new Array("124","118","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 125 | 118 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[124] = new Array("125","118","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 126 | 118 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[125] = new Array("126","118","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 127 | 118 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[126] = new Array("127","118","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 128 | 118 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[127] = new Array("128","118","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 129 | 117 | 10 | Electrical Power Generation |  | Assembly | Widget.png |  |  | datatable[128] = new Array("129","117","Electrical Power Generation","10","Widget.png"); |  |  |  |  |  |
| 130 | 124 | 11 | Solar Array |  | Component | Widget.png |  |  | datatable[129] = new Array("130","124","Solar Array","11","Widget.png"); |  |  |  |  |  |
| 131 | 124 | 11 | Solar Array Positioner |  | Component | Widget.png |  |  | datatable[130] = new Array("131","124","Solar Array Positioner","11","Widget.png"); |  |  |  |  |  |
| 132 | 124 | 11 | Radioisotope Thermionic Generator |  | Component | Widget.png |  |  | datatable[131] = new Array("132","124","Radioisotope Thermionic Generator","11","Widget.png"); |  |  |  |  |  |
| 133 | 124 | 11 | Chemical (Fuel Cells) |  | Component | Widget.png |  |  | datatable[132] = new Array("133","124","Chemical (Fuel Cells)","11","Widget.png"); |  |  |  |  |  |
| 134 | 124 | 11 | Auxiliary Power Units |  | Component | Widget.png |  |  | datatable[133] = new Array("134","124","Auxiliary Power Units","11","Widget.png"); |  |  |  |  |  |
| 135 | 124 | 11 | Other Power Sources |  | Component | Widget.png |  |  | datatable[134] = new Array("135","124","Other Power Sources","11","Widget.png"); |  |  |  |  |  |
| 136 | 117 | 10 | Electrical Power Conditioning |  | Assembly | Widget.png |  |  | datatable[135] = new Array("136","117","Electrical Power Conditioning","10","Widget.png"); |  |  |  |  |  |
| 137 | 131 | 11 | Power Control Electronics |  | Component | Widget.png |  |  | datatable[136] = new Array("137","131","Power Control Electronics","11","Widget.png"); |  |  |  |  |  |
| 138 | 131 | 11 | Power Conversion Electronics |  | Component | Widget.png |  |  | datatable[137] = new Array("138","131","Power Conversion Electronics","11","Widget.png"); |  |  |  |  |  |
| 139 | 131 | 11 | Power Dissipation Devices |  | Component | Widget.png |  |  | datatable[138] = new Array("139","131","Power Dissipation Devices","11","Widget.png"); |  |  |  |  |  |
| 140 | 131 | 11 | Power Distribution Electronics |  | Component | Widget.png |  |  | datatable[139] = new Array("140","131","Power Distribution Electronics","11","Widget.png"); |  |  |  |  |  |
| 141 | 131 | 11 | Power Switching Electronics |  | Component | Widget.png |  |  | datatable[140] = new Array("141","131","Power Switching Electronics","11","Widget.png"); |  |  |  |  |  |
| 142 | 131 | 11 | Power Regulation Electronics |  | Component | Widget.png |  |  | datatable[141] = new Array("142","131","Power Regulation Electronics","11","Widget.png"); |  |  |  |  |  |
| 143 | 131 | 11 | Other Power Conditioning Devices (Specify) |  | Component | Widget.png |  |  | datatable[142] = new Array("143","131","Other Power Conditioning Devices (Specify)","11","Widget.png"); |  |  |  |  |  |
| 144 | 117 | 10 | Electrical Power Storage |  | Assembly | Widget.png |  |  | datatable[143] = new Array("144","117","Electrical Power Storage","10","Widget.png"); |  |  |  |  |  |
| 145 | 139 | 11 | Rechargeable Batteries |  | Component | Widget.png |  |  | datatable[144] = new Array("145","139","Rechargeable Batteries","11","Widget.png"); |  |  |  |  |  |
| 146 | 139 | 11 | Charge Control Electronics |  | Component | Widget.png |  |  | datatable[145] = new Array("146","139","Charge Control Electronics","11","Widget.png"); |  |  |  |  |  |
| 147 | 139 | 11 | Other Electrical Power Storage Devices (Specify) |  | Component | Widget.png |  |  | datatable[146] = new Array("147","139","Other Electrical Power Storage Devices (Specify)","11","Widget.png"); |  |  |  |  |  |
| 148 | 117 | 10 | Harnesses and Cables |  | Assembly | Widget.png |  |  | datatable[147] = new Array("148","117","Harnesses and Cables","10","Widget.png"); |  |  |  |  |  |
| 149 | 117 | 10 | EPS Other (Specify) |  | Assembly | Widget.png |  |  | datatable[148] = new Array("149","117","EPS Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 150 | 61 | 9 | Attitude Control Subsystem (ACS) |  | Subsystem | Widget.png |  |  | datatable[149] = new Array("150","61","Attitude Control Subsystem (ACS)","9","Widget.png"); |  |  |  |  |  |
| 151 | 145 | 10 | Attitude Control Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[150] = new Array("151","145","Attitude Control Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 152 | 146 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[151] = new Array("152","146","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 153 | 146 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[152] = new Array("153","146","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 154 | 146 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[153] = new Array("154","146","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 155 | 146 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[154] = new Array("155","146","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 156 | 146 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[155] = new Array("156","146","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 157 | 145 | 10 | Attitude Determination |  | Assembly | Widget.png |  |  | datatable[156] = new Array("157","145","Attitude Determination","10","Widget.png"); |  |  |  |  |  |
| 158 | 152 | 11 | Earth (Horizon) Sensors |  | Component | Widget.png |  |  | datatable[157] = new Array("158","152","Earth (Horizon) Sensors","11","Widget.png"); |  |  |  |  |  |
| 159 | 152 | 11 | Sun Sensors |  | Component | Widget.png |  |  | datatable[158] = new Array("159","152","Sun Sensors","11","Widget.png"); |  |  |  |  |  |
| 160 | 152 | 11 | Star Tracker/Sensors |  | Component | Widget.png |  |  | datatable[159] = new Array("160","152","Star Tracker/Sensors","11","Widget.png"); |  |  |  |  |  |
| 161 | 152 | 11 | Global Positioning System (GPS) Receiver |  | Component | Widget.png |  |  | datatable[160] = new Array("161","152","Global Positioning System (GPS) Receiver","11","Widget.png"); |  |  |  |  |  |
| 162 | 152 | 11 | Imagers |  | Component | Widget.png |  |  | datatable[161] = new Array("162","152","Imagers","11","Widget.png"); |  |  |  |  |  |
| 163 | 152 | 11 | Magnetometers |  | Component | Widget.png |  |  | datatable[162] = new Array("163","152","Magnetometers","11","Widget.png"); |  |  |  |  |  |
| 164 | 152 | 11 | Altimeters |  | Component | Widget.png |  |  | datatable[163] = new Array("164","152","Altimeters","11","Widget.png"); |  |  |  |  |  |
| 165 | 152 | 11 | Inertial Reference Unit (IRU)/Inertial Measurement Unit (IMU) |  | Component | Widget.png |  |  | datatable[164] = new Array("165","152","Inertial Reference Unit (IRU)/Inertial Measurement Unit (IMU)","11","Widget.png"); |  |  |  |  |  |
| 166 | 152 | 11 | Radar |  | Component | Widget.png |  |  | datatable[165] = new Array("166","152","Radar","11","Widget.png"); |  |  |  |  |  |
| 167 | 152 | 11 | Rate Gyros |  | Component | Widget.png |  |  | datatable[166] = new Array("167","152","Rate Gyros","11","Widget.png"); |  |  |  |  |  |
| 168 | 152 | 11 | Accelerometers |  | Component | Widget.png |  |  | datatable[167] = new Array("168","152","Accelerometers","11","Widget.png"); |  |  |  |  |  |
| 169 | 152 | 11 | Bearing and Power Transfer Assembly |  | Component | Widget.png |  |  | datatable[168] = new Array("169","152","Bearing and Power Transfer Assembly","11","Widget.png"); |  |  |  |  |  |
| 170 | 152 | 11 | Other Attitude Determination Devices (Specify) |  | Component | Widget.png |  |  | datatable[169] = new Array("170","152","Other Attitude Determination Devices (Specify)","11","Widget.png"); |  |  |  |  |  |
| 171 | 145 | 10 | Attitude Control |  | Assembly | Widget.png |  |  | datatable[170] = new Array("171","145","Attitude Control","10","Widget.png"); |  |  |  |  |  |
| 172 | 166 | 11 | Reaction Wheel |  | Component | Widget.png |  |  | datatable[171] = new Array("172","166","Reaction Wheel","11","Widget.png"); |  |  |  |  |  |
| 173 | 166 | 11 | Momentum Wheel |  | Component | Widget.png |  |  | datatable[172] = new Array("173","166","Momentum Wheel","11","Widget.png"); |  |  |  |  |  |
| 174 | 166 | 11 | Control Moment Gyro |  | Component | Widget.png |  |  | datatable[173] = new Array("174","166","Control Moment Gyro","11","Widget.png"); |  |  |  |  |  |
| 175 | 166 | 11 | Other Energy Storage Devices |  | Component | Widget.png |  |  | datatable[174] = new Array("175","166","Other Energy Storage Devices","11","Widget.png"); |  |  |  |  |  |
| 176 | 166 | 11 | Magnetic Control Devices |  | Component | Widget.png |  |  | datatable[175] = new Array("176","166","Magnetic Control Devices","11","Widget.png"); |  |  |  |  |  |
| 177 | 166 | 11 | Spin Control Devices |  | Component | Widget.png |  |  | datatable[176] = new Array("177","166","Spin Control Devices","11","Widget.png"); |  |  |  |  |  |
| 178 | 166 | 11 | Control Electronics |  | Component | Widget.png |  |  | datatable[177] = new Array("178","166","Control Electronics","11","Widget.png"); |  |  |  |  |  |
| 179 | 166 | 11 | Other Attitude Control Devices (Specify) |  | Component | Widget.png |  |  | datatable[178] = new Array("179","166","Other Attitude Control Devices (Specify)","11","Widget.png"); |  |  |  |  |  |
| 180 | 145 | 10 | ACS Other (Specify) |  | Assembly | Widget.png |  |  | datatable[179] = new Array("180","145","ACS Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 181 | 61 | 9 | Propulsion Subsystem |  | Subsystem | Widget.png |  |  | datatable[180] = new Array("181","61","Propulsion Subsystem","9","Widget.png"); |  |  |  |  |  |
| 182 | 176 | 10 | Propulsion Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[181] = new Array("182","176","Propulsion Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 183 | 177 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[182] = new Array("183","177","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 184 | 177 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[183] = new Array("184","177","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 185 | 177 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[184] = new Array("185","177","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 186 | 177 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[185] = new Array("186","177","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 187 | 177 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[186] = new Array("187","177","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 188 | 176 | 10 | Tanks |  | Assembly | Widget.png |  |  | datatable[187] = new Array("188","176","Tanks","10","Widget.png"); |  |  |  |  |  |
| 189 | 183 | 11 | Oxidizer Tanks |  | Component | Widget.png |  |  | datatable[188] = new Array("189","183","Oxidizer Tanks","11","Widget.png"); |  |  |  |  |  |
| 190 | 183 | 11 | Fuel Tanks |  | Component | Widget.png |  |  | datatable[189] = new Array("190","183","Fuel Tanks","11","Widget.png"); |  |  |  |  |  |
| 191 | 183 | 11 | Propellant Tanks |  | Component | Widget.png |  |  | datatable[190] = new Array("191","183","Propellant Tanks","11","Widget.png"); |  |  |  |  |  |
| 192 | 183 | 11 | Pressurance Tanks |  | Component | Widget.png |  |  | datatable[191] = new Array("192","183","Pressurance Tanks","11","Widget.png"); |  |  |  |  |  |
| 193 | 183 | 11 | Plumbing |  | Component | Widget.png |  |  | datatable[192] = new Array("193","183","Plumbing","11","Widget.png"); |  |  |  |  |  |
| 194 | 183 | 11 | Other Tanks (Specify) |  | Component | Widget.png |  |  | datatable[193] = new Array("194","183","Other Tanks (Specify)","11","Widget.png"); |  |  |  |  |  |
| 195 | 176 | 10 | Maneuvering Thrusters |  | Assembly | Widget.png |  |  | datatable[194] = new Array("195","176","Maneuvering Thrusters","10","Widget.png"); |  |  |  |  |  |
| 196 | 190 | 11 | Bipropellant |  | Component | Widget.png |  |  | datatable[195] = new Array("196","190","Bipropellant","11","Widget.png"); |  |  |  |  |  |
| 197 | 190 | 11 | Monopropellant |  | Component | Widget.png |  |  | datatable[196] = new Array("197","190","Monopropellant","11","Widget.png"); |  |  |  |  |  |
| 198 | 190 | 11 | Solar Electric |  | Component | Widget.png |  |  | datatable[197] = new Array("198","190","Solar Electric","11","Widget.png"); |  |  |  |  |  |
| 199 | 190 | 11 | Ion |  | Component | Widget.png |  |  | datatable[198] = new Array("199","190","Ion","11","Widget.png"); |  |  |  |  |  |
| 200 | 190 | 11 | Cold Gas |  | Component | Widget.png |  |  | datatable[199] = new Array("200","190","Cold Gas","11","Widget.png"); |  |  |  |  |  |
| 201 | 190 | 11 | Other Maneuvering Thrusters (Specify) |  | Component | Widget.png |  |  | datatable[200] = new Array("201","190","Other Maneuvering Thrusters (Specify)","11","Widget.png"); |  |  |  |  |  |
| 202 | 176 | 10 | Translation Thrusters |  | Assembly | Widget.png |  |  | datatable[201] = new Array("202","176","Translation Thrusters","10","Widget.png"); |  |  |  |  |  |
| 203 | 197 | 11 | Bipropellant |  | Component | Widget.png |  |  | datatable[202] = new Array("203","197","Bipropellant","11","Widget.png"); |  |  |  |  |  |
| 204 | 197 | 11 | Monopropellant |  | Component | Widget.png |  |  | datatable[203] = new Array("204","197","Monopropellant","11","Widget.png"); |  |  |  |  |  |
| 205 | 197 | 11 | Solar Electric |  | Component | Widget.png |  |  | datatable[204] = new Array("205","197","Solar Electric","11","Widget.png"); |  |  |  |  |  |
| 206 | 197 | 11 | Ion |  | Component | Widget.png |  |  | datatable[205] = new Array("206","197","Ion","11","Widget.png"); |  |  |  |  |  |
| 207 | 197 | 11 | Cold Gas |  | Component | Widget.png |  |  | datatable[206] = new Array("207","197","Cold Gas","11","Widget.png"); |  |  |  |  |  |
| 208 | 197 | 11 | Other Translation Thrusters (Specify) |  | Component | Widget.png |  |  | datatable[207] = new Array("208","197","Other Translation Thrusters (Specify)","11","Widget.png"); |  |  |  |  |  |
| 209 | 176 | 10 | Propellant |  | Assembly | Widget.png |  |  | datatable[208] = new Array("209","176","Propellant","10","Widget.png"); |  |  |  |  |  |
| 210 | 204 | 11 | Solid Propellant |  | Component | Widget.png |  |  | datatable[209] = new Array("210","204","Solid Propellant","11","Widget.png"); |  |  |  |  |  |
| 211 | 204 | 11 | Liquid Propellant |  | Component | Widget.png |  |  | datatable[210] = new Array("211","204","Liquid Propellant","11","Widget.png"); |  |  |  |  |  |
| 212 | 204 | 11 | Prussurant Propellant |  | Component | Widget.png |  |  | datatable[211] = new Array("212","204","Prussurant Propellant","11","Widget.png"); |  |  |  |  |  |
| 213 | 204 | 11 | Other Propellant (Specify) |  | Component | Widget.png |  |  | datatable[212] = new Array("213","204","Other Propellant (Specify)","11","Widget.png"); |  |  |  |  |  |
| 214 | 176 | 11 | Solid Rocket Motors |  | Component | Widget.png |  |  | datatable[213] = new Array("214","176","Solid Rocket Motors","11","Widget.png"); |  |  |  |  |  |
| 215 | 176 | 11 | Power Electronics |  | Component | Widget.png |  |  | datatable[214] = new Array("215","176","Power Electronics","11","Widget.png"); |  |  |  |  |  |
| 216 | 176 | 11 | Propulsion Other (Specify) |  | Component | Widget.png |  |  | datatable[215] = new Array("216","176","Propulsion Other (Specify)","11","Widget.png"); |  |  |  |  |  |
| 217 | 61 | 9 | Telemetry, Tracking, and Command Subsystem (TT&C) |  | Subsystem | Widget.png |  |  | datatable[216] = new Array("217","61","Telemetry, Tracking, and Command Subsystem (TT&C)","9","Widget.png"); |  |  |  |  |  |
| 218 | 212 | 10 | TT&C Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[217] = new Array("218","212","TT&C Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 219 | 213 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[218] = new Array("219","213","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 220 | 213 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[219] = new Array("220","213","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 221 | 213 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[220] = new Array("221","213","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 222 | 213 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[221] = new Array("222","213","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 223 | 213 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[222] = new Array("223","213","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 224 | 212 | 10 | Antennas |  | Assembly | Widget.png |  |  | datatable[223] = new Array("224","212","Antennas","10","Widget.png"); |  |  |  |  |  |
| 225 | 219 | 11 | Omnidirectional |  | Component | Widget.png |  |  | datatable[224] = new Array("225","219","Omnidirectional","11","Widget.png"); |  |  |  |  |  |
| 226 | 219 | 11 | Spiral |  | Component | Widget.png |  |  | datatable[225] = new Array("226","219","Spiral","11","Widget.png"); |  |  |  |  |  |
| 227 | 219 | 11 | Horn |  | Component | Widget.png |  |  | datatable[226] = new Array("227","219","Horn","11","Widget.png"); |  |  |  |  |  |
| 228 | 219 | 11 | Patch |  | Component | Widget.png |  |  | datatable[227] = new Array("228","219","Patch","11","Widget.png"); |  |  |  |  |  |
| 229 | 219 | 11 | Parabolic |  | Component | Widget.png |  |  | datatable[228] = new Array("229","219","Parabolic","11","Widget.png"); |  |  |  |  |  |
| 230 | 219 | 11 | Phased Array |  | Component | Widget.png |  |  | datatable[229] = new Array("230","219","Phased Array","11","Widget.png"); |  |  |  |  |  |
| 231 | 219 | 11 | Other Antennas (Specify) |  | Component | Widget.png |  |  | datatable[230] = new Array("231","219","Other Antennas (Specify)","11","Widget.png"); |  |  |  |  |  |
| 232 | 212 | 10 | Waveguides/Routers |  | Assembly | Widget.png |  |  | datatable[231] = new Array("232","212","Waveguides/Routers","10","Widget.png"); |  |  |  |  |  |
| 233 | 227 | 11 | Diplexers |  | Component | Widget.png |  |  | datatable[232] = new Array("233","227","Diplexers","11","Widget.png"); |  |  |  |  |  |
| 234 | 227 | 11 | Triplexers |  | Component | Widget.png |  |  | datatable[233] = new Array("234","227","Triplexers","11","Widget.png"); |  |  |  |  |  |
| 235 | 227 | 11 | Multiplexers |  | Component | Widget.png |  |  | datatable[234] = new Array("235","227","Multiplexers","11","Widget.png"); |  |  |  |  |  |
| 236 | 227 | 11 | Multicouplers |  | Component | Widget.png |  |  | datatable[235] = new Array("236","227","Multicouplers","11","Widget.png"); |  |  |  |  |  |
| 237 | 227 | 11 | Coaxial Switches |  | Component | Widget.png |  |  | datatable[236] = new Array("237","227","Coaxial Switches","11","Widget.png"); |  |  |  |  |  |
| 238 | 227 | 11 | RF Switches |  | Component | Widget.png |  |  | datatable[237] = new Array("238","227","RF Switches","11","Widget.png"); |  |  |  |  |  |
| 239 | 227 | 11 | Filters |  | Component | Widget.png |  |  | datatable[238] = new Array("239","227","Filters","11","Widget.png"); |  |  |  |  |  |
| 240 | 227 | 11 | Waveguides |  | Component | Widget.png |  |  | datatable[239] = new Array("240","227","Waveguides","11","Widget.png"); |  |  |  |  |  |
| 241 | 227 | 11 | Other Routers (Specify) |  | Component | Widget.png |  |  | datatable[240] = new Array("241","227","Other Routers (Specify)","11","Widget.png"); |  |  |  |  |  |
| 242 | 212 | 10 | Radio Frequency Equipment |  | Assembly | Widget.png |  |  | datatable[241] = new Array("242","212","Radio Frequency Equipment","10","Widget.png"); |  |  |  |  |  |
| 243 | 237 | 11 | Amplifiers |  | Component | Widget.png |  |  | datatable[242] = new Array("243","237","Amplifiers","11","Widget.png"); |  |  |  |  |  |
| 244 | 237 | 11 | Receivers |  | Component | Widget.png |  |  | datatable[243] = new Array("244","237","Receivers","11","Widget.png"); |  |  |  |  |  |
| 245 | 237 | 11 | Transmitters |  | Component | Widget.png |  |  | datatable[244] = new Array("245","237","Transmitters","11","Widget.png"); |  |  |  |  |  |
| 246 | 237 | 11 | Transceivers |  | Component | Widget.png |  |  | datatable[245] = new Array("246","237","Transceivers","11","Widget.png"); |  |  |  |  |  |
| 247 | 237 | 11 | Transponders |  | Component | Widget.png |  |  | datatable[246] = new Array("247","237","Transponders","11","Widget.png"); |  |  |  |  |  |
| 248 | 237 | 11 | Modulators |  | Component | Widget.png |  |  | datatable[247] = new Array("248","237","Modulators","11","Widget.png"); |  |  |  |  |  |
| 249 | 237 | 11 | Demodulators |  | Component | Widget.png |  |  | datatable[248] = new Array("249","237","Demodulators","11","Widget.png"); |  |  |  |  |  |
| 250 | 237 | 11 | Modems |  | Component | Widget.png |  |  | datatable[249] = new Array("250","237","Modems","11","Widget.png"); |  |  |  |  |  |
| 251 | 237 | 11 | Traveling Wave Tube Assemblies |  | Component | Widget.png |  |  | datatable[250] = new Array("251","237","Traveling Wave Tube Assemblies","11","Widget.png"); |  |  |  |  |  |
| 252 | 237 | 11 | Solid State Power Amplifiers |  | Component | Widget.png |  |  | datatable[251] = new Array("252","237","Solid State Power Amplifiers","11","Widget.png"); |  |  |  |  |  |
| 253 | 237 | 11 | Global Positioning System (GPS) Receiver |  | Component | Widget.png |  |  | datatable[252] = new Array("253","237","Global Positioning System (GPS) Receiver","11","Widget.png"); |  |  |  |  |  |
| 254 | 237 | 11 | Downconverters |  | Component | Widget.png |  |  | datatable[253] = new Array("254","237","Downconverters","11","Widget.png"); |  |  |  |  |  |
| 255 | 237 | 11 | Upconverters |  | Component | Widget.png |  |  | datatable[254] = new Array("255","237","Upconverters","11","Widget.png"); |  |  |  |  |  |
| 256 | 237 | 11 | Other RF Equipment (Specify) |  | Component | Widget.png |  |  | datatable[255] = new Array("256","237","Other RF Equipment (Specify)","11","Widget.png"); |  |  |  |  |  |
| 257 | 212 | 10 | Command and Data Handling (C&DH) |  | Assembly | Widget.png |  |  | datatable[256] = new Array("257","212","Command and Data Handling (C&DH)","10","Widget.png"); |  |  |  |  |  |
| 258 | 252 | 11 | Processors |  | Component | Widget.png |  |  | datatable[257] = new Array("258","252","Processors","11","Widget.png"); |  |  |  |  |  |
| 259 | 252 | 11 | Solid State Memory |  | Component | Widget.png |  |  | datatable[258] = new Array("259","252","Solid State Memory","11","Widget.png"); |  |  |  |  |  |
| 260 | 252 | 11 | Decoders |  | Component | Widget.png |  |  | datatable[259] = new Array("260","252","Decoders","11","Widget.png"); |  |  |  |  |  |
| 261 | 252 | 11 | Command Units |  | Component | Widget.png |  |  | datatable[260] = new Array("261","252","Command Units","11","Widget.png"); |  |  |  |  |  |
| 262 | 252 | 11 | Telemetry Units |  | Component | Widget.png |  |  | datatable[261] = new Array("262","252","Telemetry Units","11","Widget.png"); |  |  |  |  |  |
| 263 | 252 | 11 | Command Sequencers |  | Component | Widget.png |  |  | datatable[262] = new Array("263","252","Command Sequencers","11","Widget.png"); |  |  |  |  |  |
| 264 | 252 | 11 | Timing Units |  | Component | Widget.png |  |  | datatable[263] = new Array("264","252","Timing Units","11","Widget.png"); |  |  |  |  |  |
| 265 | 252 | 11 | Frequency Generators |  | Component | Widget.png |  |  | datatable[264] = new Array("265","252","Frequency Generators","11","Widget.png"); |  |  |  |  |  |
| 266 | 252 | 11 | Signal Conditioners |  | Component | Widget.png |  |  | datatable[265] = new Array("266","252","Signal Conditioners","11","Widget.png"); |  |  |  |  |  |
| 267 | 252 | 11 | Data Switches |  | Component | Widget.png |  |  | datatable[266] = new Array("267","252","Data Switches","11","Widget.png"); |  |  |  |  |  |
| 268 | 252 | 11 | Communication Security |  | Component | Widget.png |  |  | datatable[267] = new Array("268","252","Communication Security","11","Widget.png"); |  |  |  |  |  |
| 269 | 252 | 11 | Interface Units |  | Component | Widget.png |  |  | datatable[268] = new Array("269","252","Interface Units","11","Widget.png"); |  |  |  |  |  |
| 270 | 252 | 11 | Tape Recorders |  | Component | Widget.png |  |  | datatable[269] = new Array("270","252","Tape Recorders","11","Widget.png"); |  |  |  |  |  |
| 271 | 252 | 11 | Disk Recorders |  | Component | Widget.png |  |  | datatable[270] = new Array("271","252","Disk Recorders","11","Widget.png"); |  |  |  |  |  |
| 272 | 252 | 11 | Command Sensor or Situational Awareness Sensors |  | Component | Widget.png |  |  | datatable[271] = new Array("272","252","Command Sensor or Situational Awareness Sensors","11","Widget.png"); |  |  |  |  |  |
| 273 | 252 | 11 | Other C&DH (Specify) |  | Component | Widget.png |  |  | datatable[272] = new Array("273","252","Other C&DH (Specify)","11","Widget.png"); |  |  |  |  |  |
| 274 | 212 | 10 | TT&C Other (Specify) |  | Assembly | Widget.png |  |  | datatable[273] = new Array("274","212","TT&C Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 275 | 61 | 9 | Bus Flight Software |  | Subsystem | Widget.png |  |  | datatable[274] = new Array("275","61","Bus Flight Software","9","Widget.png"); |  |  |  |  |  |
| 276 | 275 | 10 | Bus FSW Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[275] = new Array("276","275","Bus FSW Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 277 | 271 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[276] = new Array("277","271","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 278 | 271 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[277] = new Array("278","271","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 279 | 271 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[278] = new Array("279","271","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 280 | 271 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[279] = new Array("280","271","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 281 | 271 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[280] = new Array("281","271","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 282 | 270 | 11 | Thermal Control Software |  | Component | Widget.png |  |  | datatable[281] = new Array("282","270","Thermal Control Software","11","Widget.png"); |  |  |  |  |  |
| 283 | 270 | 11 | Electrical Power Software |  | Component | Widget.png |  |  | datatable[282] = new Array("283","270","Electrical Power Software","11","Widget.png"); |  |  |  |  |  |
| 284 | 270 | 11 | Attitude Control Software |  | Component | Widget.png |  |  | datatable[283] = new Array("284","270","Attitude Control Software","11","Widget.png"); |  |  |  |  |  |
| 285 | 270 | 11 | Telemetry, Tracking, and Command Software |  | Component | Widget.png |  |  | datatable[284] = new Array("285","270","Telemetry, Tracking, and Command Software","11","Widget.png"); |  |  |  |  |  |
| 286 | 270 | 11 | Other Flight Software (Specify) |  | Component | Widget.png |  |  | datatable[285] = new Array("286","270","Other Flight Software (Specify)","11","Widget.png"); |  |  |  |  |  |
| 287 | 59 | 8 | SEITPM and Support Equipment (If Applicable for Integration of Multiple Payloads) |  | System | SEITPM.png |  |  | datatable[286] = new Array("287","59","SEITPM and Support Equipment (If Applicable for Integration of Multiple Payloads)","8","SEITPM.png"); |  |  |  |  |  |
| 288 | 282 | 9 | Project Management |  | Subsystem | SEITPM.png |  |  | datatable[287] = new Array("288","282","Project Management","9","SEITPM.png"); |  |  |  |  |  |
| 289 | 282 | 9 | Systems Engineering |  | Subsystem | SEITPM.png |  |  | datatable[288] = new Array("289","282","Systems Engineering","9","SEITPM.png"); |  |  |  |  |  |
| 290 | 282 | 9 | Mission Assurance |  | Subsystem | SEITPM.png |  |  | datatable[289] = new Array("290","282","Mission Assurance","9","SEITPM.png"); |  |  |  |  |  |
| 291 | 282 | 9 | Assembly, Integration and Testing |  | Subsystem | SEITPM.png |  |  | datatable[290] = new Array("291","282","Assembly, Integration and Testing","9","SEITPM.png"); |  |  |  |  |  |
| 292 | 282 | 9 | Support Equipment |  | Subsystem | SEITPM.png |  |  | datatable[291] = new Array("292","282","Support Equipment","9","SEITPM.png"); |  |  |  |  |  |
| 293 | 59 | 8 | Payload 1 … n (Specify) |  | System | Widget.png |  |  | datatable[292] = new Array("293","59","Payload 1 … n (Specify)","8","Widget.png"); |  |  |  |  |  |
| 294 | 293 | 9 | Payload 1 SEITPM and Support Equipment |  | Subsystem | SEITPM.png |  |  | datatable[293] = new Array("294","293","Payload 1 SEITPM and Support Equipment","9","SEITPM.png"); |  |  |  |  |  |
| 295 | 289 | 10 | Project Management |  | Assembly | SEITPM.png |  |  | datatable[294] = new Array("295","289","Project Management","10","SEITPM.png"); |  |  |  |  |  |
| 296 | 289 | 10 | Systems Engineering |  | Assembly | SEITPM.png |  |  | datatable[295] = new Array("296","289","Systems Engineering","10","SEITPM.png"); |  |  |  |  |  |
| 297 | 289 | 10 | Mission Assurance |  | Assembly | SEITPM.png |  |  | datatable[296] = new Array("297","289","Mission Assurance","10","SEITPM.png"); |  |  |  |  |  |
| 298 | 289 | 10 | Assembly, Integration and Testing |  | Assembly | SEITPM.png |  |  | datatable[297] = new Array("298","289","Assembly, Integration and Testing","10","SEITPM.png"); |  |  |  |  |  |
| 299 | 289 | 10 | Support Equipment |  | Assembly | SEITPM.png |  |  | datatable[298] = new Array("299","289","Support Equipment","10","SEITPM.png"); |  |  |  |  |  |
| 300 | 288 | 9 | Payload 1 Structures and Mechanisms Subsystem |  | Subsystem | Widget.png |  |  | datatable[299] = new Array("300","288","Payload 1 Structures and Mechanisms Subsystem","9","Widget.png"); |  |  |  |  |  |
| 301 | 295 | 10 | Structures and Mechanims Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[300] = new Array("301","295","Structures and Mechanims Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 302 | 296 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[301] = new Array("302","296","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 303 | 296 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[302] = new Array("303","296","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 304 | 296 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[303] = new Array("304","296","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 305 | 296 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[304] = new Array("305","296","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 306 | 296 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[305] = new Array("306","296","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 307 | 295 | 10 | Structures |  | Assembly | Widget.png |  |  | datatable[306] = new Array("307","295","Structures","10","Widget.png"); |  |  |  |  |  |
| 308 | 295 | 10 | Mechanisms and Pyrotechnics |  | Assembly | Widget.png |  |  | datatable[307] = new Array("308","295","Mechanisms and Pyrotechnics","10","Widget.png"); |  |  |  |  |  |
| 309 | 295 | 10 | Structures and Mechanisms Other (Specify) |  | Assembly | Widget.png |  |  | datatable[308] = new Array("309","295","Structures and Mechanisms Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 310 | 288 | 9 | Payload 1 Thermal Control  Subsystem |  | Subsystem | Widget.png |  |  | datatable[309] = new Array("310","288","Payload 1 Thermal Control  Subsystem","9","Widget.png"); |  |  |  |  |  |
| 311 | 310 | 10 | Thermal Control  Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[310] = new Array("311","310","Thermal Control  Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 312 | 306 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[311] = new Array("312","306","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 313 | 306 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[312] = new Array("313","306","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 314 | 306 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[313] = new Array("314","306","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 315 | 306 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[314] = new Array("315","306","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 316 | 306 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[315] = new Array("316","306","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 317 | 316 | 10 | Cryogenic Devices |  | Assembly | Widget.png |  |  | datatable[316] = new Array("317","316","Cryogenic Devices","10","Widget.png"); |  |  |  |  |  |
| 318 | 317 | 10 | Liquid Loops |  | Assembly | Widget.png |  |  | datatable[317] = new Array("318","317","Liquid Loops","10","Widget.png"); |  |  |  |  |  |
| 319 | 318 | 10 | Electric Coolers |  | Assembly | Widget.png |  |  | datatable[318] = new Array("319","318","Electric Coolers","10","Widget.png"); |  |  |  |  |  |
| 320 | 319 | 10 | Electric heaters, Thermisters, and Thermostats |  | Assembly | Widget.png |  |  | datatable[319] = new Array("320","319","Electric heaters, Thermisters, and Thermostats","10","Widget.png"); |  |  |  |  |  |
| 321 | 320 | 10 | Passive Devices |  | Assembly | Widget.png |  |  | datatable[320] = new Array("321","320","Passive Devices","10","Widget.png"); |  |  |  |  |  |
| 322 | 321 | 10 | Sun Shields |  | Assembly | Widget.png |  |  | datatable[321] = new Array("322","321","Sun Shields","10","Widget.png"); |  |  |  |  |  |
| 323 | 322 | 10 | Thermal Control Other (Specify) |  | Assembly | Widget.png |  |  | datatable[322] = new Array("323","322","Thermal Control Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 324 | 288 | 9 | Payload 1 Electrical Power Subsystem |  | Subsystem | Widget.png |  |  | datatable[323] = new Array("324","288","Payload 1 Electrical Power Subsystem","9","Widget.png"); |  |  |  |  |  |
| 325 | 319 | 10 | Electrical Power Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[324] = new Array("325","319","Electrical Power Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 326 | 320 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[325] = new Array("326","320","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 327 | 320 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[326] = new Array("327","320","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 328 | 320 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[327] = new Array("328","320","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 329 | 320 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[328] = new Array("329","320","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 330 | 320 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[329] = new Array("330","320","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 331 | 319 | 10 | Power Sources |  | Assembly | Widget.png |  |  | datatable[330] = new Array("331","319","Power Sources","10","Widget.png"); |  |  |  |  |  |
| 332 | 319 | 10 | Power Control, Switching, and Distribution Electronics |  | Assembly | Widget.png |  |  | datatable[331] = new Array("332","319","Power Control, Switching, and Distribution Electronics","10","Widget.png"); |  |  |  |  |  |
| 333 | 319 | 10 | Power Conditioning, Conversion, and Regulation |  | Assembly | Widget.png |  |  | datatable[332] = new Array("333","319","Power Conditioning, Conversion, and Regulation","10","Widget.png"); |  |  |  |  |  |
| 334 | 319 | 10 | Harnesses and Cables |  | Assembly | Widget.png |  |  | datatable[333] = new Array("334","319","Harnesses and Cables","10","Widget.png"); |  |  |  |  |  |
| 335 | 319 | 10 | Electrical Power Other (Specify) |  | Assembly | Widget.png |  |  | datatable[334] = new Array("335","319","Electrical Power Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 336 | 288 | 9 | Payload 1 Pointing, Command, and Control Interface |  | Subsystem | Widget.png |  |  | datatable[335] = new Array("336","288","Payload 1 Pointing, Command, and Control Interface","9","Widget.png"); |  |  |  |  |  |
| 337 | 336 | 10 | Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[336] = new Array("337","336","Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 338 | 332 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[337] = new Array("338","332","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 339 | 332 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[338] = new Array("339","332","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 340 | 332 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[339] = new Array("340","332","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 341 | 332 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[340] = new Array("341","332","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 342 | 332 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[341] = new Array("342","332","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 343 | 331 | 10 | Computers and Processors |  | Assembly | Widget.png |  |  | datatable[342] = new Array("343","331","Computers and Processors","10","Widget.png"); |  |  |  |  |  |
| 344 | 331 | 10 | Command/Telemetric Units |  | Assembly | Widget.png |  |  | datatable[343] = new Array("344","331","Command/Telemetric Units","10","Widget.png"); |  |  |  |  |  |
| 345 | 331 | 10 | Control Electronics |  | Assembly | Widget.png |  |  | datatable[344] = new Array("345","331","Control Electronics","10","Widget.png"); |  |  |  |  |  |
| 346 | 331 | 10 | Pointing Sensors |  | Assembly | Widget.png |  |  | datatable[345] = new Array("346","331","Pointing Sensors","10","Widget.png"); |  |  |  |  |  |
| 347 | 331 | 10 | Payload Positioners |  | Assembly | Widget.png |  |  | datatable[346] = new Array("347","331","Payload Positioners","10","Widget.png"); |  |  |  |  |  |
| 348 | 331 | 10 | Security, Encryption, and Decryption Devices |  | Assembly | Widget.png |  |  | datatable[347] = new Array("348","331","Security, Encryption, and Decryption Devices","10","Widget.png"); |  |  |  |  |  |
| 349 | 331 | 10 | Data Storage, handling, and Interface |  | Assembly | Widget.png |  |  | datatable[348] = new Array("349","331","Data Storage, handling, and Interface","10","Widget.png"); |  |  |  |  |  |
| 350 | 331 | 10 | Multifunctional Digital Electronic Boxes |  | Assembly | Widget.png |  |  | datatable[349] = new Array("350","331","Multifunctional Digital Electronic Boxes","10","Widget.png"); |  |  |  |  |  |
| 351 | 331 | 10 | Pointing, Command, and Control Interface Other (Specify) |  | Assembly | Widget.png |  |  | datatable[350] = new Array("351","331","Pointing, Command, and Control Interface Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 352 | 288 | 9 | Payload Signal Electronics |  | Subsystem | Widget.png |  |  | datatable[351] = new Array("352","288","Payload Signal Electronics","9","Widget.png"); |  |  |  |  |  |
| 353 | 347 | 10 | Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[352] = new Array("353","347","Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 354 | 348 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[353] = new Array("354","348","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 355 | 348 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[354] = new Array("355","348","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 356 | 348 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[355] = new Array("356","348","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 357 | 348 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[356] = new Array("357","348","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 358 | 348 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[357] = new Array("358","348","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 359 | 347 | 10 | Passive Signal Flow Control |  | Assembly | Widget.png |  |  | datatable[358] = new Array("359","347","Passive Signal Flow Control","10","Widget.png"); |  |  |  |  |  |
| 360 | 347 | 10 | Transmitter/Receiver/Transceiver/Transponder |  | Assembly | Widget.png |  |  | datatable[359] = new Array("360","347","Transmitter/Receiver/Transceiver/Transponder","10","Widget.png"); |  |  |  |  |  |
| 361 | 347 | 10 | Modulators/Demodulators/Modems |  | Assembly | Widget.png |  |  | datatable[360] = new Array("361","347","Modulators/Demodulators/Modems","10","Widget.png"); |  |  |  |  |  |
| 362 | 347 | 10 | Multiplexers/Demultiplexers |  | Assembly | Widget.png |  |  | datatable[361] = new Array("362","347","Multiplexers/Demultiplexers","10","Widget.png"); |  |  |  |  |  |
| 363 | 347 | 10 | Amplifiers |  | Assembly | Widget.png |  |  | datatable[362] = new Array("363","347","Amplifiers","10","Widget.png"); |  |  |  |  |  |
| 364 | 347 | 10 | Frequency Upconverters/Downconverters |  | Assembly | Widget.png |  |  | datatable[363] = new Array("364","347","Frequency Upconverters/Downconverters","10","Widget.png"); |  |  |  |  |  |
| 365 | 347 | 10 | Frequency and Timing |  | Assembly | Widget.png |  |  | datatable[364] = new Array("365","347","Frequency and Timing","10","Widget.png"); |  |  |  |  |  |
| 366 | 347 | 10 | Signal Conditioners |  | Assembly | Widget.png |  |  | datatable[365] = new Array("366","347","Signal Conditioners","10","Widget.png"); |  |  |  |  |  |
| 367 | 347 | 10 | Multifunctional Digital Electronic Boxes |  | Assembly | Widget.png |  |  | datatable[366] = new Array("367","347","Multifunctional Digital Electronic Boxes","10","Widget.png"); |  |  |  |  |  |
| 368 | 347 | 10 | Signal Electronics Other (Specify) |  | Assembly | Widget.png |  |  | datatable[367] = new Array("368","347","Signal Electronics Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 369 | 288 | 9 | Payload 1 Optical Assembly |  | Subsystem | Widget.png |  |  | datatable[368] = new Array("369","288","Payload 1 Optical Assembly","9","Widget.png"); |  |  |  |  |  |
| 370 | 364 | 10 | Subsystem SEITPM |  | Assembly | SEITPM.png |  |  | datatable[369] = new Array("370","364","Subsystem SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 371 | 365 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[370] = new Array("371","365","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 372 | 365 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[371] = new Array("372","365","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 373 | 365 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[372] = new Array("373","365","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 374 | 365 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[373] = new Array("374","365","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 375 | 365 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[374] = new Array("375","365","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 376 | 364 | 10 | Structure/Outerbarrel/Cover |  | Assembly | Widget.png |  |  | datatable[375] = new Array("376","364","Structure/Outerbarrel/Cover","10","Widget.png"); |  |  |  |  |  |
| 377 | 364 | 10 | Mirrors/Optics |  | Assembly | Widget.png |  |  | datatable[376] = new Array("377","364","Mirrors/Optics","10","Widget.png"); |  |  |  |  |  |
| 378 | 364 | 10 | Aft Optics Assembly |  | Assembly | Widget.png |  |  | datatable[377] = new Array("378","364","Aft Optics Assembly","10","Widget.png"); |  |  |  |  |  |
| 379 | 364 | 10 | Alignment and Calibration |  | Assembly | Widget.png |  |  | datatable[378] = new Array("379","364","Alignment and Calibration","10","Widget.png"); |  |  |  |  |  |
| 380 | 364 | 10 | Thermal |  | Assembly | Widget.png |  |  | datatable[379] = new Array("380","364","Thermal","10","Widget.png"); |  |  |  |  |  |
| 374 | 364 | 10 | Control Electronics |  | Assembly | Widget.png |  |  | datatable[373] = new Array("374","364","Control Electronics","10","Widget.png"); |  |  |  |  |  |
| 375 | 364 | 10 | Optical Assembly Other |  | Assembly | Widget.png |  |  | datatable[374] = new Array("375","364","Optical Assembly Other","10","Widget.png"); |  |  |  |  |  |
| 376 | 288 | 9 | Payload 1 Sensor |  | Subsystem | Widget.png |  |  | datatable[375] = new Array("376","288","Payload 1 Sensor","9","Widget.png"); |  |  |  |  |  |
| 377 | 378 | 10 | Sensor SEITPM |  | Assembly | SEITPM.png |  |  | datatable[376] = new Array("377","378","Sensor SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 378 | 379 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[377] = new Array("378","379","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 379 | 379 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[378] = new Array("379","379","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 380 | 379 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[379] = new Array("380","379","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 381 | 379 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[380] = new Array("381","379","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 382 | 379 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[381] = new Array("382","379","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 383 | 378 | 10 | Payload Structure |  | Assembly | Widget.png |  |  | datatable[382] = new Array("383","378","Payload Structure","10","Widget.png"); |  |  |  |  |  |
| 384 | 378 | 10 | Focal Plan Array |  | Assembly | Widget.png |  |  | datatable[383] = new Array("384","378","Focal Plan Array","10","Widget.png"); |  |  |  |  |  |
| 385 | 378 | 10 | Sensor Positioners |  | Assembly | Widget.png |  |  | datatable[384] = new Array("385","378","Sensor Positioners","10","Widget.png"); |  |  |  |  |  |
| 386 | 378 | 10 | Sensor Electronics |  | Assembly | Widget.png |  |  | datatable[385] = new Array("386","378","Sensor Electronics","10","Widget.png"); |  |  |  |  |  |
| 387 | 378 | 10 | Alignment and Calibration |  | Assembly | Widget.png |  |  | datatable[386] = new Array("387","378","Alignment and Calibration","10","Widget.png"); |  |  |  |  |  |
| 388 | 378 | 10 | Magnetometer |  | Assembly | Widget.png |  |  | datatable[387] = new Array("388","378","Magnetometer","10","Widget.png"); |  |  |  |  |  |
| 389 | 378 | 10 | Spectrometer |  | Assembly | Widget.png |  |  | datatable[388] = new Array("389","378","Spectrometer","10","Widget.png"); |  |  |  |  |  |
| 390 | 378 | 10 | Radiometer |  | Assembly | Widget.png |  |  | datatable[389] = new Array("390","378","Radiometer","10","Widget.png"); |  |  |  |  |  |
| 391 | 378 | 10 | Camera |  | Assembly | Widget.png |  |  | datatable[390] = new Array("391","378","Camera","10","Widget.png"); |  |  |  |  |  |
| 392 | 378 | 10 | Sounder |  | Assembly | Widget.png |  |  | datatable[391] = new Array("392","378","Sounder","10","Widget.png"); |  |  |  |  |  |
| 393 | 378 | 10 | Flight Sensor Software |  | Assembly | Widget.png |  |  | datatable[392] = new Array("393","378","Flight Sensor Software","10","Widget.png"); |  |  |  |  |  |
| 394 | 378 | 10 | Other Sensor Types (Specify) |  | Assembly | Widget.png |  |  | datatable[393] = new Array("394","378","Other Sensor Types (Specify)","10","Widget.png"); |  |  |  |  |  |
| 395 | 378 | 10 | Mission Sensor Other (Specify) |  | Assembly | Widget.png |  |  | datatable[394] = new Array("395","378","Mission Sensor Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 396 | 288 | 9 | Payload Flight Software |  | Subsystem | Widget.png |  |  | datatable[395] = new Array("396","288","Payload Flight Software","9","Widget.png"); |  |  |  |  |  |
| 397 | 396 | 10 | Payload 1 FSW SEITPM |  | Assembly | SEITPM.png |  |  | datatable[396] = new Array("397","396","Payload 1 FSW SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 398 | 392 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[397] = new Array("398","392","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 399 | 392 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[398] = new Array("399","392","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 400 | 392 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[399] = new Array("400","392","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 401 | 392 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[400] = new Array("401","392","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 402 | 392 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[401] = new Array("402","392","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 403 | 396 | 10 | CSCI (Specify) |  | Assembly | Widget.png |  |  | datatable[402] = new Array("403","396","CSCI (Specify)","10","Widget.png"); |  |  |  |  |  |
| 404 | 288 | 9 | Payload Antenna 1 … n (Specify) |  | Subsystem | Widget.png |  |  | datatable[403] = new Array("404","288","Payload Antenna 1 … n (Specify)","9","Widget.png"); |  |  |  |  |  |
| 405 | 399 | 10 | Payload 1 Antenna SEITPM |  | Assembly | SEITPM.png |  |  | datatable[404] = new Array("405","399","Payload 1 Antenna SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 406 | 400 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[405] = new Array("406","400","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 407 | 400 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[406] = new Array("407","400","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 408 | 400 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[407] = new Array("408","400","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 409 | 400 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[408] = new Array("409","400","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 410 | 400 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[409] = new Array("410","400","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 411 | 399 | 10 | Structures and Mechanisms |  | Assembly | Widget.png |  |  | datatable[410] = new Array("411","399","Structures and Mechanisms","10","Widget.png"); |  |  |  |  |  |
| 412 | 399 | 10 | Antenna Positioners |  | Assembly | Widget.png |  |  | datatable[411] = new Array("412","399","Antenna Positioners","10","Widget.png"); |  |  |  |  |  |
| 413 | 399 | 10 | Reflector/Horn |  | Assembly | Widget.png |  |  | datatable[412] = new Array("413","399","Reflector/Horn","10","Widget.png"); |  |  |  |  |  |
| 414 | 399 | 10 | Feed |  | Assembly | Widget.png |  |  | datatable[413] = new Array("414","399","Feed","10","Widget.png"); |  |  |  |  |  |
| 415 | 399 | 10 | Waveguide/Coad/Cabling |  | Assembly | Widget.png |  |  | datatable[414] = new Array("415","399","Waveguide/Coad/Cabling","10","Widget.png"); |  |  |  |  |  |
| 416 | 399 | 10 | Transmit/Receive Modules |  | Assembly | Widget.png |  |  | datatable[415] = new Array("416","399","Transmit/Receive Modules","10","Widget.png"); |  |  |  |  |  |
| 417 | 399 | 10 | Antenna Other (Specify) |  | Assembly | Widget.png |  |  | datatable[416] = new Array("417","399","Antenna Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 418 | 288 | 9 | Payload Other (Specify) |  | Subsystem | Widget.png |  |  | datatable[417] = new Array("418","288","Payload Other (Specify)","9","Widget.png"); |  |  |  |  |  |
| 419 | 418 | 10 | Booster Adapter |  | Assembly | Widget.png |  |  | datatable[418] = new Array("419","418","Booster Adapter","10","Widget.png"); |  |  |  |  |  |
| 420 | 418 | 10 | Space Vehicle Storage |  | Assembly | Widget.png |  |  | datatable[419] = new Array("420","418","Space Vehicle Storage","10","Widget.png"); |  |  |  |  |  |
| 421 | 418 | 10 | Space Vehicle Other (Specify) |  | Assembly | Widget.png |  |  | datatable[420] = new Array("421","418","Space Vehicle Other (Specify)","10","Widget.png"); |  |  |  |  |  |
| 422 | 12 | 7 | Launch Systems Integration (LSI) |  |  | Rocket.png |  |  | datatable[421] = new Array("422","12","Launch Systems Integration (LSI)","7","Rocket.png"); |  |  |  |  |  |
| 423 | 12 | 7 | Launch Operations |  |  | Rocket.png |  |  | datatable[422] = new Array("423","12","Launch Operations","7","Rocket.png"); |  |  |  |  |  |
| 424 | 12 | 7 | Launch Operations Support |  |  | Rocket.png |  |  | datatable[423] = new Array("424","12","Launch Operations Support","7","Rocket.png"); |  |  |  |  |  |
| 425 | 12 | 7 | Launch Vehicle Services |  |  | Rocket.png |  |  | datatable[424] = new Array("425","12","Launch Vehicle Services","7","Rocket.png"); |  |  |  |  |  |
| 426 | 12 | 7 | Launch Insurance |  |  | Rocket.png |  |  | datatable[425] = new Array("426","12","Launch Insurance","7","Rocket.png"); |  |  |  |  |  |
| 427 | 13 | 7 | Ground Segment SEITPM |  | Assembly | SEITPM.png |  |  | datatable[426] = new Array("427","13","Ground Segment SEITPM","7","SEITPM.png"); |  |  |  |  |  |
| 428 | 422 | 8 | Project Management |  | Component | SEITPM.png |  |  | datatable[427] = new Array("428","422","Project Management","8","SEITPM.png"); |  |  |  |  |  |
| 429 | 422 | 8 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[428] = new Array("429","422","Systems Engineering","8","SEITPM.png"); |  |  |  |  |  |
| 430 | 422 | 8 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[429] = new Array("430","422","Mission Assurance","8","SEITPM.png"); |  |  |  |  |  |
| 431 | 422 | 8 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[430] = new Array("431","422","Assembly, Integration and Testing","8","SEITPM.png"); |  |  |  |  |  |
| 432 | 422 | 8 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[431] = new Array("432","422","Support Equipment","8","SEITPM.png"); |  |  |  |  |  |
| 433 | 13 | 7 | Mission Control Centers |  |  | Facility.png |  |  | datatable[432] = new Array("433","13","Mission Control Centers","7","Facility.png"); |  |  |  |  |  |
| 434 | 13 | 7 | Science / Data Ops Centers |  |  | Facility.png |  |  | datatable[433] = new Array("434","13","Science / Data Ops Centers","7","Facility.png"); |  |  |  |  |  |
| 435 | 13 | 7 | Terminals and Data Networks – incl Antennas  |  |  | Facility.png |  |  | datatable[434] = new Array("435","13","Terminals and Data Networks – incl Antennas ","7","Facility.png"); |  |  |  |  |  |
| 436 | 13 | 7 | Data Distribution & Archival  |  |  | Facility.png |  |  | datatable[435] = new Array("436","13","Data Distribution & Archival ","7","Facility.png"); |  |  |  |  |  |
| 437 | 13 | 7 | Training Facilities  |  |  | Facility.png |  |  | datatable[436] = new Array("437","13","Training Facilities ","7","Facility.png"); |  |  |  |  |  |
| 438 | 433 | 8 | CSA Mission Control |  |  | Facility.png |  |  | datatable[437] = new Array("438","433","CSA Mission Control","8","Facility.png"); |  |  |  |  |  |
| 439 | 438 | 9 | SatOps Mission Control Complex at JHCSC  |  |  | Facility.png |  |  | datatable[438] = new Array("439","438","SatOps Mission Control Complex at JHCSC ","9","Facility.png"); |  |  |  |  |  |
| 440 | 438 | 9 | ISS Mission Operations Complex |  |  | Facility.png |  |  | datatable[439] = new Array("440","438","ISS Mission Operations Complex","9","Facility.png"); |  |  |  |  |  |
| 441 | 433 | 8 | NASA Mission Operations Complex |  |  | Facility.png |  |  | datatable[440] = new Array("441","433","NASA Mission Operations Complex","8","Facility.png"); |  |  |  |  |  |
| 442 | 435 | 10 | RMPSR |  |  | Facility.png |  |  | datatable[441] = new Array("442","435","RMPSR","10","Facility.png"); |  |  |  |  |  |
| 443 | 435 | 10 | OEC |  |  | Facility.png |  |  | datatable[442] = new Array("443","435","OEC","10","Facility.png"); |  |  |  |  |  |
| 444 | 435 | 10 | PTOC |  |  | Facility.png |  |  | datatable[443] = new Array("444","435","PTOC","10","Facility.png"); |  |  |  |  |  |
| 445 | 439 | 10 | SatOps Mission control SEITPM |  | Assembly | SEITPM.png |  |  | datatable[444] = new Array("445","439","SatOps Mission control SEITPM","10","SEITPM.png"); |  |  |  |  |  |
| 446 | 440 | 11 | Project Management |  | Component | SEITPM.png |  |  | datatable[445] = new Array("446","440","Project Management","11","SEITPM.png"); |  |  |  |  |  |
| 447 | 440 | 11 | Systems Engineering |  | Component | SEITPM.png |  |  | datatable[446] = new Array("447","440","Systems Engineering","11","SEITPM.png"); |  |  |  |  |  |
| 448 | 440 | 11 | Mission Assurance |  | Component | SEITPM.png |  |  | datatable[447] = new Array("448","440","Mission Assurance","11","SEITPM.png"); |  |  |  |  |  |
| 449 | 440 | 11 | Assembly, Integration and Testing |  | Component | SEITPM.png |  |  | datatable[448] = new Array("449","440","Assembly, Integration and Testing","11","SEITPM.png"); |  |  |  |  |  |
| 450 | 440 | 11 | Support Equipment |  | Component | SEITPM.png |  |  | datatable[449] = new Array("450","440","Support Equipment","11","SEITPM.png"); |  |  |  |  |  |
| 451 | 434 | 10 | Hardware Components |  |  | Facility.png |  |  | datatable[450] = new Array("451","434","Hardware Components","10","Facility.png"); |  |  |  |  |  |
| 452 | 446 | 11 | Workstations |  |  | Facility.png |  |  | datatable[451] = new Array("452","446","Workstations","11","Facility.png"); |  |  |  |  |  |
| 453 | 446 | 11 | Servers |  |  | Facility.png |  |  | datatable[452] = new Array("453","446","Servers","11","Facility.png"); |  |  |  |  |  |
| 454 | 446 | 11 | Storage and Archive |  |  | Facility.png |  |  | datatable[453] = new Array("454","446","Storage and Archive","11","Facility.png"); |  |  |  |  |  |
| 455 | 446 | 11 | Network Equipment |  |  | Facility.png |  |  | datatable[454] = new Array("455","446","Network Equipment","11","Facility.png"); |  |  |  |  |  |
| 456 | 446 | 11 | Interface Equipment |  |  | Facility.png |  |  | datatable[455] = new Array("456","446","Interface Equipment","11","Facility.png"); |  |  |  |  |  |
| 457 | 446 | 11 | Security Encryption/Decryption |  |  | Facility.png |  |  | datatable[456] = new Array("457","446","Security Encryption/Decryption","11","Facility.png"); |  |  |  |  |  |
| 458 | 446 | 11 | Data Processing |  |  | Facility.png |  |  | datatable[457] = new Array("458","446","Data Processing","11","Facility.png"); |  |  |  |  |  |
| 459 | 446 | 11 | COTS Hardware Other (Specify) |  |  | Facility.png |  |  | datatable[458] = new Array("459","446","COTS Hardware Other (Specify)","11","Facility.png"); |  |  |  |  |  |
| 460 | 446 | 11 | Pre-Operations Maintenance (Specify) |  |  | Facility.png |  |  | datatable[459] = new Array("460","446","Pre-Operations Maintenance (Specify)","11","Facility.png"); |  |  |  |  |  |
| 461 | 446 | 11 | Environments |  |  | Facility.png |  |  | datatable[460] = new Array("461","446","Environments","11","Facility.png"); |  |  |  |  |  |
| 462 | 434 | 10 | SatOps GS Software |  |  | Facility.png |  |  | datatable[461] = new Array("462","434","SatOps GS Software","10","Facility.png"); |  |  |  |  |  |
| 463 | 462 | 11 | SW CSCI |  |  | Facility.png |  |  | datatable[462] = new Array("463","462","SW CSCI","11","Facility.png"); |  |  |  |  |  |
| 464 | 429 | 8 | NASA Science Operations Centers |  |  | Facility.png |  |  | datatable[463] = new Array("464","429","NASA Science Operations Centers","8","Facility.png"); |  |  |  |  |  |
| 465 | 429 | 8 | HPC (High Performance Computing) |  |  | Facility.png |  |  | datatable[464] = new Array("465","429","HPC (High Performance Computing)","8","Facility.png"); |  |  |  |  |  |
| 466 | 429 | 8 | Geospace Observatory |  |  | Facility.png |  |  | datatable[465] = new Array("466","429","Geospace Observatory","8","Facility.png"); |  |  |  |  |  |
| 467 | 429 | 8 | Other SODC (specify) |  |  | Facility.png |  |  | datatable[466] = new Array("467","429","Other SODC (specify)","8","Facility.png"); |  |  |  |  |  |
| 468 | 435 | 8 |  CSA Terminals and Antennas |  |  | Facility.png |  |  | datatable[467] = new Array("468","435"," CSA Terminals and Antennas","8","Facility.png"); |  |  |  |  |  |
| 469 | 463 | 9 | CSA St-Hubert Antenna |  |  | Facility.png |  |  | datatable[468] = new Array("469","463","CSA St-Hubert Antenna","9","Facility.png"); |  |  |  |  |  |
| 470 | 463 | 9 | Ferme Yves Bachand Antenna |  |  | Facility.png |  |  | datatable[469] = new Array("470","463","Ferme Yves Bachand Antenna","9","Facility.png"); |  |  |  |  |  |
| 471 | 463 | 9 | Ferme Beldor Antenna |  |  | Facility.png |  |  | datatable[470] = new Array("471","463","Ferme Beldor Antenna","9","Facility.png"); |  |  |  |  |  |
| 472 | 463 | 9 | Transponder |  |  | Facility.png |  |  | datatable[471] = new Array("472","463","Transponder","9","Facility.png"); |  |  |  |  |  |
| 473 | 431 | 8 | Digital Earth Canada |  |  | Facility.png |  |  | datatable[472] = new Array("473","431","Digital Earth Canada","8","Facility.png"); |  |  |  |  |  |
| 474 | 431 | 8 | Federal Geospatial Platform (FGP) |  |  | Facility.png |  |  | datatable[473] = new Array("474","431","Federal Geospatial Platform (FGP)","8","Facility.png"); |  |  |  |  |  |
| 475 | 431 | 8 | EODMS |  |  | Facility.png |  |  | datatable[474] = new Array("475","431","EODMS","8","Facility.png"); |  |  |  |  |  |
| 476 | 431 | 8 | Canadian Astronomy Data Centre |  |  | Facility.png |  |  | datatable[475] = new Array("476","431","Canadian Astronomy Data Centre","8","Facility.png"); |  |  |  |  |  |
| 477 | 431 | 8 | NASA Data Distribution & Archival |  |  | Facility.png |  |  | datatable[476] = new Array("477","431","NASA Data Distribution & Archival","8","Facility.png"); |  |  |  |  |  |
| 478 | 437 | 8 | MMLC |  |  | Facility.png |  |  | datatable[477] = new Array("478","437","MMLC","8","Facility.png"); |  |  |  |  |  |
| 479 | 437 | 8 | MOTS |  |  | Facility.png |  |  | datatable[478] = new Array("479","437","MOTS","8","Facility.png"); |  |  |  |  |  |
| 480 | 14 | 7 | CSA Mission Operations |  |  | Ops.png |  |  | datatable[479] = new Array("480","14","CSA Mission Operations","7","Ops.png"); |  |  |  |  |  |
| 481 | 475 | 8 | CSA SatOps |  |  | Ops.png |  |  | datatable[480] = new Array("481","475","CSA SatOps","8","Ops.png"); |  |  |  |  |  |
| 482 | 475 | 8 | CSA ISS Ops |  |  | Ops.png |  |  | datatable[481] = new Array("482","475","CSA ISS Ops","8","Ops.png"); |  |  |  |  |  |
| 483 | 475 | 8 | CSA ISS Sustaining Engineering |  |  | Ops.png |  |  | datatable[482] = new Array("483","475","CSA ISS Sustaining Engineering","8","Ops.png"); |  |  |  |  |  |
| 484 | 14 | 7 | NASA Mission Operations |  |  | Ops.png |  |  | datatable[483] = new Array("484","14","NASA Mission Operations","7","Ops.png"); |  |  |  |  |  |
| 485 | 14 | 7 | Industry Partners (Specify) |  |  | Ops.png |  |  | datatable[484] = new Array("485","14","Industry Partners (Specify)","7","Ops.png"); |  |  |  |  |  |
| 486 | 15 | 7 | Mission Science Support |  |  | Science.png |  |  | datatable[485] = new Array("486","15","Mission Science Support","7","Science.png"); |  |  |  |  |  |
| 487 | 481 | 8 | Science Maturation Studies & User Requirements |  |  | Science.png |  |  | datatable[486] = new Array("487","481","Science Maturation Studies & User Requirements","8","Science.png"); |  |  |  |  |  |
| 488 | 481 | 8 | Science Support for Mission Development |  |  | Science.png |  |  | datatable[487] = new Array("488","481","Science Support for Mission Development","8","Science.png"); |  |  |  |  |  |
| 489 | 481 | 8 | Science Support for Commissioning, Including Cal/Val |  |  | Science.png |  |  | datatable[488] = new Array("489","481","Science Support for Commissioning, Including Cal/Val","8","Science.png"); |  |  |  |  |  |
| 490 | 481 | 8 | Science Support for Data Handling |  |  | Science.png |  |  | datatable[489] = new Array("490","481","Science Support for Data Handling","8","Science.png"); |  |  |  |  |  |
| 491 | 15 | 7 | Science Utilization & Application Development |  |  | Science.png |  |  | datatable[490] = new Array("491","15","Science Utilization & Application Development","7","Science.png"); |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 2 - Phasing Nomenclature

| ` Table of Contents |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |
| 7 - Phasing Nomenclature |  |  |  |  |  |  |  | What do you call your phases?  |  |
| Why we we asking: |  |  |  |  |  |  |  |  |  |
|  | 1. To normalize the naming convention across all investments.  |  |  |  |  |  |  |  |  |
|  | 2. Math Models are based on Costing Sub-Phase. |  |  |  |  |  |  |  |  |
|  | 3. We want to output results in your naming convention and scope. |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  | Based on IGMF rev E |  |  |  | Based on CSA-FIN-RPT-0072 |  |  |  |  |
| Phasing according to |  |  |  | Phasing according to |  |  |  | Phasing according to |  |
| EPMO |  |  |  | Costing |  |  |  | PM |  |
|  |  |  |  | PREP | PREP 1 | Prototyping Activities (before Gate 1) |  |  |  |
| Pre-Project | Option Analysis & Planning Phase | Pre-Phase 0 |  |  | PREP 2 | Prototyping Activities (during Phase 0/A) |  |  |  |
|  |  | Phase 0 |  | Phase 0/A | Phase 0 | Concept & Feasibility |  | Phase 0 |  |
| Project | Definition Phase | Detailed Project Requirements |  |  | Phase A | Mission Requirements |  | Phase A |  |
|  |  | Preliminary Definition |  | Phase B/C | Phase B | Preliminary Design |  | Phase B |  |
|  |  | Detailed Definition |  |  | Phase C | Detailed Design |  | Phase C |  |
|  | Implementation Phase | Implementation |  | Phase D | MAIT |  Manufacturing, Assembly, Integration and Test of Canadian Subsystems and Components |  | Phase D |  |
|  |  |  |  |  | SAIT | Spacecraft Level Assembly, Test |  | Phase D |  |
|  |  |  |  |  | LEOP | Lauch and early operations |  | Phase D |  |
| Post-Project | Post-Implementation Phase | Operations & Disposal |  | Phase E | Phase E |  Nominal Operations (per design life) |  | Phase E |  |
|  |  |  |  | Phase E (EXT) | Phase X |  Extended operations (mission extension) |  |  |  |
|  |  |  |  | Phase F | Phase F |  Disposal (incl. post-mortem audit reports) |  | Phase F |  |
|  |  |  |  | Phase G | Phase G |  Post-Mortem science utilization |  |  |  |
|  |  |  |  |  |  |  |  |  |  |

## 3 - Phase Durations

| ` Table of Contents |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7b - Phasing Durations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Why we we asking: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1. Durations affect Govt Salaries calculations |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2. Durations affect Parametric estimates for Space segment, ground segment, ops |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 3. Schedule Scenarios are inputs to sensitivity analysis |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Schedule Scenario ID | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Scenario Name | Nominal Schedule Used by Gaby for RAM calculation (PM Nomenclature) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Scenario Description | Phases 0 through F |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Rationale | ORCA concept-stage schedule, consistent with CADRe Part A section 2.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Source Doc  | CADRe Part A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Phase | Expected Start | Expected End | Total D | Total M | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | 2040 | 2041 | 2042 | 2043 | 2044 | 2045 | 2046 | 2047 | 2048 | 2049 | 2050 | 2051 | 2052 | 2053 | 2054 | 2055 | 2056 | 2057 | 2058 | 2059 | 2060 |
|  | Phase 0 | 2026-01-01 00:00:00 | 2027-12-31 00:00:00 | 729 | 23.96712328767123 | 2.958904109589041 | 12 | 9.04109589041096 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Phase A | 2028-01-01 00:00:00 | 2029-12-31 00:00:00 | 730 | 24 | 0 | 0 | 2.9917808219178084 | 12 | 9.04109589041096 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Phase B1 | 2030-01-01 00:00:00 | 2030-12-31 00:00:00 | 364 | 11.967123287671233 | 0 | 0 | 0 | 0 | 2.958904109589041 | 9.04109589041096 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Phase B2 | 2031-01-01 00:00:00 | 2031-12-31 00:00:00 | 364 | 11.967123287671233 | 0 | 0 | 0 | 0 | 0 | 2.958904109589041 | 9.04109589041096 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Phase C | 2032-01-01 00:00:00 | 2033-12-31 00:00:00 | 730 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 2.9917808219178084 | 12 | 9.04109589041096 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Phase D | 2034-01-01 00:00:00 | 2040-12-31 00:00:00 | 2556 | 84.03287671232877 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.958904109589041 | 12 | 12.032876712328768 | 12 | 12 | 12 | 12.032876712328768 | 9.04109589041096 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Phase E | 2041-01-01 00:00:00 | 2055-12-31 00:00:00 | 5477 | 180.06575342465754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.958904109589041 | 12 | 12 | 12.032876712328768 | 12 | 12 | 12 | 12.032876712328768 | 12 | 12 | 12 | 12.032876712328768 | 12 | 12 | 12 | 9.04109589041096 | 0 | 0 | 0 | 0 |
|  | Phase X | 2056-01-01 00:00:00 | 2059-06-30 00:00:00 | 1276 | 41.95068493150685 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.9917808219178084 | 12 | 12 | 12 | 2.9917808219178084 |
|  | Phase F | 2059-07-01 00:00:00 | 2059-12-28 00:00:00 | 180 | 5.917808219178082 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5.950684931506849 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Phase D1-MAIT | 2034-01-01 00:00:00 | 2038-06-30 00:00:00 | 1641 | 53.950684931506856 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2.958904109589041 | 12 | 12.032876712328768 | 12 | 12 | 2.9917808219178084 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Phase D2-SAIT | 2038-07-01 00:00:00 | 2040-09-30 00:00:00 | 822 | 27.024657534246572 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9.008219178082193 | 12.032876712328768 | 6.016438356164384 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | Phase D3-LEOP | 2040-10-01 00:00:00 | 2040-12-31 00:00:00 | 91 | 2.9917808219178084 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3.0246575342465754 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## PM's sched Scenarios

|  |  | ORCA Ref. | 2026-01-01 00:00:00 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Phase | Milestone | ORCA Baseline | Orbiter Platform (Partner Agency) | ORCA Instrument Suite | Worst case duration | Worst case (+2 mo/phase) | Realistic case duration | Baseline: Realistic case date (1 month delay per phase) | Optimistic case duration | Optimistic case | Comments |  |  |  |  |  |
| Phase 0 | Mission Concept Review (MCR) | 2027-12-31 00:00:00 | N/A | N/A | 25.919842312746386 | 2028-02-29 00:00:00 | 24.967148488830485 | 2028-01-31 00:00:00 | 22.93035479632063 | 2027-11-30 00:00:00 | End of Phase 0; mission concept baseline. |  |  |  |  |  |
| Phase A | System Requirements Review (SRR) | 2029-12-31 00:00:00 | N/A | N/A | 51.905387647831795 | 2030-04-30 00:00:00 | 49.90144546649146 | 2030-02-28 00:00:00 | 45.959264126149804 | 2029-10-31 00:00:00 | End of Phase A. |  |  |  |  |  |
| Phase A | ORCA Concept Rebaseline | 2029-07-01 12:00:00 | N/A | N/A | 45.992115637319316 | 2029-11-01 00:00:00 | 43.98817345597897 | 2029-09-01 00:00:00 | 39.94743758212878 | 2029-05-01 00:00:00 | Programmatic baseline update within Phase A. |  | Phases | Duration (months) | Expected start | Expected finish |
| Phase B | Orbiter Bus / ORCA Instrument Suite Interface Complete | 2031-03-14 09:36:00 | Interface requirements | Interface requirements | 68.39684625492772 | 2031-09-14 00:00:00 | 65.37450722733246 | 2031-06-14 00:00:00 | 59.39553219448094 | 2030-12-14 00:00:00 | Partner-agency orbiter interface control document (ICD) finalized. |  | Phase 0 | 23.96712328767123 | 2026-01-01 00:00:00 | 2027-12-31 00:00:00 |
| Phase B | Preliminary Design Review (PDR) | 2031-12-31 00:00:00 | Bus accommodation | Preliminary design | 77.92378449408672 | 2032-06-30 00:00:00 | 74.93429697766096 | 2032-03-31 00:00:00 | 68.92247043363994 | 2031-09-30 00:00:00 | End of Phase B (B1+B2). |  | Phase A | 24 | 2028-01-01 00:00:00 | 2029-12-31 00:00:00 |
| Phase C | Instrument Suite Environmental Qualification Complete | 2033-03-14 00:00:00 | N/A | Qualification | 94.41524310118265 | 2033-11-14 00:00:00 | 90.37450722733246 | 2033-07-14 00:00:00 | 82.42444152431011 | 2032-11-14 00:00:00 | Vibration / thermal-vacuum qualification of the ORCA instrument suite. |  | Phase B1 | 11.967123287671233 | 2030-01-01 00:00:00 | 2030-12-31 00:00:00 |
| Phase C | Critical Design Review (CDR) | 2033-12-31 00:00:00 | Bus accommodation | Critical design | 103.94218134034165 | 2034-08-31 00:00:00 | 99.90144546649145 | 2034-04-30 00:00:00 | 91.95137976346912 | 2033-08-31 00:00:00 | End of Phase C. |  | Phase B2 | 11.967123287671233 | 2031-01-01 00:00:00 | 2031-12-31 00:00:00 |
| MAIT | Manufacturing Readiness Review (MRR) | 2036-03-31 12:00:00 | N/A | N/A | 132.98291721419184 | 2037-01-31 00:00:00 | 127.95663600525624 | 2036-08-31 00:00:00 | 117.93692509855452 | 2035-10-31 00:00:00 | Mid-MAIT manufacturing readiness checkpoint. |  | Phase C | 24 | 2032-01-01 00:00:00 | 2033-12-31 00:00:00 |
| MAIT | Pre-Ship Review of Systems to Prime (PSR) | 2040-07-04 00:00:00 | Integration readiness | Integration readiness | 184.03416557161628 | 2041-05-04 00:00:00 | 179.0735873850197 | 2040-12-04 00:00:00 | 169.0867279894875 | 2040-02-04 00:00:00 | ~6 months before launch. |  | Phase D | 84.03287671232877 | 2034-01-01 00:00:00 | 2040-12-31 00:00:00 |
| SAIT | Integrated Instrument Suite Functional Test Complete | 2040-08-31 00:00:00 | N/A | Functional test | 185.90670170827858 | 2041-06-30 00:00:00 | 180.9789750328515 | 2041-01-31 00:00:00 | 170.92641261498028 | 2040-03-31 00:00:00 | Ahead of System Integration Review. |  | Phase E | 180.06575342465754 | 2041-01-01 00:00:00 | 2055-12-31 00:00:00 |
| SAIT | System Integration Review (SIR) | 2040-09-30 00:00:00 | Bus integration | Instrument integration | 186.892247043364 | 2041-07-30 00:00:00 | 181.89881734559788 | 2041-02-28 00:00:00 | 171.9119579500657 | 2040-04-30 00:00:00 | ORCA integrated onto partner-agency orbiter bus. |  | Phase X | 41.95068493150685 | 2056-01-01 00:00:00 | 2059-06-30 00:00:00 |
| SAIT | Acceptance Review (AR) | 2040-10-02 00:00:00 | Flight acceptance | Flight acceptance | 186.99080157687254 | 2041-08-02 00:00:00 | 181.96452036793693 | 2041-03-02 00:00:00 | 171.97766097240472 | 2040-05-02 00:00:00 | ~3 months before launch. |  | Phase F | 5.917808219178082 | 2059-07-01 00:00:00 | 2059-12-28 00:00:00 |
| SAIT | Flight Software and Autonomy Verification Complete | 2040-11-01 00:00:00 | N/A | N/A | 187.97634691195793 | 2041-09-01 00:00:00 | 182.95006570302232 | 2041-04-01 00:00:00 | 172.96320630749014 | 2040-06-01 00:00:00 | Autonomy and fault-management software verified. |  | Total | 407.8684931506849 |  |  |
| LEOP | Pre-Ship Review – Spacecraft to Launch Site | 2040-11-16 00:00:00 | Bus checkout | N/A | 188.46911957950064 | 2041-09-16 00:00:00 | 183.44283837056503 | 2041-04-16 00:00:00 | 173.45597897503285 | 2040-06-16 00:00:00 | Before shipment to launch site. |  |  |  |  |  |
| LEOP | Launch | 2040-12-31 00:00:00 | N/A | N/A | 189.94743758212877 | 2041-10-31 00:00:00 | 184.92115637319316 | 2041-05-31 00:00:00 | 174.93429697766098 | 2040-07-31 00:00:00 | End of Phase D; Jupiter gravity-assist trajectory. |  |  |  |  |  |
| LEOP | Commissioning Review (CR) | 2041-01-14 00:00:00 | Bus checkout | Instrument checkout | 190.40735873850196 | 2041-11-14 00:00:00 | 185.38107752956634 | 2041-06-14 00:00:00 | 175.39421813403416 | 2040-08-14 00:00:00 | Post-launch systems checkout, ~2 weeks after launch. |  |  |  |  |  |
| Phase E | Start of Nominal Operations | 2041-01-01 00:00:00 | N/A | Plume sampling begins | 191.98423127463863 | 2042-01-01 00:00:00 | 185.9395532194481 | 2041-07-01 00:00:00 | 173.94875164257556 | 2040-07-01 00:00:00 | Start of Phase E. |  |  |  |  |  |
| Phase E | End of Nominal Operations | 2055-12-31 00:00:00 | N/A | N/A | 371.9448094612352 | 2056-12-31 00:00:00 | 365.90013140604464 | 2056-06-30 00:00:00 | 353.8764783180026 | 2055-06-30 00:00:00 | End of Phase E; 4-year prime science mission. |  |  |  |  |  |
| Phase X | End of Life / Disposal Operations Complete | 2059-06-30 00:00:00 | N/A | N/A | 415.90013140604464 | 2060-08-30 00:00:00 | 408.9027595269382 | 2060-01-30 00:00:00 | 394.90801576872536 | 2058-11-30 00:00:00 | End of Phase X; optional mission extension. |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ORCA Milestone Reference |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Milestone | Realistic Date |  | Phase | Purpose |  |  |  |  |  |  |  |  |  |  |  |
|  | Mission Concept Review (MCR) | 2027-12-31 00:00:00 |  | Phase 0 | Mission concept baseline |  |  |  |  |  |  |  |  |  |  |  |
|  | System Requirements Review (SRR) | 2029-12-31 00:00:00 |  | Phase A | Requirements baseline |  |  |  |  |  |  |  |  |  |  |  |
|  | ORCA Concept Rebaseline | 2029-07-01 12:00:00 |  | Phase A | Programmatic baseline update |  |  |  |  |  |  |  |  |  |  |  |
|  | Orbiter Bus / ORCA Instrument Suite Interface Complete | 2031-03-14 09:36:00 |  | Phase B | Interface control document finalized |  |  |  |  |  |  |  |  |  |  |  |
|  | Preliminary Design Review (PDR) | 2031-12-31 00:00:00 |  | Phase B | Preliminary design maturity |  |  |  |  |  |  |  |  |  |  |  |
|  | Instrument Suite Environmental Qualification Complete | 2033-03-14 00:00:00 |  | Phase C | Instrument suite qualification |  |  |  |  |  |  |  |  |  |  |  |
|  | Critical Design Review (CDR) | 2033-12-31 00:00:00 |  | Phase C | Design baseline approval |  |  |  |  |  |  |  |  |  |  |  |
|  | Manufacturing Readiness Review (MRR) | 2036-03-31 12:00:00 |  | MAIT | Manufacturing readiness |  |  |  |  |  |  |  |  |  |  |  |
|  | Pre-Ship Review of Systems to Prime (PSR) | 2040-07-04 00:00:00 |  | MAIT | Transfer readiness |  |  |  |  |  |  |  |  |  |  |  |
|  | Integrated Instrument Suite Functional Test Complete | 2040-08-31 00:00:00 |  | SAIT | Functional test readiness |  |  |  |  |  |  |  |  |  |  |  |
|  | System Integration Review (SIR) | 2040-09-30 00:00:00 |  | SAIT | Integrated system readiness |  |  |  |  |  |  |  |  |  |  |  |
|  | Acceptance Review (AR) | 2040-10-02 00:00:00 |  | SAIT | Flight acceptance |  |  |  |  |  |  |  |  |  |  |  |
|  | Flight Software and Autonomy Verification Complete | 2040-11-01 00:00:00 |  | SAIT | Software verification |  |  |  |  |  |  |  |  |  |  |  |
|  | Pre-Ship Review – Spacecraft to Launch Site | 2040-11-16 00:00:00 |  | LEOP | Launch-site readiness |  |  |  |  |  |  |  |  |  |  |  |
|  | Launch | 2040-12-31 00:00:00 |  | LEOP | Launch |  |  |  |  |  |  |  |  |  |  |  |
|  | Commissioning Review (CR) | 2041-01-14 00:00:00 |  | LEOP | Commissioning complete |  |  |  |  |  |  |  |  |  |  |  |
|  | Start of Nominal Operations | 2041-01-01 00:00:00 |  | Phase E | Plume-sampling operations begin |  |  |  |  |  |  |  |  |  |  |  |
|  | End of Nominal Operations | 2055-12-31 00:00:00 |  | Phase E | Nominal mission complete |  |  |  |  |  |  |  |  |  |  |  |
|  | End of Life / Disposal Operations Complete | 2059-06-30 00:00:00 |  | Phase X | Mission closeout |  |  |  |  |  |  |  |  |  |  |  |

## GR&A

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Costing CSA Ground Rules & Assumptions template  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Last review |  |  | 2025-03-31 00:00:00 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ID | Catégorie | Category | Category | Sub-category | Items | GR or A | Title | Description | Phase | CBS # linked to GR&A | Impact on Project | Impact on costing, methodology, models, tools & analysis | Excepted source  | Do not delete | Source/Link | Other rational  | Waiver deviation  |
| 1 | Hypothèses Programmatiques | Strategy Naratives | Objectifs politiques et stratégiques | Alignement sur la stratégie de l’ASC |  |  |  |  |  |  |  |  | Business Case et/ou CADRE Part C onglet CM list | Strategy |  |  |  |
| 2 | Hypothèses Programmatiques | Strategy Naratives | Objectifs politiques et stratégiques | Contraintes gouvernementales ou directives de haut niveau |  |  |  |  |  |  |  |  | Business Case et/ou CADRE Part C onglet CM list | Strategy |  |  |  |
| 3 | Hypothèses Programmatiques |  | Objectifs politiques et stratégiques | Type de mission : Flagship, LargeSat, SmallSat, NanoSat, Hosted Payload, Data stream partnership, data stream purchase |  |  |  |  |  |  |  |  | CADRE Part A | CADRE Part A ou contants |  |  |  |
| 4 | Hypothèses Programmatiques |  | Objectifs politiques et stratégiques | Disciplines et secteur : SatCom, Astronomie, exploration spatiale,... |  |  |  |  |  |  |  |  | CADRE Part A | CADRE Part A |  |  |  |
| 5 | Hypothèses Programmatiques |  | Objectifs politiques et stratégiques | Dépendances avec d'autres projets/missions |  |  |  |  |  |  |  |  | CADRE Part A | CADRE Part A |  |  |  |
| 6 | Hypothèses Programmatiques | Strategy Naratives | Budget global et financement | Soumission au Conseil du Tésor (TBSub) - But de l'exercice de costing : Budget Ask, Reprofiling,… Définir le nombre de TBSub + échéancier associé aux TBSub |  |  |  |  |  |  |  |  | CADRE Part C onglet Stratégie contractuelle   | Strategy |  |  |  |
| 7 | Hypothèses Programmatiques | Strategy Naratives | Budget global et financement | Enveloppe de la masse salariale  |  |  |  |  |  |  |  |  | CADRE Part C onglet RAM | Strategy |  |  |  |
| 8 | Hypothèses Programmatiques | Strategy Naratives | Budget global et financement | Enveloppe des frais de gestion et plan de voyages |  |  |  |  |  |  |  |  | CADRE Part C onglet Overhead Costs | Strategy |  |  |  |
| 9 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Méthodologie d'établissement des coûts  |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts | Costing Plan |  |  |  |
| 10 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Note de réflexion supplémentaire |  |  |  |  |  |  |  |  |  | Costing Plan |  |  |  |
| 11 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Au moins 2 façon différentes pour chaque incluant RAM |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts - Méthodologies | Costing Plan |  |  |  |
| 12 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Analyse de sensibilité |  |  |  |  |  |  |  |  | À compléter par Finance | Costing Plan |  |  |  |
| 13 | Hypothèses Programmatiques | Costign Plan | Budget global et financement |  Sufficiency Report or Independent Cost Estimate or Independent Cost Review  |  |  |  |  |  |  |  |  | À compléter par Finance | Costing Plan |  |  |  |
| 14 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Analogie (nearest neighboors), lesquels. |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts - Méthodologies | Costing Plan |  |  |  |
| 15 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Analyse paramétrique (True planning, PCEC, NCIM, SEER, Compact). CER Calibration Plan. |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts - Méthodologies | Costing Plan |  |  |  |
| 16 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Soumission de l'industrie et jugement d'expert |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts - Méthodologies | Costing Plan |  |  |  |
| 17 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Analyse Monte Carlo (crystal ball) |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts - Méthodologies | Costing Plan |  |  |  |
| 18 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Bottom up, qui le fait et comment |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts - Méthodologies | Costing Plan |  |  |  |
| 19 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Learning curves  |  |  |  |  |  |  |  |  | RASCI =  qui fait quoi. bottom up = Plan de l’exercice d’établissement des coûts | Costing Plan |  |  |  |
| 20 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Inducteurs de coûts princicaux  |  |  |  |  |  |  |  |  | CADRE Part C onglet CER & Tools | Costing Plan |  |  |  |
| 21 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Normalisation ( Stochométrie) - si applicable  |  |  |  |  |  |  |  |  | le choix de l'outil dicte CADRE part B qui collecte info pour l'analyse paramétrique | Costing Plan |  |  |  |
| 22 | Hypothèses Programmatiques | Costign Plan | Budget global et financement | Tracabilité - accès aux sources - répertoires normalisés -liens |  |  |  |  |  |  |  |  | CADRE Part C onglet CER & Tools | Costing Plan |  |  |  |
| 23 | Hypothèses Programmatiques | Strategy Naratives | Budget global et financement | Stratégie de financement |  |  |  |  |  |  |  |  | Business Case et/ou CADRE Part C onglet CM list | Strategy |  |  |  |
| 24 | Hypothèses Programmatiques | Strategy Naratives | Budget global et financement | Limitation des coûts :  Par exemple, les sources de financement instables, les contraintes de personnel ou un budget à ne pas dépasser devraient être documentés. |  |  |  |  |  |  |  |  | CADRE Part C onglet Stratégie contractuelle   | Strategy |  |  |  |
| 25 | Hypothèses Programmatiques | Strategy Naratives | Budget global et financement | Enveloppe Services internes - O&M et RAM  |  |  |  |  |  |  |  |  | CADRE Part C onglet Services internes | Strategy |  |  |  |
| 26 | Hypothèses Programmatiques | OBS | Partenariats (OGD, internationaux, industriels) | Rôles et responsabilités des principaux partenaires (agences spatiales, industriels, universités et autres ministères) |  |  |  |  |  |  |  |  | CADRE Part C onglet OBS | OBS |  |  |  |
| 27 | Hypothèses Programmatiques | OBS | Partenariats (OGD, internationaux, industriels) | Modalités de partage des coûts et des risques |  |  |  |  |  |  |  |  | CADRE Part C onglet OBS - Cost Sharing provisions | OBS |  |  |  |
| 28 | Hypothèses Programmatiques | Strategy Naratives | Partenariats (OGD, internationaux, industriels) | Si applicable, dépenses éligibles de l'OTAN |  |  |  |  |  |  |  |  | À définir ici | Strategy |  |  |  |
| 29 | Hypothèses Programmatiques | 8. Economic Constants and short answers | Gouvernance et autorités | Ordre de grandeur général du projet (petit, moyen, grand, flagship) |  |  |  |  |  |  |  |  | CERCES scale | Constants |  |  |  |
| 30 | Hypothèses Programmatiques | Costign Plan | Gouvernance et autorités | Nature of the costing perimeter (degree of difficulty of costing exercise) |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts | Costing Plan |  |  |  |
| 31 | Hypothèses Programmatiques | 8. Economic Constants and short answers | Gouvernance et autorités | Palier/ Tier |  |  |  |  |  |  |  |  | Business Case et/ou CADRE Part C onglet CM list | Constants |  |  |  |
| 32 | Hypothèses Programmatiques | 8. Economic Constants and short answers | Gouvernance et autorités | PCRA |  |  |  |  |  |  |  |  | Business Case et/ou CADRE Part C onglet CM list | Constants |  |  |  |
| 33 | Hypothèses Programmatiques | Milestone Register | Gouvernance et autorités | Point de décision |  |  |  |  |  |  |  |  | CADRE Part C - onglet Phasing Model | Milestone Register |  |  |  |
| 34 | Hypothèses Programmatiques | Costign Plan | Gouvernance et autorités | Costing Exercise Schedule and associated milestones - Costing Plan, Internal WebReport Dashboard and power BI dashboard for CLAD |  |  |  |  |  |  |  |  | Plan de l’exercice d’établissement des coûts | Costing Plan |  |  |  |
| 35 | Hypothèses Financières | 8. Inflation Model | Indices économiques et inflation | Taux d’inflation annuel, indice utilisé (IPC, indice sectoriel), taux de déflation |  |  |  |  |  |  |  |  | Inflation Model dans son propre document - Oracle db ID | Inflation Model |  |  |  |
| 36 | Hypothèses Financières | 8. Economic Constants and short answers | Indices économiques et inflation | Taux EBP 27% |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 37 | Hypothèses Financières | 8. Inflation Model | Indices économiques et inflation | Modèle d'inflation appliqué |  |  |  |  |  |  |  |  | Inflation Model dans son propre document - Oracle db ID | Inflation Model |  |  |  |
| 38 | Hypothèses Financières | 8. Economic Constants and short answers | Indices économiques et inflation | Année de base / Base year  |  |  |  |  |  |  |  |  |  | Constants |  |  |  |
| 39 | Hypothèses Financières | 8. Economic Constants and short answers | Indices économiques et inflation | SSC 4% |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 40 | Hypothèses Financières | 8. Economic Constants and short answers | Indices économiques et inflation | PSPC 13% |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 41 | Hypothèses Financières | 8. Economic Constants and short answers | Indices économiques et inflation | Taux du Fairness Monitor  |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 42 | Hypothèses Financières | 8. Economic Constants and short answers | Taux de change | Monnaies concernées et valeur de référence (CAD, USD, EUR, etc.) |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 43 | Hypothèses Financières | 8. Economic Constants and short answers | Taux de change | Seuil de variation accepté avant révision budgétaire |  |  |  |  |  |  |  |  | Defined in constnats, used in risk analysis. risk reserve - Risk register | Constants |  |  |  |
| 44 | Hypothèses Financières | 8. Economic Constants and short answers | Contingence et marges de sécurité | Pourcentage de contingence sur le coût total du projet (p. ex. 10 à 20 %) |  |  |  |  |  |  |  |  | Defined in constnats, used in risk analysis. risk register  onglet. Unknown-Unknown Risk margin | Constants |  |  |  |
| 45 | Hypothèses Financières | Strategy Naratives | Contingence et marges de sécurité | Barème d’évaluation des risques majeurs pour justifier la marge appliquée (modèle d’analyse de risques) |  |  |  |  |  |  |  |  | À définir ici  | Strategy | Je ne comprends pas la question |  |  |
| 46 | Hypothèses Financières | Procurement Plan | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Sunk Costs Report (STDP, EOADP, Cap Demo, Stedia FAST, ESA Program, Cubesats, space hub, Pre-Phase 0 etc) |  |  |  |  |  |  |  |  | CADRe part C - Expenditure plan | Procurement Plan |  |  |  |
| 47 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Stratégie contractuel Phase 0/A - 1 / 2 contrats |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 48 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Note de réflexion supplémentaire |  |  |  |  |  |  |  |  |  | Strategy |  |  |  |
| 49 | Hypothèses Financières | Procurement Plan | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Nombre de contrats et valeur approximative prévus par phase |  |  |  |  |  |  |  |  | CADRe Part C - Procurement Plan (list) | Procurement Plan |  |  |  |
| 50 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Contrats en parallèle avec des concepts différents et un down select |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 51 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Agile ou waterfall |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 52 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | STDP ou CapDemo en même temps que la phase 0 ou A |  |  |  |  |  |  |  |  | PREP 2 | Strategy |  |  |  |
| 53 | Hypothèses Financières | OBS | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Les fournisseurs attendus et leur capacite de production  |  |  |  |  |  |  |  |  | OBS | OBS |  |  |  |
| 54 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Type de SOW - SOW directif versus une architecture de mission proposée par le fournisseur |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 55 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Freedom of Design of Vendor |  |  |  |  |  |  |  |  | CADRE Part C onglet OBS Maturité orgnisationelle du fourniseur | Strategy |  |  |  |
| 56 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Types de contrat – source unique ou compétitif (Contrat dirigé en Phase E ops aura une incidence sur le design du ground segment)  |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 57 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Types de contrat – cout remboursable ou prix ferme |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
|  | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Type de contrat: gonogo, options, milestones in April for CAFÉ |  |  |  |  |  |  |  |  |  | Strategy | Split next line into 2 |  |  |
| 58 | Hypothèses Financières | 12 - Dispose, Divest, Descope, Delay | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Gestion du scope change et des risques dans chaque situation : cout remboursable (TA, options, gouvernance) ; prix ferme (descope, go no go, qualité du SOW a décrire le scope) |  |  |  |  |  |  |  |  | Descope est dans DDD | DDDD |  |  |  |
| 59 | Hypothèses Financières |  | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | G&C (cassiope ou radarsat 2) nous appartient pas |  |  |  |  |  |  |  |  | Business model (CADRe part A) et le procurement strategy le repete | CADRE Part A |  |  |  |
| 60 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | incitatif commercial (ex. modele de commercialization comme a prior mission)  |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 61 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Pour chaque phase et sous-systeme majeur -  CSA led, industry led, academia led (ex. En Phase E, CSA va mener les operations) |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 62 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Competitif - ouvert a l'international |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 63 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Competitif - ouvert au Canada |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 64 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Fausse competition |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 65 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | monopole |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 66 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Dependences : Le fournisseur X doit etre le meme fournisseur que le fournisseur Y (Ex. Data processing handled by same supplier) |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 67 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Long lead Item - flux de trésorie en capital vs contrat vs échéancier |  |  |  |  |  |  |  |  | CADRE Part C onglet QUANTITIES - LLI, spares, EM, PFM, RE-NRE | Strategy |  |  |  |
| 68 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Contenu Canadien |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 69 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Chaque contrat couvre quel partie du travail, liste d'inclusions et exclusions. List of inclusions and exclusions |  |  |  |  |  |  |  |  | CBS Dictionary | Strategy |  |  |  |
| 70 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | GFE and GFS (ex. DFL) |  |  |  |  |  |  |  |  | CBS Dictionary | Strategy |  |  |  |
| 71 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Frais de transport et responsabilité |  |  |  |  |  |  |  |  | CBS Dictionary | Strategy |  |  |  |
| 72 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Frais d'assurance et limitation de responsabilité |  |  |  |  |  |  |  |  | CBS Dictionary | Strategy |  |  |  |
| 73 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Qualité du SOW |  |  |  |  |  |  |  |  | RISK posture | Strategy |  |  |  |
| 74 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Stabilité des exigences. Par exemple, des exigences très instables, un nombre standard de demandes de modification technique, des exigences stables avec peu ou pas de changements attendus, etc. |  |  |  |  |  |  |  |  | CADRe Part C - Procurement strategy  | Strategy |  |  |  |
| 75 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Résultats du RFI |  |  |  |  |  |  |  |  | Procurement strategy | Strategy |  |  |  |
| 76 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Stratégie contractuelle Phase BCD - Concurrentiel, source unique (voir note de réflexion du point 2.4.1) |  |  |  |  |  |  |  |  | Procurement strategy | Strategy |  |  |  |
| 77 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Stratégie contractuelle Phase EF - Concurrentiel, source unique (voir note de réflexion du point 2.4.1) |  |  |  |  |  |  |  |  | Procurement strategy | Strategy |  |  |  |
| 78 | Hypothèses Financières | Strategy Naratives | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Capacité du vendeur dans le marché actuel, surcharge contractuel, effectif disponible |  |  |  |  |  |  |  |  | OBS Maturité orgnisationelle du fourniseur | Strategy |  |  |  |
| 79 | Hypothèses Financières | 8. Economic Constants and short answers | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Taux standard pour les ingénieurs, techniciens, gestionnaires, etc. |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 80 | Hypothèses Financières | 8. Economic Constants and short answers | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Taux spécifiques pour les consultants ou experts externes |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 81 | Hypothèses Financières | 8. Economic Constants and short answers | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Barème pour les appels d’offres et la sous-traitance (plafonds, politiques internes) |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 82 | Hypothèses Financières | 8. Economic Constants and short answers | Stratégie contractuelle, coûts de main-d’œuvre et de sous-traitance | Taux de frais et de profit appliqué au contrat |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 83 | Hypothèses Financières | Risk Register | Plan de gestion des risques financiers | Existence d’une réserve pour risques identifiés (p. ex. volatilité du marché, retards de paiement) |  |  |  |  |  |  |  |  | Registre de risque | Risk Register |  |  |  |
| 84 | Hypothèses Financières | 12 - Dispose, Divest, Descope, Delay | Plan de gestion des risques financiers | Descope Plan and other strategies to deal with funding shortfalls,  |  |  |  |  |  |  |  |  | À définir ici et lié au CADRE Part C - onglet DDDD | DDDD |  |  |  |
| 85 | Hypothèses Financières | Procurement Plan | Plan de gestion des risques financiers | Source of funding for each CBS element and Risk to A-Base |  |  |  |  |  |  |  |  | Expenditure plan | Procurement Plan |  |  |  |
| 86 | Hypothèses Financières | 8. Economic Constants and short answers | Taxes  | Pays, province et taux de taxes applicables |  |  |  |  |  |  |  |  | Financial Constants Reports  - CSA-FIN-RPT-XXXX rev 3 | Constants |  |  |  |
| 87 | Hypothèses Techniques (Space & Ground Segment) | TRRA | Technologie et niveau de maturité (TRL) | TRL initial prévu pour les composants clés |  |  |  |  |  |  |  |  | CADRE Part C onglet TRL | TRL |  |  |  |
| 88 | Hypothèses Techniques (Space & Ground Segment) | TRRA | Technologie et niveau de maturité (TRL) | Objectifs de TRL à atteindre pour chaque phase du projet |  |  |  |  |  |  |  |  | CADRE Part C onglet TRL | TRL |  |  |  |
| 89 | Hypothèses Techniques (Space & Ground Segment) | 4a. CBS and CBS Dictionary | Sous-systèmes et architecture globale  | Liste et description des principaux sous-systèmes (structure, propulsion, contrôle d’attitude, communication, etc.) |  |  |  |  |  |  |  |  | CBS | CBS |  |  |  |
| 90 | Hypothèses Techniques (Space & Ground Segment) | TRRA | Sous-systèmes et architecture globale  | Interfaces critiques (par ex. protocole de communication, alignement mécanique) |  |  |  |  |  |  |  |  | TRL assessment tab - worry list | TRL |  |  |  |
| 91 | Hypothèses Techniques (Space & Ground Segment) | Costign Plan | Sous-systèmes et architecture globale  | This ground rule should state, at a high level, what is within scope of the estimate. For example, an estimate may cover the space segment, ground segment, and government oversight during phases B, C and D. Further clarification should be given if required, such as refurbishment of the ground segment rather than complete rebuild. |  |  |  |  |  |  |  |  | Perimeter of costing exercise. Further Claraifications in CBs dictionary | Costing Plan |  |  |  |
| 92 | Hypothèses Techniques (Space & Ground Segment) |  | Durée de vie du projet et cycles de développement | Stratégie de validation (modèles d’ingénierie, prototypes, simulations) |  |  |  |  |  |  |  |  | CADRE Part C onglet QUANTITIES - LLI, spares, EM, PFM, RE-NRE | Quantities |  |  |  |
| 93 | Hypothèses Techniques (Space & Ground Segment) |  | Durée de vie du projet et cycles de développement | Méthodes d’essais en environnement (thermique, vibration, vide, etc.) |  |  |  |  |  |  |  |  | CADRE Part C onglet QUANTITIES - LLI, spares, EM, PFM, RE-NRE | Quantities |  |  |  |
| 94 | Hypothèses Techniques (Space & Ground Segment) |  | Durée de vie du projet et cycles de développement | This assumption should state the expected build approach for the mission. For example, the bus/platform and payloads could be built in series or parallel. |  |  |  |  |  |  |  |  | CADRE Part C onglet QUANTITIES - LLI, spares, EM, PFM, RE-NRE | Quantities |  |  |  |
| 95 | Hypothèses Techniques (Space & Ground Segment) |  | Durée de vie du projet et cycles de développement | This assumption should state the cost improvement curve, as a percentile, for any items to be acquired with more than a single unit. If appropriate, items should be marked as Xth unit within a lot, such as the 8th unit, to allow for cost improvement curve theory to be reflected. |  |  |  |  |  |  |  |  | CADRE Part C onglet QUANTITIES - LLI, spares, EM, PFM, RE-NRE | Quantities |  |  |  |
| 96 | Hypothèses Techniques (Space & Ground Segment) | Engineering Parameters in CADRe part B | Contraintes techniques spécifiques | Estimation de masse et de volume du système |  |  |  |  |  |  |  |  | CADRE part B | CADRE part B |  |  |  |
| 97 | Hypothèses Techniques (Space & Ground Segment) | Engineering Parameters in CADRe part B | Contraintes techniques spécifiques | Consommation électrique maximale |  |  |  |  |  |  |  |  | CADRE part B | CADRE part B |  |  |  |
| 98 | Hypothèses Techniques (Space & Ground Segment) | Engineering Parameters in CADRe part B | Contraintes techniques spécifiques | Besoins minimaux pour assurer la fiabilité |  |  |  |  |  |  |  |  | CADRE part B | CADRE part B |  |  |  |
| 99 | Hypothèses Qualité, Fiabilité et Sécurité | Strategy Naratives | Normes et standards de qualité | ECSS-Q-ST-20, ISO 9001, etc. |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 100 | Hypothèses Qualité, Fiabilité et Sécurité | Strategy Naratives | Normes et standards de qualité | Méthodes d’assurance qualité (revues, audits internes et externes) |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 101 | Hypothèses Qualité, Fiabilité et Sécurité | 8. Economic Constants and short answers | Safety and mission assurance | Classe de Mission  |  |  |  |  |  |  |  |  | À définir ici  | Constants |  |  |  |
| 102 | Hypothèses Qualité, Fiabilité et Sécurité | Strategy Naratives | Safety and mission assurance | La mesure de la surveillance et de la rigueur appliquées par la CSA |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 103 | Hypothèses Opérationnelles | RAM | Ressources humaines et expertise | Équipe de base (ETP internes) et besoins en personnel spécialisé externe |  |  |  |  |  |  |  |  | CADRE Part C onglet RAM | RAM |  |  |  |
| 104 | Hypothèses Opérationnelles | Strategy Naratives | Ressources humaines et expertise | Disponibilité du personnel et plan de montée en compétence |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 105 | Hypothèses Opérationnelles | Milestone Register | Calendrier, jalons et ressources temporelles | Dates clés (ex. PDR – Preliminary Design Review, CDR – Critical Design Review, FRR – Flight Readiness Review) / Project Milestone Register (short report, detailed report) |  |  |  |  |  |  |  |  | milestone Register | Milestone Register |  |  |  |
| 106 | Hypothèses Opérationnelles |  | Calendrier, jalons et ressources temporelles | Diagram of Phase Overlaps and Gaps |  |  |  |  |  |  |  |  | we draw it form phasing | GANTT Charts |  |  |  |
| 107 | Hypothèses Opérationnelles | Schedule Constraints and Dependencies | Calendrier, jalons et ressources temporelles | Marges pour délais |  |  |  |  |  |  |  |  | Phasing Model, phases | Schedule Constraints |  |  |  |
| 108 | Hypothèses Opérationnelles | 12 - Dispose, Divest, Descope, Delay | Calendrier, jalons et ressources temporelles | Gestion des retards : conditions de replanification, procédures d’escalade |  |  |  |  |  |  |  |  | À définir ici et lié au CADRE Part C - onglet DDDD | DDDD |  |  |  |
| 109 | Hypothèses Opérationnelles | Phasing Schedules | Calendrier, jalons et ressources temporelles | Modèle de phase utilisé pour analyse de sensibilité (Phasing Model) |  |  |  |  |  |  |  |  | Phasing model (for risk analysis) | Phasing Schedules |  |  |  |
| 110 | Hypothèses Opérationnelles | Phasing Schedules | Calendrier, jalons et ressources temporelles | Échéancier de l'industrie  |  |  |  |  |  |  |  |  | Phasing model (for risk analysis) | Phasing Schedules |  |  |  |
| 111 | Hypothèses Opérationnelles | Phasing Schedules | Calendrier, jalons et ressources temporelles | Schedule Scenarios for sensitivity analysis : Adjust Durations - optimistic, pessimistic and expected |  |  |  |  |  |  |  |  | Phasing model (for risk analysis) | Phasing Schedules |  |  |  |
| 112 | Hypothèses Opérationnelles | Strategy Naratives | Planification des infrastructures et installations | Is DFL being used as GFE |  |  |  |  |  |  |  |  | DFL being used? Strategy | Strategy |  |  |  |
| 112 | Hypothèses Opérationnelles | 4a. CBS and CBS Dictionary | Planification des infrastructures et installations | Lieux de développement, sites d’intégration et de test (chambres à vide, bancs de test) |  |  |  |  |  |  |  |  | CBS Dictionary - Ground Segment - Test facilities | CBS Dictionary |  |  |  |
| 113 | Hypothèses Opérationnelles | Schedule Constraints and Dependencies | Planification des infrastructures et installations | Disponibilité des installations (ex. créneaux de test partagés avec d’autres projets) |  |  |  |  |  |  |  |  | schedule risk =  risk register -> pessimistic schedule model | Schedule Constraints |  |  |  |
| 114 | Hypothèses Opérationnelles | Schedule Constraints and Dependencies | Gestion de la logistique et de la chaîne d’approvisionnement | Délai de livraison des composants critiques (satellites, propulseurs, éléments électroniques) |  |  |  |  |  |  |  |  | schedule risk =  risk register -> pessimistic schedule model | Schedule Constraints |  |  |  |
| 115 | Hypothèses Opérationnelles | Strategy Naratives | Gestion de la logistique et de la chaîne d’approvisionnement | Plans de contingence en cas de rupture d’approvisionnement |  |  |  |  |  |  |  |  | CADRE Part C onglet DDDD - dispose, descope, divest, delay | Strategy |  |  |  |
| 116 | Hypothèses Opérationnelles |  | Plan de gestion de mission (SatOps) | Description des opérations prévues : phases de lancement, mise à l’orbite, opérations nominales, etc. |  |  |  |  |  |  |  |  | Cadre part A | CADRE Part A |  |  |  |
| 117 | Hypothèses Opérationnelles |  | Plan de gestion de mission (SatOps) | Mode de supervision et contrôle (centres de contrôle, horaires, équipes) |  |  |  |  |  |  |  |  | À définir ici  | Cadre Part A |  |  |  |
| 118 | Hypothèses Opérationnelles |  | Plan de gestion de mission (SatOps) | Mission Operation Center |  |  |  |  |  |  |  |  | À définir ici  | Cadre Part A |  |  |  |
| 119 | Hypothèses Opérationnelles |  | Plan de gestion de mission (SatOps) | GoC Science Operation Centers (SOCs) |  |  |  |  |  |  |  |  | À définir ici  | Cadre Part A |  |  |  |
| 120 | Hypothèses Opérationnelles |  | Plan de gestion de mission (SatOps) | External Science Operation Centers (ESOCs) |  |  |  |  |  |  |  |  | À définir ici  | Cadre Part A |  |  |  |
| 121 | Hypothèses sur la science | Schedule Constraints and Dependencies | Science et applications | Échéancier lié au volet de science du projet |  |  |  |  |  |  |  |  |  | Schedule Constraints |  |  |  |
| 122 | Hypothèses sur la science | Strategy Naratives | Science et applications | Expected cost of science utilization related to the mission. |  |  |  |  |  |  |  |  |  | Strategy |  |  |  |
| 123 | Hypothèses sur la science | Strategy Naratives | Portée de la mission sur le milieu public et académique | Coût en lien avec la portée de la mission |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 124 | Hypothèses Lancement |  | Véhicule de lancement | Sélection du lanceur (ex. Falcon 9, Ariane, etc.) ou fenêtre de lancement partagée |  |  |  |  |  |  |  |  | Cadre part A | CADRE Part A |  |  |  |
| 125 | Hypothèses Lancement |  | Véhicule de lancement | Capacités du lanceur (masse, volume, orbite cible) |  |  |  |  |  |  |  |  | Cadre part A un petit peu et le reste dans le LV database CM list | CADRE Part A |  |  |  |
| 126 | Hypothèses Lancement | Schedule Constraints and Dependencies | Calendrier de lancement | Fenêtres de lancement disponibles (contraintes de météo, alignement orbital, etc.) |  |  |  |  |  |  |  |  | schedule risk =  risk register -> pessimistic schedule model | Schedule assumptions and constraints for JCL Analysis |  |  |  |
| 127 | Hypothèses Lancement | 12 - Dispose, Divest, Descope, Delay | Calendrier de lancement | Contingences pour reports éventuels |  |  |  |  |  |  |  |  | schedule risk =  risk register -> pessimistic schedule model | DDDD |  |  |  |
| 128 | Hypothèses Lancement | OBS | Contrat et services associés | Responsabilités du fournisseur de lancement (intégration, tests, qualification) |  |  |  |  |  |  |  |  | OBS (roles et responsiblity) - CSa qui paye ou MDa qui paye | OBS |  |  |  |
| 129 | Hypothèses Lancement | 4a. CBS and CBS Dictionary | Contrat et services associés | Assurances (couverture du satellite, du lanceur, etc.) |  |  |  |  |  |  |  |  | CBS Dictionary - if insurance | CBS Dictionary |  |  |  |
| 130 | Hypothèses Opérations en orbite  |  | Mode opératoire | Gestion du satellite ou rover (téléopération vs. autonomie) |  |  |  |  |  |  |  |  |  | Cadre Part A |  |  |  |
| 131 | Hypothèses Opérations en orbite  | Engineering Parameters in CADRe part B | Mode opératoire | Durée et fréquence des communications |  |  |  |  |  |  |  |  | CADRE Part B | CADRE part B |  |  |  |
| 132 | Hypothèses Opérations en orbite  |  | Maintenance, réparations et évolutions | Possibilité ou non de mise à jour logicielle en vol (OTA updates) |  |  |  |  |  |  |  |  | CADRE part A - Bus FSW section | CADRE Part A |  |  |  |
| 133 | Hypothèses Opérations en orbite  |  | Maintenance, réparations et évolutions | Stratégiques de réparation ou d’assistance robotique  |  |  |  |  |  |  |  |  | CADRE part A - does it have any robotic repair interfaces | CADRE Part A |  |  |  |
| 134 | Hypothèses Opérations en orbite  | 12 - Dispose, Divest, Descope, Delay | Fin de mission et désorbitation | Scénario de désorbitation contrôlée ou passivation (réservoirs, batteries) |  |  |  |  |  |  |  |  | CADRE Part C onglet DDDD - dispose, descope, divest, delay | DDDD |  |  |  |
| 135 | Hypothèses Opérations en orbite  | 12 - Dispose, Divest, Descope, Delay | Fin de mission et désorbitation | Dépôt sur orbite-cimetière pour le matériel en fin de vie (si admissible) |  |  |  |  |  |  |  |  | CADRE Part C onglet DDDD - dispose, descope, divest, delay | DDDD |  |  |  |
| 136 | Hypothèses Opérations en orbite  | Strategy Naratives | Flux de documentation et reporting | Fréquence des rapports d’avancement (hebdomadaires, mensuels) |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 137 | Hypothèses Opérations en orbite  | Strategy Naratives | Classifications et diffusion | Niveau de confidentialité (projet public, secret défense, propriété intellectuelle) |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 138 | Hypothèses Opérations en orbite  | Strategy Naratives | Classifications et diffusion | Politiques de publication ou de diffusion des résultats |  |  |  |  |  |  |  |  | À définir ici et/ou Business Case | Strategy |  |  |  |
| 139 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Réglementations gouvernementales | Exigences fédérales (agences spatiales, ministères, etc.) |  |  |  |  |  |  |  |  | À définir ici et/ou Business Case | Strategy |  |  |  |
| 140 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Réglementations gouvernementales | Normes internationales (ECSS, ISO, NASA, CSA, etc.) |  |  |  |  |  |  |  |  | À définir ici et/ou Business Case | Strategy |  |  |  |
| 141 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Réglementations gouvernementales | Règles et régulations afférentes |  |  |  |  |  |  |  |  | À définir ici et/ou Business Case | Strategy |  |  |  |
| 142 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Contrôle à l’exportation (ex. ITAR, EAR) | Identification des composants ou technologies soumis à licences |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 143 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Contrôle à l’exportation (ex. ITAR, EAR) | Implications sur la gestion des fournisseurs et des partenaires étrangers |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 144 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Sécurité et sûreté | Mesures de cybersécurité (protection des données, des communications, etc.) |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 145 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Sécurité et sûreté | Exigences de sûreté pour le personnel et les installations (accès restreints, habilitations) |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 146 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Droit spatial et aspects juridiques | Propriété et exploitation des données spatiales |  |  |  |  |  |  |  |  | À définir ici  | Strategy |  |  |  |
| 147 | Hypothèses Légales, Réglementaires et Sécuritaires | 12 - Dispose, Divest, Descope, Delay | Droit spatial et aspects juridiques | Protocole en cas de débris spatiaux, en fin de vie du satellite |  |  |  |  |  |  |  |  | CADRE Part C onglet DDDD - dispose, descope, divest, delay | DDDD |  |  |  |
| 148 | Hypothèses Légales, Réglementaires et Sécuritaires | Strategy Naratives | Propriété intellectuelle | Propriété intellectuel en lien avec le projet - enjeux  |  |  |  |  |  |  |  |  | À définir ici et/ou Business Case | Strategy |  |  |  |
| 149 | Hypothèses Environnementales | 12 - Dispose, Divest, Descope, Delay | Gestion des débris spatiaux | Respect des lignes directrices d’atténuation des débris (liaisons, désorbitation en fin de vie) |  |  |  |  |  |  |  |  | CADRE Part C onglet DDDD - dispose, descope, divest, delay | DDDD |  |  |  |
| 150 | Hypothèses Environnementales | 12 - Dispose, Divest, Descope, Delay | Gestion des débris spatiaux | Méthodes envisagées pour minimiser la pollution orbitale |  |  |  |  |  |  |  |  | CADRE Part C onglet DDDD - dispose, descope, divest, delay | DDDD |  |  |  |
| 151 | Hypothèses Environnementales | Green space | Impacts environnementaux terrestres | Contrôle des émissions lors du lancement (polluants, bruit, etc.) |  |  |  |  |  |  |  |  | CADRE Part C onglet Green Space | Green Space |  |  |  |
| 152 | Hypothèses Environnementales | Strategy Naratives | Impacts environnementaux terrestres | Politique de recyclage ou de réutilisation des composants |  |  |  |  |  |  |  |  | CADRE Part C onglet Green Space | Strategy |  |  |  |
| 153 | Hypothèses sur le risques | Risk Register | Risques  | Risque du Projet Phase A à D |  |  |  |  |  |  |  |  | Registre de risque | Risk Register |  |  |  |
| 154 | Hypothèses sur le risques | Risk Register | Risques  | Risque du Projet Phase E |  |  |  |  |  |  |  |  | Registre de risque | Risk Register |  |  |  |
| 155 | Hypothèses sur le risques | Risk Register | Risques  | Risque du Projet Phase F |  |  |  |  |  |  |  |  | Registre de risque | Risk Register |  |  |  |
| 156 | Hypothèses sur le risques | Risk Register | Risques  | Risque Science |  |  |  |  |  |  |  |  | Registre de risque | Risk Register |  |  |  |
| 157 | Hypothèses sur le risques | Risk Register | Risques  | Risque Salaire |  |  |  |  |  |  |  |  | Registre de risque | Risk Register |  |  |  |
| 158 | Hypothèses sur le risques | Risk Register | Risques  | Schedule Risk Assessment file (ms project) as input to the Joint Cost and Schedule Confidence Analysis Report |  |  |  |  |  |  |  |  | Registre de risque | Risk Register |  |  |  |
| 159 | Hypothèses sur le risques | Risk Register | Risques  | Registre de risque |  |  |  |  |  |  |  |  | Registre de risque | Risk Register |  |  |  |
| 160 | Hypothèses sur le risques | Strategy Naratives | Risques  | Aspect critique de la mission et impact si la mission n'est pas respectée |  |  |  |  |  |  |  |  | minimum mission success criteria - DRM - CADRE part C Taxon | Strategy |  |  |  |
| 161 | Hypothèse sur les mesures de performance par la valeur acquise | CADRe part D - EVM | Mesures de performance par la valeur acquise (EVM = Earn Value Management) | Seuil orange et rouge pour EVM justifiant une réduction de la portée, une replanification |  |  |  |  |  |  |  |  |  | pas dans ce fichier, pas avant PDR |  |  |  |
| 162 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 163 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 164 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 165 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 166 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 167 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 168 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 169 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 170 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 171 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 172 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 173 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 174 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 175 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 176 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 177 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 178 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 179 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 180 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 181 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 182 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 183 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 184 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 185 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 186 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 187 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 188 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 189 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 190 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 191 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 192 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 193 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 194 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 196 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 197 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 198 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 199 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 200 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 201 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 202 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 203 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 204 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 205 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 206 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 207 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 208 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 209 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 210 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 211 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 212 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 213 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 214 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 215 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 216 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 217 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 218 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 219 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 220 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 221 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 222 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 223 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 224 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 225 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 226 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 227 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 228 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 229 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 230 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 231 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 232 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 233 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 234 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 235 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 236 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 237 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 238 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 239 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 240 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 241 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 242 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 243 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 244 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 245 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 246 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 247 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 248 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 249 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 250 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 251 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 252 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 253 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 254 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 255 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 256 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 257 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 258 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 259 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 260 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 261 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 262 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 263 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 264 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 265 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 266 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 267 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 268 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 269 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 270 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 271 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 272 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 273 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 274 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 275 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 276 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 277 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 278 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 279 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 280 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 281 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 282 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 283 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 284 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 285 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 286 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 287 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 288 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 289 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 290 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 291 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 292 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 293 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 294 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 295 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 296 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 297 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 298 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 299 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 300 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 301 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 302 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 303 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 304 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 305 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 306 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 307 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 308 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 309 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 310 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 311 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 312 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 313 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 314 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 315 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 316 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 317 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 318 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 319 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 320 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 321 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 322 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 323 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 324 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 325 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 326 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 327 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 328 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 329 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 330 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 331 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 332 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 333 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 334 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 335 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 336 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 337 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 338 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 339 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 340 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 341 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 342 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 343 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 4 - RAM LoE

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 - RAM LoE Inputs |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Why we are asking: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | To capture the ORCA project's Resource Allocation Matrix: every position on the team, its classification, and its Level of Effort (LoE) as a fraction of full-time equivalent (FTE) by mission phase. Rate is looked up from 'Labour Rates lookup' by Classification, and the fiscal-year \$ columns are computed self-contained on this sheet from LoE x rate x schedule-phase-month overlap (see '3 - Phase Durations'). EBP and inflation figures are illustrative placeholders. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | RAM Scenario ID | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Scenario Name | Nominal RAM |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Scenario Description | The baseline RAM used for ORCA's staffing plan. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Rationale | Derived from the ORCA instrument suite WBS/CBS and the Phase Durations schedule. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Source Doc | N/A - illustrative, pending confirmed CSA staffing plan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Defaults |  |  |  |  |  |  |  |  | Provided by PM |  |  |  |  |  |  | LoE as % of one FTE, by phase (PM input) |  |  |  |  |  |  | Rates tab | FTE per fiscal year, calculated from '3 - Phase Durations' and the phase LoE on the left |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Row Num | Agency / Dep't | Team | Skillset Group | Skillset | Title - Role | Additional Labels | Branch | Directorate | Employee Name | Position No | New or Existing | Classification | Echelon | Math Model | Funding Source | Phase 0 | Phase A | Phase B | Phase C | Phase D | Phase E | Phase F | Rate ($) | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | 2040 | 2041 | 2042 | 2043 | 2044 | 2045 | 2046 | 2047 | 2048 | 2049 | 2050 | 2051 | 2052 | 2053 | 2054 | 2055 | 2056 | 2057 | 2058 | 2059 | 2060 | Total (FTE-yrs) |
| 1 | CSA | Project Team | Project Manager | PM | Portfolio Manager | Program Office | Space Exploration | Program Management | Alan Whitfield | ORCA-PM-001 | Existing | EN-ENG-6 | Max Echelon | Labour Rates | FF-CSA | 0 | 0 | 0.21 | 0 | 0.42 | 1 | 0 | 165000 | 0 | 0 | 0 | 0 | 0.051780821917808216 | 0.21 | 0.1582191780821918 | 0 | 0.10356164383561643 | 0.42 | 0.4211506849315069 | 0.42 | 0.42 | 0.42 | 0.4211506849315069 | 0.563013698630137 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 0.2493150684931507 | 21.869150684931505 |
| 2 | CSA | Project Team | Project Manager | Mission Management | ORCA Mission Manager | Program Office | Space Exploration | Program Management | Marie Tremblay | ORCA-PM-002 | Existing | PC-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 1 | 0.05 | 0.1 | 0.67 | 1 | 0 | 122000 | 0 | 0 | 0.2493150684931507 | 1 | 0.7657534246575343 | 0.05000000000000001 | 0.06260273972602741 | 0.10000000000000002 | 0.24054794520547942 | 0.67 | 0.6718356164383562 | 0.67 | 0.67 | 0.67 | 0.6718356164383562 | 0.7513698630136987 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 0.2493150684931507 | 25.503534246575338 |
| 3 | CSA | Project Team | Scientific | Mission Ops | Mission Operations Scientist | Science Segment | Space Exploration | Planetary Science | Devon Okafor | ORCA-SCI-001 | New | PC-3 | Max Echelon | Labour Rates | FF-CSA | 0 | 1 | 1 | 0 | 0.73 | 0 | 0 | 105000 | 0 | 0 | 0.2493150684931507 | 1 | 1 | 1 | 0.7534246575342466 | 0 | 0.17999999999999997 | 0.73 | 0.7320000000000001 | 0.73 | 0.73 | 0.73 | 0.7320000000000001 | 0.55 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9.116739726027397 |
| 4 | CSA | Project Team | Project Manager | PM | Lead Project Manager | Program Office | Space Exploration | Program Management | Priya Raman | ORCA-PM-003 | New | EN-ENG-5 | Max Echelon | Labour Rates | FF-CSA | 0 | 1 | 0.25 | 0.25 | 0.27 | 1 | 0 | 145000 | 0 | 0 | 0.2493150684931507 | 1 | 0.815068493150685 | 0.25 | 0.25068493150684934 | 0.25 | 0.2549315068493151 | 0.27 | 0.2707397260273973 | 0.27 | 0.27 | 0.27 | 0.2707397260273973 | 0.45 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 0.2493150684931507 | 23.40175342465753 |
| 5 | CSA | Project Team | Project Manager | PM | Deputy Project Manager | Program Office | Space Exploration | Program Management | Étienne Lacroix | ORCA-PM-004 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.15 | 0 | 0 | 0.7 | 0 | 0 | 128000 | 0 | 0 | 0.0373972602739726 | 0.15 | 0.113013698630137 | 0 | 0 | 0 | 0.17260273972602738 | 0.6999999999999998 | 0.7019178082191782 | 0.6999999999999998 | 0.6999999999999998 | 0.6999999999999998 | 0.7019178082191782 | 0.5273972602739726 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5.204246575342466 |
| 6 | CSA | Project Team | Project Manager | Planning | Project Management Engineer | Program Office | Space Exploration | Program Management | Grace Lindqvist | ORCA-PM-005 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.2 | 0.1 | 0 | 0.48 | 0.1 | 0 | 128000 | 0 | 0 | 0.04986301369863014 | 0.20000000000000004 | 0.1753424657534247 | 0.10000000000000002 | 0.07534246575342467 | 0 | 0.11835616438356163 | 0.48 | 0.4813150684931507 | 0.48 | 0.48 | 0.48 | 0.4813150684931507 | 0.3863013698630137 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.02493150684931507 | 5.813863013698624 |
| 7 | CSA | Project Team | Project Manager | Cost & Schedule | Schedule and Cost Management Engineer | Program Office | Space Exploration | Program Management | Samuel Boucher | ORCA-PM-006 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 1 | 0.1 | 1 | 0.45 | 1 | 0 | 128000 | 0 | 0 | 0.2493150684931507 | 1 | 0.7780821917808219 | 0.10000000000000002 | 0.32465753424657534 | 1 | 0.8643835616438357 | 0.45 | 0.4512328767123288 | 0.45 | 0.45 | 0.45 | 0.4512328767123288 | 0.5856164383561645 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 0.2493150684931507 | 25.864794520547942 |
| 8 | CSA | Project Team | Systems | Systems Engineering | Lead Spacecraft Systems Engineer | Instrument Suite | Space Exploration | Engineering | Naomi Fitzgerald | ORCA-SE-001 | New | EN-ENG-5 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.3 | 0 | 0.25 | 0.37 | 0.05 | 0 | 145000 | 0 | 0 | 0.0747945205479452 | 0.3 | 0.226027397260274 | 0 | 0.06232876712328767 | 0.25 | 0.2795890410958904 | 0.36999999999999994 | 0.37101369863013706 | 0.36999999999999994 | 0.36999999999999994 | 0.36999999999999994 | 0.37101369863013706 | 0.2910958904109589 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.012465753424657534 | 4.618876712328764 |
| 9 | CSA | Project Team | Systems | Systems Engineering | Spacecraft Systems Engineer | Instrument Suite | Space Exploration | Engineering | Kevin Anand | ORCA-SE-002 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.1 | 0.05 | 1 | 0.05 | 0.21 | 0 | 128000 | 0 | 0 | 0.02493150684931507 | 0.10000000000000002 | 0.08767123287671234 | 0.05000000000000001 | 0.28698630136986303 | 1 | 0.7657534246575343 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.08945205479452055 | 0.21 | 0.21 | 0.21057534246575346 | 0.21 | 0.21 | 0.21 | 0.21057534246575346 | 0.21 | 0.21 | 0.21 | 0.21057534246575346 | 0.21 | 0.21 | 0.21 | 0.21057534246575346 | 0.21 | 0.21 | 0.21 | 0.052356164383561644 | 6.539726027397258 |
| 10 | CSA | Project Team | Speciality Engineer | GNC | Instrument Pointing / GNC Engineer | Instrument Suite | Space Exploration | Engineering | Isabelle Roy | ORCA-GNC-001 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0 | 0 | 0 | 0.02 | 0 | 0 | 128000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.004931506849315068 | 0.02 | 0.02005479452054795 | 0.02 | 0.02 | 0.02 | 0.02005479452054795 | 0.015068493150684932 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.1401095890410959 |
| 11 | CSA | Project Team | Speciality Engineer | Robotics | Sampling Arm (ISA) Systems Engineer (Option C) | Instrument Suite | Space Exploration | Engineering | Marcus Delgado | ORCA-ISA-001 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0 | 0 | 0.55 | 0.07 | 0.55 | 0 | 128000 | 0 | 0 | 0 | 0 | 0 | 0 | 0.13712328767123289 | 0.55 | 0.43164383561643843 | 0.07 | 0.07019178082191782 | 0.07 | 0.07 | 0.07 | 0.07019178082191782 | 0.18835616438356165 | 0.55 | 0.55 | 0.5515068493150687 | 0.55 | 0.55 | 0.55 | 0.5515068493150687 | 0.55 | 0.55 | 0.55 | 0.5515068493150687 | 0.55 | 0.55 | 0.55 | 0.5515068493150687 | 0.55 | 0.55 | 0.55 | 0.13712328767123289 | 11.77065753424658 |
| 12 | CSA | Project Team | Speciality Engineer | S&MA | Safety and Mission Assurance Engineer | Instrument Suite | Space Exploration | Engineering | Fatima Haidari | ORCA-SMA-001 | New | EN-ENG-5 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.3 | 1 | 0.35 | 0.37 | 0.3 | 0 | 145000 | 0 | 0 | 0.0747945205479452 | 0.3 | 0.47260273972602745 | 1 | 0.8406849315068494 | 0.3499999999999999 | 0.35493150684931507 | 0.36999999999999994 | 0.37101369863013706 | 0.36999999999999994 | 0.36999999999999994 | 0.36999999999999994 | 0.37101369863013706 | 0.3527397260273973 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.0747945205479452 | 11.445863013698636 |
| 13 | CSA | Project Team | Speciality Engineer | FDIR | Fault Detection, Isolation and Recovery Engineer | Instrument Suite | Space Exploration | Engineering | Robert Cianci | ORCA-FDIR-001 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.1 | 0 | 0.05 | 0 | 0.3 | 0 | 128000 | 0 | 0 | 0.02493150684931507 | 0.10000000000000002 | 0.07534246575342467 | 0 | 0.012465753424657534 | 0.05000000000000001 | 0.037671232876712334 | 0 | 0 | 0 | 0 | 0 | 0 | 0.07397260273972601 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.0747945205479452 | 5.852465753424656 |
| 14 | CSA | Project Team | Speciality Engineer | SatOps | Mission Operations and Ground Systems Engineer | Ground Segment | Space Exploration | Mission Operations | Simone Bergeron | ORCA-OPS-001 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.1 | 0.4 | 0 | 0.05 | 0.2 | 0 | 128000 | 0 | 0 | 0.02493150684931507 | 0.10000000000000002 | 0.17397260273972603 | 0.4000000000000001 | 0.30136986301369867 | 0 | 0.012328767123287671 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.08698630136986302 | 0.20000000000000004 | 0.20000000000000004 | 0.20054794520547947 | 0.20000000000000004 | 0.20000000000000004 | 0.20000000000000004 | 0.20054794520547947 | 0.20000000000000004 | 0.20000000000000004 | 0.20000000000000004 | 0.20054794520547947 | 0.20000000000000004 | 0.20000000000000004 | 0.20000000000000004 | 0.20054794520547947 | 0.20000000000000004 | 0.20000000000000004 | 0.20000000000000004 | 0.04986301369863014 | 5.05191780821918 |
| 15 | CSA | Project Team | Speciality Engineer | Instruments | Mass Spectrometer Lead Engineer | Instrument Suite | Space Exploration | Engineering | Yusuf Karimi | ORCA-INS-001 | New | PC-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.1 | 1 | 0.2 | 0.33 | 0.05 | 0 | 122000 | 0 | 0 | 0.02493150684931507 | 0.10000000000000002 | 0.3219178082191781 | 1 | 0.8032876712328768 | 0.20000000000000004 | 0.23205479452054797 | 0.33 | 0.33090410958904115 | 0.33 | 0.33 | 0.33 | 0.33090410958904115 | 0.26095890410958905 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.012465753424657534 | 5.837972602739724 |
| 16 | CSA | Project Team | Speciality Engineer | Radar | Ice-Penetrating Radar Lead Engineer | Instrument Suite | Space Exploration | Engineering | Charlotte Nadeau | ORCA-INS-002 | New | PC-3 | Max Echelon | Labour Rates | FF-CSA | 0 | 0 | 1 | 0.65 | 0.35 | 0.07 | 0 | 105000 | 0 | 0 | 0 | 0 | 0.2465753424657534 | 1 | 0.9154794520547945 | 0.65 | 0.576027397260274 | 0.3499999999999999 | 0.3509589041095891 | 0.3499999999999999 | 0.3499999999999999 | 0.3499999999999999 | 0.3509589041095891 | 0.28095890410958907 | 0.07 | 0.07 | 0.07019178082191782 | 0.07 | 0.07 | 0.07 | 0.07019178082191782 | 0.07 | 0.07 | 0.07 | 0.07019178082191782 | 0.07 | 0.07 | 0.07 | 0.07019178082191782 | 0.07 | 0.07 | 0.07 | 0.01745205479452055 | 7.0491780821917835 |
| 17 | CSA | Project Team | Speciality Engineer | EMC/EMI | Electromagnetic Compatibility (EMC/EMI) Specialist | Instrument Suite | Space Exploration | Engineering | Daniel Osei | ORCA-EMC-001 | New | EN-ENG-5 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.25 | 0 | 0.2 | 0.37 | 1 | 0 | 145000 | 0 | 0 | 0.06232876712328767 | 0.25 | 0.18835616438356165 | 0 | 0.04986301369863014 | 0.20000000000000004 | 0.2419178082191781 | 0.36999999999999994 | 0.37101369863013706 | 0.36999999999999994 | 0.36999999999999994 | 0.36999999999999994 | 0.37101369863013706 | 0.5253424657534246 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 0.2493150684931507 | 22.00010958904109 |
| 18 | CSA | Project Team | Speciality Engineer | Radiation | Space Environment and Radiation Engineer | Instrument Suite | Space Exploration | Engineering | Vera Kowalski | ORCA-RAD-001 | New | EN-ENG-5 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.35 | 0.1 | 0.1 | 0.1 | 0.1 | 0 | 145000 | 0 | 0 | 0.08726027397260273 | 0.3499999999999999 | 0.28835616438356165 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.02493150684931507 | 3.652465753424659 |
| 19 | CSA | Project Team | Speciality Engineer | Structures | Instrument Suite Structures Engineer | Instrument Suite | Space Exploration | Engineering | Thomas Girard | ORCA-STR-001 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 1 | 0.25 | 1 | 0.25 | 0.05 | 0 | 128000 | 0 | 0 | 0.2493150684931507 | 1 | 0.815068493150685 | 0.25 | 0.43767123287671234 | 1 | 0.815068493150685 | 0.25 | 0.25068493150684934 | 0.25 | 0.25 | 0.25 | 0.25068493150684934 | 0.20068493150684932 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.05013698630136987 | 0.05000000000000001 | 0.05000000000000001 | 0.05000000000000001 | 0.012465753424657534 | 7.182191780821914 |
| 20 | CSA | Project Team | Speciality Engineer | Mechanical | Launch and Mechanical Environment Engineer | Instrument Suite | Space Exploration | Engineering | Aline Petit | ORCA-MEC-001 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 1 | 0 | 0.1 | 0.13 | 1 | 0 | 128000 | 0 | 0 | 0.2493150684931507 | 1 | 0.7534246575342466 | 0 | 0.02493150684931507 | 0.10000000000000002 | 0.1073972602739726 | 0.13 | 0.13035616438356165 | 0.13 | 0.13 | 0.13 | 0.13035616438356165 | 0.34452054794520554 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 1.0027397260273974 | 1 | 1 | 1 | 0.2493150684931507 | 21.620575342465752 |
| 21 | CSA | Project Team | Speciality Engineer | Robotics | Sampling Arm Mechanisms Engineer (Option C) | Instrument Suite | Space Exploration | Engineering | Hassan Malik | ORCA-ISA-002 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 1 | 0.3 | 0.05 | 0.38 | 0.1 | 0 | 128000 | 0 | 0 | 0.2493150684931507 | 1 | 0.8273972602739726 | 0.3 | 0.23849315068493152 | 0.05000000000000001 | 0.13136986301369863 | 0.38000000000000006 | 0.38104109589041096 | 0.38000000000000006 | 0.38000000000000006 | 0.38000000000000006 | 0.38104109589041096 | 0.3109589041095891 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.02493150684931507 | 7.215643835616431 |
| 22 | CSA | Project Team | Speciality Engineer | GNC | Guidance, Navigation and Control (GNC) Engineer | Instrument Suite | Space Exploration | Engineering | Julie Beaulieu | ORCA-GNC-002 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0 | 0.25 | 0.1 | 0.35 | 0 | 0 | 128000 | 0 | 0 | 0 | 0 | 0.06164383561643835 | 0.25 | 0.21328767123287673 | 0.10000000000000002 | 0.16164383561643836 | 0.3499999999999999 | 0.3509589041095891 | 0.3499999999999999 | 0.3499999999999999 | 0.3499999999999999 | 0.3509589041095891 | 0.2636986301369863 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3.152191780821918 |
| 23 | CSA | Project Team | Speciality Engineer | Thermal | Thermal Control Engineer | Instrument Suite | Space Exploration | Engineering | Owen MacKenzie | ORCA-THM-001 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.1 | 1 | 0 | 0.35 | 0.3 | 0 | 128000 | 0 | 0 | 0.02493150684931507 | 0.10000000000000002 | 0.3219178082191781 | 1 | 0.7534246575342466 | 0 | 0.08630136986301369 | 0.3499999999999999 | 0.3509589041095891 | 0.3499999999999999 | 0.3499999999999999 | 0.3499999999999999 | 0.3509589041095891 | 0.33767123287671236 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.3008219178082192 | 0.3 | 0.3 | 0.3 | 0.0747945205479452 | 10.204246575342468 |
| 24 | CSA | Project Team | Speciality Engineer | Power | RTG / Power Systems Engineer | Instrument Suite | Space Exploration | Engineering | Leila Amini | ORCA-PWR-001 | New | EN-ENG-5 | Max Echelon | Labour Rates | FF-CSA | 0 | 0.05 | 0.15 | 1 | 0.03 | 0.1 | 0 | 145000 | 0 | 0 | 0.012465753424657534 | 0.05000000000000001 | 0.07465753424657534 | 0.15 | 0.3623287671232877 | 1 | 0.7608219178082192 | 0.03 | 0.03008219178082192 | 0.03 | 0.03 | 0.03 | 0.03008219178082192 | 0.04726027397260274 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.02493150684931507 | 4.463726027397259 |
| 25 | CSA | Project Team | Speciality Engineer | Software | Flight Software and Autonomy Engineer | Instrument Suite | Space Exploration | Engineering | Nathan Cormier | ORCA-SW-001 | New | EN-ENG-4 | Max Echelon | Labour Rates | FF-CSA | 0 | 1 | 0.1 | 0.25 | 0.42 | 0.1 | 0 | 128000 | 0 | 0 | 0.2493150684931507 | 1 | 0.7780821917808219 | 0.10000000000000002 | 0.13767123287671235 | 0.25 | 0.29191780821917807 | 0.42 | 0.4211506849315069 | 0.42 | 0.42 | 0.42 | 0.4211506849315069 | 0.3410958904109589 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.10027397260273974 | 0.10000000000000002 | 0.10000000000000002 | 0.10000000000000002 | 0.02493150684931507 | 7.496410958904104 |
| 26 | CSA | CSA Internal Services | Internal Services | Multiple - See Model | Multiple - See Model | Other |  |  |  |  | N/A |  | Standard | IS Model (%) | A-Base |  |  |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 27 | Partner Agency (NASA/ESA) | Orbiter Interface Liaison | Internal Services | Interface Coordination | Orbiter Bus Interface Liaison | Other |  |  | TBD | N/A | MOU |  | Standard | Partner Agency Model | MOU |  |  |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 28 | CSA | Horizontal Services | Internal Services | Infrastructure | Real Property and IT Infrastructure | Other |  |  | N/A | N/A | MOU |  | Standard | IS Model (%) | A-Base |  |  |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 29 | PSPC | Horizontal Services | Internal Services | Contracts | Fairness Monitor | Other |  |  | N/A | N/A | MOU |  | Standard | IS Model (%) | A-Base |  |  |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 30 | Shared Services Canada | Horizontal Services | Internal Services | IT | IT Support | Other |  |  | N/A | N/A | MOU |  | Standard | IS Model (%) | A-Base |  |  |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 31 | Justice Canada | Horizontal Services | Internal Services | Legal | Legal Services | Other |  |  | N/A | N/A | MOU |  | Standard | IS Model (%) | A-Base |  |  |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Total FTE |  |  |  |  |  |  |  |  |  |  | 0 | 10.099999999999998 | 7.31 | 7.199999999999999 | 7.709999999999998 | 8.579999999999998 | 0 |  | 0 | 0 | 2.518082191780822 | 10.099999999999998 | 9.412054794520547 | 7.31 | 7.302602739726027 | 7.199999999999999 | 7.325753424657535 | 7.709999999999998 | 7.731123287671235 | 7.709999999999998 | 7.709999999999998 | 7.709999999999998 | 7.731123287671235 | 7.924520547945205 | 8.579999999999998 | 8.579999999999998 | 8.60350684931507 | 8.579999999999998 | 8.579999999999998 | 8.579999999999998 | 8.60350684931507 | 8.579999999999998 | 8.579999999999998 | 8.579999999999998 | 8.60350684931507 | 8.579999999999998 | 8.579999999999998 | 8.579999999999998 | 8.60350684931507 | 8.579999999999998 | 8.579999999999998 | 8.579999999999998 | 2.1391232876712327 | 262.068410958904 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Salary without inflation in "Then Year" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 0 | 324471.095890411 | 1301450 | 1206567.808219178 | 916650 | 925331.9178082194 | 941400 | 955171.2328767122 | 997250 | 999982.1917808219 | 997250 | 997250 | 997250 | 999982.1917808219 | 1040013.5616438356 | 1170680 | 1170680 | 1173887.3424657532 | 1170680 | 1170680 | 1170680 | 1173887.3424657532 | 1170680 | 1170680 | 1170680 | 1173887.3424657532 | 1170680 | 1170680 | 1170680 | 1173887.3424657532 | 1170680 | 1170680 | 1170680 | 291868.1643835617 | 34976957.53424658 |
|  |  |  |  |  | Employee Benefit Plan (EBP) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0.27 | 0 | 0 | 87607.19589041098 | 351391.5 | 325773.3082191781 | 247495.50000000003 | 249839.61780821928 | 254178.00000000003 | 257896.2328767123 | 269257.5 | 269995.19178082194 | 269257.5 | 269257.5 | 269257.5 | 269995.19178082194 | 280803.66164383566 | 316083.60000000003 | 316083.60000000003 | 316949.58246575337 | 316083.60000000003 | 316083.60000000003 | 316083.60000000003 | 316949.58246575337 | 316083.60000000003 | 316083.60000000003 | 316083.60000000003 | 316949.58246575337 | 316083.60000000003 | 316083.60000000003 | 316083.60000000003 | 316949.58246575337 | 316083.60000000003 | 316083.60000000003 | 316083.60000000003 | 78804.40438356166 | 9443778.534246571 |
|  |  |  |  |  | Salary and EBP in "Then Year" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 0 | 412078.291780822 | 1652841.5 | 1532341.1164383562 | 1164145.5 | 1175171.5356164388 | 1195578 | 1213067.4657534244 | 1266507.5 | 1269977.3835616438 | 1266507.5 | 1266507.5 | 1266507.5 | 1269977.3835616438 | 1320817.2232876713 | 1486763.6 | 1486763.6 | 1490836.9249315066 | 1486763.6 | 1486763.6 | 1486763.6 | 1490836.9249315066 | 1486763.6 | 1486763.6 | 1486763.6 | 1490836.9249315066 | 1486763.6 | 1486763.6 | 1486763.6 | 1490836.9249315066 | 1486763.6 | 1486763.6 | 1486763.6 | 370672.5687671234 | 44420736.06849317 |
|  |  |  |  |  | Bring historic data into Base Year 2026 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 0 | 412078.291780822 | 1652841.5 | 1532341.1164383562 | 1164145.5 | 1175171.5356164388 | 1195578 | 1213067.4657534244 | 1266507.5 | 1269977.3835616438 | 1266507.5 | 1266507.5 | 1266507.5 | 1269977.3835616438 | 1320817.2232876713 | 1486763.6 | 1486763.6 | 1490836.9249315066 | 1486763.6 | 1486763.6 | 1486763.6 | 1490836.9249315066 | 1486763.6 | 1486763.6 | 1486763.6 | 1490836.9249315066 | 1486763.6 | 1486763.6 | 1486763.6 | 1490836.9249315066 | 1486763.6 | 1486763.6 | 1486763.6 | 370672.5687671234 | 44420736.06849317 |
|  |  |  |  |  | Apply inflation to future years |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 0 | 432939.75530222605 | 1779929.5159609374 | 1691417.8771593613 | 1317123.7796996627 | 1362838.695125519 | 1421166.535999134 | 1478004.9151489849 | 1581694.3179109925 | 1625678.4201761885 | 1661767.5927552364 | 1703311.7825741172 | 1745894.57713847 | 1794444.7962013613 | 1912937.1627666587 | 2207108.920793532 | 2262286.6438133703 | 2325196.8066481794 | 2376814.9051564215 | 2436235.2777853315 | 2497141.1597299646 | 2566582.208418345 | 2623558.9309412935 | 2689147.904214826 | 2756376.601820196 | 2833026.5265009487 | 2895918.167287343 | 2968316.1214695266 | 3042524.0245062644 | 3127131.1994343144 | 3196551.8032468935 | 3276465.598328065 | 3358377.2382862666 | 858226.4024689083 | 71806136.16476884 |
|  |  |  |  |  | Salary and EBP in "Base Year" 2026 with inflation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 0 | 432939.75530222605 | 1779929.5159609374 | 1691417.8771593613 | 1317123.7796996627 | 1362838.695125519 | 1421166.535999134 | 1478004.9151489849 | 1581694.3179109925 | 1625678.4201761885 | 1661767.5927552364 | 1703311.7825741172 | 1745894.57713847 | 1794444.7962013613 | 1912937.1627666587 | 2207108.920793532 | 2262286.6438133703 | 2325196.8066481794 | 2376814.9051564215 | 2436235.2777853315 | 2497141.1597299646 | 2566582.208418345 | 2623558.9309412935 | 2689147.904214826 | 2756376.601820196 | 2833026.5265009487 | 2895918.167287343 | 2968316.1214695266 | 3042524.0245062644 | 3127131.1994343144 | 3196551.8032468935 | 3276465.598328065 | 3358377.2382862666 | 858226.4024689083 | 71806136.16476884 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Please provide an explanation why positions are required |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Method: FTE per fiscal year = sum over phases of (phase LoE % x months of that phase falling in the fiscal year, from '3 - Phase Durations') / 12. Salary = sum of (FTE x Rate), with Rate looked up by Classification from 'Labour Rates lookup'. EBP rate (blue input above) and inflation factors ('Inflation Rate' tab) are illustrative placeholders pending confirmed CSA parameters. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 5 - Risk Register

| ` Table of Contents |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 - Risk Register for Costing Purposes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Why we we asking: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | EVM needs it, sensitivity analysis needs it |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Probability scale: 1 Very Low 10% \| 2 Low 30% \| 3 Medium 50% \| 4 High 70% \| 5 Very High 90%.  Costs in thousands of CAD ($000). Weighted Exposure = Probability x Most Likely cost. Risk Category / Sub-category follow the 'Risk Breakdown Structure' tab. Figures are illustrative. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | # | ID | Risk Category | Risk Sub-category | Risk Name | Type of Risk | Description | Internal Factors | External Factors | Probability | Mitigation Strategy | Mitigation Strategy Narrative | Cost Impact – Optimistic ($000) | Cost Impact – Most Likely ($000) | Cost Impact – Pessimistic ($000) | Weighted Exposure ($000) | Cost Impact in Phase | Schedule Impact in Phase | Impact on Project | Impact on Analysis |
|  | 1 | R-001 | Programmatic Integration & Execution | Partnership & External Agreements | RTG Fuel Supply Delay | Schedule | Pu-238 production is limited and allocated across multiple missions; ORCA's supply commitment with the international partner is not yet finalized. | RTG procurement depends on the partner; no CSA-held fuel allocation | Limited Pu-238 production; competing mission demand | 0.5 | Mitigate | Secure a fuel allocation letter through the partner agency before PDR, track fuel-production milestones at every gate, and carry a launch-opportunity reserve. | 1000 | 4000 | 9500 | 2000 | B2–D | C–D | Schedule slip to launch window; possible multi-year wait for the next Jupiter gravity-assist opportunity. | Adds schedule contingency and extended Phase D standing-army LoE to the estimate. |
|  | 2 | R-002 | Technological & Engineering Factors | Technology Readiness & Maturity | Ice-Penetrating Radar TRL Immaturity | Technical | Ice-penetrating radar performance at Enceladus's ice shell has not been demonstrated at flight TRL; ground and airborne analogue testing is still needed. | Immature antenna and processing design; limited ice-analogue test data | Access to analogue test sites; RF component availability | 0.5 | Mitigate | Fund an airborne and ground analogue campaign in Phases A–B1, set a TRL 6 exit criterion at PDR, and keep a descoped radar mode as a fallback. | 450 | 1800 | 4200 | 900 | B1–C | B2–C | Could require redesign, additional testing, increased costs, and schedule delays. | Adds instrument engineering and test LoE in Phases B and C. |
|  | 3 | R-003 | Technological & Engineering Factors | System Performance & Reliability | Mass Spectrometer Sensitivity Risk | Technical | Detecting biosignature-relevant compounds at parts-per-billion concentrations has not yet been demonstrated in a flight-qualified instrument of this mass and power class. | Detector noise and contamination budget not closed | Detector supplier performance; availability of heritage instrument data | 0.5 | Mitigate | Demonstrate sensitivity on a breadboard before PDR, hold an end-to-end error budget from inlet to detector, and reserve mass and power margin. | 350 | 1500 | 3500 | 750 | B2–C | C–D | Could require redesign, additional testing, and reduced science return if sensitivity targets are not met. | Adds instrument engineering, calibration and verification LoE. |
|  | 4 | R-004 | External & Environmental Factors | Regulatory & Legal | Export Control Delays | Governance | A Technical Assistance Agreement (TAA) covering instrument-level data exchange with the partner agency has not yet been established. | Late identification of controlled data items | Foreign export-licensing review timelines | 0.5 | Mitigate | Start the TAA application in Phase A, identify controlled technical data early, and schedule data exchanges around licence approval dates. | 200 | 900 | 2100 | 450 | A–B2 | B1–C | Could delay data exchange, joint testing, and integration activities with the partner agency. | Adds PM and legal coordination LoE plus schedule contingency. |
|  | 5 | R-005 | Programmatic Integration & Execution | Partnership & External Agreements | Partner Schedule Dependency | Programmatic | ORCA's instruments are accommodated payloads on a partner-led spacecraft; ORCA does not control the host mission's own schedule risk. | Limited ORCA-side float before instrument delivery | Host mission development and launch schedule | 0.5 | Mitigate | Write need dates and interface milestones into the partner agreement and hold ORCA-side float ahead of instrument delivery. | 700 | 3000 | 7000 | 1500 | C–D | C–D | Delays on the partner's side could cascade directly into ORCA's integration and launch readiness dates. | Adds standing-army LoE and storage cost if delivery must wait for the host. |
|  | 6 | R-006 | Programmatic Integration & Execution | Schedule Planning & Control | Launch Window Availability | Schedule | Manifest slots on the required class of launch vehicle are not yet reserved for the ~2041 launch opportunity. | Instrument readiness must support a fixed trajectory window | Launch-provider manifest; gravity-assist geometry | 0.3 | Accept | Launch procurement is the partner's responsibility; accept the residual exposure but track manifest status and backup trajectory options at each gate. | 800 | 3500 | 8000 | 1050 | D | D–E | Missing the trajectory window could force a multi-year delay to the next viable gravity-assist path. | A missed window adds multi-year storage and standing-army cost. |
|  | 7 | R-007 | Programmatic Integration & Execution | Cost & Budget Management | Early-Stage Cost Uncertainty | Cost | Estimating maturity is consistent with Phase B/C; several subsystem costs are still based on analogous-mission estimates rather than vendor quotes. | Analogy-based estimates; immature WBS | Volatility in supplier quotations | 0.5 | Mitigate | Refresh bottom-up estimates at PDR and CDR, replace analogy costs with vendor quotes, and reconcile the RAM and CBS at each gate. | 600 | 2500 | 6000 | 1250 | B1–D | B2–D | Could result in cost growth as design matures and vendor quotes replace parametric estimates. | Widens the cost uncertainty range and drives contingency sizing. |
|  | 8 | R-008 | External & Environmental Factors | Geopolitical & Economic | Currency Exchange Exposure | Cost | Major payload contracts and the partner-agency relationship involve non-CAD-denominated costs. | Foreign-denominated subcontracts | Exchange-rate movements | 0.5 | Transfer | Use CAD-denominated contracts where possible and forward-purchase foreign currency for large milestone payments. | 300 | 1200 | 2800 | 600 | C–D | C–D | Unfavourable exchange-rate movement could increase the CAD cost of foreign-denominated contracts. | Adds FX contingency to foreign-content CBS elements. |
|  | 9 | R-009 | Technological & Engineering Factors | System Performance & Reliability | Deep-Space Radiation/Thermal Margin | Technical | Component qualification levels are based on analogous outer-planet missions and have not yet been validated against ORCA's specific trajectory and RTG thermal design. | Analogy-based qualification levels | Jovian and Saturnian radiation environment; RTG heat output | 0.3 | Mitigate | Run trajectory-specific radiation and RTG thermal analyses in Phase B and qualify parts to mission-specific levels with margin. | 650 | 2800 | 6500 | 840 | B2–C | C–D | Could require additional shielding, thermal design changes, or component requalification. | Adds shielding mass, parts qualification and thermal test LoE. |
|  | 10 | R-010 | Technological & Engineering Factors | Software & Algorithms | Autonomous Operations Complexity | Technical | The autonomy and fault-management software architecture for the instrument suite has not yet been baselined. | Underestimated software complexity | Light-time delay; host spacecraft FDIR interfaces | 0.5 | Mitigate | Baseline the autonomy architecture before PDR, prototype fault-management logic early, and run long-duration autonomy simulations. | 400 | 1600 | 3700 | 800 | B2–D | C–D | Increased software development and validation effort could cause cost and schedule growth. | Adds flight software development and V&V LoE. |
|  | 11 | R-011 | Programmatic Integration & Execution | Partnership & External Agreements | DSN Allocation Contention | Programmatic | ORCA's downlink allocation has not yet been negotiated as part of the partnership agreement. | Onboard storage sizing not yet tied to downlink plan | Deep Space Network demand from other missions | 0.5 | Mitigate | Negotiate a documented downlink allocation in the partner agreement and design onboard data prioritization for flythrough passes. | 200 | 900 | 2100 | 450 | E | E | Insufficient downlink priority could limit science data return during plume flythroughs. | Adds operations planning LoE; mainly reduces science return rather than adding cost. |
|  | 12 | R-012 | Technological & Engineering Factors | Technology Readiness & Maturity | Sampling Arm TRL Immaturity (Option C) | Technical | The ISA (Ice Sampling Arm) concept builds on Canadarm heritage but has not been adapted or tested for the Enceladus surface/plume environment. | Heritage design not adapted to cryogenic environment | Uncertainty in Enceladus surface and plume conditions | 0.5 | Mitigate | Run a dedicated ISA risk-reduction campaign in Phases A–B1, with a go/no-go decision on Option C at SRR. | 350 | 1400 | 3300 | 700 | A–C | B1–C | Could require a dedicated technology risk-reduction campaign, adding cost and schedule. | Adds robotics engineering and test LoE (Option C only). |
|  | 13 | R-013 | Safety, Assurance & Compliance | Certification & Standards | Planetary Protection Scope | Governance | A formal planetary protection plan has not yet been developed jointly with the partner agency. | Planetary protection requirements not yet flowed down | COSPAR category assignment; partner planetary protection policy | 0.5 | Mitigate | Develop a joint planetary protection plan with the partner in Phase A and build bioburden controls into the AIT flow. | 250 | 1100 | 2600 | 550 | A–D | C–D | Late-defined planetary protection requirements could drive late design or trajectory changes. | Adds cleanroom, bioburden testing and assurance LoE. |
|  | 14 | R-014 | Organizational & Human Factors | Resource & Staffing Capacity | Workforce Continuity | Programmatic | Program duration spans more than one career stage for most engineering staff; no succession plan is yet in place. | Long mission duration; small specialist pool | Labour-market competition for space specialists | 0.5 | Mitigate | Establish a succession plan, pair senior and junior staff on key roles, and capture design rationale in controlled documents. | 150 | 700 | 1600 | 350 | 0–F | B1–E | Loss of key personnel could cause knowledge gaps, rework, and schedule delays. | Raises labour-rate and FTE assumptions and adds knowledge-transfer LoE. |
|  | 15 | R-015 | Safety, Assurance & Compliance | Product Assurance & Quality Control | Multi-Party Configuration Management | Technical | A single joint configuration management authority across all contractors and the partner agency has not yet been established. | Multiple baselines across CSA and contractors | Partner configuration-management practices | 0.5 | Mitigate | Stand up a joint configuration control board with the partner and prime before PDR and audit baselines at each gate. | 200 | 800 | 1900 | 400 | B2–D | C–D | Could lead to interface mismatches, rework, and integration delays. | Adds configuration-management and reconciliation LoE. |
|  | 16 | R-016 | Strategic & Alignment Factors | Strategic Direction & Policy Alignment | Partner Agency Stability | Strategic | The mission concept assumes stable multi-decade support from a single partner agency; this has not been contractually secured. | Single-partner mission architecture | Partner budget and policy changes | 0.3 | Accept | Accept the residual exposure after securing a binding intergovernmental agreement, and keep a documented descope and re-host option. | 1000 | 4500 | 10500 | 1350 | B1–E | B2–E | Loss of the partner relationship could require a costly architecture change or mission redesign. | A partner exit would require re-estimating the mission architecture. |
|  | 17 | R-017 | Programmatic Integration & Execution | Governance Processes & Controls | Governance Workload | Governance | Gate documentation and decision-note preparation draw on the same technical leads responsible for design closure activities. | Same leads prepare gates and close the design | Departmental review cycles | 0.5 | Accept | Accept; plan gate-preparation windows into the integrated schedule and assign a dedicated gate coordinator. | 75 | 300 | 700 | 150 | A–C | A–C | Could slow design progress during gate-preparation windows. | Adds PM and governance LoE around gates. |
|  | 18 | R-018 | Programmatic Integration & Execution | Cost & Budget Management | Unallocated Reserve (Unknown-Unknowns) | Cost | Held as management reserve per CSA cost-estimating policy for unknown-unknown risk at Phase B/C maturity. | Estimate maturity at Phase B/C | Risks not yet identified | 0.5 | Accept | Hold as management reserve and release only through change control. | 400 | 1500 | 3500 | 750 | 0–F | 0–F | Provides cost cover for risks not yet individually identified. | Carried as reserve; not allocated to a CBS element. |
|  | 19 | R-019 | Technological & Engineering Factors | System Performance & Reliability | Instrument Degradation During Cruise | Technical | The ~10-year outbound cruise may degrade detectors, seals or calibration sources before the instruments reach Enceladus. | Limited in-cruise checkout plan; aging consumables | Cruise radiation dose; thermal cycling | 0.3 | Mitigate | Plan periodic in-cruise instrument checkouts and calibrations, and select parts with lifetime margin. | 350 | 1500 | 3500 | 450 | E | E | May reduce science performance at arrival or require recalibration campaigns. | Adds cruise operations and calibration LoE. |
|  | 20 | R-020 | Technological & Engineering Factors | Design & Development | Plume Sample Contamination | Technical | Terrestrial contamination or spacecraft outgassing may mask low-concentration organics in plume samples. | Contamination control plan not yet baselined | Host spacecraft outgassing; propulsion plume products | 0.3 | Mitigate | Define contamination budgets early, bake out sample inlets, and carry blank samples for background subtraction. | 300 | 1200 | 2800 | 360 | C–D | D | Could compromise biosignature measurements. | Adds contamination-control and cleanroom LoE. |
|  | 21 | R-021 | Data, Knowledge & Integration | Data Integration & Consistency | Science Data Processing Capacity | Technical | The CSA science operations centre may lack the processing and archive capacity for flythrough data volumes and joint partner data products. | Early data-volume assumptions | Changes to partner data formats | 0.3 | Mitigate | Size processing and archive capacity from flythrough scenarios and agree data-product formats in the partner ICD. | 250 | 1000 | 2400 | 300 | D–E | D–E | May delay science products after each flythrough. | Adds ground-segment software and operations LoE. |
|  | 22 | R-022 | External & Environmental Factors | Market & Supply Chain | Instrument Supplier Insolvency | Cost | A key instrument subcontractor may exit the market or become insolvent during the long development cycle. | Single-source instrument components | Small space-supplier base; market conditions | 0.2 | Transfer | Include data-package delivery and escrow clauses in contracts and qualify second sources for critical items. | 400 | 1800 | 4300 | 360 | C–D | C–D | Could force re-procurement and requalification. | Adds procurement and requalification cost. |
|  | 23 | R-023 | Technological & Engineering Factors | Parts, Components & Materials | Long-Lead Radiation-Hardened Parts | Schedule | Radiation-hardened EEE parts and detectors may arrive later than the integration schedule requires. | Late parts list; late purchase orders | Supplier backlog; export-controlled parts | 0.4 | Mitigate | Release long-lead orders after PDR, track parts at weekly reviews, and qualify alternates. | 250 | 1000 | 2400 | 400 | B2–D | C–D | May delay instrument assembly and environmental testing. | Adds procurement management and schedule contingency. |
|  | 24 | R-024 | Technological & Engineering Factors | Integration & Verification | Instrument Environmental Test Failure | Technical | Instrument-level thermal-vacuum or vibration testing may reveal design or workmanship defects requiring rework and retest. | Limited margin on first-of-kind hardware | Test facility availability | 0.3 | Mitigate | Test engineering models early, apply workmanship screening, and reserve facility time for retest. | 300 | 1300 | 3000 | 390 | D | D | May delay delivery to the host spacecraft. | Adds rework, retest and facility cost. |
|  | 25 | R-025 | Safety, Assurance & Compliance | Certification & Standards | End-of-Mission Disposal Requirements | Programmatic | Planetary protection disposal requirements for the Saturn system may extend Phase X/F operations or constrain the end-of-mission trajectory. | Disposal concept not yet defined | Partner end-of-mission plan; planetary protection policy | 0.2 | Accept | Accept; the host spacecraft owns disposal, and ORCA carries only operations-support LoE. | 100 | 500 | 1200 | 100 | X–F | X–F | May extend operations and data archiving. | Adds Phase X/F operations LoE. |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | Total ($000) | 10025 | 42300 | 99100 | 17200 |  |  |  |  |

## Risk Breakdown Structure

| Risk Category | Risk Sub-category | Risk Name | Type of Risk | Description | Internal Factors | External Factors | Cost - Impact in Phase | Schedule - Initial Impact in Phase | Parent CBS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Organizational & Human Factors | Leadership, Governance & Culture | Ineffective Governance and Decision-Making | Governance | Governance structures, roles, and escalation paths are unclear or inconsistently applied, delaying key decisions and creating misalignment across the program. | - Unclear authority  - Slow approvals  - Inconsistent executive oversight | - Evolving GoC governance expectations  - Partner governance incompatibility | All Phases | All Phases |  |
| Organizational & Human Factors | Leadership, Governance & Culture | Misaligned Organizational Incentives | Strategic | Incentives prioritize innovation or technical achievement over disciplined cost/schedule performance, reducing accountability. | - Incentives tied to technical milestones - Weak KPIs | - Public/political pressure for innovation | PREP 1 to MAIT | None |  |
| Organizational & Human Factors | Leadership, Governance & Culture | Leadership Turnover and Instability | Governance | High turnover in key leadership roles reduces continuity and strategic alignment across program phases. | - Succession gaps - Staffing instability | - Broader public sector mobility pressures | All Phases | All Phases |  |
| Organizational & Human Factors | Leadership, Governance & Culture | Risk Governance Culture | Programmatic | Risk processes are inconsistently followed or valued, leading to late identification of major issues. | - Lack of active risk boards - Inconsistent risk scoring | - Changing departmental reporting expectations | PREP 1 to MAIT | PREP 1 to MAIT |  |
| Organizational & Human Factors | Communication & Coordination | Internal Miscommunication and Information Silos | Programmatic | Teams lack timely, consistent information sharing, resulting in misaligned decisions and rework. | - Poor knowledge sharing - Unclear reporting paths | - Increased complexity in multi-site or remote collaboration | PREP 1 to MAIT | PREP 1 to MAIT |  |
| Organizational & Human Factors | Communication & Coordination | Interface Definition Gaps | Technical | Unclear or incomplete interface definitions lead to integration challenges and design errors. | - Documentation gaps - Inconsistent configuration control | - Partner documentation misalignment | Phase 0 to SAIT | Phase 0 to SAIT |  |
| Organizational & Human Factors | Communication & Coordination | International Coordination Challenges | Programmatic | Communication barriers across time zones, cultures, and languages delay critical alignment with partners. | - Limited resources for partner coordination | - Diverse international work practices | All Phases | All Phases |  |
| Organizational & Human Factors | Stakeholder Engagement | Unclear or Misaligned Stakeholder Expectations | Strategic | Stakeholder needs are not fully understood or aligned, causing redefinition of scope or priorities. | - Insufficient early engagement | - User community evolution - Science priorities | PREP 1 to Phase C | PREP 1 to Phase C |  |
| Organizational & Human Factors | Stakeholder Engagement | Insufficient Executive Sponsorship | Governance | Executive sponsors are not consistently engaged, weakening decision support and program momentum. | - Competing leadership priorities | - Shifts in departmental focus | PREP 1 to Phase C | PREP 1 to Phase C |  |
| Organizational & Human Factors | Resource & Staffing Capacity | Skilled Resource Shortages | Programmatic | Lack of experienced personnel delays technical development and increases rework. | - Training gaps - Turnover | - Labour market shortages in space-specialized skills | PREP 1 to Phase C | PREP 1 to Phase C |  |
| Organizational & Human Factors | Resource & Staffing Capacity | Knowledge Loss and Continuity Gaps | Programmatic | Loss of key personnel or weak documentation undermines continuity across phases. | - Insufficient knowledge management | - Competitive hiring environment | All Phases | All Phases |  |
| Organizational & Human Factors | Resource & Staffing Capacity | Overreliance on Individual Experts | Programmatic | Critical knowledge is concentrated in a few individuals, creating vulnerability if unavailable. | - Limited SME capacity | - Industry-wide SME scarcity | All Phases | All Phases |  |
| Technological & Engineering Factors | Technology Readiness & Maturity | Insufficient Technology Readiness Level (TRL) | Technical | Technology maturity is overestimated or not demonstrated early enough, causing downstream delays. | - Over-optimistic internal assessments | - Vendor overstatements of maturity | PREP 1 to Phase C | PREP 1 to Phase C |  |
| Technological & Engineering Factors | Technology Readiness & Maturity | Immature or Unproven Materials/Processes | Technical | New materials or manufacturing processes fail to meet requirements or require redesign. | - Limited early testing | - Supplier process immaturity | MAIT | MAIT |  |
| Technological & Engineering Factors | Design & Development | Unstable or Incomplete Design Baseline | Technical | Delays in achieving a stable baseline cascade into integration and manufacturing issues. | - Late requirements - Design churn | - Changing partner specifications | PREP 1 to SAIT | PREP 1 to SAIT |  |
| Technological & Engineering Factors | Design & Development | Design Complexity Beyond Analytical Capability | Technical | Engineering tools or models cannot fully resolve complex design interactions. | - Tool limitations | - Novel mission or payload architectures | PREP 1 to Phase C | PREP 1 to Phase C |  |
| Technological & Engineering Factors | Design & Development | Over-Customization Instead of COTS Adoption | Technical | Excessive customization increases cost, lead time, and risk compared with qualified COTS alternatives. | - Preference for bespoke solutions | - Limited space-qualified COTS availability | PREP 1 to Phase C | PREP 1 to Phase C |  |
| Technological & Engineering Factors | Parts, Components & Materials | EEE Part Failure or Obsolescence | Technical | Component failures or discontinuations disrupt design choices and testing schedules. | - Inadequte part screening | - Supply chain obsolescence | MAIT & SAIT | MAIT & SAIT |  |
| Technological & Engineering Factors | Parts, Components & Materials | Long-Lead Item Delays | Schedule | Critical components with long procurement cycles delay integration readiness. | - Late ordering | - Supplier backlog or disruption | MAIT & SAIT | MAIT & SAIT |  |
| Technological & Engineering Factors | Integration & Verification | Incomplete Integration Planning | Programmatic | Integration sequencing or planning gaps result in late rework and testing conflicts. | - Inadequate early I&T definition | - Partner delays | MAIT & SAIT | MAIT & SAIT |  |
| Technological & Engineering Factors | Integration & Verification | Environmental or Vibration Test Failures | Technical | Hardware fails during qualification or environmental tests, requiring redesign or rework. | - Weak margins - Design flaws | - Facility constraints | Phase B to Phase C | Phase B to Phase C |  |
| Technological & Engineering Factors | Manufacturing & Assembly | Poor Workmanship or QA Deficiencies | Technical | Manufacturing quality issues result in defects discovered late in testing or integration. | - Insufficient QA processes | - Supplier QA variability | MAIT & SAIT | MAIT & SAIT |  |
| Technological & Engineering Factors | Manufacturing & Assembly | Immature Manufacturing Processes | Technical | New or insufficiently validated processes lead to production delays or variability. | - Lac of documentation | - Small-capacity suppliers | MAIT & SAIT | MAIT & SAIT |  |
| Technological & Engineering Factors | Software & Algorithms | Underestimated Software Complexity | Technical | Software complexity is underestimated, requiring additional development time and testing. | - Limited early prototyping | - Integration with partner systems | Phase B to SAIT | Phase B to SAIT |  |
| Technological & Engineering Factors | Software & Algorithms | Insufficient Software Validation | Technical | Gaps in software validation cause faults discovered late in testing. | - Limited regression testing | - Late partner code deliveries | Phase B to SAIT | Phase B to SAIT |  |
| Technological & Engineering Factors | System Performance & Reliability | Insufficient System Margin | Technical | System lacks adequate performance margins, requiring late design changes. | - Underestimated loads | - Evolving partner or payload requirements | Phase B to SAIT | Phase B to SAIT |  |
| Technological & Engineering Factors | System Performance & Reliability | Unproven Redundancy or Fail-Safe Design | Technical | Redundant designs are untested or do not function as intended. | - Inadequate model validation | - Supplier delays in providing redundancy analyses | Phase B to SAIT | Phase B to SAIT |  |
| Technological & Engineering Factors | Obsolescence & Sustainment | Technology Obsolescence During Development | Technical | Long development timelines result in components or systems becoming outdated before launch. | - Slow decision-making | - Rapid commercial technology cycles | LEOP & ATLO |  |  |
| Technological & Engineering Factors | Obsolescence & Sustainment | Inadequate Sustainment Planning | Programmatic | Lifecycle sustainment needs are not fully planned, risking long-term mission continuity. | - Limited spares strategy | - Supplier discontinuation | Phase E & Phase X |  |  |
| Programmatic Integration & Execution | Cost & Budget Management | Optimistic Cost Baselines | Cost | Early cost estimates underestimate complexity or required effort, resulting in overruns and re-baselining. | - Immature designs - Optimistic modelling - Incomplete scoping | - Vendor underestimation - Inflation volatility | PREP 1 to Phase A |  |  |
| Programmatic Integration & Execution | Cost & Budget Management | Inadequate Contingency and Reserves | Cost | Cost reserves are insufficient to address risks, requirement changes, or technical growth. | - Pressure to reduce contingency - Lack of quantitative risk analysis | - Unpredictable supplier or market cost changes | All Phases |  |  |
| Programmatic Integration & Execution | Cost & Budget Management | Funding Gaps Across Phases | Programmatic | Delays or gaps in funding between phases disrupt schedules and lead to inefficiencies. | - Internal budget reallocations - Fragmented planning | - Treasury Board sequencing - GoC budget cycles | PREP 1 to Phase C | PREP 1 to Phase C |  |
| Programmatic Integration & Execution | Cost & Budget Management | Long-Term Cost Unsustainability | Cost | Operational or lifecycle costs exceed long-term funding, jeopardizing mission continuity. | - Underestimated O&M demands | - Shifting fiscal priorities | Phase E & Phase X |  |  |
| Programmatic Integration & Execution | Schedule Planning & Control | Overly Optimistic Schedule Baselines | Schedule | Schedules underestimate duration or complexity of integration, test and partner interactions. | - Underestimated task durations - Limited slack | - Partner timeline dependencies | Phase C, MAIT or SAIT | Phase C, MAIT or SAIT |  |
| Programmatic Integration & Execution | Schedule Planning & Control | Insufficient Schedule Margin | Schedule | Lack of adequate float/margin makes the project vulnerable to minor disruptions. | - Compressed internal timelines | - External approvals  - Provider availability |  | PREP 1 to SAIT |  |
| Programmatic Integration & Execution | Schedule Planning & Control | Poor Schedule Integration Across Teams | Schedule | Schedules are not fully integrated across subsystems or partners, creating conflicting paths. | - Weak configuration control of schedule updates | - Misaligned partner planning cycles |  | PREP 1 to SAIT |  |
| Programmatic Integration & Execution | Requirements & Scope Management | Evolving or Unstable Requirements | Technical | Requirements shift during development, prompting redesign and rescheduling. | - Incomplete early requirements - Late discoveries | - Regulatory or partner-driven changes | Phase 0 to Phase C | Phase 0 to Phase C |  |
| Programmatic Integration & Execution | Requirements & Scope Management | Scope Creep | Programmatic | Additional features or changes are added without corresponding increases in budget or schedule. | - Internal mission re-design | - Requests from science/user community | Phase 0 to Phase C | Phase 0 to Phase C |  |
| Programmatic Integration & Execution | Requirements & Scope Management | Unclear Definition of Deliverables | Programmatic | Deliverables or success criteria are not explicitly defined, resulting in rework and disputes. | - Vague SOW - Weak requirement traceability | - Partner interpretation differences | Phase 0 to Phase C | Phase 0 to Phase C |  |
| Programmatic Integration & Execution | Contracting & Procurement | Procurement and Contract Delays | Schedule | Delays in contract awards, evaluations, or negotiations slow project initiation and execution. | - Insufficient procurement staffing | - Federal procurement rules and oversight | PREP 1 & 2, Phase 0 to Phase B, MAIT | PREP 1 & 2, Phase 0 to Phase B, MAIT |  |
| Programmatic Integration & Execution | Contracting & Procurement | Misaligned Contract Structures | Governance | Contract types or terms do not support risk-sharing or needed flexibility. | - Inexperienced contracting officers | - Mandatory policy constraints | PREP 1 to MAIT | PREP 1 to MAIT |  |
| Programmatic Integration & Execution | Contracting & Procurement | Vendor Performance Issues | Programmatic | Prime or subcontractor performance problems cause rework or schedule delays | - Weak performance oversight | - Supplier instability | PREP 1 to MAIT | PREP 1 to MAIT |  |
| Programmatic Integration & Execution | Contracting & Procurement | Waste, Fraud, or Abuse Vulnerabilities | Governance | Inadequate internal controls expose the program to misuse of funds or fraudulent activity. | - Limited review time - Weak monitoring | - Complex multinational supply chains | All Phases |  |  |
| Programmatic Integration & Execution | Industrial Capability & Supplier Performance | Supplier Maturity Limitations | Programmatic | Suppliers lack mature processes, certifications, or capacity to deliver quality components on time. | - Insufficient oversight | - Small national supplier base | MAIT & SAIT | MAIT & SAIT |  |
| Programmatic Integration & Execution | Industrial Capability & Supplier Performance | Manufacturing Defects or Quality Issues | Technical | Supplier quality defects result in delays, retesting, or redesign. | - Weak acceptance processes | - Supplier QA inconsistency | MAIT & SAIT | MAIT & SAIT |  |
| Programmatic Integration & Execution | Industrial Capability & Supplier Performance | Overstretched SMEs | Programmatic | Small suppliers lack the throughput or staffing required for schedule-critical work. | - Inadequate supplier monitoring | - High demand across space industry | MAIT & SAIT | MAIT & SAIT |  |
| Programmatic Integration & Execution | Partnership & External Agreements | Misaligned Partner Schedules or Deliverables | Schedule | International partners operate on different timelines or processes, leading to integration delays. | - Insufficient internal integration planning | - Partner readiness issues | SAIT & ATLO | SAIT & ATLO |  |
| Programmatic Integration & Execution | Partnership & External Agreements | Partner Scope or Commitment Changes | Strategic | Changes in partner priorities, scope, or funding affect shared milestones or system architecture. | - Weak MOU/LOA clarity | - Changing political or budgetary environments | PREP 1 to ATLO | PREP 1 to ATLO |  |
| Programmatic Integration & Execution | Partnership & External Agreements | Export Control and Licensing Constraints | Governance | Export control requirements (ITAR, TAAs) delay access to components, data, or test facilities. | - Limited early export planning | - Regulatory changes | Phase B to ATLO | Phase B to ATLO |  |
| Programmatic Integration & Execution | Governance Processes & Controls | Weak Phase-Gate Discipline | Governance | Phase reviews lack rigor, allowing unresolved issues to carry forward. | - Inconsistent review criteria | - Pressure to meet partner timelines | Phase 0 to ATLO | Phase 0 to ATLO |  |
| Programmatic Integration & Execution | Governance Processes & Controls | Fragmented Technical/Cost/Schedule Reporting | Programmatic | Reports are inconsistent or disconnected, obscuring emerging risks. | - Misaligned data system | - Adjusted GoC reporting frameworks | All Phases | All Phases |  |
| External & Environmental Factors | Regulatory & Legal | Export Licensing or Regulatory Delays | Governance | Licensing processes delay hardware transfers, testing, or component acquisition. | - Unclear internal responsibilities | - ITAR/Canadian regulations | MAIT, SAIT, ATLO | MAIT, SAIT, ATLO |  |
| External & Environmental Factors | Regulatory & Legal | Changes in Laws, Policies, or Standards | Strategic | Domestic or international policy changes impact program scope, design, or compliance obligations. | - Slow adaptation | - New global or national regulations | Phase 0 to Phase C | Phase 0 to Phase C |  |
| External & Environmental Factors | Market & Supply Chain | Supplier Insolvency or Instability | Programmatic | Key suppliers face financial or operational challenges that disrupt delivery. | - Dependence on single supplier | - Market volatility | PREP 1 to SAIT | PREP 1 to SAIT |  |
| External & Environmental Factors | Market & Supply Chain | Price Escalation or Market Shock | Cost | Unexpected increase in material or component costs exceed planned budgets. | - Long-term fixed-price contracts | - Global supply shocks | MAIT & SAIT | MAIT & SAIT |  |
| External & Environmental Factors | Market & Supply Chain | Logistics and Shipping Disruptions | Schedule | Transportation or customs delays impact integration timelines. | - Limited logistics planning | - International border issues | MAIT, SAIT, ATLO | MAIT, SAIT, ATLO |  |
| External & Environmental Factors | Geopolitical & Economic | Currency Exchange Volatility | Cost | Foreign-denominated contracts become more expensive due to unstable currency rates. | - High foreign procurement content | - Global economic instability | PREP 1 to SAIT |  |  |
| External & Environmental Factors | Geopolitical & Economic | Inflation Spikes | Cost | Inflation increase labour, materials, and subcontractor prices beyond assumptions. | - Long program timeline | - Global economic trends | PREP 1 to SAIT |  |  |
| External & Environmental Factors | Geopolitical & Economic | Geopolitical Instability or Sanctions | Strategic | Political instability or sanctions disrupt suppliers, partners, or launch providers. | - Limited diversification | - International conflicts or trade actions | PREP 1 to ATLO | PREP 1 to ATLO |  |
| External & Environmental Factors | Force Majeure & Environmental Events | Natural Disasters or Environmental Accidents | Schedule | Floods, fires, or contamination events disrupt testing or manufacturing. | - Facility resilience gaps | - Environmental events | MAIT & SAIT | MAIT & SAIT |  |
| External & Environmental Factors | Force Majeure & Environmental Events | Space Weather Impacts | Technical | Radiation storms or solar activity necessitate design changes or additional testing. | - Margins underestimated | - Solar activity cycles | PREP 1 to SAIT | PREP 1 to SAIT |  |
| Strategic & Alignment Factors | Strategic Direction & Policy Alignment | Shifting GoC or Agency Priorities | Strategic | Changes in federal or departmental priorities alter program direction, scope, or funding. | - Misalignment with strategic planning | - New government mandates | Phase 0 to Phase C | Phase 0 to Phase C |  |
| Strategic & Alignment Factors | Strategic Direction & Policy Alignment | Policy-Driven Changes in Agency Focus | Strategic | Agency focus shifts between mission delivery and administrative compliance due to policy changes. | - Leadership turnover | - Political direction | Phase 0 to Phase C | Phase 0 to Phase C |  |
| Strategic & Alignment Factors | Value, Stewardship & "Mission vs Resources" Balance | Priority on Technology over Stewardship | Strategic | Culture prioritizes technical success over disciplines resource management, contribution to overruns. | - Incentives tied to innovation | - Public expectations for technological leadership | PREP 1 to ATLO |  |  |
| Strategic & Alignment Factors | Value, Stewardship & "Mission vs Resources" Balance | Unclear Mission Success Criteria | Governance | Lack of clear definition of success undermines tracking, reporting, and accountability. | - Weak KPI framework | - Evolving departmental expectations | PREP 1 to ATLO | PREP 1 to ATLO |  |
| Safety, Assurance & Compliance | System Safety & Human Protection | Inadequate Hazard Identification and Mitigation | Safety | Hazards are not fully identified or mitigated, increasing risk during testing or integration. | - Limited safety analysis | - New or updated safety regulations | MAIT & SAIT | MAIT & SAIT |  |
| Safety, Assurance & Compliance | System Safety & Human Protection | Safety Procedures Not Followed | Safety | Deviations from safety protocol create risk of injury or system damage. | - Training gaps | - Contractor procedure variance | MAIT & SAIT | MAIT & SAIT |  |
| Safety, Assurance & Compliance | Product Assurance & Quality Control | Inadequate QA or Inspection Processes | Technical | Weak QA processes lead to undetected defects in hardware or documentation. | - Insufficient QA staffing | - Supplier quality variability | MAIT & SAIT | MAIT & SAIT |  |
| Safety, Assurance & Compliance | Product Assurance & Quality Control | Configuration Management Lapses | Technical | CM issues result in inconsistencies between design, test, and manufacturing data. | - Weak configuration discipline | - Partner CM incompatibility | MAIT & SAIT | MAIT & SAIT |  |
| Safety, Assurance & Compliance | Test & Verification | Incomplete or Insufficient Test Plans | Technical | Gaps in test coverage allow defects to be discovered late. | - Inadequate early test planning | - Facility limitations | MAIT, SAIT, LEOP, ATLO, Early Ops, Phase E | MAIT, SAIT, LEOP, ATLO, Early Ops, Phase E |  |
| Safety, Assurance & Compliance | Test & Verification | Late Discovery of Non-Compliance | Technical | Key requirements failures are found late in qualification, increasing cost and schedule impact. | - Weak integration testing | - Late partner deliveries | MAIT & SAIT | MAIT & SAIT |  |
| Safety, Assurance & Compliance | Certification & Standards | Delayed Safety or Standards Certification | Governance | Delays obtaining required certifications impede integration or launch activities | - Incomplete documentation | - Changing standards | LEOP, ATLO, Cruise Out | LEOP, ATLO, Cruise Out |  |
| Data, Knowledge & Integration | Data Integration & Consistency | Misaligned Baselines (Cost, Schedule, Technical) | Programmatic | Cost, schedule, and technical baselines are not consistently aligned, obscuring issues. | - Tool integration gaps | - Partner baseline mismatches | PREP 1 to ATLO | PREP 1 to ATLO |  |
| Data, Knowledge & Integration | Data Integration & Consistency | Inconsistent Data Exchange Across Teams | Programmatic | Data is inconsistent or incompatible across engineering, finance, and risk systems. | - Multiple unlinked tools | - Partner data format variability | PREP 1 to ATLO | PREP 1 to ATLO |  |
| Data, Knowledge & Integration | Knowledge Management | Knowledge Loss Through Poor Documentation | Programmatic | Documentation gaps cause loss of design rationale and technical context across phases. | - Weak KM discipline | - Staff turnover | Phase 0 to Phase C | Phase 0 to Phase C |  |
| Data, Knowledge & Integration | Knowledge Management | Absence of a Knowledge Management Framework | Governance | Lack of organizational KM policy results in inconsistent retention of critical program information. | - No formal KM process | - Cross-agency documentation expectations | PREP 1 to Phase C | PREP 1 to Phase C |  |

## Raw Labour Rates

| Raw Labour Rates |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Illustrative extract of published Treasury Board of Canada pay-scale bands, top (MAX) step only, for the classification groups used on the ORCA project. Placeholder figures pending confirmed CSA compensation data; not authoritative. |  |  |  |  |  |
|  |  |  |  |  |  |
| Classification | Classification Name | Step | Salary | Effective Date | Active |
| AS-1 | Administrative Services 1 | MAX | 55000 | 2026-04-01 | Yes |
| AS-2 | Administrative Services 2 | MAX | 62000 | 2026-04-01 | Yes |
| CR-4 | Clerical and Regulatory 4 | MAX | 58000 | 2026-04-01 | Yes |
| CS-2 | Computer Systems 2 | MAX | 78000 | 2026-04-01 | Yes |
| EC-1 | Economics and Social Science Services 1 | MAX | 70000 | 2026-04-01 | Yes |
| EG-6 | Engineering and Scientific Support 6 | MAX | 95000 | 2026-04-01 | Yes |
| EN-ENG-3 | Engineering 3 | MAX | 110000 | 2026-04-01 | Yes |
| EN-ENG-4 | Engineering 4 | MAX | 128000 | 2026-04-01 | Yes |
| EN-ENG-5 | Engineering 5 | MAX | 145000 | 2026-04-01 | Yes |
| EN-ENG-6 | Engineering 6 | MAX | 165000 | 2026-04-01 | Yes |
| EX-2 | Executive 2 | MAX | 175000 | 2026-04-01 | Yes |
| GT-4 | General Technical 4 | MAX | 72000 | 2026-04-01 | Yes |
| PC-3 | Physical Sciences 3 | MAX | 105000 | 2026-04-01 | Yes |
| PC-4 | Physical Sciences 4 | MAX | 122000 | 2026-04-01 | Yes |
| PC-5 | Physical Sciences 5 | MAX | 140000 | 2026-04-01 | Yes |

## Labour Rates lookup

| Labour Rates lookup |  |  |
| --- | --- | --- |
| One row per classification actually used on the ORCA RAM, with its top-step (MAX) annual rate pulled from 'Raw Labour Rates' by formula. The RAM sheet's Rate column looks up against this table. |  |  |
|  |  |  |
| Classification | MaxStep |  |
| AS-1 | 55000 |  |
| AS-2 | 62000 |  |
| CR-4 | 58000 |  |
| CS-2 | 78000 |  |
| EC-1 | 70000 |  |
| EG-6 | 95000 |  |
| EN-ENG-3 | 110000 |  |
| EN-ENG-4 | 128000 |  |
| EN-ENG-5 | 145000 |  |
| EN-ENG-6 | 165000 |  |
| EX-2 | 175000 |  |
| GT-4 | 72000 |  |
| PC-3 | 105000 |  |
| PC-4 | 122000 |  |
| PC-5 | 140000 |  |

## Rolodex

| Rolodex |  |  |  |  |
| --- | --- | --- | --- | --- |
| Fictional placeholder directory for the ORCA project team. Names are illustrative and used only to drive the RAM sheet's Classification lookup; no real CSA personnel data is represented here. |  |  |  |  |
|  |  |  |  |  |
| Employee Name | Classification | Position Title | Position No | Directorate |
| Alan Whitfield | EN-ENG-6 | Portfolio Manager | ORCA-PM-001 | Program Management |
| Marie Tremblay | PC-4 | ORCA Mission Manager | ORCA-PM-002 | Program Management |
| Devon Okafor | PC-3 | Mission Operations Scientist | ORCA-SCI-001 | Planetary Science |
| Priya Raman | EN-ENG-5 | Lead Project Manager | ORCA-PM-003 | Program Management |
| Étienne Lacroix | EN-ENG-4 | Deputy Project Manager | ORCA-PM-004 | Program Management |
| Grace Lindqvist | EN-ENG-4 | Project Management Engineer | ORCA-PM-005 | Program Management |
| Samuel Boucher | EN-ENG-4 | Schedule and Cost Management Engineer | ORCA-PM-006 | Program Management |
| Naomi Fitzgerald | EN-ENG-5 | Lead Spacecraft Systems Engineer | ORCA-SE-001 | Engineering |
| Kevin Anand | EN-ENG-4 | Spacecraft Systems Engineer | ORCA-SE-002 | Engineering |
| Isabelle Roy | EN-ENG-4 | Instrument Pointing / GNC Engineer | ORCA-GNC-001 | Engineering |
| Marcus Delgado | EN-ENG-4 | Sampling Arm (ISA) Systems Engineer (Option C) | ORCA-ISA-001 | Engineering |
| Fatima Haidari | EN-ENG-5 | Safety and Mission Assurance Engineer | ORCA-SMA-001 | Engineering |
| Robert Cianci | EN-ENG-4 | Fault Detection, Isolation and Recovery Engineer | ORCA-FDIR-001 | Engineering |
| Simone Bergeron | EN-ENG-4 | Mission Operations and Ground Systems Engineer | ORCA-OPS-001 | Mission Operations |
| Yusuf Karimi | PC-4 | Mass Spectrometer Lead Engineer | ORCA-INS-001 | Engineering |
| Charlotte Nadeau | PC-3 | Ice-Penetrating Radar Lead Engineer | ORCA-INS-002 | Engineering |
| Daniel Osei | EN-ENG-5 | Electromagnetic Compatibility (EMC/EMI) Specialist | ORCA-EMC-001 | Engineering |
| Vera Kowalski | EN-ENG-5 | Space Environment and Radiation Engineer | ORCA-RAD-001 | Engineering |
| Thomas Girard | EN-ENG-4 | Instrument Suite Structures Engineer | ORCA-STR-001 | Engineering |
| Aline Petit | EN-ENG-4 | Launch and Mechanical Environment Engineer | ORCA-MEC-001 | Engineering |
| Hassan Malik | EN-ENG-4 | Sampling Arm Mechanisms Engineer (Option C) | ORCA-ISA-002 | Engineering |
| Julie Beaulieu | EN-ENG-4 | Guidance, Navigation and Control (GNC) Engineer | ORCA-GNC-002 | Engineering |
| Owen MacKenzie | EN-ENG-4 | Thermal Control Engineer | ORCA-THM-001 | Engineering |
| Leila Amini | EN-ENG-5 | RTG / Power Systems Engineer | ORCA-PWR-001 | Engineering |
| Nathan Cormier | EN-ENG-4 | Flight Software and Autonomy Engineer | ORCA-SW-001 | Engineering |

## Inflation Rate

| Inflation Rate |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Base Year 2026 |  |  |  |
| Illustrative escalation table. Historic years use placeholder Bank-of-Canada-style CPI figures; future years assume a flat 2.5% escalation. Not authoritative; pending confirmed CSA/TBS economic parameters. |  |  |  |  |
| FY | Inflation Rate | In BY 2026 | Forward Index | Source |
| 2010 | Historical CPI | 1.33 |  | Illustrative - Bank of Canada CPI series |
| 2011 | Historical CPI | 1.31 |  | Illustrative - Bank of Canada CPI series |
| 2012 | Historical CPI | 1.29 |  | Illustrative - Bank of Canada CPI series |
| 2013 | Historical CPI | 1.27 |  | Illustrative - Bank of Canada CPI series |
| 2014 | Historical CPI | 1.25 |  | Illustrative - Bank of Canada CPI series |
| 2015 | Historical CPI | 1.23 |  | Illustrative - Bank of Canada CPI series |
| 2016 | Historical CPI | 1.21 |  | Illustrative - Bank of Canada CPI series |
| 2017 | Historical CPI | 1.19 |  | Illustrative - Bank of Canada CPI series |
| 2018 | Historical CPI | 1.17 |  | Illustrative - Bank of Canada CPI series |
| 2019 | Historical CPI | 1.15 |  | Illustrative - Bank of Canada CPI series |
| 2020 | Historical CPI | 1.13 |  | Illustrative - Bank of Canada CPI series |
| 2021 | Historical CPI | 1.11 |  | Illustrative - Bank of Canada CPI series |
| 2022 | Historical CPI | 1.09 |  | Illustrative - Bank of Canada CPI series |
| 2023 | Historical CPI | 1.07 |  | Illustrative - Bank of Canada CPI series |
| 2024 | Historical CPI | 1.05 |  | Illustrative - Bank of Canada CPI series |
| 2025 | Historical CPI | 1.03 |  | Illustrative - Bank of Canada CPI series |
| 2026 | 0 | 1 | 1 | Base year |
| 2027 | 0.025 |  | 1.025 | Illustrative flat 2.5%/yr escalation |
| 2028 | 0.025 |  | 1.050625 | Illustrative flat 2.5%/yr escalation |
| 2029 | 0.025 |  | 1.0768906249999999 | Illustrative flat 2.5%/yr escalation |
| 2030 | 0.025 |  | 1.1038128906249998 | Illustrative flat 2.5%/yr escalation |
| 2031 | 0.025 |  | 1.1314082128906247 | Illustrative flat 2.5%/yr escalation |
| 2032 | 0.025 |  | 1.1596934182128902 | Illustrative flat 2.5%/yr escalation |
| 2033 | 0.025 |  | 1.1886857536682123 | Illustrative flat 2.5%/yr escalation |
| 2034 | 0.025 |  | 1.2184028975099175 | Illustrative flat 2.5%/yr escalation |
| 2035 | 0.025 |  | 1.2488629699476652 | Illustrative flat 2.5%/yr escalation |
| 2036 | 0.025 |  | 1.2800845441963566 | Illustrative flat 2.5%/yr escalation |
| 2037 | 0.025 |  | 1.3120866578012655 | Illustrative flat 2.5%/yr escalation |
| 2038 | 0.025 |  | 1.344888824246297 | Illustrative flat 2.5%/yr escalation |
| 2039 | 0.025 |  | 1.3785110448524545 | Illustrative flat 2.5%/yr escalation |
| 2040 | 0.025 |  | 1.4129738209737657 | Illustrative flat 2.5%/yr escalation |
| 2041 | 0.025 |  | 1.4482981664981096 | Illustrative flat 2.5%/yr escalation |
| 2042 | 0.025 |  | 1.4845056206605622 | Illustrative flat 2.5%/yr escalation |
| 2043 | 0.025 |  | 1.521618261177076 | Illustrative flat 2.5%/yr escalation |
| 2044 | 0.025 |  | 1.5596587177065029 | Illustrative flat 2.5%/yr escalation |
| 2045 | 0.025 |  | 1.5986501856491653 | Illustrative flat 2.5%/yr escalation |
| 2046 | 0.025 |  | 1.6386164402903942 | Illustrative flat 2.5%/yr escalation |
| 2047 | 0.025 |  | 1.679581851297654 | Illustrative flat 2.5%/yr escalation |
| 2048 | 0.025 |  | 1.721571397580095 | Illustrative flat 2.5%/yr escalation |
| 2049 | 0.025 |  | 1.7646106825195973 | Illustrative flat 2.5%/yr escalation |
| 2050 | 0.025 |  | 1.8087259495825871 | Illustrative flat 2.5%/yr escalation |
| 2051 | 0.025 |  | 1.8539440983221516 | Illustrative flat 2.5%/yr escalation |
| 2052 | 0.025 |  | 1.9002927007802053 | Illustrative flat 2.5%/yr escalation |
| 2053 | 0.025 |  | 1.9478000182997102 | Illustrative flat 2.5%/yr escalation |
| 2054 | 0.025 |  | 1.9964950187572028 | Illustrative flat 2.5%/yr escalation |
| 2055 | 0.025 |  | 2.0464073942261325 | Illustrative flat 2.5%/yr escalation |
| 2056 | 0.025 |  | 2.097567579081786 | Illustrative flat 2.5%/yr escalation |
| 2057 | 0.025 |  | 2.15000676855883 | Illustrative flat 2.5%/yr escalation |
| 2058 | 0.025 |  | 2.2037569377728006 | Illustrative flat 2.5%/yr escalation |
| 2059 | 0.025 |  | 2.2588508612171205 | Illustrative flat 2.5%/yr escalation |
| 2060 | 0.025 |  | 2.315322132747548 | Illustrative flat 2.5%/yr escalation |
