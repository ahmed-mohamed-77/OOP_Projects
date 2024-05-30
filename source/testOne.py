class Vehicle:
  color = "White"
  def __init__(self,model_name,max_speed,mileage):
    self.model_name = model_name
    self.max_speed = max_speed
    self.mileage = mileage

  def __str__(self):
    return f"Color: {Vehicle.color}\nVehicle name: {self.model_name}\nMax speed: {self.max_speed}\nMileage: {self.mileage}"

class Bus(Vehicle):
  capacity = 50

  def __init__(self, model_name, max_speed, mileage):
    super().__init__(model_name, max_speed, mileage)
    self.passengers = []

  @classmethod
  def max_seating_capacity(cls):
    return f"Max seats available: {cls.capacity}"

  @staticmethod
  def seating_capacity(bus_name,capacity):
    return f"the seating capacity of a {bus_name} is {capacity} passengers"

  def add_passenger(self,passenger):
    if len(self.passengers) < self.capacity:
      self.passengers.append(passenger)
      print(f"{passenger} has been added to bus")
    else:
      print("The bus is already full. Cannot add more passengers.")

  def get_passenger_count(self):
    return len(self.passengers)

model_1X = Bus("school volvo",180, 18)
print(model_1X)
print(Bus.add_passenger(1))
print(Bus.seating_capacity("volvo bus",51))


