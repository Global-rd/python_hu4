city= input("Please enter the city:").title()
price= int(input("Please enter the price (USD):"))
if city in ["San Francisco", "New York"] and (price < 4000):
     print(f"The flat is in {city} costs {price} USD. This matches Sarah's criteria!")
elif city == "Washington":
     print(f"The flat is in {city} costs {price} USD. This does NOT match Sarah's criteria!")
elif city == "Chicago":
     print(f"The flat is in {city} costs {price} USD. This matches Sarah's criteria!")
elif price<= 3000:
        print(f"The flat is in {city} costs {price} USD. This matches Sarah's criteria!")