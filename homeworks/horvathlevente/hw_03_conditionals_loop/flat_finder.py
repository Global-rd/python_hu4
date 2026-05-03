valid_cities = ["chicago", "new york", "san fransisco", "washington"]
user_quotation = input("Write the city and the rent price (in USD), separated by a comma: ")
print (user_quotation)
city_and_price = user_quotation.split(",")
city_and_price[1] = int(city_and_price[1].strip())
print (city_and_price)
if city_and_price[0].lower() == valid_cities[0]:
    print (f"Sarah is going to {city_and_price[0]} and the rent will be {city_and_price[1]} $.")
elif city_and_price[1] <4000 and city_and_price[0].lower() == valid_cities[1] or city_and_price[0].lower() == valid_cities[2]:
    print (f"Sarah is going to {city_and_price[0]} and the rent will be {city_and_price[1]} $.")
elif city_and_price[0].lower() == valid_cities[3]:
    print (f"Sarah is not going to {city_and_price[0]}")
elif city_and_price[1] <=3000:
    print (f"Sarah is going to {city_and_price[0]} and the rent will be {city_and_price[1]} $.")
else:    print (f"Sarah is keep searching for flats")
