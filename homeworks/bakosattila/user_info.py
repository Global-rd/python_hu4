# HW 2

# Adott dictionary
user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza",
                        "carbonarra",
                        "sushi"
                        ],
    "phone_contact": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    }
}

# 1. Kérj be 4 programozási nyelvet
skills_input = input("Enter 4 programming languages separated by commas (no spaces): ")
user_info["skills"] = skills_input.split(",")

# 2. favourite_meals lista elemek abc szerinti növekvő sorrendbe.
user_info["favourite_meals"].sort()
print("favourite_meals after sorting:", user_info["favourite_meals"])

# 3. Print favourite_meals lista utolsó előtti eleme
print("Last but one element of favourite_meals:", user_info["favourite_meals"][-2])

# 4. "spaghetti" string ugyanehhez a listához.
user_info["favourite_meals"].append("spaghetti")
print("favourite_meals after adding spaghetti:", user_info["favourite_meals"])

# 5. aktuális favourite_meals lista harmadik és negyedik elem hozzáadása.
third = user_info["favourite_meals"][2]
fourth = user_info["favourite_meals"][3]
user_info["favourite_meals"].extend([third, fourth])
print("favourite_meals after adding third and fourth elements again:", user_info["favourite_meals"])

# 6. duplikátumok törlése
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
print("favourite_meals after removing duplicates:", user_info["favourite_meals"])

# 7. favourite_meals lista első és utolsó elemcsere
first = user_info["favourite_meals"][0]
last = user_info["favourite_meals"][-1]
user_info["favourite_meals"][0] = last
user_info["favourite_meals"][-1] = first
print("favourite_meals after swapping first and last:", user_info["favourite_meals"])

# 8. új elem
user_info["phone_contact"]["John"] = "+36500123456"
print("phone_contact after adding John:", user_info["phone_contact"])

# 9. Tim törlése
del user_info["phone_contact"]["Tim"]
print("phone_contact after deleting Tim:", user_info["phone_contact"])

# 10. Adj hozzá egy olyan új embert "phone_contacts"-hoz, akinek 2 telefonszáma is van!
user_info["phone_contact"]["Anna"] = ["+36600123456", "+36600765432"]
print("phone_contact after adding Anna with two numbers:", user_info["phone_contact"])

# Extra 1: Printeld ki a "skills" lista utolsó 3 elemét ellentétes sorrendben!
last_three_reversed = user_info["skills"][-3:][::-1]
print("Last 3 skills in reverse order:", last_three_reversed)

# Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
user_info["phone_contact"]["Tim"] = user_info["phone_contact"].pop("Tim2")
print("phone_contact after renaming Tim2 to Tim:", user_info["phone_contact"])