'''
Ebben a feladatban egy képzeletbeli karaktert fogsz létrehozni
(mintázhatod nyugodtan magadról is :)). 
A feladatod, hogy a felhasználótól bekérd a következő input-okat 
(ezeknek megfelelő, leíró változóneveket adj):
Név
Életkor
Python tapasztalat években
'''
print('Kérem add meg az adataidat:')
your_name=input("Neved: ").title().strip()
#print(your_name) #teszt
age_in_years=input("Életkorod: ")
python_experience=input("Hány éve foglalkozol Pythonnal: ")

'''
Az életkort konvertáld át a megfelelő adattípusra, 
és egy új változóban tárold el hogy mennyi idős a karakter napokban 
(Kerekíts az években megadott életkor alapján, tételezzük fel hogy ma van az illető szülinapja).
'''
age_in_days=int(age_in_years)*365

# Az extra feladat előtti üzenet
#print(f"A karaktered {age_in_days} napos. A neved {your_name} és a {python_experience} éves tapasztalattal rendelkezel.")

#developer_question=
# Bekérjük a választ
developer_question = input("Szeretnél profi Python-os fejlesztővé válni? (igen/nem): ").lower().strip()

# Ternary operátorral eldöntjük az üzenetet
developer_answer = "és profi Python-os fejlesztővé szeretnék válni" if developer_question == "igen" else "és a Python-t hobbiként szeretnéd használni"
# A válasz alapján újragenerálom a végső üzenetet
print(f"A karaktered {age_in_days} napos. A neved {your_name} és a {python_experience} éves tapasztalattal rendelkezel {developer_answer}.")

