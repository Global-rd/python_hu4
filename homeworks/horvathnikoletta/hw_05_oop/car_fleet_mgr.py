class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive (self, distance):
        fuel_need = distance*0.1
        if self.fuel_level >= fuel_need:
            self.mileage += distance
            self.fuel_level -= fuel_need
            print(f"Megtettél {distance} km-t a (z) {self.brand}{self.model} típusú autóval.")
        else:
            max_distance = self.fuel_level/0.1
            self.mileage += max_distance
            print(f"Nincs elég üzemanyag a megadott km-re, maximum {max_distance} km-t tudsz megtenni!")

    def refuel(self, amount):
        if amount < 0:
            print("Hibás érték, kérlek adj meg pozitív számot!")
            return
        if self.fuel_level + amount > 100:
            print(f"A tank megtelt! A tankolás csak 100%-ig lehetséges!")
            self.fuel_level = 100
        else:
            self.fuel_level += amount
            print(f"Tankolás sikeres! Jelenlegi szint: {self.fuel_level}%")

    def show_details(self):
        print(f"{self.brand} {self.model} ({self.year}) KM: {self.mileage} Üzemanyag: {self.fuel_level}%")

class Fleet:
    def __init__(self):
        self.cars = []
    def add_car(self, car):
        self.cars.append(car)
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
    def total_mileage(self):
        osszes = 0
        for car in self.cars:
            osszes += car.mileage
        return osszes

    def show_status(self):
        print("\n--- Flotta állapota ---")
        for car in self.cars:
            car.show_details()
        print(f"Összesen megtett út: {self.total_mileage()} km")

if __name__== "__main__":
    car1 = Car("Mercedes", "CLA", "2015")
    car2 = Car("Skoda", "Superb", "2013")
    car3 = Car("Nissan", "X-trail", "2006")

flotta = Fleet()
flotta.add_car(car1)
flotta.add_car(car2)
flotta.add_car(car3)
car1.drive(100)
car2.drive(300)
car3.drive(900)
flotta.show_status()
car2.refuel(10)