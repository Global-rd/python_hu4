'''
Hozz létre egy user_info.py file-t, és kódold le a következő feladat
megoldását. Nyugodtan használj kommenteket a különböző feladatpontok
előtt, hogy később könnyedén átlásd hogy melyik sor milyen funkciót lát el.
Adott a következő dictionary, amely egy felhasználó adatai tartalmazza
(másold át a kódodba):


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
'''

# MAKE DICT
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

'''
*** ugyanaz a helyzet, nincs szükség ezekre a sorokra.

# VARIABLE DEFINITION
input_temp: str = ''
list_temp: list = []
'''

# MODIFY DICT
'''
1.  Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,
szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá
a fenti dictionary-hez “skills” néven.

            - pass

'''
# INPUT DATA
input_temp: str = input('Please provide 4 programming languages '
                   '(separated by commas, without spaces): ')

# input_temp = 'basic,assembly,python,c++'
list_temp = input_temp.strip().split(',')
user_info['skills'] = list_temp

# Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
# - pass
user_info['favourite_meals'] = sorted(user_info['favourite_meals'])

# Printeld ki a favourite_meals lista utolsó előtti elemét
# - pass
print(user_info['favourite_meals'][-2])

# Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
# - pass
user_info['favourite_meals'].append('spaghetti')

# Add hozzá a favourite_meals-hez az aktuális favourite_meals lista
# harmadik és negyedik elemét (nem az index-ét) újra.
# - pass
'''
*** itt a 3 - 1 helyett miért nem használtál simán 2-t? :)
    meg tudod egyébként a teljes feladatot oldani egy soron, ha range-ekre
    hivatkozol

    ha például az lett volna a feladat hogy add hozzá a 3., 4., 5., 6., 7., 8.
    elemet újra, akkor már 6 sornyi kódot kellett volna egymás alá másolnod.
    Ezért effektívebb a lista elemeire index range-ekkel hivatkozni, mert így
    1 soron megoldod a problémát.
user_info['favourite_meals'].append(user_info['favourite_meals'][3 - 1])
user_info['favourite_meals'].append(user_info['favourite_meals'][4 - 1])
'''
user_info['favourite_meals'].append(user_info['favourite_meals'][2:4])

# Ezután töröld az így keletkezett duplikátumokat!
# - pass
user_info['favourite_meals'] = list(set(user_info['favourite_meals']))

# Cseréld fel a favourite_meals lista első és utolsó elemét!
# - pass
user_info['favourite_meals'][0], user_info['favourite_meals'][-1] = \
    user_info['favourite_meals'][-1], user_info['favourite_meals'][0]

# A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges
# névvel és telefonszámmal.
# - pass
user_info['phone_contacts']['John'] = '+36307677965'

# Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban,
# viszont a "Tim" key mögött lévő telefonszám már nem él.
# Töröld ki a telefonkönyvből!
# - pass
user_info['phone_contacts'].pop('Tim', None)

# Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2
# telefonszáma is van!
# - pass
user_info['phone_contacts']['Tomp'] = ['+36307677965', '+362057954856']

# Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!
# - pass
print(user_info['skills'][-1:-4:-1])

# Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne
# átnevezni Tim2-t Tim-re!
# - pass
user_info['phone_contacts']['Tim'] = user_info['phone_contacts'].pop('Tim2')
