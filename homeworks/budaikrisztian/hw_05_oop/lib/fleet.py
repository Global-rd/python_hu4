"""
Fleet model for the car fleet manager application.
"""

from lib.car import Car


class Fleet:
    """Manage a list of cars."""

    def __init__(self) -> None:
        """Initialize an empty fleet."""
        self.cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        """Add a car to the fleet."""
        self.cars.append(car)

    def remove_car(self, car: Car) -> None:
        """Remove a car from the fleet if it is present."""
        if car in self.cars:
            self.cars.remove(car)

    def get_total_mileage(self) -> float:
        """Return the total mileage of all cars in the fleet."""
        return sum(car.mileage for car in self.cars)

    def display_cars(self) -> None:
        """Print the current state of every car in the fleet."""
        if len(self.cars) == 0:
            print("The fleet is empty.")
            return

        print("Cars in the fleet:")

        for car_number, car in enumerate(self.cars, start=1):
            print(f"{car_number}. {car.get_status()}")

    def display_summary(self) -> None:
        """Print fleet-level summary data."""
        print("\nFleet summary:")
        print(f"Number of cars: {len(self.cars)}")
        print(f"Total mileage: {self.get_total_mileage():.1f} km")
