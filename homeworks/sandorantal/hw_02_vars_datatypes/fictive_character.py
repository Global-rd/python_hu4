name = input("What is your name? ")
age = input("What is your age? ")
python_experience = input("How many years of experience do you have with python? ")

name = name.strip().upper()

age = int(age)
age_in_days = age * 365

python_experience = int(python_experience)

print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience.")