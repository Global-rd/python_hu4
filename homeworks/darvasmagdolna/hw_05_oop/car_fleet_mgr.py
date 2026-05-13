class Car:
    def __init__(self, brand, model, year): #konstruktor: feladat beállítani minden egyes adattagnak (kezdő) értéket
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100 #%-ban értendő

    def drive(self, km):
    
        requried_fuel = km * 0.1
        if requried_fuel > self.fuel_level:
            max_km = self.fuel_level / 0.1
            print(f"{self.brand} {self.model}: There isn't enough fuel, so you could only travel {round(max_km, 1)} km.")

        else: 
            self.mileage += km
            self.fuel_level -= requried_fuel
            print(f"{self.brand} {self.model}: You have successfully covered {km} km.")



    def refuel(self, amount):
        if amount <=0:
            print("The refueling amount cannot be negative. or zero.")
            return
        
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100

        print(f"{self.brand} {self.model}: Fueled up {amount}%.\n"
              f"Current fuel level is {self.fuel_level}%.")

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Car added to fleat: {car.brand} {car.model}")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Car removed from fleet: {car.brand} {car.model}")
        
        else:
            print(f"Car not found in fleet")

    
    def total_mileage(self):
        return sum(car.mileage for car in self.cars)
    
    def show_fleet(self):
        print("\n--- Fleet status---")
        for car in self.cars:
            print(f"{car.brand} {car.model} {car.year}: {car.mileage}km {car.fuel_level}%")
        print(f"Total fleet distance: {self.total_mileage()}km.")

    
car1 = Car("Suzuki", "Swift", 2005)
car2 = Car("Toyota", "Corola", 2007)
car3 = Car("Nissan", "Juke", 2025)

fleet = Fleet()

fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)

car1.drive(100)
car2.drive(50)
car3.drive(700)

car1.refuel(5)
car3.refuel(50)

fleet.show_fleet()



        


