# === project.py ===
# CS50 Final Project (Starter): Space Explorer Toolkit
# Starter goals:
#   - Keep structure ready, leave core logic as TODOs.
#   - ≥3 helper functions + main().
#   - No external libraries in code (pytest only for tests).
#   - Pytest tests in test_project.py will FAIL until TODOs are completed.

from math import sqrt
from typing import Tuple, Dict

# Gravitational constant for escape velocity (m^3 kg^-1 s^-2)
G = 6.67430e-11

# Minimal starter dataset. You can add more planets later.
# g_ratio is relative to Earth (1.0).
PLANETS: Dict[str, Dict[str, float]] = {
    "Mercury": {"g_ratio": 0.38, "mass": 3.3011e23, "radius_m": 2439.7e3, "day_hours": 1407.5, "year_days": 87.97},
    "Earth":   {"g_ratio": 1.00, "mass": 5.972e24,  "radius_m": 6371.0e3, "day_hours": 24.0,   "year_days": 365.25},
    "Jupiter": {"g_ratio": 2.34, "mass": 1.898e27,  "radius_m": 69911e3,  "day_hours": 9.9,    "year_days": 4332.59},
}

def list_planets() -> Tuple[str, ...]:
    """Return supported planet names in a stable order."""
    # TODO (optional): sort alphabetically if you add more planets later.
    return tuple(PLANETS.keys())

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Return BMI on Earth (kg/m^2).
    TODO:
      - Validate inputs: both must be > 0, else raise ValueError.
      - Compute BMI = weight_kg / (height_m ** 2).
    """
    raise NotImplementedError

def weight_on_planet(weight_kg: float, planet: str) -> float:
    """
    Return effective weight on a given planet using its gravity ratio.
    TODO:
      - Validate weight_kg > 0, else raise ValueError.
      - Look up planet (use planet.capitalize()).
      - If planet not found, raise ValueError("Unknown planet: <name>").
      - Return weight_kg * g_ratio.
    """
    raise NotImplementedError

def escape_velocity_ms(planet: str) -> float:
    """
    Return escape velocity for a planet in m/s using sqrt(2 * G * M / R).
    TODO:
      - Look up planet; if missing raise ValueError as above.
      - Use M = mass (kg), R = radius_m (meters).
      - Return sqrt(2 * G * M / R).
    """
    raise NotImplementedError

def planet_facts(planet: str) -> Tuple[float, float]:
    """
    Return (day_hours, year_days) for a planet.
    TODO:
      - Look up planet; if missing raise ValueError as above.
      - Return (float(day_hours), float(year_days)).
    """
    raise NotImplementedError


def _prompt_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).strip())
        except ValueError:
            print("Invalid number, try again.")


def _prompt_planet() -> str:
    print("Planets:", ", ".join(list_planets()))
    return input("Choose a planet: ").strip().capitalize()


def main() -> None:
    print("=== Space Explorer Toolkit (Starter) ===")
    print("This is starter code. Implement the TODOs to make tests pass.")
    print("Menu:")
    print("  1) bmi")
    print("  2) weight")
    print("  3) escape")
    print("  4) facts")
    print("  q) quit")
    choice = input("> ").strip().lower()

    try:
        if choice in ("1", "bmi"):
            weight = _prompt_float("Enter your weight in kg: ")
            height = _prompt_float("Enter your height in meters: ")
            bmi = calculate_bmi(weight, height)
            print(f"Your Earth BMI is {bmi:.2f}")

        elif choice in ("2", "weight"):
            weight = _prompt_float("Enter your Earth weight in kg: ")
            planet = _prompt_planet()
            w = weight_on_planet(weight, planet)
            print(f"On {planet}, your effective weight is {w:.2f} kg")

        elif choice in ("3", "escape"):
            planet = _prompt_planet()
            ev = escape_velocity_ms(planet)
            print(f"Escape velocity on {planet}: {ev:.0f} m/s ({ev/1000:.2f} km/s)")

        elif choice in ("4", "facts"):
            planet = _prompt_planet()
            day_h, year_d = planet_facts(planet)
            print(f"{planet} day length: {day_h} hours")
            print(f"{planet} year length: {year_d} Earth days")

        elif choice == "q":
            print("Bye!")
        else:
            print("Unknown choice.")
    except Exception as e:
        # Keep beginner-friendly behavior while TODOs are incomplete
        print(e)

if __name__ == "__main__":
    main()
