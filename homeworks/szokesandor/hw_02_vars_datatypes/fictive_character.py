"""
Egy képzeletbeli személy adatainak bekérése,
a személy adatainak eltárolása egy-egy változóban,
műveletek végrehajtása, majd az összes információ 
kiprintelése.
"""

# Személys adatok bekérése
print("Enter your personal details:")
name = input(" - name: ").upper().strip()                           # név bekérése, nagy betűre alakítása, megelőző és követő szóközök levágása
age_in_years = int(input(" - age in years: "))                      # életkor bekérése és egész számmá alakítása 
python_exp_in_years = int(input(" - Phyton experience in years: ")) # Python tapasztalat bekérése és egész számmá alakítása

# Szeretne-e profi Phyton-os fickóvá válni?
phyton_pro = input("Would you like to become a professional Python developer? (yes/no) ").lower().strip()  # a felhasználó által megadott szöveget kis betűre alakítjuk és a megelőző és követő szóközöket levágjuk

# Napokban kifejezett életkor kiszámítása (A szökőéveket elhanyagoljuk.)
age_in_days = age_in_years * 365

# Adatok kiprintelése f-string és ternary operator használatával
print("----")
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")
print("He/she wants to be a professional Python developer!" if phyton_pro=="yes" else "He/she does not want to be a Python developer!")
