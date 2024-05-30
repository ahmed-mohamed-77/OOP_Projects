class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        # Initialize the Vehicle class with make, model, and year
        self.make = make
        self.model = model
        self.year = year


class ElectricVehicle:
    def __init__(self, battery_capacity: int, ability_to_charge: int) -> None:
        # Set the battery capacity
        self.battery_capacity = battery_capacity
        # Use the setter to validate and set the ability to charge
        self._ability_to_charge = ability_to_charge

    @property
    def ability_to_charge(self) -> int:
        # Getter for the ability to charge
        return self._ability_to_charge

    @ability_to_charge.setter
    def ability_to_charge(self, ability_to_charge: int) -> None:
        # Setter for the ability to charge with validation
        if 40 <= ability_to_charge <= 100:
            self._ability_to_charge = ability_to_charge
        # Optionally, you might want to raise an error for invalid values
        else:
            raise ValueError("ability_to_charge must be between 40 and 100")

    def get_range(self, distance_travel: int):
        # Fuel consumption = Fuel used / Distance traveled
        return self.battery_capacity / distance_travel


class GasolineVehicle:
    def __init__(self, fuel_capacity: int, ability_to_refuel: str) -> None:
        # Set the fuel capacity
        self.fuel_capacity = fuel_capacity
        # Use the setter to validate and set the ability to refuel
        self._ability_to_refuel = ability_to_refuel

    @property
    def ability_to_refuel(self) -> str:
        # Getter for the ability to refuel
        return self._ability_to_refuel

    @ability_to_refuel.setter
    def ability_to_refuel(self, ability_to_refuel: str) -> None:
        # Define the list of valid petrol types
        petrol_types = ["diesel", "gasoline", "premium gas", "octane", "ethanol"]
        # Validate the ability to refuel against the list of petrol types
        if ability_to_refuel.lower() in [fuel.lower() for fuel in petrol_types]:
            self._ability_to_refuel = ability_to_refuel.lower()
        # Optionally, you might want to raise an error for invalid values
        else:
            raise ValueError(
                "ability_to_refuel must be one of: diesel, gasoline, premium gas, octane, ethanol\n\
you cannot refuel the car"
            )

    def get_range(self):
        # Fuel consumption = Fuel used / Distance traveled
        return self.fuel_capacity * 20


class HybridCar(Vehicle, ElectricVehicle, GasolineVehicle):
    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        battery_capacity: int,
        ability_to_charge: int,
        fuel_capacity: int,
        ability_to_refuel: str,
    ) -> None:
        Vehicle.__init__(self, make, model, year)
        ElectricVehicle.__init__(self, battery_capacity, ability_to_charge)
        GasolineVehicle.__init__(self, fuel_capacity, ability_to_refuel)

    def __str__(self) -> str:
        return f"HybridCar:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\n\
Battery Capacity: {self.battery_capacity}\nAbility to charge: {self.ability_to_charge}\n\
Fuel Capacity: {self.fuel_capacity}\nAbility to refuel: {self.ability_to_refuel}"


# # Example usage:
hybrid = HybridCar("Toyota", "Prius", 2023, 50, 60, 60, "gasoline")
print(hybrid)
print(HybridCar.__mro__)

