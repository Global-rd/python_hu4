
<<<<<<< Updated upstream
name = input("Hogy hívnak?" )
age = int(input("Hány éves vagy? "))
python_exp_in_years = int(input("Hány év Python gyakorlatod van? "))
=======
name = input("Hogy hívnak? ")
age = int(input("Hány éves vagy? "))
python_exp_in_years = int(input("Hány év Python tapasztalatod van? "))
>>>>>>> Stashed changes

print(name)
print(age)
print(python_exp_in_years)

print(name.strip().capitalize())
print(name.strip().upper())

age_in_days = int(age)*365

print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")


# extra task

<<<<<<< Updated upstream
question = input("Szeretnél-e profi python fejlesztő lenni?")
dev_intention = "wants" if question== "yes" else "does not want"
   
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she {"wants" if question== "yes" else "does not want"} to be a Python developer!")
=======
question = input("Szeretnél-e profi python fejlesztő lenni? (yes/no) ")

# változó = érték_ha_igaz if feltétel else érték_ha_hamis
dev_intention = "wants" if question == "yes" else "does not want"

print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she {dev_intention} to be a Python developer!")
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she {'wants' if question == 'yes' else 'does not want'} to be a Python developer!")
>>>>>>> Stashed changes
