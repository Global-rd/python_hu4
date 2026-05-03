city= input("Please enter the city:").title()
price= int(input("Please enter the price (USD):"))
if("New York" in city or "San Francisco" in city) and (price < 4000):
     print(f"The flat is in {city} costs {price} USD. This matches Sarah's criteria!")
elif("Washington" in city):
     print(f"The flat is in {city} costs {price} USD. This does NOT match Sarah's criteria!")
elif("Chicago" in city):
     print(f"The flat is in {city} costs {price} USD. This matches Sarah's criteria!")
else:
    if(price <= 3000):
        print(f"The flat is in {city} costs {price} USD. This matches Sarah's criteria!")