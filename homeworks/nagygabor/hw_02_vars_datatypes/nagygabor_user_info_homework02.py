user_info = {
    "name": "Gábor",
    "age": 39,
    "favorite_meals" : ["Kievi", "Bakonyi", "Gomba pörkölt", "Sushi", "Gyros", "Bécsi szelet" ],
    "phone_contacts": { 
        "Tamás" : "+3650123458",
        "Balázs" : "+3620046984",
        "János" : "+3640248887"
    }
}
#-------SKILL INPUT-------- -----------------------------------------------------
skill_input = input('Adj meg 4 programozási nyelvet (vesszővel elválasztva):')
user_info['skills'] = skill_input.split(',')

#-----ABC ORDERING
user_info["favorite_meals"].sort()

#-----PENULTIMATE ITEM ERASE
print(f"A rendezett lista utolsó előtti eleme: {user_info['favorite_meals'][-2]}")

#----ADD SPAGETTI----------------------------------------------------------------
user_info["favorite_meals"].append("Spagetti")
print(f"Verzion 1 list {user_info["favorite_meals"]}")

#----READD 3rd AND 4th ITEM------------------------------------------------------
third_item = user_info["favorite_meals"][2]
forth_item = user_info["favorite_meals"][3]
user_info["favorite_meals"].extend([third_item, forth_item])
print(f"extendend List: {user_info['favorite_meals']}")

#-----ERASE DUPLICATED ITEMS (SET)---------------------------------------------
user_info["favorite_meals"] = list(set(user_info["favorite_meals"]))
user_info["favorite_meals"].sort()
print(f"ERASE DUPLICANTED ITEMS: {user_info['favorite_meals']}")

#-----REPLACE THE FIRST AND THE LAST ITEMs-------------------------------------
user_info["favorite_meals"][0], user_info["favorite_meals"][-1] = \
    user_info["favorite_meals"][-1], user_info["favorite_meals"][0]
print(f"Replace the first and the last items: {user_info['favorite_meals']}")

#----PHONEBOOK REFRESH--------------------------------------------------------
user_info["phone_contacts"]["Marina"] = "+3670215975"
if "János" in user_info["phone_contacts"]:
    del user_info["phone_contacts"]["János"]

#----ADD PÉTER---TWO PHONE NUMBER---------------------------------------------
user_info["phone_contacts"]["Péter"] = ["+36104879524, +3620459785"]

#----RENAME BALÁZS TO TIM----------------------------------------------------
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Balázs")

print("\n8-10. LÉPÉS - Telefonkönyv frissítve.")
print(f"Új névsor: {list(user_info['phone_contacts'].keys())}")

print("\n=== HOMEWORK READZ FULL OBJECT BELLOW: ===")
import json
print(json.dumps(user_info, indent=4, ensure_ascii=False))