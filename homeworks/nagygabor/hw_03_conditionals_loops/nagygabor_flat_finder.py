# FLAT FINDER - Sarah's apartment search

# INPUT
city = input("Enter the city: ").strip().title()
rent = int(input("Enter the monthly rent in USD: "))

# CONDITIONS
if city == "Washington":
    print(f"Sarah would NOT move to {city} for any price!")

elif city == "Chicago":
    print(f"Sarah would MOVE to {city}! She loves it no matter the price!")

elif city in ["New York", "San Francisco"] and rent < 4000:
    print(f"Sarah would MOVE to {city} for ${rent}/month!")

elif city not in ["Washington", "Chicago", "New York", "San Francisco"] and rent <= 3000:
    print(f"Sarah would MOVE to {city} for ${rent}/month!")

else:
    print(f"Sarah would NOT move to {city} for ${rent}/month. Too expensive!")