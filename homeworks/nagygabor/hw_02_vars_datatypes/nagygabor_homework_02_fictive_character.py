#----- FICTIVE CHARACTER -------

# INPUT BEKÉRÉS
name = input("Add meg a neved").strip().title()
age = int(input("Hány éves vagy?"))
python_exp = input('Hány év python tapasztalatod van?')

#ÉLETKOR NAPOKBAN
age_in_days = age * 365 

#EXTRA: SZERETNE PYTHON FEJLESZTŐ LENNI?
want_dev = input("Szeretnél python fejlesztő lenni? (yes/no):")

#TERNARY OPERATOR 
dev_status = "Akar python fejlesztő lenni!" if want_dev == 'yes' else "Nem akar python fejlesztő lenni!"

#KIÍRÁS
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp} years experience. {dev_status}") 