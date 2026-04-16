# HW 1 : Feladat 1: Változók, user input, string metódusok, type conversion, f-string használata

# Bekérjük a felhasználótól a szükséges adatokat
name = input("Név: ").upper().strip()
age_input = input("Életkor: ")
python_exp_input = input("Python tapasztalat években: ")

# Konvertáljuk az életkort int-re és számoljuk ki napokban
age = int(age_input)
age_in_days = round(age * 365)

# Python tapasztalat int-re
python_exp_in_years = int(python_exp_input)

# Extra feladat: Bekérjük, hogy profi Python fejlesztő-e
response = input("Szeretné-e hogy a karaktere profi Python fejlesztő legyen? (yes/no): ").lower()
developer_status = "wants to be a Python developer!" if response == "yes" else "does not want to be a Python developer!"

# Kiírjuk az információt f-string-gel
introduction = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she {developer_status}"
print(introduction)


# HW 2

user_info = {
    "name": "Mike",
    "age": 25,
    "favorite_meals": ["pizza",
           "pizza",
         "carbonarra",
         "sushi",
    ],
    "phone_contact": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    }1
}   

skills_input = input("Enter 4 programming languages separated by commas (no spaces): ")
user_info["skills"] = skills_input.split(",")

