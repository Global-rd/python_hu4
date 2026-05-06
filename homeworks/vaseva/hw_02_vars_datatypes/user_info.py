
from pprint import pprint

# az eredeti user-info, amit módosítani kell:
user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza", "carbonara", "sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }
}

# 1. Inputtal bekért rogramnyelvek hozzáadása a user-info könyvtárhoz, skills néven:
print("--------------------------------------------------------------------")
user_info["skills"] = input("\nInput knowledge of 4 prg-languages, no spaces, separated by commas: ").split(",")
print(f"\n1. Added prg-skills to user_info: {user_info ['skills']}")

print(f"\nFavourite_meals before next changes: {user_info ['favourite_meals']}")
user_info["favourite_meals"].sort() # 2. A favourite_meals elemei abc-sorrendben legyenek
print(f"2. Favourite_meals in alphabetical order: {user_info ['favourite_meals']}")

# 3. Melyik a favourite_meals utolsó előtti eleme?
print(f"3. The penultimate item of favourite_meals: {user_info["favourite_meals"][-2]}")

user_info["favourite_meals"].append("spaghetti") #4. A spegetti hozzáadása a kedvenc ételekhez
print(f"4. Spaghetti is added to the favorite_meals: {user_info["favourite_meals"]}")

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4]) #5. A kedvenc ételekhez + a 3. és 4. elem
print(f"5. Favourite_meals list + its 3rd and 4th elements: {user_info["favourite_meals"]}")

user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) # 6. A dupla ételek törlése a menüről
print(f"6. Favourite_meals without duplicates: {user_info["favourite_meals"]}")
# ez összekeveri a lista elemeit, ezért majd megint sorrendbe kell tenni.

# 7.​ Az első és utolsó elem felcserélése a favourite_meals listában:
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(f"7. Swap the first and last items in favourite_meals: {user_info["favourite_meals"]}")

print(f"\nPhone-contacts before next changes: \n{user_info ['phone_contacts']}\n")
user_info["phone_contacts"]["Daddy"] = "+36303555507" # 8. Daddy felvétele a telefonlistába
print(f"8. Adding Daddy to the phone_contacts: \n{user_info["phone_contacts"]}\n")

user_info["phone_contacts"].pop("Tim", None) # 9. Tim telefonszámának törlése
print(f"9. Tim's phone number is deleted from phone_contacs: \n{user_info["phone_contacts"]}\n") 

user_info["phone_contacts"]["Bogi"] = ["+xx000000001", "+xx000000002"] # 10.​ Új kontakt felvétele 2 telefonszámmal
print(f"10. Bogi is added to phone_contacts width two phone numbers: \n{user_info["phone_contacts"]}\n")

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2", None) # 11. Tim2 kontakt átnevezése Timre
print(f"11. Tim2 is renamed to Tim in phone_contacts: \n{user_info["phone_contacts"]}\n")

# 12: A skills-lista utolsó három elemének nyomtatása ellentétes sorrendben:
print(f"12. The last three elements of skills printed in reverse order: {user_info["skills"][-3:] [::-1]}")
print(f"The list d'snt change if the items are printed out of order {user_info["skills"]}\n")

print("Up-to-date user_info dictionary after all changes: ")
print("----------------------------------------------------")
print("user info = ")
pprint(user_info)
# modified to restore in PR 04-05-26