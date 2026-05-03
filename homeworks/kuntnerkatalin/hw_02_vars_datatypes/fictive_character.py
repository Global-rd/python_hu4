"""HW_02_Fictive Character: Kérj be adatokat a felhasználótól, nevek nagybetűvel, 
szókoz nélkül, karakter életkora napokban, f-string print """

character_name = input("Name: ").upper().strip()
character_age = int(input("Age: "))
character_experience = int(input("Python experience in years: "))

#convert age to days
character_age_days = character_age * 365

#print
print(f"Your character is {character_age_days} days old. His/her name is {character_name}"
      f" and he/she has {character_experience} years experience in Python")