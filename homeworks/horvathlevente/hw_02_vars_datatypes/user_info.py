import pprint
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
    },
}
skills_inp = input("Which programming languages do you know? (separate with commas): ") #taking the input of the user and storing it in a variable, then removing the spaces and splitting the string into a list of skills, which is then added to the user_info dictionary under the key "skills"
skills_wo_space = skills_inp.replace(" ", "")
skill_list = skills_wo_space.split(",")
user_info["skills"] = skill_list
user_info["favourite_meals"].sort() #sorting the list of favourite meals in alphabetical order
print(user_info["favourite_meals"][-2]) #printing the second to last element of the list of favourite meals
user_info["favourite_meals"].append("spaghetti") #adding a new meal to the list of favourite meals
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4]) #extending the list of favourite meals with the elements from index 2 to 3 (inclusive)
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"])) #removing duplicates from the list with dict.fromkeys() method
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0] #swapping the first and last element of the list
user_info["phone_contacts"]["John"] = "+36201234567" #adding a new contact to the phone_contacts dictionary with the key "John" and the value "+36201234567"
del user_info["phone_contacts"]["Tim"] #deleting the contact with the key "Tim" from the phone_contacts dictionary
user_info["phone_contacts"]["Louis"] = ["+36301234567", "+36307654321"] #adding a new contact to the phone_contacts dictionary with the key "Louis" and the value being a list of two phone numbers
print(user_info["skills"][-1:-4:-1]) #printing the last three elements of the skills list in reverse order
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2") #moving the contact with the key "Tim2" to the key "Tim" in the phone_contacts dictionary using the pop() method to remove the old key and return its value, which is then assigned to the new key