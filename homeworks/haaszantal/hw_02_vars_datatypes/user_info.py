from pprint import pprint
user_info = { 
    "name": "Mike", 
    "age": 25, 
    "favourite_meals": [ 
        "pizza", 
        "carbonara", 
        "sushi" 
    ], 
    "phone_contacts": { 
        "Mary": "+36701234567", 
        "Tim": "+36207654321", 
        "Tim2": "+36304567321", 
        "Jim": "+364005000" 
    } 
 }

pprint(user_info) #formázva kinyomtatom

#egy kis gyakorlás
print(user_info["name"])
print(user_info["favourite_meals"][1])
print(user_info["phone_contacts"]["Mary"])

#1./a bekérem a 4 programozási nyelvet
pr_languages = input("Adj meg 4 programozási nyelvet, vesszővel elválasztva, szóközök nélkül!")
print(type(pr_languages)) #string

#1./b csinálok belóle listát
pr_lang_list = pr_languages.split(",")
print(type(pr_lang_list)) #lista
print(pr_lang_list) #ellenőrzöm, hogy a listaelemek jól jelennek-e meg

#1./c a skills-et hozzáadom a user_info dictionary-hez 
user_info["skills"] = pr_lang_list
pprint(user_info) # ellenőrzöm, hogy bekerült-e a skills a dictionary-ba

#2. favourite_meals lista elemeit abc szerinti növekvő sorrendbe
user_info["favourite_meals"].sort()
print("-----------------------------")
pprint(user_info) #ellenörzöm

#3. kiprintelem a a favourite_meals lista utolsó előtti elemét
print(user_info["favourite_meals"][-2])

#4. Hozzáadok egy “spaghetti” string-et ugyanehhez a listához, betűrendet figyelembe veszem
user_info["favourite_meals"].insert(2, "spaghetti")
pprint(user_info)

#5. Hozzáadom a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
#ha manuálisan adok hozzá a listához 2 elemet
#user_info["favourite_meals"].extend(["spagetthi", "sushi"])
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print("--------------------")
pprint(user_info)

#6. Ezután törlöm az így keletkezett duplikátumokat!
#először set-té alakítom a listát - ez eltávolítja a duplumokat, majd vissza listává
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print("----------------------------")
pprint(user_info)

#újrarendezem betűrendbe a listát
user_info["favourite_meals"].sort()
pprint(user_info)

print("------------------------------")

#7. Felcserélem a favourite_meals lista első és utolsó elemét!
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
pprint(user_info)

print("------------------")

#8. A “phone_contacts” dictionary-hez hozzáadok egy új elemet, tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"]["Antal"]  = "+361111111"
pprint(user_info)

print("------------------")

#9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. 
# KItörlöm a telefonkönyvből!
del user_info["phone_contacts"]["Tim"]
pprint(user_info)

print("------------------")

#10. Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"]["Károly"]  = ["+362222222", "+363333333"]
pprint(user_info)

#+Extra1: Kiprinteld a “skills” lista utolsó 3 elemét ellentétes sorrendben!
print(user_info["skills"])
print(user_info["skills"][-3:][::-1])

print("------------------------------")

#Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
#Ezt 2 lépésben tudom megtenni: 1) a telefonszám átvitele az új kulcsra, 2) régi kulcs-érték törlése
#user_info["phone_contacts"]["Tim"]  = "+36304567321"
#del user_info["phone_contacts"]["Tim2"]
#De ez a jobb változat, 1 lépésben
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint(user_info)