#Adatok bekérése
#név: nagybetűsítve, szóközök eltávolítása
# kor és python tapasztalat számmá (integer) alakítása
name = input("Mi a neved? ").upper().strip()
age = int(input("Hány éves vagy? "))
python_exp_in_years = int(input("Hány éve foglalkozol pythonnal? "))

#az életkor napokra átszámítva
age_in_days = age * 365

#az információk visszaadása egy interpolált string-ben
print(f"Az én karakterem {age_in_days} napos. A neve: {name} és {python_exp_in_years} év tapasztalattal rendelkezik a Python nyelvben.")