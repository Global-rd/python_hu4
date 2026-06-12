
class Car:
    """Egy autót reprezentáló osztály."""

    FUEL_PER_KM = 0.1   # 0.1% üzemanyag fogy kilométerenként
    MAX_FUEL = 100      # Maximális üzemanyag-szint (%)

    def __init__(self, brand: str, model: str, year: int,
                 mileage: float = 0, fuel_level: float = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def drive(self, km: float) -> float:
        """Adott km-t vezet az autó. Csak annyit megy, amennyire elég az üzemanyag."""
        if km <= 0:
            print(f"  ⚠️  A megadott km érték ({km}) nem érvényes.")
            return 0

        # Mennyi km-re elég a jelenlegi üzemanyag?
        max_km = self.fuel_level / self.FUEL_PER_KM

        if km > max_km:
            print(f"  ⚠️  Nincs elég üzemanyag {km} km-hez. "
                  f"Csak {max_km:.1f} km-t tudok menni.")
            km = max_km

        self.mileage += km
        self.fuel_level -= km * self.FUEL_PER_KM

        # Kerekítési hibák miatti negatív érték elkerülése
        if self.fuel_level < 0:
            self.fuel_level = 0

        print(f"  🚗 {self.brand} {self.model}: {km:.1f} km megtéve. "
              f"Üzemanyag: {self.fuel_level:.1f}%")
        return km

    def refuel(self, amount: float) -> float:
        """Feltölti az üzemanyag-szintet. A 100%-os limit fölé nem megy."""
        if amount <= 0:
            print(f"  ⚠️  A tankolási mennyiség ({amount}) nem érvényes.")
            return 0

        free_capacity = self.MAX_FUEL - self.fuel_level
        actual = min(amount, free_capacity)
        self.fuel_level += actual

        if actual < amount:
            print(f"  ⛽ {self.brand} {self.model}: csak {actual:.1f}% fért bele "
                  f"(a tank megtelt). Üzemanyag: {self.fuel_level:.1f}%")
        else:
            print(f"  ⛽ {self.brand} {self.model}: {actual:.1f}% tankolva. "
                  f"Üzemanyag: {self.fuel_level:.1f}%")
        return actual

    def __str__(self):
        return (f"{self.brand} {self.model} ({self.year}) – "
                f"km: {self.mileage:.1f}, üzemanyag: {self.fuel_level:.1f}%")


class Fleet:
    """Egy autóflottát kezelő osztály."""

    def __init__(self):
        self.cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        """Hozzáad egy autót a flottához."""
        if not isinstance(car, Car):
            print("  ⚠️  Csak Car objektum adható hozzá.")
            return
        self.cars.append(car)
        print(f"  ➕ Hozzáadva: {car.brand} {car.model}")

    def remove_car(self, car: Car) -> None:
        """Eltávolít egy autót a flottából."""
        if car in self.cars:
            self.cars.remove(car)
            print(f"  ➖ Eltávolítva: {car.brand} {car.model}")
        else:
            print("  ⚠️  Az autó nem található a flottában.")

    def total_mileage(self) -> float:
        """Visszaadja a flotta összes autójának összesített kilométerét."""
        return sum(car.mileage for car in self.cars)

    def show_status(self) -> None:
        """Kiírja a flotta összes autójának állapotát és az összes km-t."""
        print("\n📋 Flotta állapota:")
        if not self.cars:
            print("  (üres flotta)")
            return
        for i, car in enumerate(self.cars, 1):
            print(f"  {i}. {car}")
        print(f"  ── Összes megtett km: {self.total_mileage():.1f}")


# ─── Demó / Tesztelés ──────────────────────────────────────────────
if __name__ == "__main__":
    # Autók létrehozása
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Volkswagen", "Golf", 2019)
    car3 = Car("Tesla", "Model 3", 2022)

    # Flotta összeállítása
    print("=== Flotta összeállítása ===")
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    fleet.show_status()

    # Vezetés
    print("\n=== Vezetés ===")
    car1.drive(250)
    car2.drive(500)
    car3.drive(1500)   # Túl sok – maximum 1000 km megy ki 100% üzemanyagból

    # Tankolás
    print("\n=== Tankolás ===")
    car1.refuel(30)
    car2.refuel(80)    # Túl sok – a tank megtelik
    car3.refuel(50)

    fleet.show_status()

    # Autó eltávolítása
    print("\n=== Autó eltávolítása ===")
    fleet.remove_car(car2)

    fleet.show_status()