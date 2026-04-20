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
    try:
        age=int(input("Kérlek add meg az életkorod:"))
        break
    except ValueError:
        print(f"nem jó a szám {age}")
        continue
#konverted date        
days=age*365
#while the python_experinece is not in good conversion
python_experinece=0
while True:
    try:
        python_experinece=int(input("Kérlek add meg hány év Python tapasztalatod van:"))
        break
    except ValueError:
        print(f"nem jó a szám {python_experinece}")

#want to be a professional
is_professional=True if input("Szeretnél profi lenni:").upper()=="YES" else False

print(f"My character {age} (years) in {days} (days) old. His/her name is {name} and he/she has {python_experinece} years experience. ")
print("He/she wants to be a Python developer!" if is_professional else "He/she  dont wants to be a Python developer!")

