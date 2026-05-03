import logging

# Logging beállítása - konzolra és fájlba egyszerre
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Konzol handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Fájl handler
file_handler = logging.FileHandler("to_do.log")
file_handler.setLevel(logging.DEBUG)

# Formátum
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Feladatok listája memóriában
tasks = []

# 1. Feladatok olvasása fájlból
def read_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        logger.info("Feladatok sikeresen betöltve.")
    except FileNotFoundError:
        logger.warning("A tasks.txt fájl nem található. Üres listával indulunk.")
    except Exception as e:
        logger.error(f"Hiba a fájl olvasásakor: {e}")

# 2. Feladatok írása fájlba
def write_tasks():
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info("Feladatok sikeresen mentve.")
    except Exception as e:
        logger.error(f"Hiba a fájl írásakor: {e}")

# 3. Feladatok megjelenítése
def display_tasks():
    if not tasks:
        print("Nincs feladat a listában!")
        logger.info("Feladatlista üres.")
    else:
        print("\n--- Feladatok ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        logger.info(f"{len(tasks)} feladat megjelenítve.")

# 4. Feladat hozzáadása
def add_task(task):
    tasks.append(task)
    print(f"'{task}' hozzáadva!")
    logger.info(f"Új feladat hozzáadva: {task}")

# 5. Feladat törlése
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"'{task}' törölve!")
        logger.info(f"Feladat törölve: {task}")
    else:
        print(f"'{task}' nem található a listában!")
        logger.warning(f"Nem található feladat: {task}")

# 6. Menü megjelenítése
def display_menu():
    print("\n--- Feladatkezelő ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Program indítása
read_tasks()

while True:
    display_menu()
    choice = input("\nVálassz (1-4): ").strip()

    if choice == "1":
        task = input("Írd be az új feladatot: ").strip()
        add_task(task)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        task = input("Írd be a törlendő feladatot: ").strip()
        remove_task(task)
    elif choice == "4":
        write_tasks()
        print("Viszlát!")
        logger.info("Program leállítva.")
        break
    else:
        print("Hibás választás! Csak 1, 2, 3 vagy 4 lehet!")
        logger.warning(f"Érvénytelen menüpont: {choice}")