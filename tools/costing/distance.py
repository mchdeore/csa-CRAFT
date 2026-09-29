"""
CADRe mission parameter distance engine.

Computes: z-score normalize target against population, weighted Euclidean
distance with rank-based weights, returns top-N matches.
"""

import math
import statistics
from typing import Any


# Dimensions used in comparison
ALL_DIMENSIONS = [
    "mass_kg",
    "power_w_gen",
    "power_w_nom",
    "power_w_peak",
    "payload_mass_kg",
    "propellant_mass_kg",
    "delta_v_ms",
    "duration_years",
    "number_spacecraft",
    "data_gb_day",
]


def _build_population_stats(data_store):
    """Load all missions from cadre_params table and compute mean/stddev per dimension."""
    rows = data_store._conn.execute("SELECT * FROM cadre_params").fetchall()

    stats = {}
    for dim in ALL_DIMENSIONS:
        vals = [float(r[dim]) for r in rows if r[dim] is not None]
        if len(vals) < 2:
            stats[dim] = {"mean": 0.0, "stddev": 1.0}
        else:
            stats[dim] = {
                "mean": statistics.mean(vals),
                "stddev": statistics.stdev(vals),
            }

    return stats


def _z_score(value, dim_stats):
    """Standardize a value to z-score using population mean/stdev."""
    if value is None or dim_stats["stddev"] == 0:
        return 0.0
    return (value - dim_stats["mean"]) / dim_stats["stddev"]


def _weighted_distance(target_z, mission_z, weights):
    """Weighted Euclidean distance between two z-score vectors."""
    total = 0.0
    for dim, weight in weights.items():
        delta = target_z.get(dim, 0) - mission_z.get(dim, 0)
        total += weight * delta * delta
    return math.sqrt(total)


def compute_comparison(
    target_params: dict,
    weight_order: list[str],
    active_dimensions: set[str] | None,
    n: int,
    data_store,
) -> dict[str, Any]:
    """Run full parametric comparison of target mission against population.

    Args:
        target_params: Dict of extracted fields (dim → raw_value).
        weight_order: Ordered list of dimensions (first = heaviest weight).
        active_dimensions: Set of currently active dimensions. None means all.
        n: Number of top matches to return.
        data_store: SqliteDataStore instance for querying cadre_params.

    Returns dict with top_n, all_rankings, target_z, weights, population_stats.
    """
    if active_dimensions is None:
        active_dimensions = set(weight_order)

    # Filter to active dimensions only, preserving order
    active_order = [d for d in weight_order if d in active_dimensions]
    ndim = len(active_order)

    if ndim == 0:
        raise ValueError("No active dimensions selected for comparison")

    # Compute rank-based weights: 2*(n-i)/(n*(n-1)) gives descending weights summing to 1
    # First dimension gets highest weight
    weights = {}
    if ndim == 1:
        weights = {active_order[0]: 1.0}
    else:
        for i, dim in enumerate(active_order):
            weights[dim] = 2 * (ndim - i) / (ndim * (ndim - 1))

    # Build population stats
    population_stats = _build_population_stats(data_store)

    # Compute target z-scores
    target_z = {}
    for dim in active_order:
        val = target_params.get(dim)
        target_z[dim] = _z_score(val, population_stats.get(dim, {"mean": 0.0, "stddev": 1.0}))

    # Query all missions
    rows = data_store._conn.execute("SELECT * FROM cadre_params").fetchall()

    results = []
    for row in rows:
        mission_z = {}
        raw_values = {}

        for dim in active_order:
            val = row[dim] if dim in row.keys() else None
            raw_values[dim] = val
            mission_z[dim] = _z_score(
                val, population_stats.get(dim, {"mean": 0.0, "stddev": 1.0})
            )

        distance = _weighted_distance(target_z, mission_z, weights)

        deltas = {}
        for dim in active_order:
            deltas[dim] = mission_z[dim] - target_z.get(dim, 0)

        results.append(
            {
                "mission_name": row["mission_name"],
                "distance": distance,
                "z_scores": mission_z,
                "deltas": deltas,
                "raw_values": raw_values,
            }
        )

    # Sort by distance (ascending)
    results.sort(key=lambda r: r["distance"])

    return {
        "top_n": results[:n],
        "all_rankings": results,
        "target_z": target_z,
        "weights": weights,
        "population_stats": population_stats,
        "active_dimensions": active_order,
    }