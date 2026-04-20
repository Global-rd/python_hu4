"""
List és Dictionary használata
"""
from pprint import pprint

user_info = {
    "name": "Mike",
    "age": 25,    
    "favourite_meals": ["pizza","carbonara","sushi"],
    "phone_contacts":{
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }
}   

#Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,
#szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá
#a fenti dictionary-hez “skills” néven.

prog_languages = input("Enter four programming languages separated by a coma!").split(",")
user_info ["skills"] = prog_languages

#2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő
#sorrendbe.

user_info ["favourite_meals"]  .sort()

#3.Printeld ki a favourite_meals lista utolsó előtti elemét

print("-------")
print(f"Utolsó előtti elem: {user_info["favourite_meals"][-2]}")
print(f"Teljes lista: {user_info["favourite_meals"]}")

#4.Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
user_info["favourite_meals"].append("spaghetti")

#5.Add hozzá a favourite_meals-hez az aktuális favourite_meals lista
#harmadik és negyedik elemét (nem az index-ét) újra.

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

#6.Ezután töröld az így keletkezett duplikátumokat!

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

#7.Cseréld fel a favourite_meals lista első és utolsó elemét!

user_info["favourite_meals"] [0],user_info["favourite_meals"] [-1] = user_info["favourite_meals"] [-1], user_info["favourite_meals"][0]

#8.A “phone_contacts” dictionary-hez adj hozzá egy új elemet,
#tetszőleges névvel és telefonszámmal.

user_info["phone_contacts"] ["Jack Sparrow"] = "+3620493892"

#9.9. Tim és Tim2 ugyanazt az embert reprezentálják a
#“phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám
#már nem él. Töröld ki a telefonkönyvből!

user_info["phone_contacts"].pop("Tim",None)

#10.Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2
#telefonszáma is van!

user_info["phone_contacts"] ["Dalai Láma"] = ("+36308378874, +36203473306")

#Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!

print("------")
print(f"Utolsó három elem ellentétes sorrendben: {user_info["skills"][-1:-4:-1]}")
print(f"Teljes Lista: {user_info["skills"]}")

#Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne
#átnevezni Tim2-t Tim-re!

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2",None)

#Teljes lista megtekintése
print("----------")
print("user_info =")
pprint(user_info)
