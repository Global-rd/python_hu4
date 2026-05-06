city = input("In which city is the apartment located?? ")
rent = int(input("How much is the monthly rent (USD)? "))
if city == "Chicago":
    can_move_in = True
elif city == "Washington":
    can_move_in = False
elif city in ["New York","San Francisco"] and rent < 4000:
    can_move_in = True
elif rent <= 3000:
    can_move_in = True
else:
    can_move_in = False

if can_move_in:
    print(f"Sarah can move into {city} for {rent} USD.")
else:
    print(f"Unfortunately, Sarah is NOT moving to {city} for {rent} USD.")