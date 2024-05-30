import json
"""Title: Country Information System"""

class Country:
    def __init__(self, country_name: str, capital: str, population: int) -> None:
        self.country_name = country_name
        self.capital = capital
        self.population = population
    
    def get_info(self):
        country_dict = {
            "country name": self.country_name,
            "capital": self.capital,
            "population": self.population
        }
        return country_dict

class DevelopedCountry(Country):
    def __init__(self, country_name: str, capital: str, population: int, gdp: int) -> None:
        super().__init__(country_name, capital, population)
        self.gdp = gdp #Gross Domestic Product
    
    def info(self):
        gdp_override = super().get_info()
        gdp_override["Gross Domestic Product (GDP)"] = self.gdp
        return gdp_override

class DevelopingCountry(Country):
    def __init__(self, country_name: str, capital: str, population: int, hdi) -> None:
        super().__init__(country_name, capital, population)
        self.hdi = hdi #The Human Development Index (HDI)
    
    def info(self):
        hdi = super().get_info()
        hdi["human development index (HDI)"] = self.hdi
        return hdi

class World:
    def __init__(self) -> None:
        self.countries = []
    
    def add_country(self, country: object):
        self.countries.append(country)
        
    def remove_country(self, country: object):
        self.countries.remove(country)
        
    def get_country_info(self, country_name):
        for country in self.countries:
            if country.country_name == country_name:
                return country.info()
        return None
    
    def find_country(self, country_name: str):
        country_name = country_name.capitalize()
        for country in self.countries:
            if country.country_name == country_name:
                return country
        return None
    

egypt_gdp = DevelopedCountry("Egypt", "Cairo", 120_000_000, 476_748_000_000)
egypt_hdi = DevelopingCountry("egypt", "Cairo", 120_000_000, 0.73)


# Create instances of countries
usa = DevelopedCountry("United States", "Washington, D.C.", 331_000_000, 21_439_453_000_000)
germany = DevelopedCountry("Germany", "Berlin", 83_000_000, 3_845_630_000_000)
india = DevelopingCountry("India", "New Delhi", 1_366_000_000, 0.645)
nigeria = DevelopingCountry("Nigeria", "Abuja", 206_000_000, 0.539)

# Create the World instance
world = World()

# Add countries to the world
world.add_country(usa)
world.add_country(germany)
world.add_country(india)
world.add_country(nigeria)
world.add_country(egypt_gdp)
world.add_country(egypt_hdi)

# Retrieve and print information about the countries
print("United States Info:")
print(json.dumps(world.get_country_info("United States"), indent=4))

print("\nGermany Info:")
print(json.dumps(world.get_country_info("Germany"), indent=4))

print("\nIndia Info:")
print(json.dumps(world.get_country_info("India"), indent=4))

print("\nNigeria Info:")
print(json.dumps(world.get_country_info("Egypt"), indent=4))

print("\nEgypt Info:")
print(json.dumps(world.get_country_info("egypt"), indent=4))