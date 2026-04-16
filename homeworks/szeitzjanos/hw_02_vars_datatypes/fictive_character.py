'''
Megjegyzés:
A program feltételezi (egyelőre), hogy a válaszok értelmes lénytől érkeznek....

Feladat 1:
Változók, user input, string metódusok, type conversion, f-string
használata

Hozz létre egy fictive_character.py file-t, és kódold le a következő feladat
megoldását:

Ebben a feladatban egy képzeletbeli karaktert fogsz létrehozni (mintázhatod
nyugodtan magadról is :)). A feladatod, hogy a felhasználótól bekérd a
következő input-okat (ezeknek megfelelő, leíró változóneveket adj):

        Név
        Életkor
        Python tapasztalat években

A tanultak alapján kódold le, hogy a beírt név minden esetben nagy betűvel
legyen eltárolva a változóban, és szóköz se előtte, se utána ne szerepeljen.

Az életkort konvertáld át a megfelelő adattípusra, és egy új változóban tárold
el hogy mennyi idős a karakter napokban (Kerekíts az években megadott
életkor alapján, tételezzük fel hogy ma van az illető szülinapja).
Printeld ki az összes információt egy interpolált string-ben (f-string). A
végeredmény valami ilyesmi kell hogy legyen: "My character is
<age_in_days> old. His/her name is <name> and he/she has
<python_exp_in_years> years experience."

Extra feladat (szorgalmi):
Kérd be inputként a felhasználótól, hogy szeretné-e hogy a karaktere profi
Python fejlesztő legyen. Erre a válasz "yes" vagy "no" kell hogy legyen (az
inputok validálást később tanuljuk). Nézz utána a ternary operator-oknak
Python-ban, és ezek használatával oldd meg a feladatot. Ezután add hozzá a
végső kiprintelendő f-string-hez. A végeredménynek ekkor így kell kinéznie:

"My character is <age_in_days> old. His/her name is <name> and he/she has
<python_exp_in_years> years experience. He/she wants to be a Python developer!"

Vagy

"My character is <age_in_days> old. His/her name is <name> and he/she has
<python_exp_in_years> years experience. He/she does not want to be a Python
developer!"

    fictive_character.py        - pass
    input data                  - pass
        naming conventions      - pass
    calculation                 - pass
    print string                - pass

    *** EXTRA ***
    evaluating the condition    - pass
    print string                - pass

'''

'''
*** Python-ban nincs szükség arra, hogy létrehozd a változókat egy
    kezdeti értékkel. Elég, ha ahol az input()-ot kéred be, ott
    létrejön a user_name változó. Ha szeretnél type annotation-öket
    használni, ott is megteheted, így egyszerűsödik a kódod. Igaz ez
    minden ilyen előre létrehozott változóra, ezeket töröld kérlek.

# VARIABLE DEFINITION
user_name: str = ''
user_age: int = 0
user_age_in_days: int = 0
user_python_experience_in_years: int = 0
is_user_to_be_prof: str = ''
'''

# INPUT DATAS
user_name: str = input('Could you give me your name, please: ').upper().strip()
user_age: int = int(input('Could you give me your age, please: '))
user_python_experience_in_years: int = \
    int(input('Could you give me your Python experience in years, please: '))
is_user_to_be_prof: str = \
    input('Would you like to be a professional Python developer? (yes/no) ')

# THE CALCULATION ALSO ACCOUNTS FOR LEAP YEARS
user_age_in_days: int = int(user_age * 365.25)

# PRINTING THE RESULT
print(f'\nMy character is {user_age_in_days} days old. His/her name is'
      f' {user_name} and he/she has {user_python_experience_in_years}'
      f' years experience.', end=' ')

# EVALUATING THE CONDITION AND PRINTING THE FINAL RESULT
'''
*** szuper a megoldásod, de ha megnézed akkor a két lehetséges kimenetel között
    egy apró különbség van csak:

        wants - does not want.

    létrehozhatnál egy változót
    így nem ismétled a mondat nagy részét kétszer (DRY = don't repeat yourself,
    erről nemsokára tanulunk), és a ternary operator-os kifejezésed is kifér
    egy sorra, ami elegánsabb python-os megoldást eredményez.

print('He/she wants to be a Python developer!') \
    if is_user_to_be_prof == 'yes' \
    else print('He/she does not want to be a Python developer!')
'''
modify: str = 'wants' if is_user_to_be_prof == 'yes' else 'does not want'
print(f'He/she {modify} to be a Python developer!')
