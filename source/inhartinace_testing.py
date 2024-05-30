class Animal:
    def __init__(self, region: str, animal_type: str, color: str, lethal: bool) -> None:
        self.region = region
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal
    
    def animal_bio(self):
        print("Animal Passport!")
        print(f"Found in: {self.region}")
        print(f"Species: {self.animal_type}")
        print(f"Color: {self.color}")
        print(f"Dangerous: {self.lethal}")

class Clinic(Animal):
    def animal_info(self):
        print(f"this is a {self.animal_type} from {self.region}")
    
    def search(self, animals):
        region = input("enter region: ".title()).strip().lower()
        for animal in animals:
            if animal.region == region:
                print(f"species: {animal.animal_type}")

animals = []
amount_animals = int(input("enter amount of animals: ".title()).strip())
for animal in range(amount_animals):
    region = input("Enter Region: ").strip().lower()
    animal_type = input("Enter Animal Type: ").strip().lower()
    color = input("Enter Color: ").strip().lower()
    lethal = input("is it dangerous: ").strip().lower()
    lethal = lethal == 'yes'
    
    animal = Animal(region, animal_type, color, lethal)
    
    animals.append(animal)

clinic = Clinic("asia", "tiger", "orange", True)
clinic.animal_bio()
clinic.animal_info()
clinic.search(animals)