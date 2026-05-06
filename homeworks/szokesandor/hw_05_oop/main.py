"""
Jármű flotta adatok kezelése, Car és Fleet class -ok segítségével

"""

from car_fleet_mgr import Car, Fleet
from random import random

def main():
    # Car objektumok létrehozása
    peugeot_car = Car("SZS-001", "Peugeot", "308 1.2 Hybrid Allure", 2023)
    opel_car = Car("SZS-002", "Opel", "Astra - J", 2017)
    isuzu_car = Car("SZS-003", "Isuzu", "D-max 1.9", 2024)
    suzuki_car = Car("SZS-004", "Suzuki", "Vitara 1.4 Hybrid GL+", 2025)

    # Flotta objektum létrehozása, és az autók hozzáadása a flottához
    fleet = Fleet("Developers' fleet")
    fleet.add_car(peugeot_car)
    fleet.add_car(opel_car)
    fleet.add_car(isuzu_car)
    fleet.add_car(suzuki_car)

    # Az Opellel megyünk egy kört, tankolunk bele egy keveset, és kiprinteljük az adatait
    print("----------")
    opel_car.drive(325)
    opel_car.refuel(15.3)
    print(opel_car)

    # Mindegyik autóval megteszünk egy random távolságot 100 és 2000 km között. Ha kifogy útközben az üzemanyag, akkor tankolunk bele 30%-ot
    for car in fleet.cars:
        km_to_travel = 100 + random() * 1900  # 100 és 2000 km közötti véletlen szám. Ennyi km-t teszünk meg az adott autóval
        while True:  # Útközben több tankolásra is szükség lehet. A ciklus addig fut, amíg a megtett km el nem éri a véletlen számként generált km-t
            km_traveled = car.drive(km_to_travel) # A metódus visszaadja a ténylegesen megtett km-t.
            # Ha a ténylegesen megtett km kevesebb mint az argumentumként átadott km, akkor az azt jelenti, kifogyott az üzemanyag. Ilyenkor tankonlni kell, és folytatni tovább az utazást.
            if km_traveled < km_to_travel:
                car.refuel(30) # Nincs nálunk sok zsé, ezért csak 30%-ot tankolunk bele.
                km_to_travel -= km_traveled # Ennyit kell még tankolás után megtenni.
            else:
                break

    # Kiprinteljük a flotta összes járművének az adatait
    print()
    print("----------")
    fleet.print_all()

#----------------------------------------
# Main
#----------------------------------------

if __name__ == "__main__":
    main()
