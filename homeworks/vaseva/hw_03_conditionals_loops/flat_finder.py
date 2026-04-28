
print("APARTMENT RENTAL SEARCH")
print("-----------------------")

while True:
    city = input("Enter the name of city (or type stop when you're done): ").strip().lower()
    if city == "stop":
        print("Have a successful apartment review!")
        print("-----------------------------------") 
        break

    # HIBAKEZELÉS: csak akkor megyünk tovább, ha számot adott meg
    rent_input = input("What monthly rental fee is appropriate in USD?? ").strip()
    if not rent_input.isdigit():
        print("Data entry error: please enter the rental fee in numbers.\n")
        continue

    rent = int(rent_input)

    # Döntés logikája
    if city in ["new york", "san francisco"]:
        if rent < 4000:
            decision = "Yes, Sarah would rent this apartment in"
        else:
            decision = "This is too expensive. Sarah wouldn't rent this apartment in"

    elif city == "washington":
        decision = "Sarah would never move to"

    elif city == "chicago":
        decision = "Sarah would rent an apartment at any price in"

    else:
        if rent <= 3000:
            decision = "Yes, Sarah would rent this apartment in"
        else:
            decision = "This is too expensive. Sarah wouldn't rent this apartment in"

    # f-string összefoglaló
    print(f"{decision} {city.title()} and pay rental fee ${rent} per month.\n")