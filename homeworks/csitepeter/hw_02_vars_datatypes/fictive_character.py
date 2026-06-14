# Inputok bekérése
name = input("Kérlek add meg a neved: ")
age = input("Kérlek add meg hány éves vagy: ")
python_exp = input("Hány év Python tapasztalatod van: ")

# A név formázása, a szóközök eltávolítása és nagy kezdőbetű
name = name.strip().capitalize()

# Életkor konvertálása
age = int(age)

# Életkor napokban

age_in_days = age * 365
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp} years experience.")