
#1. feladat
name=input("Add meg a neved").upper().strip()
age=int(input("Add meg hány éves vagy"))
python_experience=int(input("hány éve programozol Pythonban"))
age_in_days=age*365

print(f" My  character is {age_in_days} old. Her/His name is {name}  and he/she has {python_experience} years experience.")

 #szorgalmi feladat
print("----------------------------")
name=input("Add meg a neved").upper().strip()
age=int(input("Add meg hány éves vagy"))
python_experience=int(input("hány éve programozol Pythonban"))
python_developer=input("Szeretné python programozó lenni. Add meg: Yes/No").lower().strip()
result="Szeretne python programozó lenni" if python_developer=="yes" else "Nem szeretne python programozó lenni"
print(f" My  character is {age_in_days} old. Her/His name is {name}  and he/she has {python_experience} years experience. {result}")

 
