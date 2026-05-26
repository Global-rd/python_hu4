class Car:
    def __init__(self, brand : str, model : str, year : int, mileage : int = 0, fuel_level : float = 100.00):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, distance):
        fuel_consumed = distance * 0.01
        if fuel_consumed > self.fuel_level:
            print(f"The max. possible distance is {self.fuel_level / 0.01:.2f} miles.")
            self.mileage += self.fuel_level / 0.01
            self.fuel_level = 0.00
            return
        self.mileage += distance
        self.fuel_level -= fuel_consumed

    def refuel(self, amount):
        if amount < 0:
            print("Cannot refuel a negative amount.")
            return
        self.fuel_level = min(100.00, self.fuel_level + amount)

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)
    
    def list_cars(self):
        for car in self.cars:
            print(f"{car.brand} {car.model} ({car.year}) - Mileage: {car.mileage} miles, Fuel level: {car.fuel_level:.2f}%")

    def remove_car(self, car: Car):
        self.cars.remove(car)

    def total_mileage(self):
        total_mileage = sum(car.mileage for car in self.cars)
        print(f"Total mileage of the fleet: {total_mileage} miles.")

fleet = Fleet()    

fleet.add_car(Car(brand="Toyota", model="Corolla", year=2020))
fleet.add_car(Car(brand="Honda", model="Civic", year=2019))
fleet.add_car(Car(brand="Skoda", model="Octavia", year=2018))
fleet.cars[0].drive(15000)
fleet.cars[1].drive(200)
fleet.cars[2].drive(250)
fleet.list_cars()
print("-------------------------- ")
fleet.cars[0].refuel(20)
fleet.list_cars()
fleet.remove_car(fleet.cars[1])
print("-------------------------- ")
fleet.list_cars()
fleet.total_mileage()

