import pprint

user_info={
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza", 
                        "carbonara",  
                        "sushi"],
    "phone_contacts":{
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+36304005000"
    }
 }

#1.
print("---------")
print("1.feladat")
programnyelv=(input("Adj meg 4 programozási nyelvet, szóköz nélkül, vesszővel elválasztva: ")).split(",")

user_info["skills"]=programnyelv #a programnyelv lista hozzáadása a könvytárhoz
pprint.pprint(user_info)

#2.
print("---------")
print("2.feladat - Rendezés abc szerint")

user_info["favourite_meals"].sort() #abc sorrend
print(user_info["favourite_meals"])


#3
print("---------")
print("3.feladat - utolsó előtti elem")
print(f"Az utolsó előtti elem: {user_info["favourite_meals"][-2]}") #utolsó előtti elem kiírása a favourite-meals-ből

#4
print("---------")
print("4.feladat - Spagetti hozzáadása ")
user_info["favourite_meals"].append("sphagetti") #sphagetti hozzáadása
print(user_info["favourite_meals"])

#5
print("---------")
print("5.feladat  A harmadik és negyedik elem hozzáadása a listához")
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:])
print(user_info["favourite_meals"])

#6
print("---------")
print("6.feladat - törlés")
del user_info["favourite_meals"][-2:]
print(user_info["favourite_meals"])

#7elemek felcserélése
print("---------")
print("7.feladat - elemek felcserélése")
x=user_info["favourite_meals"][0] #1.elemet beteszem agy x változóba
user_info["favourite_meals"][0]=user_info["favourite_meals"][-1] #az utolsó elemet az első helyére
user_info["favourite_meals"][-1]=x #az x-ben tárolt elemet pedog az utolsó elem helyére teszem
print(user_info["favourite_meals"])



#8
print("-----------------")
print("8.feladat - új kontakt hozzáadása")
user_info["phone_contacts"]["Anna"]=["+36306998745"] # új contact hozzáadása
print(user_info["phone_contacts"]) #ellenőrzés kiírással


#9
print("-----------------")
print("9.feladat - Tim törlése")
del user_info["phone_contacts"]["Tim"]
pprint.pprint(user_info)

#10
print("-----------------")
print("10.feladat - új ember hozzáadása")
user_info["phone_contacts"]["Zolika"]=["+36208526547", "+360785214636"]
pprint.pprint(user_info)

#szorgalmi
print("-----------------")
print("szorgalmi - fordított sorrend")
print(f"Eredeti sorrend: {user_info["skills"]}") #skills lista
print(user_info["skills"][-3:][::-1]) #utolsó három fordított sorrendben

print("-----------------")
print("szorgalmi - átnevezés")
user_info["phone_contacts"]["Tim"]=user_info["phone_contacts"].pop("Tim2")
pprint.pprint(user_info)
