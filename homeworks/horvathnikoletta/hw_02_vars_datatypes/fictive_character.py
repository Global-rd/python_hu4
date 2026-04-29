name= input("Please enter your name!").upper().strip()
age = int(input("Please enter your age!"))
python_experience= int(input("Please enter how many years Python experience do you have!"))
age_in_days= age*365
informations = f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years experience."
print(informations)
