
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

#1
skills = list(input("Enter skills separated by comma: ").split(","))

#only get 4 elements
skill_list_len = len(skills)
if skill_list_len > 3:
    for i in range(4,skill_list_len):
        skills.pop(4)

user_info.update({"skills": skills})

#print(user_info)

#2 favourite meal abc
favourite_meals_sorted = sorted(user_info["favourite_meals"])

#3 print one before last
favourite_meals_sorted_len = len(favourite_meals_sorted)
print(favourite_meals_sorted[favourite_meals_sorted_len-2])

#4 +speghetti
favourite_meals_sorted.append("spaghetti")

#5 append
favourite_meals_sorted.append(favourite_meals_sorted[2])
favourite_meals_sorted.append(favourite_meals_sorted[3])

#6 delete duplicates
favourite_meals_sorted = list(set(favourite_meals_sorted))

#7 swap
leng = len(favourite_meals_sorted)
favourite_meals_sorted[0], favourite_meals_sorted[leng-1] = favourite_meals_sorted[leng-1], favourite_meals_sorted[0]

#8 +phone call
user_info["phone_contacts"].update({"Gegge": 123456})

#9 delete
user_info["phone_contacts"].pop("Tim")

#10 double phone
user_info["phone_contacts"].update({"Double": [222222222,888888888]})

print(user_info)