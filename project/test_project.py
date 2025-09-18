# === test_project.py ===
# CS50 Project tests with pytest.
# Each test is named test_<functionname> as required.

from math import isclose
import pytest

from project import (
    calculate_bmi,
    weight_on_planet,
    escape_velocity_ms,
    planet_facts,
)

def test_calculate_bmi():
    # valid case
    assert round(calculate_bmi(70, 1.75), 2) == 22.86
    # invalid: zero height
    with pytest.raises(ValueError):
        calculate_bmi(70, 0.0)
    # invalid: negatives
    with pytest.raises(ValueError):
        calculate_bmi(-1.0, 1.70)
    with pytest.raises(ValueError):
        calculate_bmi(70.0, -1.0)

def test_weight_on_planet():
    # valid cases
    assert round(weight_on_planet(100.0, "Mercury"), 2) == 38.00
    assert round(weight_on_planet(50.0, "Jupiter"), 2) == 117.00
    # invalid planet
    with pytest.raises(ValueError):
        weight_on_planet(70.0, "Krypton")
    # invalid weight
    with pytest.raises(ValueError):
        weight_on_planet(-10.0, "Earth")

def test_escape_velocity_ms():
    # valid case (Earth ~11,186 m/s)
    ev = escape_velocity_ms("Earth")
    assert isclose(ev, 11186, rel_tol=0.02, abs_tol=200)
    # invalid planet
    with pytest.raises(ValueError):
        escape_velocity_ms("Nowhere")

def test_planet_facts():
    # valid case
    day_h, year_d = planet_facts("Earth")
    assert isclose(day_h, 24.0, abs_tol=0.01)
    assert isclose(year_d, 365.25, abs_tol=0.01)
    # invalid planet
    with pytest.raises(ValueError):
        planet_facts("Nowhere")