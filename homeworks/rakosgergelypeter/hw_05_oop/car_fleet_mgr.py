import datetime

class FuelException(Exception):
    pass

class Car:
    def __init__(self,brand:str,model:str,year:datetime,mileage:float=0,fuel_level:int=100):
        self.brand=brand
        self.model=model
        self.year=year
        self.mileage=mileage
        self.fuel_level=fuel_level

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.year} - {self.mileage} - {self.fuel_level}"

    def drive(self,distance:int):
        if distance!=0:
            if (self.fuel_level>(distance*0.1)):
                self.mileage+=distance
                self.fuel_level-=(distance*0.1)
                return f"Az autó ennyi km-et tett meg{self.mileage} és ennyi a jeléenlegi üzemanyag {self.fuel_level}"
            else:   
                raise FuelException("Nincs elég üzemeanyagod!")
        else:
            raise ValueError()
        
    def refuel(self,liter:int):
            if liter <= 0:
                raise FuelExcpetion("A tankolás mennyisége pozitív kell legyen.")
            
            current_fuel_l = self.fuel_level + liter
            rest=current_fuel_l-100
            if rest>0:
                current_fuel_l-=rest
            self.fuel_level=current_fuel_l
            return f"Jelenlegi üzemanyagszint: {self.fuel_level}"
        
class Fleet:
    def __init__(self):
        self.cars:list[Car]=[]
    
    def __str__(self):
        return "\n".join(str(car) for car in self.cars)

    def add_cars_to_fleet(self,new_car):
        self.cars.append(new_car)
    
    def remove_cars_from_fleet(self,remove_car):
        self.cars.remove(remove_car)
    
    def sum_whole_fleet_mileage(self):
        return sum(car.mileage for car in self.cars)

def main():
    car1=Car("Toyota","Corolla",2023)
    car1.drive(90)
    car1.refuel(50)
    #CustomExcpetion Catch
    try:
        car1.drive(1000000)
        car1.refuel(100000)
    except FuelException as e:
        print(e)
    #DivideByZero Catch
    try:
        car1.drive(0)
    except ValueError as e:
        print(e)
    
    car2=Car("Mercedes","S",2023)
    car2.drive(500)
    car2.refuel(20)
    
    car3=Car("Nissan","Skyline",1995)
    car3.drive(500)
    car3.refuel(10000)

    fleet=Fleet()
    fleet.add_cars_to_fleet(car1)
    fleet.add_cars_to_fleet(car2)
    fleet.add_cars_to_fleet(car3)
    print(fleet)
    fleet.remove_cars_from_fleet(car1)
    print(fleet)
    print(fleet.sum_whole_fleet_mileage())
    print(fleet)

if __name__ == "__main__":
    main()