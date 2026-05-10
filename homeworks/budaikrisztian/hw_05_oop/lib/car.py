"""
Car model for the car fleet manager application.
"""


class Car:
    """Represent a car with mileage and fuel management."""

    FUEL_CONSUMPTION_PER_KM: float = 0.1
    MAX_FUEL_LEVEL: float = 100.0
    MIN_FUEL_LEVEL: float = 0.0

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        mileage: float = 0,
        fuel_level: float = 100,
    ) -> None:
        """Initialize the car with its basic data."""
        if mileage < 0:
            raise ValueError("Mileage cannot be negative.")

        if (
            fuel_level < self.MIN_FUEL_LEVEL
            or fuel_level > self.MAX_FUEL_LEVEL
        ):
            raise ValueError("Fuel level must be between 0 and 100.")

        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, distance: float) -> float:
        """
        Drive the car and return the actually completed distance.

        The car consumes 0.1% fuel for every kilometer, so the available
        fuel level limits how far the car can go.
        """
        if distance <= 0:
            raise ValueError("Distance must be greater than 0.")

        max_distance: float = self.fuel_level / self.FUEL_CONSUMPTION_PER_KM
        driven_distance: float = min(distance, max_distance)
        fuel_used: float = driven_distance * self.FUEL_CONSUMPTION_PER_KM

        self.mileage += driven_distance
        self.fuel_level = max(self.MIN_FUEL_LEVEL, self.fuel_level - fuel_used)

        return driven_distance

    def refuel(self, amount: float) -> None:
        """Increase the fuel level without going above 100%."""
        if amount <= self.MIN_FUEL_LEVEL:
            raise ValueError("Refuel amount must be greater than 0.")

        if self.fuel_level + amount > self.MAX_FUEL_LEVEL:
            raise ValueError(
                "Refuel amount would exceed the maximum fuel level."
            )

        self.fuel_level += amount

    def get_name(self) -> str:
        """Return the car's name as a string."""
        return f"{self.brand} {self.model}"

    def get_status(self) -> str:
        """Return a readable summary of the car state."""
        return (
            f"{self.get_name()} ({self.year}) - "
            f"mileage: {self.mileage:.1f} km, "
            f"fuel level: {self.fuel_level:.1f}%"
        )
