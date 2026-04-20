user_info = {
    "name": "Mike",
    "age": 25,
    "favouritemeals": ["pizza","carbonara","sushi"],
    "phone_contacts": { "Mary": "+36701234567",
                        "Tim": "+36207654321",
                        "Tim2": "+36304567321",
                        "Jim": "+364005000"}
}
skills=input("Kérlek adj meg 4 programozási nyelvet , -vel elválasztva:")
skill_set=skills.split(",")
user_info["skills"]=skill_set
#print(user_info)

#2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
user_info["favouritemeals"]=sorted(user_info["favouritemeals"])
print(user_info["favouritemeals"])

#Printeld ki a favourite_meals lista utolsó előtti elemét
print(user_info["favouritemeals"][-2])
#Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
user_info["favouritemeals"].append("spaghetti")
print(sorted(user_info["favouritemeals"]))
#Add hozzá a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
user_info["favouritemeals"]+=user_info["favouritemeals"][2:4]
print(user_info["favouritemeals"])
#Ezután töröld az így keletkezett duplikátumokat!
user_info["favouritemeals"]=sorted(set(user_info["favouritemeals"]))
print(user_info["favouritemeals"])
#Cseréld fel a favourite_meals lista első és utolsó elemét!
user_info["favouritemeals"][0],user_info["favouritemeals"][-1]=user_info["favouritemeals"][1],user_info["favouritemeals"][0]
print(user_info["favouritemeals"])
#A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"]["Jim2"]="+311111111"
print(user_info["phone_contacts"])
#Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!
user_info["phone_contacts"].pop("Tim","None")
print(user_info["phone_contacts"])
#Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2telefonszáma is van!
user_info["phone_contacts"]["Jim3"]=["+311111111","311111112"]
print(user_info["phone_contacts"])
#Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!
print(user_info["skills"][-3:][::-1])
