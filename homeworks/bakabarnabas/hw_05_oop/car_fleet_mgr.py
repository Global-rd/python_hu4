class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100.0

    def drive(self, km):
        # Max km amire elég az üzemanyag (0.1% / km)
        max_km = self.fuel_level / 0.1
        actual_km = min(km, max_km)

        if actual_km <= 0:
            print(f"[{self.brand} {self.model}] Nincs elég üzemanyag a vezetéshez!")
            return

        self.mileage += actual_km
        self.fuel_level -= actual_km * 0.1
        self.fuel_level = round(self.fuel_level, 2)

        if actual_km < km:
            print(f"[{self.brand} {self.model}] Csak {actual_km:.1f} km-t sikerült megtenni, "
                  f"mert elfogyott az üzemanyag.")
        else:
            print(f"[{self.brand} {self.model}] Megtett: {actual_km:.1f} km | "
                  f"Összes km: {self.mileage:.1f} | Üzemanyag: {self.fuel_level:.1f}%")

    def refuel(self, amount):
        if amount <= 0:
            print(f"[{self.brand} {self.model}] Érvénytelen tankolási mennyiség.")
            return

        space = 100 - self.fuel_level
        actual_fill = min(amount, space)
        self.fuel_level += actual_fill
        self.fuel_level = round(self.fuel_level, 2)

        print(f"[{self.brand} {self.model}] Tankolt: {actual_fill:.1f}% | "
              f"Üzemanyag szint: {self.fuel_level:.1f}%")

    def status(self):
        print(f"  {self.brand} {self.model} ({self.year}) | "
              f"Km: {self.mileage:.1f} | Üzemanyag: {self.fuel_level:.1f}%")


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Hozzáadva a flottához: {car.brand} {car.model} ({car.year})")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Eltávolítva a flottából: {car.brand} {car.model} ({car.year})")
        else:
            print(f"Az autó nem található a flottában: {car.brand} {car.model}")

    def total_mileage(self):
        total = sum(car.mileage for car in self.cars)
        return total

    def show_status(self):
        print("\n--- Flotta állapota ---")
        if not self.cars:
            print("  (Nincs autó a flottában)")
        for car in self.cars:
            car.status()
        print(f"  Összes megtett km (flotta): {self.total_mileage():.1f} km")
        print("-----------------------\n")


# --- Demo ---

if __name__ == "__main__":
    # Autók létrehozása
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("BMW", "530d", 2022)
    car3 = Car("Ford", "Transit", 2019)

    # Flotta létrehozása és autók hozzáadása
    fleet = Fleet()
    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

    print()

    # Műveletek
    car1.drive(300)
    car2.drive(150)
    car3.drive(800)   # Több mint amennyire elég az üzemanyag

    print()

    car1.refuel(50)
    car3.refuel(200)  # Túltöltés próba

    print()

    car1.drive(200)
    car2.refuel(30)
    car2.drive(100)
    
    # Flotta állapotának megjelenítése
    fleet.show_status()

    # Egy autó eltávolítása
    fleet.remove_car(car3)
    fleet.show_status()