#while the name is not in good conversion (upper,strip)
name=input("Kérlek add meg a neved nagybetűvel : ")
counter=0
while  name!=name.upper().strip():
    name=input("Kérlek add meg a neved nagybetűvel : ")
    counter+=1
    if(counter>=4):
        name=name.upper().strip()
        break
#while the age is not in good conversion
age=0
while True:
    user_input=input("Kérlek add meg az életkorod:")
    try:
        age=int(user_input)
        break
    except ValueError:
        print(f"nem jó a szám {user_input}")
        continue
#konverted date        
days=age*365
#while the python_experinece is not in good conversion
python_experinece=0
while True:
    try:
        python_experinece=int(input("Kérlek add meg hány év Python tapasztalatod van:"))
        if python_experinece < 0:
            print("Nem lehet negatív szám!")
            continue
        break
    except ValueError:
        print(f"nem jó a szám {python_experinece}")

#want to be a professional
dev_intention = "wants" if input("Szeretnél profi lenni:").upper()== "YES" else "does not want"

print(f"My character {age} (years) in {days} (days) old. His/her name is {name} and he/she has {python_experinece} years experience. ")
print(f"He/she {dev_intention} to be a Python developer!")