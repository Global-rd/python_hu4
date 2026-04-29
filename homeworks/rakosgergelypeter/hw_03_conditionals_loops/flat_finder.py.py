"""
● Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban
kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD
havonta.
● Gyűlöli Washington-t, és semmi pénzért nem lakna ott
● Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit
megadna azért hogy ott lakhasson
● Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
ellenében költözne oda.
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott
feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""
import csv
import random

#USA városok file beolvasása
def file_reader(path)->list:
    cities=[]
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';') 
        
            for row in reader:
                cities.append(row["City"])
        return cities
    except FileNotFoundError as e :
        print(f"Nem megfelelő az elérési útvonal:{path}. Exception: {e}")
    except UnicodeDecodeError as e:
        print(f"Nem megfelelő az encoding :{path}. Exception: {e}")

#validálja, hogy a ,megadott város tényleg létezik USA-ban
def checking_the_city_existing(city,cities)->bool:
    #Létező város?
    return city in cities

#validálja és castolja az input-ot
def input_validator(input_text,input_type="str"):
    while True:
        user_input=input(input_text)
        try:
            if user_input!="" and input_type.lower()=="int":
                return int(user_input)
            else:   
                return user_input
        except ValueError:
            print(f"Nem jó a formátum: {user_input}")
            continue

#ez generálja ki az inputot
def output_generator (city,price) ->str:
    if city is not None and price is not None:
        return print(f"A megadott paraméterek alapján neked ez a legoptimálisabb választás : Város :{city}, Albérlet ára:{price} ")

def options(cities,city=None,price=None):
    #city van és price is van
    if checking_the_city_existing(city,cities) :
        if city =="Chicago":
            return city,price
            exit
        else:
            if city !="Washington":
                if price<=3000:
                    return city,price
                elif price<=4000 and city in ("New York","San Francisco"):
                    return city,price
            # ha Wahsingotnt választotta akkor kell egy random város
            else:
                return random.choice(cities),price
    # city van de price nincs
    elif checking_the_city_existing(city,cities) and price is None:
        if city =="Chicago":
            return city,0
            exit
        else:
            # ha Wahsingotnt választotta akkor kell egy random város
            if city =="Washington":
                return random.choice(cities),random.randint(1000, 10000)
            else:
                return city,random.randint(1000, 10000)
    #ha csak price van
    elif city=="":
        if price<=3000:
            return random.choice(cities),random.randint(1000, 10000)
    else:
        return "Wonderland",0
               
def main():               
    cities=file_reader("homeworks/rakosgergelypeter/hw_03_conditionals_loops/cities.csv")
    your_city=input_validator("Kérem adjon meg egy várost:")
    prefered_price=input_validator("Kérem adjon meg egy preferált árat:","int")
    output_generator(*options(cities,your_city,prefered_price))

main()