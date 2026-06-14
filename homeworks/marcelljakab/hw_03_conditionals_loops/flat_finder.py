# Feladat 1: Flat Finder-Sarah lakáskeresése

city = input("Add meg a várost: ").strip().title()
rent = int(input("Add meg a havi lakbért (USD): "))

if city == "Washington":
    can_move = False
elif city == "Chicago":
    can_move = True
elif city in ["New York", "San Francisco"]:
    can_move = rent < 4000
else:
    can_move = rent <=3000

if can_move:
    print(f"Sarah beköltözne {city}-ba/be, {rent} USD/hó lakbérért. - IGEN")
else:
    print(f"Sarah NEM költözne {city}-ba/be, {rent} USD/hó lakbérért. - NEM")