# car_fleet_mgr.py
# 5. hazi feladat - OOP gyakorlas: Car es Fleet osztaly

# ============================================================
# CAR osztaly - egy autot reprezental
# ============================================================

class Car:
    def __init__(self, brand, model, year):
        # Az init beallitja a parameterkent kapott attributumokat
        self.brand = brand
        self.model = model
        self.year = year
        # A mileage es fuel_level induloertekeket kap
        # ezekre nem kell parameter, mindig ugyanaz minden uj autora
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, km):
        # Kiszamoljuk mennyi benzint igenyel az ut
        # 0.1% benzin / km
        fuel_needed = km * 0.1

        # Ellenorzes: van eleg benzin?
        if fuel_needed > self.fuel_level:
            # Nincs eleg - csak annyit megyunk amennyi a benzinbol kijon
            possible_km = self.fuel_level / 0.1
            self.mileage += possible_km
            self.fuel_level = 0
            print(f"{self.brand} {self.model}: Nincs eleg benzin! Csak {possible_km} km-t tudtunk menni.")
        else:
            # Van eleg - normal vezetes
            self.mileage += km
            self.fuel_level -= fuel_needed
            print(f"{self.brand} {self.model}: {km} km megtetve. Benzin: {self.fuel_level:.1f}%")

    def refuel(self, amount):
        # Tankolas - figyelni kell hogy a fuel_level ne menjen 100% fole
        if self.fuel_level + amount > 100:
            # Tul sok lenne - csak addig toltjuk amig 100% lesz
            added = 100 - self.fuel_level
            self.fuel_level = 100
            print(f"{self.brand} {self.model}: Tankolva {added}%-kal (tank tele). Benzin: 100%")
        else:
            self.fuel_level += amount
            print(f"{self.brand} {self.model}: Tankolva {amount}%-kal. Benzin: {self.fuel_level}%")

    def show_status(self):
        # Egy egyszeru metodus az auto allapotanak kiirasara
        print(f"{self.brand} {self.model} ({self.year}) - Mileage: {self.mileage} km, Benzin: {self.fuel_level:.1f}%")


# ============================================================
# FLEET osztaly - Car objektumokat kezel
# Ez a COMPOSITION: a Fleet TARTALMAZ Car objektumokat
# (a tanar peldajaban: "az autonak vannak kerekei" - has-a kapcsolat)
# ============================================================

class Fleet:
    def __init__(self):
        # A flotta egy ures listaval indul, ide kerulnek a Car objektumok
        self.cars = []

    def add_car(self, car):
        # Hozzaadunk egy Car objektumot a listahoz
        self.cars.append(car)
        print(f"Flottahoz adva: {car.brand} {car.model}")

    def remove_car(self, car):
        # Eltavolitunk egy Car objektumot a listabol
        if car in self.cars:
            self.cars.remove(car)
            print(f"Flottabol eltavolitva: {car.brand} {car.model}")
        else:
            print(f"Ez az auto nincs a flottaban: {car.brand} {car.model}")

    def total_mileage(self):
        # Vegigmegyunk a listan es osszeadjuk az osszes auto mileage-et
        total = 0
        for car in self.cars:
            total += car.mileage
        return total

    def show_fleet(self):
        # Kiirja a flotta osszes autojanak allapotat es a teljes km-t
        print("\n===== FLOTTA ALLAPOTA =====")
        if not self.cars:
            print("A flotta ures.")
            return
        for car in self.cars:
            car.show_status()
        print(f"Flotta osszes km: {self.total_mileage()} km")
        print("===========================\n")


# ============================================================
# FOPROGRAM - itt teszteljuk a kodot
# ============================================================

# Letrehozunk nehany Car objektumot
print("--- Autok letrehozasa ---")
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Focus", 2021)

# Letrehozzuk a flottat es hozzaadjuk az autokat
print("\n--- Flotta osszeallitasa ---")
my_fleet = Fleet()
my_fleet.add_car(car1)
my_fleet.add_car(car2)
my_fleet.add_car(car3)

# Kezdeti allapot
my_fleet.show_fleet()

# Nehany vezetes
print("--- Vezetes ---")
car1.drive(200)
car2.drive(500)
car3.drive(150)

# Tankolas
print("\n--- Tankolas ---")
car1.refuel(20)
car2.refuel(80)

# Probaljuk meg tul sokat menni
print("\n--- Hosszu ut (kevesebb a benzin) ---")
car3.drive(2000)

# Auto eltavolitasa
print("\n--- Auto eltavolitasa ---")
my_fleet.remove_car(car2)

# Vegso allapot
my_fleet.show_fleet()
