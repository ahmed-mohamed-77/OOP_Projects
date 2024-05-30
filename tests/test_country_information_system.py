import pytest
from oo_projects.source.country_information_system import DevelopedCountry, DevelopingCountry, World

# Fixture to create a World object and add some countries
@pytest.fixture
def world_wide():
    world = World()
    countries = [
        DevelopedCountry("Egypt", "Cairo", 120_000_000, 476_748_000_000),
        DevelopingCountry("egypt", "Cairo", 120_000_000, 0.73),
        DevelopedCountry("United States", "Washington, D.C.", 331_000_000, 21_439_453_000_000),
        DevelopedCountry("Germany", "Berlin", 83_000_000, 3_845_630_000_000),
        DevelopingCountry("India", "New Delhi", 1_366_000_000, 0.645),
        DevelopingCountry("Nigeria", "Abuja", 206_000_000, 0.539)
    ]
    
    for country in countries:
        world.add_country(country)
    
    return world

@pytest.mark.parametrize("country_name, expected_info", [
    ("Egypt", {
        "country name": "Egypt",
        "capital": "Cairo",
        "population": 120_000_000,
        "Gross Domestic Product (GDP)": 476_748_000_000
    }),
    ("egypt", {
        "country name": "egypt",
        "capital": "Cairo",
        "population": 120_000_000,
        'human development index (HDI)': 0.73,
    }),
    ("United States", {
        "country name": "United States",
        "capital": "Washington, D.C.",
        "population": 331_000_000,
        "Gross Domestic Product (GDP)": 21_439_453_000_000
    }),
    ("Germany", {
        "country name": "Germany",
        "capital": "Berlin",
        "population": 83_000_000,
        "Gross Domestic Product (GDP)": 3_845_630_000_000
    }),
    ("India", {
        "country name": "India",
        "capital": "New Delhi",
        "population": 1_366_000_000,
        'human development index (HDI)': 0.645,
    }),
    ("Nigeria", {
        "country name": "Nigeria",
        "capital": "Abuja",
        "population": 206_000_000,
        'human development index (HDI)': 0.539,
    })
])
def test_get_country_info(world_wide, country_name, expected_info):
    world = world_wide
    country_info = world.get_country_info(country_name)
    assert country_info == expected_info

def test_add_country(world_wide):
    world = world_wide
    new_country = DevelopedCountry("Japan", "Tokyo", 126_000_000, 5_000_000_000_000)
    world.add_country(new_country)
    country_info = world.get_country_info("Japan")
    expected_info = {
        "country name": "Japan",
        "capital": "Tokyo",
        "population": 126_000_000,
        "Gross Domestic Product (GDP)": 5_000_000_000_000
    }
    assert country_info == expected_info

def test_remove_country(world_wide):
    world = world_wide
    country_to_remove = world.find_country("Germany")
    world.remove_country(country_to_remove)
    country_info = world.get_country_info("Germany")
    assert country_info is None

def test_get_nonexistent_country_info(world_wide):
    world = world_wide
    country_info = world.get_country_info("NonExistentCountry")
    assert country_info is None
