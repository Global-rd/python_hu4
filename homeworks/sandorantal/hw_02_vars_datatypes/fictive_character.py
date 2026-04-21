name = input("Sandor Antal ")
age = input("37")
python_experience = input("0 ")

name = name.strip().upper()

age = int(age)
age_in_days = age * 365

python_experience = int(python_experience)

print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience.")