"""
Main car fleet manager application class.
"""

from collections.abc import Iterator
from dataclasses import dataclass

from lib.car import Car
from lib.fleet import Fleet


@dataclass
class DemoCars:
    """Store demo cars with named access and iteration support."""

    toyota: Car
    ford: Car
    tesla: Car

    def __iter__(self) -> Iterator[Car]:
        """Iterate over demo cars."""
        return iter((self.toyota, self.ford, self.tesla))


class CarFleetApp:
    """Run the car fleet manager demo flow."""

    SECTION_SEPARATOR: str = f"\n{'=' * 80}\n"

    def __init__(self) -> None:
        """Initialize the application with an empty fleet."""
        self.fleet = Fleet()

    @staticmethod
    def __create_demo_cars() -> DemoCars:
        """Create demo cars."""

        return DemoCars(
            toyota=Car("Toyota", "Corolla", 2020),
            ford=Car("Ford", "Focus", 2018),
            tesla=Car("Tesla", "Model 3", 2022),
        )

    @staticmethod
    def __run_demo_operations(demo_cars: DemoCars) -> None:
        """Run driving and refueling operations on the demo cars."""
        print("Demo operations:")

        toyota_distance: float = demo_cars.toyota.drive(120)
        print(f"{demo_cars.toyota.get_name()} drove {toyota_distance:.1f} km.")

        ford_distance: float = demo_cars.ford.drive(1_200)
        print(f"{demo_cars.ford.get_name()} drove {ford_distance:.1f} km.")

        demo_cars.ford.refuel(40)
        print(f"{demo_cars.ford.get_name()} was refueled by 40%.")

        ford_second_distance: float = demo_cars.ford.drive(150)
        print(
            f"{demo_cars.ford.get_name()} drove {ford_second_distance:.1f} km."
        )

        tesla_distance: float = demo_cars.tesla.drive(80)
        print(f"{demo_cars.tesla.get_name()} drove {tesla_distance:.1f} km.")

    def run(self) -> None:
        """Run the complete car fleet manager demo."""
        print(self.SECTION_SEPARATOR)
        print("Car Fleet Manager")
        print(self.SECTION_SEPARATOR)

        cars: DemoCars = self.__create_demo_cars()

        for car in cars:
            self.fleet.add_car(car)

        self.__run_demo_operations(cars)

        print(self.SECTION_SEPARATOR)
        self.fleet.display_cars()
        self.fleet.display_summary()

        self.fleet.remove_car(cars.tesla)
        print(self.SECTION_SEPARATOR)
        print("After removing the Tesla Model 3:")
        self.fleet.display_cars()
        self.fleet.display_summary()
