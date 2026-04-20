"""
Homework 2.2: List and dictionary manipulation.
Author: Budai Krisztián
"""

from pprint import pprint
from typing import NotRequired, TypedDict

section_separator: str = f"\n{'=' * 100}\n"

"""
Initial user information.
"""


# Define a TypedDict for user information.
class UserInfo(TypedDict):
    name: str
    age: int
    favourite_meals: list[str]
    phone_contacts: dict[str, str | list[str]]
    skills: NotRequired[list[str]]


# Initialize the user information with the provided data.
user_info: UserInfo = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza", "carbonara", "sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    },
}

print("Initial user info:")
pprint(user_info)

print(section_separator)

"""
Programming languages tasks:
- Ask the user for 4 programming languages separated by commas
without spaces.
- Convert the input string into a list
and add it to the dictionary above as "skills".
"""

# Read and process the input for programming languages
input_data: str = input(
    "Please provide 4 programming languages "
    "(separated by commas, without spaces): "
)
skills_list: list[str] = input_data.strip().split(",") if input_data else []

# Validate the number of provided languages
if (skills_list_length := len(skills_list)) != 4:
    print(
        f"Error: Expected 4 programming languages, "
        f"but got {skills_list_length}."
    )
    pprint(skills_list)
    exit(1)

user_info["skills"] = skills_list
print("User info after adding skills:")
pprint(user_info)

print(section_separator)

"""
Favourite meals tasks:
- Sort the items in the "favourite_meals" list
  in ascending alphabetical order.
- Print the second-to-last item in the "favourite_meals" list.
- Add the string "spaghetti" to the same list.
- Add the current third and fourth items of the "favourite_meals" list
  to the end of the list again.
- Then delete the duplicates created this way.
- Swap the first and last items in the "favourite_meals" list.
"""
print("Favourite meals tasks\n")

# Sort the favourite meals alphabetically
user_info["favourite_meals"].sort()
print("After sorting favourite meals:")
pprint(user_info["favourite_meals"])

# Print the second-to-last item in the "favourite_meals" list.
print("Second-to-last favourite meal:")
print(user_info["favourite_meals"][-2])

# Append "spaghetti" meal to the list
user_info["favourite_meals"].append("spaghetti")
print("After appending spaghetti:")
pprint(user_info["favourite_meals"])

# Extend the list with the 3rd and 4th meals
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print("After extending with the 3rd and 4th meals:")
pprint(user_info["favourite_meals"])

# Delete the duplicated 3rd and 4th mealsA
del user_info["favourite_meals"][-2:]
print("After deleting the duplicated two meals:")
pprint(user_info["favourite_meals"])

# Swap the first and last meals
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0],
)
print("After swapping the first and last meals:")
pprint(user_info["favourite_meals"])

print(section_separator)

"""
Phone contacts tasks:
- Add a new entry to the "phone_contacts" dictionary
  with any name and phone number.
- Tim and Tim2 represent the same person in "phone_contacts",
  but the phone number under the "Tim" key is no longer valid.
  Remove it from the phone book.
- Add a new person to "phone_contacts" who has 2 phone numbers.
"""
print("Phone contacts tasks\n")

# Add a new contact for Christopher
user_info["phone_contacts"]["Christopher"] = "+36303455132"
print("After adding Christopher's contact:")
pprint(user_info["phone_contacts"])

# Delete Tim's outdated phone number.
del user_info["phone_contacts"]["Tim"]
print("After deleting Tim's contact:")
pprint(user_info["phone_contacts"])

# Add multiple contacts for John
user_info["phone_contacts"]["John"] = ["+36203456789", "+36204567890"]
print("After adding John's contacts:")
pprint(user_info["phone_contacts"])

print(section_separator)

"""
Extra tasks:
- Print the last 3 items in the "skills" list in reverse order.
- Now that only one phone number remains for Tim, rename Tim2 to Tim.
"""
print("Extra tasks:\n")

# Print the last 3 skills in reverse order
print("Last 3 skills in reverse order:")
print(user_info["skills"][-1:-4:-1])

# Rename Tim2 to Tim now that only one number remains
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print("After renaming Tim2 to Tim:")
pprint(user_info["phone_contacts"])
