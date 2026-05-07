class Car:
    def __init__(self, brand, model, year): # kezelőfelület 
        # akkor fut le, ha létrehozunk egy autót
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0 # induló érték: a km-óra automatikusan felveszi a 0 értéket induláskor
        self.fuel_level = 100  # induló érték 100%: a tank automatikusan tele van induláskor

    def drive(self, km):
        fuel_needed = km * 0.1  # 0.1% üzemanyag / km

        if fuel_needed > self.fuel_level:
            # csak annyi utat lehet megtenni, amennyi üzemanyag van
            max_km = self.fuel_level / 0.1
            print(
            f"⚠️  {self.brand} {self.model}: The fuel was enough only for {max_km:.0f} km. "
            f"Instead of entered {km} km, only 🚗 {max_km:.0f} km were recorded in the logbook.\n"
            )
            self.mileage += max_km
            self.fuel_level = 0
        else:
            self.mileage += km
            self.fuel_level -= fuel_needed
            print(f"🚗 {self.brand} {self.model}: {km:.0f} km were recorded in the logbook.\n")

    def refuel(self, amount):
        max_addable = 100 - self.fuel_level
        if amount > max_addable:
            print(
            f"⚠️  {self.brand} {self.model}: Only {max_addable:.0f}% of fuel can be filled into the tank. "
            f"The additional {amount - max_addable:.0f}% cannot be counted."
            )                 
            self.fuel_level = 100
            print(
            f"⛽ Paid refueling: +{max_addable:.0f}%."
            f" Current fuel level: {self.fuel_level}%.\n"
            )
        else:
            self.fuel_level += amount
            print(
            f"⛽ {self.brand} {self.model}: Paid refueling: +{amount}%."
            f" Current fuel level: {self.fuel_level:.0f}%.\n"
            )

    def __str__(self): # Ez is DUNDER metódus (“double underscore”), string formájában történik a kiírás
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage:.0f} km traveled, {self.fuel_level:.0f}% fuel level.\n"


class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car): # autók hozzáadása a flottához
        self.cars.append(car)

    def remove_car(self, car): # autók törlése a flottából
        if car in self.cars:
            self.cars.remove(car)

    def total_mileage(self): # A flotta által megtett összes km
        return sum(car.mileage for car in self.cars)

    def show_fleet(self): # a flotta minden tagja állapotának listázása.
        for car in self.cars:
            print(car)

# Autók létrehozása
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("BMW", "X5", 2022)
car3 = Car("Audi", "A4", 2019)
car4 = Car("Volkswagen", "Passat", 2015)
car5 = Car("Renault", "Scenic", 2010)
car6 = Car("Opel", "Insignia", 2017)          

# Flotta létrehozása
fleet = Fleet()

# Autók hozzáadása a flottához
fleet.add_car(car1)
fleet.add_car(car2)
fleet.add_car(car3)
fleet.add_car(car4)
fleet.add_car(car5)
fleet.add_car(car6)

# Művelet - vezetett km
car1.drive(150)
car2.drive(80)
car3.drive(300)
car4.drive(570)
car5.drive(670)
car6.drive(1070)

# Művelet - tankolás (%)
car1.refuel(20)
car3.refuel(50)
car4.refuel(57)
car5.refuel(60)

# a flotta tagjainak állapota egyenként:
print("🚗 Current status of the fleet:")
fleet.show_fleet()

# A flotta által megtett összes km:
print(f"📊 Total kilometers traveled by the fleet: {fleet.total_mileage():.0f} km.\n")

fleet.remove_car(car1)

# Állapotok autónként - újbóli kiírás, miután egy autó törölve lett a flottából:
print("🚗 Current status of the fleet:")
fleet.show_fleet()

#  A flotta által megtett összes km, miután egy autó törölva lett a flottából:
print(f"📊 Total kilometers traveled by the fleet: {fleet.total_mileage():.0f} km.")