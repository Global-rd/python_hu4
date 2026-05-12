'''
    Hozz létre egy új mappát a neveddel ellátott mappán belül “hw_05_oop”
    néven. A  következő feladatokhoz tartozó .py file-okat ide mentsd el.

    Feladat 1:

    Hozz létre egy car_fleet_mgr.py nevű file-t, és kódold le a következő
    feladat megoldását:

    Készíts egy Car osztályt, amely rendelkezik a következő tulajdonságokkal:
        - Márka (brand)
        - Modell (model)
        - Gyártási év (year)
        - Kilométeróra állása (mileage), induló értéke 0.
        - Üzemanyag-szint (fuel_level), induló értéke 100 (százalékban).

    Az osztály tartalmazza a következő metódusokat:
        - Egy konstruktor, amely beállítja a fenti attribútumokat.
        - Egy drive() metódus, amely adott számú kilométerrel növeli a
          kilométeróra állását, és csökkenti az üzemanyag-szintet (tételezzük
          fel, hogy 0.1% üzemanyag fogy megtett kilométerenként).
          A drive() metódus csak annyit km-et engedjen vezetni, amennyire
          elegendő üzemanyag van.
        - Egy refuel() metódus, amely feltölti az üzemanyag-szintet egy adott
          mennyiséggel. Figyelj a limitekre.

    Készíts egy Fleet osztályt, amely kezeli a Car objektumokat:
        - Az osztály rendelkezzen egy listával, amelyben az autók találhatóak.
        - Tartalmazzon metódusokat Car objektumok hozzáadására és
          eltávolítására a flottába/flottából.
        - Tartalmazzon egy metódust, amely összesíti a flotta összes autójának
          összes kilométerét.
        - Hozz létre néhány Car objektumot, add hozzá őket a flottához, hajts
          végre néhány műveletet (vezetés, tankolás),  jelenítsd meg az autók
          állapotát és a flotta összesítő adatait.
'''


class Car:

    def __init__(self, brand: str, model: str, year: int, mileage: int = 0, fuel_level: int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level

    def __str__(self):
        return f'{self.brand.upper()} {self.model.upper()}\t • {self.year} • {int(self.mileage)}\t • {int(self.fuel_level)}'

    def no_more_gasoline(self):
        print(f"\n{self.brand.upper()} {self.model.upper()} "
              "no more gasoline, tank is full!")

    def drive(self, distance: int):
        if self.fuel_level != 0:
            if self.fuel_level / 0.1 > distance:
                self.mileage += distance
            else:
                self.mileage += self.fuel_level / 0.1
                print(f"\n{self.brand.upper()} {self.model.upper()} "
                      "couldn’t reach the intended distance.")
        else:
            print(f"\n{self.brand.upper()} {self.model.upper()} "
                  "won't go anywhere, the tank is empty.")
            # ha van elegendo uzemanyag, akkor mehet a tavolság
            # ha nincs, akkor csak annyi, mig porzik a tank

        self.fuel_level -= distance * 0.1 if self.fuel_level / 0.1 > distance \
            else self.fuel_level
        # ha van elegendo uzemanyag, akkor fogyhat a nafta
        # ha nincs, nullazunk: porzik a tank és a kocsi valahol a sivatagban kalozok martaleka lesz

    def refuel(self, fuel_volume: int):
        if self.fuel_level < 100:
            if self.fuel_level + fuel_volume < 100:
                self.fuel_level += fuel_volume
            else:
                self.fuel_level = 100
                self.no_more_gasoline()
        else:
            self.no_more_gasoline()
        # maximum szint jelzes feltoltés utan a nafta robbano elegyet alkot a kocsi alatt


class Fleet:

    def __init__(self):
        self.cars: list = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car: Car):
        self.cars.remove(car)

    def list_of_cars(self):
        print('\nList of cars:')
        print('------------')
        print('Car \t\t   Year\t  km\t   Fuel %')
        print('-----------------------------------------')
        for car in self.cars:
            print(car)

    def summ_car_distance(self):
        summ_car_dist = sum(car.mileage for car in self.cars)
        print(f'\nThe overall mileage of the fleet: {int(summ_car_dist)} km.')


car_1 = Car('audi', 'a3 allroad', 2026, 1500, 10)
car_2 = Car('vw', 'passat', 2011, 88000, 80)
car_3 = Car('mercedes', 'c200', 2020, 54100, 20)
car_4 = Car('bmw', 'm5 cabrio', 2006, 52410, 5)
car_5 = Car('fiat', 'uno', 1988, 99800, 10)

fleet_1 = Fleet()

fleet_1.add_car(car_1)
fleet_1.add_car(car_2)
fleet_1.add_car(car_3)
fleet_1.add_car(car_4)
fleet_1.add_car(car_5)

fleet_1.list_of_cars()
fleet_1.summ_car_distance()

car_1.drive(50)         # OK
fleet_1.list_of_cars()
car_1.drive(100)        # részben teljesül
fleet_1.list_of_cars()
car_1.drive(100)        # nem ok
fleet_1.list_of_cars()

car_2.refuel(50)        # részben teljesül
fleet_1.list_of_cars()
car_2.refuel(20)        # nem ok
fleet_1.list_of_cars()
car_1.refuel(85)        # ok
fleet_1.list_of_cars()

fleet_1.remove_car(car_2)
fleet_1.list_of_cars()

fleet_1.summ_car_distance()
