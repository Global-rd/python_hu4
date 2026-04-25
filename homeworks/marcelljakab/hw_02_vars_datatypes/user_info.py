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
# 1. feladat: 4 programozási nyelv bekérése és hozzáadása
languages = input("Adj meg 4 programozási nyelvet vesszővel elválasztva: ")
user_info["skills"] = [lang.strip() for lang in languages.split(",")]

# 2. feladat: favourite_meals ABC sorrendben rendezése
user_info["favourite_meals"].sort()

#3. feladat: utolsó előtti elem kiírása
print(user_info["favourite_meals"][-2])
print(user_info["favourite_meals"])

#4. feladat: spaghetti hozzáadása
user_info["favourite_meals"].append("spaghetti")

#5. feladat: 3. és 4. elem hozzáadása újra
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])

#6. feladat: duplikátumok törlése
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

#7. feladat: első és utolsó elem felcserélése
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

#8. feladat: új elem hozzáadása phone_contacts-hoz
user_info["phone_contacts"]["Anna"] = "+36201234567"

#9. feladat: Tim törlése
del user_info["phone_contacts"]["Tim"]

#10. feladat: új ember 2 telefonszámmal
user_info["phone_contacts"]["Bob"] = ["+36301234567", "+36701234567"]

print(user_info)

                                              