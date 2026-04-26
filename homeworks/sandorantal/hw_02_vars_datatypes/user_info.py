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
input_skills = input("Python,JavaScript,Java,Cplusplus ")
skills_list = input_skills.split(",")
user_info["skills"] = skills_list
user_info["favourite_meals"].sort()
print(f"Carbonara {user_info['favourite_meals'][-2]}")
user_info["favourite_meals"].append("spaghetti")
third_item = user_info["favourite_meals"][2]
fourth_item = user_info["favourite_meals"][3]
user_info["favourite_meals"].extend([third_item, fourth_item])
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
user_info["phone_contacts"]["Anna"] = "+36301112233"
if "Tim" in user_info["phone_contacts"]:
    del user_info["phone_contacts"]["Tim"]
    user_info["phone_contacts"]["Gabor"] = ["+36209998877", "+36704445566"]
    import pprint
pprint.pprint(user_info)
