
#SINGLE LINE COMMENT / EGYSOROS KOMMENT

print("*************************")
print("Egy, megérett a meggy :)") # Az első Python-program köszöntése
print("*************************")

# MULTILINE COMMENT TYPES/ TÖBBSOROS KOMMENTTÍPUSOK    
"""
This is
my first 
Python 
program :)
"""

'''
This is my first 
Python program :)
'''

# PRIMITIVE DATA TYPES / PRIMITÍV ADATTÍPUSOK

# 1. STRING TYPE / KARAKTERLÁNC ADATTÍPUS
print("PRIMITIVE DATA TYPES")
print("1. STRING TYPE")
print("Popeye likes New Zealand spinach.")
print('"444"')  # Ez string, mert idézőjelben van, nem pedig szám
print('"True"') # Ez string, mert idézőjelben van, nem pedig logikai érték

# 2. INTEGER TYPE / EGÉSZ SZÁM ADATTÍPUS
print("2. INTEGER TYPE")
print(55555)

# 3. FLOAT TYPE / LEBEGŐPONTOS SZÁMTÍPUS (Nem egész számok)
print("3. FLOAT TYPE")
print(3.14159265358979323846) # A Python 15-16 tizedesjegyig számol pontosan
print(0.666666666666667)      # 2/3

# 4. BOLEAN TYPE / LOGIKAI SZÁMTÍPUS
print("4. BOLEAN TYPE")
print(True)  # "ez vagy az, de megalkuvás nincsen, mert a langyosat kiköpi az Isten"


# COMPOUND DATA TYPES / ÖSSZETETT ADATTÍPUSOK (Voluntary task, practical example)

from datetime import datetime
def get_greeting():
    current_hour = datetime.now().hour # Egész számot ad vissza
    if current_hour < 12:              # Logikai értéket ad vissza
        return "good morning :)"       # Stringet ad vissza
    elif current_hour < 18:
        return "good afternoon :)"
    else:
        return "good evening :)"
print("What a nice weather,", get_greeting())