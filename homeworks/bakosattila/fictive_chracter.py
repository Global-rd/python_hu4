
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
developer_status = "wants" if response == "yes" else "does not want"

# Kiírjuk az információt f-string-gel
introduction = f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she {developer_status} to be a Python developer"
print(introduction)

