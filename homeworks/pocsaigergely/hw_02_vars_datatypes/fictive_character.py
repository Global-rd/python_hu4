import re

#Get input data from user
namevar = input("Enter Your Name")
agevar = input("Enter Your Age")
pyvar = input("Pythone exp. in Years")

User = {
    "name": namevar,
    "age": agevar,
    "Python": pyvar,
}

#Remove extra Space-s and Capital first letter
if namevar[0] == " ":
#    namevar = re.sub(r' ', '', namevar)
    namevar = namevar.strip(" ")

#namevar = namevar[0].upper() + namevar[1:]
namevar = namevar.title()

leng = len(namevar)

if namevar[leng-1] == " ":
    namevar = re.sub(r' ', '', namevar)

#Calculate age of days from years

agevar_int = int(agevar)
agevar_days = agevar_int * 365

#Formatted string output
print(f"My character is {agevar_days} days old. His name is {namevar} and he has {pyvar} years experience.")

