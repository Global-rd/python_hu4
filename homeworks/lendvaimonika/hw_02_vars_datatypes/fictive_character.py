"""
Változók, user input, string metódusok, type conversion, f-string használata 
egy fiktív karakter esetén

Adatok bekérése: név, kor, Python tapasztalat
"""

name = input("Name: ").upper().strip()
age = int(input("Age: "))
python_exp_in_years = int(input("Python experience in years: "))

#életkor átszámítása napokra
age_in_days = age * 365

#az információk kiírása f-stringben

print(f'My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience')
