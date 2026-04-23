
city = input("Melyik város? ")
rent = int(input("Mekkora a havi albérlet ára? "))


if city == "New York" or city == "San Francisco":
    can_move = rent < 4000
elif city == "Washington":
    can_move = False
elif city == "Chicago":
    can_move = True
else:
    can_move = rent <= 3000


result = "Oda tudnál költözni" if can_move else "Nem tudnál oda költözni"
print(f"A(z) {city} város, {rent} USD havi albérlet mellett: {result}.")


