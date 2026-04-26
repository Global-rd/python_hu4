name =input("what is your name?: ")
capitalized_name = name.strip().title() #removing any leading or trailing whitespace with strip() method and capitalizing the first letter of each word with title() method
age =input("What is your age, in numbers?: ")
age_in_days = int(age) * 365 #converting the age from string to integer with int() function and calculating the age in days by multiplying it by 365
experience =int(input("How many years of experience do you have, in numbers?: "))
python_pro = input("Do you want to be a Python pro? (yes/no): ")
if python_pro.lower() == "yes":
    print(f"My character is {age_in_days} days old. His name is {capitalized_name} and he has {experience} years of experience. He wants to be a Python pro!")
else:
    print(f"My character is {age_in_days} days old. His name is {capitalized_name} and he has {experience} years of experience. He doesn't want to be a Python pro.")