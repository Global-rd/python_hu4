city = input("In which city is the apartment located?? ")
rent = int(input("How much is the monthly rent (USD)? "))
if city == "Chicago":
    can_move_in = True
elif city == "Washington":
    can_move_in = False
elif (city == "New York" or city == "San Francisco") and rent < 4000:
    can_move_in = True
elif rent <= 3000 and city not in ["Chicago", "Washington", "New York", "San Francisco"]:
    # Ez az ág minden más városra vonatkozik
    can_move_in = True
else:
    # Ha egyik fenti feltétel sem teljesült
    can_move_in = False

# kiírom fstringgel is a megoldást
if can_move_in:
    print(f"Sarah can move into {city} for {rent} USD.")
else:
    print(f"Unfortunately, Sarah is NOT moving to {city} for {rent} USD.")