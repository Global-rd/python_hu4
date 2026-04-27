
# A fiktív NPC karakter szülinapjának kiszámításához:
from datetime import datetime

# A fiktív NPC karakter létrehozása a Mad Max univerzumban (user input):

first_name = (input("What is NPC's first name?")) # az input() mindig stringet ad vissza
print(first_name)
print(type(first_name))
print(len(first_name)) # előtte és utána 3-3 space van, mert a user véletlenül elrontotta

last_name = (input("What is NPC's last name?"))
print(last_name)
print(type(last_name))
print(len(last_name)) # előtte és utána 3-3 space van, mert a user véletlenül elrontotta

age_in_years = int((input("How old is NPC in Years?"))) # az életkor stringből integerre konvertálva
print(age_in_years)
print(type(age_in_years))

experience_py_in_years = int((input("NPC's experience with Python in years?"))) # stringből integer
print(experience_py_in_years)
print(type(experience_py_in_years))

# a nevek csupa nagybetűvel, előttük-utánuk space nélkül, az életkor napokban, a gyakorlat években:

first_name = first_name.upper().strip()
last_name = last_name.upper().strip()
age_in_days = age_in_years * 365

print(first_name, last_name, age_in_days)

print(len(first_name))
print(len(last_name))


# A karakter jellemzőinek kiiratása:

print("---------")
print("The NonPlayer Character in Mad Max is characterized by the following attributes:")
print("----------------------------------------------------------------------------------")
print(f"NPC's name is {first_name} {last_name} who has been in Wasteland for {age_in_days} days, and has {experience_py_in_years} years of experience with Python.")


# A karakter szülinapja a mai dátum (dátum kiiratása):

now = datetime.now()
print(f"This report was made today on {now:%m-%d-%Y} {now:%H:%M} CET, on {first_name} {last_name}'s happy birthday.")

