class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0

    def drive(self, km: float) -> float:
        max_km = self.fuel_level / 0.1
        driven = min(km, max_km)
        self.mileage += driven
        self.fuel_level -= driven * 0.1
        return driven

    def refuel(self, amount: float):
        self.fuel_level = min(100.0, self.fuel_level + amount)

    def __str__(self):
        return (
            f"{self.year} {self.brand} {self.model} | "
            f"mileage: {self.mileage:.1f} km | "
            f"fuel: {self.fuel_level:.1f}%"
        )


class Fleet:
    def __init__(self):
        self.cars: list[Car] = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car: Car):
        self.cars.remove(car)

    def total_mileage(self) -> float:
        return sum(car.mileage for car in self.cars)

    def status(self):
        for car in self.cars:
            print(car)
        print(f"Fleet total mileage: {self.total_mileage():.1f} km")


if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("BMW", "3 Series", 2022)
    car3 = Car("Tesla", "Model 3", 2023)

    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    print("=== Initial state ===")
    fleet.status()

    car1.drive(500)
    car2.drive(300)
    car3.drive(1200)  # only 1000 km possible with 100% fuel

    print("\n=== After driving ===")
    fleet.status()

    car1.refuel(30)
    car3.refuel(50)

    print("\n=== After refueling ===")
    fleet.status()

    car1.drive(200)

    print("\n=== After second drive ===")
    fleet.status()

    fleet.remove_car(car2)
    print("\n=== After removing BMW ===")
    fleet.status()
