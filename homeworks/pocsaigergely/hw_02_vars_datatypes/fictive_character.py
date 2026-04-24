import re

#Get input data from user
namevar = input("Enter Your Name")
#agevar = input("Enter Your Age")
agevar = 39
#pyvar = input("Pythone exp. in Years")
pyvar = 5

User = {
    "name": namevar,
    "age": agevar,
    "Python": pyvar,
}

#Remove extra Space-s and Capital first letter
if namevar[0] == " ":
    namevar = re.sub(r' ', '', namevar)

namevar = namevar[0].upper() + namevar[1:]

leng = len(namevar)

if namevar[leng-1] == " ":
    namevar = re.sub(r' ', '', namevar)

#Calculate age of days from years

agevar_int = int(agevar)
agevar_days = agevar_int * 365

print(namevar,agevar_days)

x = 5

y = 10

print(x is y)