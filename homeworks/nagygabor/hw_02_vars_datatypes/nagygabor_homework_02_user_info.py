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

# 1. SKILL INPUT
skill_input = input("Enter 4 programming languages separated by commas: ")
user_info['skills'] = [s.strip() for s in skill_input.split(',')]

# 2. ABC ORDERING
user_info["favourite_meals"].sort()

# 3. PRINT PENULTIMATE ITEM
print(f"Penultimate item: {user_info['favourite_meals'][-2]}")
print(f"Full list: {user_info['favourite_meals']}")

# 4. ADD SPAGHETTI
user_info["favourite_meals"].append("spaghetti")
print(f"After append: {user_info['favourite_meals']}")

# 5. READD 3RD AND 4TH ITEMS
third_item = user_info["favourite_meals"][2]
fourth_item = user_info["favourite_meals"][3]
user_info["favourite_meals"].extend([third_item, fourth_item])
print(f"After extend: {user_info['favourite_meals']}")

# 6. ERASE DUPLICATES
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
user_info["favourite_meals"].sort()
print(f"After removing duplicates: {user_info['favourite_meals']}")

# 7. SWAP FIRST AND LAST
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = \
    user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(f"After swap: {user_info['favourite_meals']}")

# 8. ADD NEW CONTACT
user_info["phone_contacts"]["Marina"] = "+3670215975"

# 9. DELETE TIM (old number no longer active)
if "Tim" in user_info["phone_contacts"]:
    del user_info["phone_contacts"]["Tim"]

# 10. ADD PERSON WITH 2 PHONE NUMBERS
user_info["phone_contacts"]["Peter"] = ["+36104879524", "+3620459785"]

# EXTRA 2: RENAME TIM2 TO TIM
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

print("\nPhone contacts updated:")
print(f"Contacts: {list(user_info['phone_contacts'].keys())}")

# EXTRA 1: LAST 3 SKILLS IN REVERSE ORDER
print(f"\nExtra 1 - Last 3 skills reversed: {user_info['skills'][-1:-4:-1]}")

print("\n=== FULL OBJECT: ===")
import json
print(json.dumps(user_info, indent=4, ensure_ascii=False))