#real life example: egy gépezet ami játékokat gyárt

# van egy kezelőfelülete amin be tudjuk állítani a következőket:
#- játék típus (pl: barbie, matchbox)
#- játék színe (rózsazín, sárga stb.)
# ezután a gép legyártja a játékot

# class: maga a gépezet, ami tudja hogy kell megcsinálni az adott paraméterek alapján a játékot, van hozzá egy leírása
# __init__(): a gép kezelőfelülete, amivel interaktálunk amikor létre akarjuk hozni a játékot
# instance (példány): a gép által létrehozott játék
# instance variable (attribute): a konkrét tulajdonságok, amik jellemzik a létrehozott játékokat
# instance method: a játékokat módosító/ használó cselekmény (metódus)
# class variable: egy olyan tulajdonság ami a gépet jellemzi (pl hány játékot gyártott le eddig)
# class method: egy olyan cselekmény ami a gépezethez tartozik (például kiírja a kijelzőre hogy hány játékot gyártott le)
# static method: nincs hozzáférése sem az osztályhoz, sem a példányhoz, de logikailag ide tartozik: pl: használhatja e a gyerek a játékot x éves kor alatt

class Toy:

    toy_count = 0

    def __init__(self, t_type, t_color):
        self.toy_type = t_type
        self.toy_color = t_color
        Toy.toy_count += 1
    
    def play(self): #instance method
        print(f"Currently playing with {self.toy_color} {self.toy_type}")

    def move(self, distance, direction):
        print(f"{self.toy_color} {self.toy_type} moved {distance} meters to {direction}")

    @classmethod #decorator
    def get_toy_count(cls): #GETTER
        return cls.toy_count
    
    @staticmethod
    def is_toy_safe_for_age(toy_type, age):

        if toy_type == "barbie" and age < 3:
            return False
        return True


toy_matchbox = Toy(t_type="matchbox", t_color="yellow")
print(toy_matchbox)
print(toy_matchbox.toy_color)
print(toy_matchbox.toy_type)
toy_matchbox.play()
toy_matchbox.toy_color = "orange"
toy_matchbox.play()

toy_barbie = Toy(t_type="barbie", t_color="pink")
toy_barbie.play()

toy_matchbox.move(100, "left")

print(Toy.toy_count)
print(Toy.get_toy_count())

print(Toy.is_toy_safe_for_age(toy_barbie.toy_type, 4))