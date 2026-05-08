class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: int = 0, fuel_level: float = 100.0 ):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level 
    
    #kilométerállás növelése a megadott értékkel, üzemanyagszint csökkentése
    def drive(self, desired_distance):
        max_possible_distance = self.fuel_level * 10
        if desired_distance <= max_possible_distance:
           self.mileage += desired_distance
           self.fuel_level -= desired_distance * 0.1 
        else:
           self.mileage += max_possible_distance
           self.fuel_level -= max_possible_distance * 0.1
    
    #üzemanyag szint feltöltése
    def refuel(self, fueling):
        if self.fuel_level + fueling <= 100:
           self.fuel_level += fueling
        else:  
           self.fuel_level = 100
    
    def __str__(self):
        return f"{self.brand}, {self.model}, {self.year}, {self.mileage}, {self.fuel_level}"

class Fleet:
    def __init__(self):
         self.cars = []
    
    #car objektumok hozzáadása a flottához
    def add_car(self, car): 
        if isinstance(car, Car):
           self.cars.append(car)      
    
    #objektum törlése a flottából
    def del_car(self, car):
        if car in self.cars:
           self.cars.remove(car)  
    
    #a flotta összes autójának összesített km-állása
    def sum_fleet_mileage (self):
        all_fleet_mileage = 0
        for car in self.cars:
            all_fleet_mileage += car.mileage 
        return all_fleet_mileage
    
    def __str__(self):
        fleet_content = "" 
        for car in self.cars:
         fleet_content += str(car) + "\n"
        return fleet_content

#car objektumok létrehozása
car_1 = Car(brand="Hunday", model="i10", year=2023, mileage=100, fuel_level=50.0)

car_2 = Car(brand="Dacia", model="Logan", year=2021, mileage=200, fuel_level=40.0)

car_3 = Car(brand="Toyota", model="Yaris", year=2019, mileage=400, fuel_level=70.0)

print(car_1)
print(car_2)
print(car_3)

#Első flotta létrehozása
fleet_1 = Fleet()

fleet_1.add_car(car_1)
fleet_1.add_car(car_2)

print ("----------------------")
print(fleet_1)

#Második flotta létrehozása
fleet_2 = Fleet()

fleet_2.add_car(car_3)

print("-------------------")
print(fleet_2)

#Vezetés a Hunday i10-el (car_1)
car_1.drive(50)

print("------------------")
print(car_1)

#Megint vezetés a Hunday i10-el (car_1), nagyobb távolságra, mint amit lehet
car_1.drive(460)

print("-------------------")
print(car_1)

#Tankolás a Hunday i10-be (car_1)           
car_1.refuel(50)

print("-------------------")
print(car_1)
print("--------------------")
print(fleet_1)

#Az 1-es flotta összes autójának összes km-állása
print(fleet_1.sum_fleet_mileage())

#Törlés a 2. flottából
fleet_2.del_car(car_3)

print(car_1)
print(car_2)

print("----------------------")
print(fleet_1)
print(fleet_2)