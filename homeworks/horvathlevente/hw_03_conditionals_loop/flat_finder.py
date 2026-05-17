user_quotation = input("Write the city and the rent price (in USD), separated by a comma: ")
city, price_raw = user_quotation.split(",")
price = int(price_raw.strip())
city = city.strip().lower()
if city == "chicago":
    print (f"Sarah is going to Chicago and the rent will be {price} $.")
elif price <4000 and city in ["new york", "san fransisco"]:
    print (f"Sarah is going to {city} and the rent will be {price} $.")
elif city == "washington":
    print (f"Sarah is not going to {city}")
elif price <=3000:
    print (f"Sarah is going to {city} and the rent will be {price} $.")
else:    print (f"Sarah is keep searching for flats")
