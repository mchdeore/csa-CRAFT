"""
Compliance checking — 5 hardcoded design rules for CADRe Part A documents.

Rules return pass/warn/fail with detail messages.
"""

# Hardcoded compliance rules
RULES = [
    {
        "name": "Mass Budget ≤ 650 kg",
        "check": lambda f: float(f.get("mass_kg", 0)) <= 650 if f.get("mass_kg") else None,
        "detail": lambda f: (
            f"Unit mass: {f.get('mass_kg')} kg — {'within' if float(f.get('mass_kg', 0)) <= 650 else 'EXCEEDS'} 650 kg limit"
        ),
    },
    {
        "name": "Power Generation ≥ 400 W",
        "check": lambda f: float(f.get("power_w_gen", 0)) >= 400 if f.get("power_w_gen") else None,
        "detail": lambda f: (
            f"Power generation: {f.get('power_w_gen')} W — "
            f"{'meets' if float(f.get('power_w_gen', 0)) >= 400 else 'BELOW'} 400 W minimum"
        ),
    },
    {
        "name": "Peak Power Margin ≥ 20%",
        "check": lambda f: (
            (float(f.get("power_w_peak", 0)) - float(f.get("power_w_nom", 0)))
            / float(f.get("power_w_nom", 1)) >= 0.2
        ) if f.get("power_w_peak") and f.get("power_w_nom") else None,
        "detail": lambda f: (
            f"Peak: {f.get('power_w_peak')} W, Nominal: {f.get('power_w_nom')} W — "
            f"margin: {((float(f.get('power_w_peak', 0)) - float(f.get('power_w_nom', 0))) / float(f.get('power_w_nom', 1))) * 100:.0f}%"
        ),
    },
    {
        "name": "Payload Fraction ≤ 25%",
        "check": lambda f: (
            float(f.get("payload_mass_kg", 0)) / float(f.get("mass_kg", 1)) <= 0.25
        ) if f.get("payload_mass_kg") and f.get("mass_kg") else None,
        "detail": lambda f: (
            f"Payload: {f.get('payload_mass_kg')} kg / Unit mass: {f.get('mass_kg')} kg = "
            f"{float(f.get('payload_mass_kg', 0)) / float(f.get('mass_kg', 1)) * 100:.0f}%"
        ),
    },
    {
        "name": "Delta-V Budget ≥ 80 m/s",
        "check": lambda f: float(f.get("delta_v_ms", 0)) >= 80 if f.get("delta_v_ms") else None,
        "detail": lambda f: (
            f"Delta-V: {f.get('delta_v_ms')} m/s — "
            f"{'meets' if float(f.get('delta_v_ms', 0)) >= 80 else 'BELOW'} 80 m/s minimum"
        ),
    },
]


def run_compliance(extracted_fields: dict) -> dict:
    """Run all 5 compliance rules against extracted CADRe Part A fields.

    Returns dict with rules list (each has name, status, detail) and summary
    with pass/warn/fail/skip counts. Rules that can't run due to missing data
    get status "warn" rather than failing silently.

    >>> result = run_compliance({"mass_kg": 500, "power_w_gen": 600, "power_w_peak": 800, "power_w_nom": 600, "payload_mass_kg": 100, "delta_v_ms": 120})
    >>> result["summary"]["total"]
    5
    >>> result["summary"]["passed"]
    5
    >>> result["rules"][0]["status"]
    'pass'

    >>> result = run_compliance({"mass_kg": 700})
    >>> result["summary"]["passed"] + result["summary"]["warned"] + result["summary"]["failed"]
    5
    >>> result["rules"][0]["status"]
    'fail'
    """
    results = []
    passed = 0
    warned = 0
    failed = 0
    skipped = 0

    for rule in RULES:
        check_result = rule["check"](extracted_fields)

        if check_result is None:
            status = "warn"
            detail = f"Cannot check: missing required fields."
            warned += 1
        elif check_result is True:
            status = "pass"
            detail = rule["detail"](extracted_fields)
            passed += 1
        else:
            status = "fail"
            detail = rule["detail"](extracted_fields)
            failed += 1

        results.append(
            {
                "name": rule["name"],
                "status": status,
                "detail": detail,
            }
        )

    return {
        "rules": results,
        "summary": {
            "total": len(results),
            "passed": passed,
            "warned": warned,
            "failed": failed,
            "skipped": skipped,
        },
    }