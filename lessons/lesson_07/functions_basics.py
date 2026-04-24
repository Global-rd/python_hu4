#mire jók a function-ök?
#kód újrahasznosítás
#rendezettség fokozása
#"separation of concerns" - különböző feladatok különböző function-ökre bontása
#DRY- Don't Repeat Yourself -> repetitív logika absztrakciója function-ökkel
#Single responsibility principle -> egy function egy feladatért legyen felelős
# kerüljük el a mutable object-eket default argumentekként!

# bad example

name_1 = "Dexter"
name_2 = "John"
name_3 = "Emily"

print(f"Hello {name_1}, welcome home!")
print(f"Hello {name_2}, welcome home!")
print(f"Hello {name_3}, welcome home!")

# good example
print("---------------------")
def greet_user(name):
    print(f"Hello {name}, welcome on board!")


greet_user(name_1)
greet_user(name_2)
greet_user(name_3)



names = ["Alice", "Bob", "Dexter"]

for name in names:
    greet_user(name)
