

print ("HW3: Sarah looking for a flat.... ")


city_name = input("choose a city to analyse : ")
rent_in_the_city = int(input("how much is the rent there? (number only in USD) "))

if city_name == "Washington":
        print(f"in {city_name} she will never live. ")

elif city_name == "New York" or city_name == "San Fransisco":
    if rent_in_the_city <= 4000: 
        print(f"in {city_name} she will take the flat, because it is well priced. ")
    else: 
        print(f"in {city_name} she will NOT take the flat, because it is over priced. ")

elif city_name == "Chicago":
        rent_in_the_city *= 2 
        print(f"in {city_name} she will pay double rent for me: {rent_in_the_city} USD")
else:
    if rent_in_the_city <= 3000: 
         print(f"for {rent_in_the_city} USD she would live in {city_name}  ")
    else:
         print(f"for {rent_in_the_city} USD she would rather live elswhere ")



print("game over")

