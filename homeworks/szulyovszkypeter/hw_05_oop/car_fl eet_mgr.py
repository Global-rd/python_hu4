'''
Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
● Márka (brand)
● Modell (model)
● Gyártási év (year)
● Kilométeróra állása (mileage), induló értéke 0.
● Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).
Az osztály tartalmazza a következő metódusokat:
● Egy konstruktor, amely beállítja a fenti attribútumokat.
● Egy drive() metódus, amely adott számú kilométerrel növeli a kilométeróra állását,
  és csökkenti az üzemanyag-szintet (tételezzük fel, hogy 0.1% üzemanyag fogy megtett kilométerenként). 
  A drive() metódus csak annyit km-et engedjen vezetni, amennyire elegendő üzemanyag van.
● Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott mennyiséggel. Figyelj a limitekre.

Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
● Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
● Tartalmazzon metódusokat Car objektumok hozzáadására és eltávolítására a flottába/flottából.
● Tartalmazzon egy metódust, amely összesíti a flotta összes autójának összes kilométerét.
● Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts végre néhány műveletet (vezetés, tankolás), 
  jelenítsd meg az autók állapotát és a flotta összesítő adatait.
'''

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_level = 100

    def drive(self, kilometers):
        """
        Vezetés: 0.1% üzemanyagot fogyaszt kilométerenként.
        Csak addig mehet, amíg ki nem ürül a tank.
        """
        # Kiszámoljuk, maximum hány km-re elég a nafta (fuel / 0.1)
        #max_distance = self.fuel_level / 0.1
        if kilometers <= 0:
            print("Hiba: A távolságnak nagyobbnak kell lennie, mint 0 km!")
            return
        actual_distance = min(kilometers, self.fuel_level / 0.1)
        fuel_consumed = actual_distance * 0.1
        
        self.mileage += actual_distance
        self.fuel_level -= fuel_consumed
        
        if actual_distance < kilometers:
            print(f"Figyelem: Elfogyott az üzemanyag! Csak {actual_distance:.1f} km-t sikerült megtenni.")
        else:
            print(f" {self.brand} {self.model} Sikeres út:  {actual_distance} km megtéve.")

    def refuel(self, amount):
        """Feltölti az üzemanyagot, maximum 100%-ig."""
        if amount < 0:
            print("Hiba: Negatív mennyiséget nem lehet tankolni.")
            return
            
        self.fuel_level = min(100, self.fuel_level + amount)
        print(f" {self.brand} {self.model} Tankolás utáni üzemanyagszint: {self.fuel_level:.1f}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - Km: {self.mileage:.1f}, Üzemanyag: {self.fuel_level:.1f}%"
    
class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Autó hozzáadva: {car.brand} {car.model}")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Autó eltávolítva: {car.brand} {car.model}")
        else:
            print("Ez az autó nem található a flottában.")

    def total_mileage(self):
        """Összegzi a flotta összes autójának kilométeróra állását."""
        return sum(car.mileage for car in self.cars)

    def display_fleet_status(self):
        print("\n--- Flotta állapota ---")
        for car in self.cars:
            print(car)
        print(f"Összesített flotta kilométer: {self.total_mileage():.1f} km")
        print("-----------------------\n")

# --- Próba ---
if __name__ == "__main__":
    # Flotta és autók létrehozása
    my_fleet = Fleet()
    autoim1 = Car("Skoda", "S100", 1987)
    autoim2 = Car("Opel", "Ascona", 1993)
    autoim3 = Car("Renault", "Thalia", 2002)
    aAutoim4 = Car("Ford", "SMax", 2016)

    # Autók hozzáadása
    my_fleet.add_car(autoim1)
    my_fleet.add_car(autoim2)
    my_fleet.add_car(autoim3)
    my_fleet.add_car(aAutoim4)

    # utazás
    print("\n--- Utazások, tankolások ---")
    autoim1.drive(-1)   # negatív km tesztelése
    autoim1.drive(300)   # 30% üzemanyag használat
    autoim1.drive(400)   # még 40% üzemanyag használat
    autoim1.drive(400)   # túlhajtunk? elfogy a nafta?
    print(autoim1)
    autoim2.drive(1200)  # Elfogy az üzemanyag 1000 km után
    print(autoim2)
    autoim2.refuel(50)   # Tankolás
    autoim2.drive(200)   # tovább utazás
    print(autoim2) 
 
    # Flotta állapotának megjelenítése
    my_fleet.display_fleet_status()

    # Autó eltávolítása és frissített adatok
    print("\n--- Autó eladása ---")
    my_fleet.remove_car(autoim3)
    my_fleet.display_fleet_status()