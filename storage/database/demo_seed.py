"""
Demo database seeder — populates SQLite with mission params and demo users.

Reads cadre_mission_params.py (extracted from Part A files) and inserts
into cadre_params table. Creates demo users from demo/profiles.py.

Usage: python -m storage.database.demo_seed
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from werkzeug.security import generate_password_hash

from storage.database.connection import create_connection
from storage.database.runner import run_migrations

# Import the hand-extracted mission params
from storage.database.cadre_mission_params import MISSIONS

# Demo users
DEMO_USERS = {
    "fredmoney": {"password": "1", "role": "finance", "division": "OCFO", "region": "HQ"},
    "joemotochar": {"password": "1", "role": "engineer", "division": "Engineering", "region": "HQ"},
    "murphyslipz": {"password": "1", "role": "risk", "division": "Risk Management", "region": "HQ"},
}


def main():
    """Seed the database with missions and demo users."""
    db_path = Path("app/database/cheddar.db")

    print("=" * 50)
    print("  Demo Quick — Database Seeder")
    print("=" * 50)

    # Reset database for clean demo
    if db_path.exists():
        db_path.unlink()
        print("  Cleared existing database.")

    conn = create_connection(db_path)
    run_migrations(conn)

    # Create cadre_params table
    _create_cadre_params_table(conn)

    # Seed missions
    _seed_missions(conn)

    # Seed demo users
    _seed_users(conn)

    conn.commit()
    conn.close()

    print(f"\n  Seeded {len(MISSIONS)} missions and {len(DEMO_USERS)} users.")
    print("  Ready to run: python -m demo.runner")


def _create_cadre_params_table(conn):
    """Create the cadre_params table for mission parameter storage."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS cadre_params (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mission_key TEXT NOT NULL UNIQUE,
            mission_name TEXT NOT NULL,
            mass_kg REAL,
            power_w_gen REAL,
            power_w_nom REAL,
            power_w_peak REAL,
            payload_mass_kg REAL,
            propellant_mass_kg REAL,
            delta_v_ms REAL,
            duration_years REAL,
            number_spacecraft INTEGER,
            data_gb_day REAL,
            source_file TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
        """
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_cadre_params_name ON cadre_params(mission_name)"
    )


def _seed_missions(conn):
    """Insert all extracted mission parameters into cadre_params."""
    now = datetime.now(timezone.utc).isoformat()
    count = 0

    for key, params in MISSIONS.items():
        conn.execute(
            """
            INSERT OR REPLACE INTO cadre_params
            (mission_key, mission_name, mass_kg, power_w_gen, power_w_nom, power_w_peak,
             payload_mass_kg, propellant_mass_kg, delta_v_ms, duration_years,
             number_spacecraft, data_gb_day, source_file, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                key,
                params.get("mission_name", key),
                params.get("mass_kg"),
                params.get("power_w_gen"),
                params.get("power_w_nom"),
                params.get("power_w_peak"),
                params.get("payload_mass_kg"),
                params.get("propellant_mass_kg"),
                params.get("delta_v_ms"),
                params.get("duration_years"),
                params.get("number_spacecraft"),
                params.get("data_gb_day"),
                params.get("file", ""),
                now,
            ),
        )
        count += 1
        print(f"  Seeded: {params.get('mission_name', key)}")

    print(f"\n  {count} missions inserted.")


def _seed_users(conn):
    """Insert demo users with hashed passwords."""
    now = datetime.now(timezone.utc).isoformat()

    for username, profile in DEMO_USERS.items():
        password_hash = generate_password_hash(profile["password"])

        # Check if user already exists
        existing = conn.execute(
            "SELECT username FROM users WHERE username=?", (username,)
        ).fetchone()

        if existing:
            conn.execute(
                "UPDATE users SET role=?, division=?, region=? WHERE username=?",
                (profile["role"], profile["division"], profile["region"], username),
            )
        else:
            conn.execute(
                """
                INSERT INTO users
                (username, password_hash, role, division, region, flags, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    username,
                    password_hash,
                    profile["role"],
                    profile["division"],
                    profile["region"],
                    json.dumps([]),
                    now,
                ),
            )
        print(f"  User: {username} ({profile['role']})")


if __name__ == "__main__":
    main()