#----- FICTIVE CHARACTER -------

# INPUT
name = input("Enter your name: ").strip().title()
age = int(input("How old are you? "))
python_exp = int(input("How many years of Python experience do you have? "))

# AGE IN DAYS
age_in_days = age * 365

# EXTRA: WANTS TO BE A PYTHON DEVELOPER?
want_dev = input("Do you want to be a Python developer? (yes/no): ")

# TERNARY OPERATOR
dev_status = "He/she wants to be a Python developer!" if want_dev == 'yes' else "He/she does not want to be a Python developer!"

# PRINT
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp} years experience. {dev_status}")