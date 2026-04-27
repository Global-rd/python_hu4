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
# 1. feladat:
#programozasi nyelvek: python,java,Javascript,go,ruby
skills = input("Kérek programozási nyelvet:")
skills = skills.split(",")
user_info["skills"] = skills

# 2. feladat
#Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])

# 3. feladat
print(user_info["favourite_meals"][-2])

# 4. feladat
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])

# 5. feladat
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])
print(user_info["favourite_meals"])

# 6. feladat
uj_lista = []
for elem in user_info["favourite_meals"]:
    if elem not in uj_lista:
        uj_lista.append(elem)
user_info["favourite_meals"] = uj_lista

# 7.feladat
elem1 = user_info["favourite_meals"][0]
elem_utolso = user_info["favourite_meals"][-1]

user_info["favourite_meals"][0] = elem_utolso
user_info["favourite_meals"][-1] = elem1
print(user_info["favourite_meals"])

# 8.feladat
user_info["phone_contacts"]["Gábor"]= "+3612345678"
print(user_info["phone_contacts"])

# 9. feladat
del user_info["phone_contacts"]["Tim"]
print(user_info["phone_contacts"])

# 10. feladat
user_info["phone_contacts"]["Sanyi"] = ["+3619874563", "+3699999999"]
print(user_info["phone_contacts"])
