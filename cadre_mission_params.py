"""
CADRe Part A — extracted numeric spacecraft parameters from 19 mission files.
Source: /Users/cheddar/Documents/CODE/csa-cheddar/data/cadre-missions/*part-a*.md

Only includes parameters that could be confidently extracted from the
spacecraft/unit specification table or equivalent text in each file.
Missing entries mean the parameter was not found or not applicable.
"""

MISSIONS = {
    # astronomy-keralis-part-a.md
    "astronomy-keralis": {
        "file": "astronomy-keralis-part-a.md",
        "mission_name": "Keralis",
        "mass_kg": 340,
        "power_w_gen": 630,
        "power_w_nominal": 320,
        "power_w_peak": 500,
        "payload_mass_kg": 64,
        "propellant_mass_kg": 80,
        "delta_v_ms": 550,
        "duration_years": 3.0,  # 36 months launch-to-closeout
        "number_spacecraft": 1,
        "data_gb_day": 2.0,
    },

    # astronomy-lumen-observatory-part-a.md
    "astronomy-lumen-observatory": {
        "file": "astronomy-lumen-observatory-part-a.md",
        "mission_name": "LUMEN",
        # CEAM instrument: 140 kg, 300 W — instrument only, spacecraft is ESA-provided
        "payload_mass_kg": 140,
        "power_w_gen": 300,  # CEAM during science observations
        "duration_years": 5,
        "number_spacecraft": 4,  # constellation of 4; 4th is on-orbit spare
    },

    # astronomy-myralis-part-a.md
    "astronomy-myralis": {
        "file": "astronomy-myralis-part-a.md",
        "mission_name": "Myralis",
        "mass_kg": 210,
        "power_w_gen": 780,
        "power_w_nominal": 410,
        "power_w_peak": 625,
        "payload_mass_kg": 38,
        "propellant_mass_kg": 24,
        "delta_v_ms": 180,
        "duration_years": 5.5,  # five-year science + six-month cruise
        "number_spacecraft": 3,
        "data_gb_day": 0.75,
    },

    # eo-hyperspectral-part-a.md
    "eo-hyperspectral": {
        "file": "eo-hyperspectral-part-a.md",
        "mission_name": "Syrelis",
        "mass_kg": 620,
        "power_w_gen": 1600,
        "power_w_nominal": 900,
        "power_w_peak": 1300,
        "payload_mass_kg": 140,
        "propellant_mass_kg": 40,
        "delta_v_ms": 120,
        "duration_years": 6,  # six-year design life
        "number_spacecraft": 1,
        "data_gb_day": 25,
    },

    # food-production-peluvia-part-a.md
    "food-production-peluvia": {
        "file": "food-production-peluvia-part-a.md",
        "mission_name": "Peluvia",
        "mass_kg": 445,
        "power_w_gen": 450,
        "power_w_nominal": 450,
        "power_w_peak": 800,
        "payload_mass_kg": 445,  # entire unit is the payload (surface habitat)
        "duration_years": 3,
        "number_spacecraft": 1,
        "data_gb_day": 0.2,
    },

    # health-thovaren-part-a.md
    "health-thovaren": {
        "file": "health-thovaren-part-a.md",
        "mission_name": "Thovaren",
        "mass_kg": 95,
        "power_w_gen": 180,
        "power_w_nominal": 30,
        "power_w_peak": 180,
        "payload_mass_kg": 95,
        "duration_years": 2,
        "number_spacecraft": 1,
        "data_gb_day": 0.05,
    },

    # planetary-isru-part-a.md
    "planetary-isru": {
        "file": "planetary-isru-part-a.md",
        "mission_name": "Kerovar",
        "mass_kg": 520,
        "power_w_gen": 3000,
        "power_w_nominal": 450,
        "power_w_peak": 1800,
        "payload_mass_kg": 520,
        "duration_years": 1,  # one-year design life
        "number_spacecraft": 1,
        "data_gb_day": 0.5,
    },

    # planetary-science-casce-part-a.md
    "planetary-science-casce": {
        "file": "planetary-science-casce-part-a.md",
        "mission_name": "CASCE",
        # CSA-built instrument on ESA-provided bus; no unit mass/power table
        "duration_years": 5,  # 60 months nominal operations
        "number_spacecraft": 4,  # constellation of 4, 4th is on-orbit spare
    },

    # planetary-science-europa-vitality-part-a.md
    "planetary-science-europa-vitality": {
        "file": "planetary-science-europa-vitality-part-a.md",
        "mission_name": "EVE",
        # Orbiter values from detailed subsystem paragraphs
        "power_w_gen": 7200,  # EOL at 5.2 AU
        "propellant_mass_kg": 1850,
        "delta_v_ms": 2650,  # nominal mission ΔV (3.00 km/s total capability)
        "number_spacecraft": 1,  # 1 orbiter (plus lander + rover)
    },

    # planetary-science-orca-part-a.md
    "planetary-science-orca": {
        "file": "planetary-science-orca-part-a.md",
        "mission_name": "ORCA",
        # Canadian instrument suite on NASA flagship; suite-level allocations
        "payload_mass_kg": 85,
        "power_w_peak": 110,
        "duration_years": 4,  # prime science mission at Saturn
        "number_spacecraft": 1,
    },

    # planetary-science-qoralis-part-a.md
    "planetary-science-qoralis": {
        "file": "planetary-science-qoralis-part-a.md",
        "mission_name": "Qoralis",
        # QO-1 (orbiter) values; QS-1 lander is separate
        "mass_kg": 650,  # QO-1 target
        "power_w_gen": 1050,  # QO-1 EOL at 3.35 AU
        "payload_mass_kg": 95,  # QO-1 payload
        "delta_v_ms": 780,  # QO-1 total
        "duration_years": 2,  # 24 months nominal science
        "number_spacecraft": 2,  # orbiter + lander
        "data_gb_day": 9.2,  # 8 GB/day QO-1 + 1.2 GB/day QS-1
    },

    # planetary-velum-flyby-part-a.md
    "planetary-velum-flyby": {
        "file": "planetary-velum-flyby-part-a.md",
        "mission_name": "Velum",
        "mass_kg": 650,
        "power_w_gen": 3150,
        "power_w_nominal": 410,
        "power_w_peak": 720,
        "payload_mass_kg": 86,
        "propellant_mass_kg": 100,
        "delta_v_ms": 320,
        "duration_years": 4.5,  # 48-month cruise + 6-month approach
        "number_spacecraft": 1,
        "data_gb_day": 20,  # encounter burst; cruise is ~1 GB/day
    },

    # platform-tech-rovenna-part-a.md
    "platform-tech-rovenna": {
        "file": "platform-tech-rovenna-part-a.md",
        "mission_name": "Rovenna",
        "mass_kg": 480,
        "power_w_gen": 1100,
        "power_w_nominal": 720,
        "power_w_peak": 950,
        "payload_mass_kg": 130,
        "propellant_mass_kg": 28,
        "delta_v_ms": 90,
        "duration_years": 2,
        "number_spacecraft": 1,
        "data_gb_day": 5,
    },

    # satcom-vpcs-part-a.md
    "satcom-vpcs": {
        "file": "satcom-vpcs-part-a.md",
        "mission_name": "Virelan",
        "mass_kg": 1150,
        "power_w_gen": 5400,
        "power_w_nominal": 3200,
        "power_w_peak": 4700,
        "payload_mass_kg": 180,
        "propellant_mass_kg": 550,
        "delta_v_ms": 1850,
        "duration_years": 10,
        "number_spacecraft": 3,
        "data_gb_day": 18,
    },

    # solar-terrestrial-calithra-part-a.md
    "solar-terrestrial-calithra": {
        "file": "solar-terrestrial-calithra-part-a.md",
        "mission_name": "Calithra",
        "mass_kg": 120,
        "power_w_gen": 450,
        "power_w_nominal": 270,
        "power_w_peak": 385,
        "payload_mass_kg": 24,
        "propellant_mass_kg": 8,
        "delta_v_ms": 110,
        "duration_years": 3,
        "number_spacecraft": 4,
        "data_gb_day": 1.0,
    },

    # solar-terrestrial-orastra-part-a.md
    "solar-terrestrial-orastra": {
        "file": "solar-terrestrial-orastra-part-a.md",
        "mission_name": "Orastra",
        "mass_kg": 260,
        "power_w_gen": 720,
        "power_w_nominal": 410,
        "power_w_peak": 600,
        "payload_mass_kg": 40,
        "propellant_mass_kg": 10,
        "delta_v_ms": 70,
        "duration_years": 4,
        "number_spacecraft": 2,
        "data_gb_day": 6,
    },

    # solar-terrestrial-tavora-part-a.md
    "solar-terrestrial-tavora": {
        "file": "solar-terrestrial-tavora-part-a.md",
        "mission_name": "Tavora",
        "mass_kg": 180,
        "power_w_gen": 520,
        "power_w_nominal": 310,
        "power_w_peak": 445,
        "payload_mass_kg": 43,
        "propellant_mass_kg": 12,
        "delta_v_ms": 95,
        "duration_years": 4,
        "number_spacecraft": 2,
        "data_gb_day": 20,
    },

    # space-surveillance-sam-part-a.md
    "space-surveillance-sam": {
        "file": "space-surveillance-sam-part-a.md",
        "mission_name": "SAM",
        "mass_kg": 500,  # target launch mass
        "power_w_gen": 500,  # payload continuous allocation
        "power_w_peak": 750,
        "payload_mass_kg": 150,
        "delta_v_ms": 99.6,
        "duration_years": 5,
        "number_spacecraft": 2,
        "data_gb_day": 125,
    },

    # ssa-zelvora-debris-part-a.md
    "ssa-zelvora-debris": {
        "file": "ssa-zelvora-debris-part-a.md",
        "mission_name": "ZELVORA",
        # No numeric mass, power, or ΔV table in this Part A
        "number_spacecraft": 1,
    },
}