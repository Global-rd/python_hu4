"""
Homework 2.1: Variables, user input, string methods, type conversions
and f-string usage.
Author: Budai Krisztián
"""

section_separator: str = f"\n{'=' * 100}\n"

"""
User input tasks:
- Create a fictive character.
- Ask the user for their name, age, and Python experience in years.
- Use descriptive variable names for the collected data.
- Store the name in uppercase and remove any leading or trailing spaces.
- Convert the age to the correct data type.
- Ask the user whether the character should become
  a professional Python developer.
- Accept "yes" or "no" as input.
- Calculate and store the character's age in days in a new variable.
- Round the result and assume that today is the character's birthday.
"""
# Get the name from the user and normalize its format.
full_name: str = input("Could you give me your full name, please: ")
full_name = full_name.upper().strip()

# Get the age and Python experience, ensuring they are integers.
age: int = int(input("Could you give me your age, please: "))

# Get the Python experience in years, ensuring it is an integer.
python_experience_in_years: int = int(
    input("Could you give me your Python experience in years, please: ")
)

# Normalize the yes/no answer to make the check easier.
wants_to_be_prof: str = (
    input("Would you like to be a professional Python developer? (yes/no) ")
    .lower()
    .strip()
)

# Convert age to days approximately, including leap years.
age_in_days: int = round(age * 365.25)

print(section_separator)

"""
Message construction tasks:
- Use a ternary operator to build the final part of the message.
- Print all collected information in an interpolated string (f-string).
"""
# This part of the final message depends on the user's answer.
final_message_part: str = (
    "He/she wants to be a Python developer!"
    if wants_to_be_prof == "yes"
    else "He/she does not want to be a Python developer!"
)

# Print the final message with all the collected and processed information.
print(
    f"My character is {age_in_days} days old.\n"
    f"His/her name is {full_name} and "
    f"he/she has {python_experience_in_years} years experience.\n"
    f"{final_message_part}"
)
