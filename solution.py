def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Return BMI on Earth (kg/m^2).
    - Validate inputs: both must be > 0, else raise ValueError.
    - Compute BMI = weight_kg / (height_m ** 2).
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive.")
    return weight_kg / (height_m ** 2)


def weight_on_planet(weight_kg: float, planet: str) -> float:
    """
    Return effective weight on a given planet using its gravity ratio.
    - Validate weight_kg > 0, else raise ValueError.
    - Look up planet via .capitalize().
    - If planet not found, raise ValueError("Unknown planet: <name>").
    - Return weight_kg * g_ratio.
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be positive.")
    key = planet.capitalize()
    info = PLANETS.get(key)
    if info is None:
        raise ValueError(f"Unknown planet: {planet}")
    return weight_kg * info["g_ratio"]


def escape_velocity_ms(planet: str) -> float:
    """
    Return escape velocity for a planet in m/s using sqrt(2 * G * M / R).
    - Look up planet; if missing raise ValueError as above.
    - Use M = mass (kg), R = radius_m (meters).
    """
    key = planet.capitalize()
    info = PLANETS.get(key)
    if info is None:
        raise ValueError(f"Unknown planet: {planet}")
    M = info["mass"]
    R = info["radius_m"]
    return sqrt(2 * G * M / R)


def planet_facts(planet: str) -> Tuple[float, float]:
    """
    Return (day_hours, year_days) for a planet.
    - Look up planet; if missing raise ValueError as above.
    - Return (float(day_hours), float(year_days)).
    """
    key = planet.capitalize()
    info = PLANETS.get(key)
    if info is None:
        raise ValueError(f"Unknown planet: {planet}")
    return float(info["day_hours"]), float(info["year_days"])