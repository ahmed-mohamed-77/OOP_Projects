class Vehicle:
    def __init__(self, make, model ,year) -> None:
        self.make = make
        self.model = model
        self.year = year
    

class ElectricCar:
    def __init__(self, battery_capacity) -> None:
        self.battery_capacity = battery_capacity
    
    def charge(self):
        return self.battery_capacity
    
    def electric_range(self):
        return self.battery_capacity * 5
    
class GasCar:
    def __init__(self, fuel_capacity: int | float) -> None:
        self.fuel_capacity = fuel_capacity
    
    def refuel(self) -> int | float:
        return self.fuel_capacity
    
    def fuel_range(self) -> int | float:
        return self.fuel_capacity * 20

class HybridCar(Vehicle, ElectricCar, GasCar):
    def __init__(self, make, model, year, battery_capacity, fuel_capacity) -> None:
        Vehicle.__init__(self,make, model, year)
        ElectricCar.__init__(self, battery_capacity)
        GasCar.__init__(self, fuel_capacity)
    
    def __str__(self) -> str:
        return (f"HybridCar:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\n\
Battery Capacity: {self.battery_capacity} kwh\nFuel Capacity: {self.fuel_capacity} Gallon")

car = HybridCar('BMW', 'M5', 2025, 5, 45)
battery_capacity = car.charge()
print(car)
print(battery_capacity)
print(f"{car.fuel_range()} Mile")
