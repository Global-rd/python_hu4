from pprint import pprint
user_info = { 
"name": "Mike", 
"age": 25, 
"favourite_meals": [ 
"pizza", 
"carbonara", 
"sushi" 
], 
"phone_contacts": { 
"Mary": "+36701234567", 
"Tim": "+36207654321", 
"Tim2": "+36304567321", 
"Jim": "+364005000" 
} 
}

#4 programnyelv bekérése vesszővel elválasztva, szóközök nélkül

program_language=input("Please enter 4 programming languages seperated by comma!").strip()
program_language = program_language.split(",")
user_info["skills"]= program_language

#favourite_meals sorbarendezése abc szerint
user_info["favourite_meals"].sort()

#favourite_meals lista utolsó előtti elemének kiprintelése
print(user_info["favourite_meals"][-2])

#spaghetti hozzáadása ugyanehhez a listához
user_info["favourite_meals"].append("spaghetti")

#a favourite meals-hez az aktuális favourite meals harmadik és negyedik elemének hozzáadása
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

#duplikátumok kitörlése ebből a listából
user_info["favourite_meals"]=list(set(user_info["favourite_meals"]))

#favourite meals lista első és utolsó elemének felcserélése
user_info["favourite_meals"][0], user_info["favourite_meals"][-1]=user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

#phone contacthoz hozzáadás
user_info["phone_contacts"]["Hannah"]="+36201234567"

#Tim törlése
del user_info["phone_contacts"]["Tim"]

#új ember hozzáadása akinek 2 telefonszáma is van
user_info["phone_contacts"]["Robert"]=["+36709876543", "+3611234567"]
pprint(user_info)
