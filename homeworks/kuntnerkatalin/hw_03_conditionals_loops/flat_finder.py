"""Sarah-nak kell segítened a lakáskeresésben.
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott
feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""

city = input("Enter the name of the city: ").strip().title() 
rent = float(input("Enter the monthly rent: "))

if city == "Chicago": 
    print(f"There are a few available apartments in {city}. Would you like to see them?")

elif city == "Washington":
    print(f"I thought you don't want to move here...")

elif city in ["New York", "San Francisco"]  and rent < 4000:
        print(f"There are a few available apartments in {city} for {rent}. Would you like to see them?")

elif rent <= 3000: 
    print(f"There are a few available apartments in {city} for {rent}. Would you like to see them?")

else: 
    print("No apartments found. Please restart your search.")

# Kérdés: muszáj előre megadani a lakbért inputként? Chicago és Washington esetében nem számít. Utólag, "kód közben" is lehet
# inputot meghatározni? 