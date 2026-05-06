"""
Class-okat tartalmazó modul

"""

class InvalidArgumentError(Exception):
    pass

# ----------------------------------------------------------------------------------------------
class Car:
    
    FUEL_CONSUMPTION = 0.1  # 0.1 százalékpont üzemanyag fogy el megtett kilométerenként

    def __init__(self, license_plate: str, brand: str, model: str, year: int, mileage: float=0, fuel_level: float=100) -> None:
        """
        Car object init
        """
        self.license_plate = license_plate.upper() # A rendszámot nagybetűre alakítva írjuk az objektum attributumba.
        self.brand = brand
        self.model = model
        self.year = year
        if mileage < 0:
            raise InvalidArgumentError(f"{self._description_str()}: Mileage must be positive!")
        self.mileage = mileage
        if fuel_level < 0 or fuel_level > 100:
            raise InvalidArgumentError(f"{self._description_str()}: Fuel level must be between 0 and 100% !")
        self.fuel_level = fuel_level

    def __str__(self):
        """
        Converts car data to a multiline string
        """
        return f"{self.brand} {self.model}:\n - license plate: {self.license_plate}\n - year: {self.year}\n - mileage: {round(self.mileage, 3)} km\n - fuel level: {round(self.fuel_level, 2)} %"

    def _description_str(self):
        """
        Write the car's main data into a single-line string (for using in an exception message)
        """
        return f"{self.brand} {self.model} ({self.license_plate})"

    def drive(self, distance: float) -> float: 
        """
        Increases the mileage by a given number of kilometers and decreases the fuel level
        """
        if distance < 0:
            raise InvalidArgumentError(f"{self._description_str()}: Distance must be positive!")
        max_distance = self.fuel_level / Car.FUEL_CONSUMPTION  # Az aktuális üzemanyag szint esetén ennyi a maximális megtehető távolság
        if max_distance < distance:
            self.mileage += max_distance
            self.fuel_level = 0
            return max_distance # Ha nincs elegendő üzemanyag, akkor az autó kevesebb távolságot tesz meg. A metódus visszaadja a ténylegesen megtett utat.
        else:
            self.mileage += distance
            self.fuel_level -= distance * Car.FUEL_CONSUMPTION
            return distance # Elegendő üzemanyag esetén a paraméterként átadott távolsággal tér vissza

    def refuel(self, volume:float=None) -> None:
        """
        Refuels the car
        """
        if volume: 
            if volume < 0 or volume > 100:
                raise InvalidArgumentError(f"{self._description_str()}: Volume must be between 0 and 100% !")
            self.fuel_level += volume
            # 100%-nál magasabb nem lehet a feltöltöttségi szint
            if self.fuel_level  > 100:
                self.fuel_level = 100
        else: # Ha nem adtak meg volume értéket, akkor csurig töltjük a tankot
            self.fuel_level = 100

# ----------------------------------------------------------------------------------------------
class Fleet:
    def __init__(self, fleet_name: str) -> None:
        """
        Fleet object init
        """
        self.fleet_name = fleet_name
        self.cars = []

    def add_car(self, car: Car) -> None:
        """
        Adds a car to the fleet
        """
        self.cars.append(car)

    def remove_car(self, license_plate: str) -> None:
        """
        Removes a car from the fleet
        """
        # A flottából eltávolítandó autó rendszámát kell megadni. Az alábbiakban megkeressük a rendszámot
        for car in self.cars:
            if car.license_plate == license_plate.upper():
                 self.cars.remove(car)
                 return
        raise InvalidArgumentError(f"The car with license plate {license_plate} is not part of the fleet!") # Ha a megadott rendszámmal nem található autó a flottában, akkor exception generálódik.

    def get_mileage_total(self) -> float:
        """
        Calculates the total kilometers of all cars in the fleet.
        """
        total = 0
        for car in self.cars:
            total += car.mileage

    def print_all(self):
        """
        Prints out the data of all cars in the fleet
        """
        print(self.fleet_name)
        if self.cars:
            for id, car in enumerate(self.cars, 1):
                print(f"{id}. {car}")
                print()
        else:
            print("There are no cars in this fleet.")
