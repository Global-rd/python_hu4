import re

#Get input data from user
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
py = input("Pythone exp. in Years: ")

user = {
    "name": name,
    "age": age,
    "Python": py,
}

#Remove extra Space-s and Capital first letter
#if name[0] == " ":
#    namevar = re.sub(r' ', '', namevar)
name = name.strip(" ")

#namevar = namevar[0].upper() + namevar[1:]
name = name.title()

#

name = name.rstrip()

#Calculate age of days from years

agevar_int = int(age)
agevar_days = agevar_int * 365

#Formatted string output
print(f"My character is {agevar_days} days old. His name is {name} and he has {py} years experience.")

