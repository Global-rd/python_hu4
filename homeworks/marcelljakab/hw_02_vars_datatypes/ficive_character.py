# Feladat 1: Ficitve character

name = input("Mi a karakter neve? ")
age = input("Hány éves a karakter? ")
python_exp = input("Hány év Python tapasztalata van? ")

# Név: első betű nagy, szóköz eltávolítása
name = name.strip().title()

#Életkor napokra átszámítása
age_in_days = int(age) * 365

#Eredmény kiírása f-string-gel
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp} years experience.")



