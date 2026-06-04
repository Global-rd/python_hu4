class Car:

    fuel_cons = 0.1

    def __init__(
        self,
        brand: str,
        modell: str,
        year: int,
        mileage: float=0,
        fuel_level: float=100):

        self.brand = brand
        self.modell = modell
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, distance: float):
        req_fuel = distance * self.fuel_cons
        
        if self.fuel_level >= req_fuel:
            self.mileage += distance
            self.fuel_level -= req_fuel
            print(f"Travel executed, {distance} km with {self.brand}.")
        else:
            distance_en = self.fuel_level / 0.1           #Distance enabled
            print(f"Not enough fuel! You can only drive {distance_en} km with {self.brand}.")
            self.mileage += distance_en
            self.fuel_level = 0


    def refuel(self, fuel):
        fuel_missing = 100 - self.fuel_level

        if fuel <= fuel_missing:
            self.fuel_level += fuel
            print(f"Refuel completed, {self.brand} tank level is at: {self.fuel_level} %")
        else:
            print(f"Too much fuel for {self.brand} ! Tank only missing: ", fuel_missing,"%")

    def __str__(self):
        return f"{self.brand} {self.modell} ({self.year}) - Km: {self.mileage:.1f}, Üzemanyag: {self.fuel_level:.1f}%"

class Fleet:

    def __init__(self):
        self.autos = []

    def add_car(self, auto: Car):
        self.autos.append(auto)
        print(f"{auto.brand} {auto.modell} {auto.year} Added to the fleet")

    def remove_car(self, auto: Car):
        if auto in self.autos:
            self.autos.remove(auto)
            print(f"{auto.brand} {auto.modell} {auto.year} Removed from the fleet")
        else:
            print("Invalid car")

    def total_mile(self):             #Total distance
        sum_mile = sum(auto.mileage for auto in self.autos)

        print(f"Total mileage for fleet: {sum_mile}")

    def display_all_stuff(self):
        print(f"------TOTAL FLEET DATA------")
        for auto in self.autos:
            print(auto)
#       print("Total Fleet mileage {sum_mile}")
        print(f"Total Fleet mileage {sum(auto.mileage for auto in self.autos)}")

"""
Datas
"""
if __name__ == "__main__":

    auto1 = Car("Suzuki", "Scross", 2018)
    auto2 = Car("Toyota", "Highlander", 2022)
    auto3 = Car("Volkswagen", "Sharan", 2000)

    auto1.drive(350)    #Successful drive
    auto1.drive(1500)   #Not enough fuel drive

    print(f"=============================================")

    auto2.drive(900)    #Successful drive
    auto2.refuel(10)    #Successful refuel
    auto2.refuel(90)    #Too much refuel

    current_fleet = Fleet()
    current_fleet.add_car(auto1)
    current_fleet.add_car(auto2)
    current_fleet.add_car(auto3)

    print(f"=============================================")
    current_fleet.display_all_stuff()

    print(f"=============================================")

    current_fleet.remove_car(auto3)

