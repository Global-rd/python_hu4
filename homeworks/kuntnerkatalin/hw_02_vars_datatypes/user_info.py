"""HW_02_User information"""

# User information 
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

# 1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül. 
# Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven.
languages = input("Languages: ").split(",")
user_info["skills"] = languages

# 2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
user_info["favourite_meals"].sort()

# 3. Printeld ki a favourite_meals lista utolsó előtti elemét
print(user_info["favourite_meals"][-2])

# 4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
user_info["favourite_meals"].append("spaghetti")

# 5. Add hozzá a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# 6. Ezután töröld az így keletkezett duplikátumokat!
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# 7. Cseréld fel a favourite_meals lista első és utolsó elemét!
new_meals = user_info["favourite_meals"]
new_meals[0], new_meals[-1] = new_meals[-1], new_meals[0]

# 8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet,tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"]["Lizzie"] = "+3614664356"

# 9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. 
# Töröld ki a telefonkönyvből!
user_info["phone_contacts"].pop("Tim","None")

# 10.Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"]["Hanna"] = ["+3614664356", "+802765188"]