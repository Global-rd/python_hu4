
name = "Darvas Magdolna"
age = "53"
python_exp_in_years = "0"

print(name)
print(age)
print(python_exp_in_years)

print(name.strip().capitalize())
print(name.strip().upper())

age_in_days = int(age)*365

print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")

# extra task

question = input("Szeretnél-e profi python fejlesztő lenni?")
if question == "yes":
    print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she wants to be a Python developer!")
elif question == "no":
    print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience.  He/she does not want to be a Python developer!")
    
