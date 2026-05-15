'''
Készíts egy Feladatkezelő alkalmazást!
Definiálj 5 függvényt a következőkre: feladatok olvasása, feladatok írása, feladatok megjelenítése, 
egy feladat hozzáadása, egy feladat törlése
Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges opciókat:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok közül mit szeretne csinálni, 
és hívd meg a válaszhoz megfelelő függvényt.
A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! 
Ha az 1-es vagy 3-as opciót választja, mindkét esetben paramétert kell átadnod a megfelelő függvénynek. 
“Exit”-re lépjen ki a program.
Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd a logging module-t. 
Egyszerre logolj a konzolra és egy .log file-ba. 
A .txt file legyen része a pull request-nek. 
Tipp: A program futása során a feladatokat memóriában (egy listában) tartsd nyilván (itt adj hozzá vagy törölj elemeket a function hívásoknál).
A file-ból való olvasás automatikusan történjen meg a program indulásakor. 
A fájlba írás csak a program befejezésekor (“Exit” opció választásakor) történjen meg, 
ekkor a program írja felül a korábbi feladatlistát a módosított
tartalommal (nem kell minden Add Task vagy Remove Task opciónál módosítani a file-t).
'''


import logging
from pathlib import Path
import sys
import os

# path konkrét beállítása
homeworks_4_path = Path("homeworks") / "szulyovszkypeter"/ "hw_04_exceptions_logging"
#homeworks_4_path = Path("homeworks/szulyovszkypeter/hw_04_exceptions_logging")
#fájl nevek beállítása
log_file = os.path.join(homeworks_4_path, "lista_app.log")
FILE_NAME = os.path.join(homeworks_4_path, "feladat_lista.txt")

# Logging beállítása: konzolra és fájlba is naplózunk
logger = logging.getLogger("TaskManagerLogger")
logger.setLevel(logging.INFO)

# Formázó létrehozása
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Fájlba író handler
#file_handler = logging.FileHandler(homeworks_4_path /'lista_app.log', encoding='utf-8')
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setFormatter(formatter)

# Konzolra író handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Handlerek hozzáadása a loggerhez
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#FILE_NAME = "Feladat_lista.txt"

def read_tasks():
    """Beolvassa a feladatokat a fájlból a program indulásakor."""
    tasks = []
    try:
        #with open(homeworks_4_path / FILE_NAME, "r", encoding="utf-8") as f:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
        logger.info(f"Sikeres beolvasás: {len(tasks)} feladat betöltve.")
    except FileNotFoundError:
        logger.warning(f"A(z) {FILE_NAME} még nem létezik. Új lista indul.")
    except Exception as e:
        logger.error(f"Hiba történt a beolvasáskor: {e}")
    return tasks

def write_tasks(tasks):
    """Kiírja a feladatokat a fájlba, felülírva a régit."""
    try:
        #with open(homeworks_4_path / FILE_NAME, "w", encoding="utf-8") as f:
        with open(FILE_NAME, "w", encoding="utf-8") as f:    
            for task in tasks:
                f.write(f"{task}\n")
        logger.info("Feladatok sikeresen mentve a fájlba.")
    except Exception as e:
        logger.error(f"Hiba történt a mentéskor: {e}")

def display_menu():
    """Megjeleníti a menüopciókat."""
    print("\n--- FELADATKEZELŐ MENÜ ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("--------------------------")

def view_tasks(tasks):
    """Megjeleníti a memóriában lévő feladatokat."""
    if not tasks:
        print("\nA feladatlista jelenleg üres.")
    else:
        print("\nAktuális feladatok:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks, task_name):
    """Új feladatot ad a listához (csak memóriában)."""
    if task_name.strip():
        tasks.append(task_name.strip())
        logger.info(f"Feladat hozzáadva: '{task_name}'")
    else:
        print("Hiba: A feladat neve nem lehet üres!")

def remove_task(tasks, task_index):
    """Eltávolít egy feladatot index alapján (csak memóriában)."""
    try:
        index = int(task_index) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            logger.info(f"Feladat eltávolítva: '{removed}'")
        else:
            print("Hiba: Nincs ilyen sorszámú feladat!")
            logger.warning(f"Sikertelen törlési kísérlet (érvénytelen index: {task_index})")
    except ValueError:
        print("Hiba: Kérlek számot adj meg a törléshez!")
        logger.error("A felhasználó nem számot adott meg a törlésnél.")

def main():
    # 1. Beolvasás indításkor
    task_list = read_tasks()
    
    while True:
        display_menu()
        choice = input("Válasz egy opciót (1-4): ")

        if choice == '1':
            new_task = input("Add meg az új feladatot: ")
            add_task(task_list, new_task) # Paraméter átadás
            
        elif choice == '2':
            view_tasks(task_list)
            
        elif choice == '3':
            view_tasks(task_list)
            if task_list:
                idx = input("Melyik feladatot töröljem? (szám): ")
                remove_task(task_list, idx) # Paraméter átadás
                print("Frissített feladatlista:")
                view_tasks(task_list)            
        elif choice == '4':
            # 2. Mentés kilépéskor
            write_tasks(task_list)
            logger.info("A program leállt.")
            print("Kilépés... Szép napot!")
            break
        else:
            print("Érvénytelen választás! Kérlek 1, 2, 3 vagy 4-et üss be.")
            logger.warning(f"Érvénytelen menüpont: {choice}")

if __name__ == "__main__":
    main()