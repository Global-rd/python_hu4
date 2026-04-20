"""
Egy fiktív karakter adtainak bekérése,
azok eltárolása egy-egy változóban, majd
minden ilyen adat kiprintelése
"""
#Személyes adatok bekérése
print("Enter your pesonal details:")
name = input("- name : ").upper().strip()           #név bekérése, nagy betűssé alakítása, majd szóköz levágása
age_in_years = int(input("- age in years: "))       #életkör bekérése egész számokban
python_exp_in_years = int(input(" - Python experience in years: "))     #python tapasztalat bekérése években

#Szeretne-e profi Python fejlesztő lenni
python_pro = input("Would you like to become a professional Python developer? (yes/no)") .lower().strip()

#Napokban kifejezett életkor kiszámítása
age_in_days = age_in_years * 365

#Adatok kiprintelése f-string és ternary operatorok használatával

print("----")
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience ")
print("He/she wants to be a professional Python developer!" 
      if python_pro == "yes"
        else " He/she does not want to be a Python developer! ")
