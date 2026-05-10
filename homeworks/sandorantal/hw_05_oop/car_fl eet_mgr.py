class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, distance):
        required_fuel = distance * 0.1
        
        if self.fuel_level >= required_fuel:
            self.mileage += distance
            self.fuel_level -= required_fuel
            print(f"Successfully traveled {distance} km with {self.brand}.")
        else:
            achievable_distance = self.fuel_level / 0.1
            print(f"There is not enough fuel for the entire journey! You have only traveled {achievable_distance:.1f} km with {self.brand}.")
            self.mileage += achievable_distance
            self.fuel_level = 0

    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level > 100:
            self.fuel_level = 100
        print(f"{self.brand} refueled. Current fuel level: {self.fuel_level}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) | Mileage: {self.mileage:.1f} km | Fuel: {self.fuel_level:.1f}%"


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added to the fleet: {car.brand} {car.model}")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Removed from the fleet: {car.brand} {car.model}")
        else:
            print("This car is not in the fleet.")

    def get_total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        return total

    def display_fleet_status(self):
        print("\n--- FLEET STATUS ---")
        for car in self.cars:
            print(car)
        print(f"Total fleet mileage: {self.get_total_mileage():.1f} km")
        print("-----------------------\n")



if __name__ == "__main__":
    auto1 = Car("Toyota", "Corolla", 2022)
    auto2 = Car("Ford", "Focus", 2018)
    auto3 = Car("Tesla", "Model 3", 2023)

    my_fleet = Fleet()
    my_fleet.add_car(auto1)
    my_fleet.add_car(auto2)
    my_fleet.add_car(auto3)

    print("\n--- Performing operations ---")
    auto1.drive(250)    # Normal driving
    auto2.drive(1200)   # Running out of fuel test (can go up to 1000 km)
    auto2.refuel(40)    # Refueling
    auto3.drive(150)    # Driving a new car
    
    my_fleet.display_fleet_status()

    my_fleet.remove_car(auto3)
    my_fleet.display_fleet_status()