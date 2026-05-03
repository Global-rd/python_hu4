import logging

# Logging beállítása 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("to_do.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

FILE_NAME = "tasks.txt"


def read_tasks():
    """Beolvassa a feladatokat a file-ból egy listába."""
    tasks = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        logging.info(f"Sikeres beolvasás: {len(tasks)} feladat a {FILE_NAME} file-ból.")
    except FileNotFoundError:
        logging.warning(f"A {FILE_NAME} nem található, üres listával indul a program.")
    except PermissionError:
        logging.error(f"Nincs jogosultság a {FILE_NAME} olvasásához.")
    except Exception as e:
        logging.error(f"Ismeretlen hiba olvasáskor: {e}")
    return tasks


def write_tasks(tasks):
    """Felülírja a file tartalmát az aktuális feladatlistával."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        logging.info(f"Sikeres írás: {len(tasks)} feladat mentve a {FILE_NAME} file-ba.")
    except PermissionError:
        logging.error(f"Nincs jogosultság a {FILE_NAME} írásához.")
    except Exception as e:
        logging.error(f"Ismeretlen hiba íráskor: {e}")


def view_tasks(tasks):
    """Megjeleníti az összes feladatot számozva."""
    if not tasks:
        print("Nincsenek feladatok a listában.")
        logging.info("View Tasks meghívva - a lista üres.")
        return
    print("\n--- Feladatok ---")
    for id, task in enumerate(tasks, 1):
        print(f"{id}. {task}")
    print("-----------------")
    logging.info(f"View Tasks meghívva - {len(tasks)} feladat kiírva.")


def add_task(tasks, task):
    """Hozzáad egy új feladatot a listához (memóriában)."""
    tasks.append(task)
    logging.info(f"Feladat hozzáadva: '{task}'")
    print(f"'{task}' feladat hozzáadva.")


def remove_task(tasks, task_id):
    """Töröl egy feladatot ID alapján (1-től indexelve)."""
    try:
        task_id = int(task_id)
        if 1 <= task_id <= len(tasks):
            removed = tasks.pop(task_id - 1)
            logging.info(f"Feladat törölve: '{removed}'")
            print(f"'{removed}' feladat törölve.")
        else:
            print(f"Érvénytelen ID! 1 és {len(tasks)} között kell legyen.")
            logging.warning(f"Érvénytelen task_id: {task_id}")
    except ValueError:
        print("Az ID-nek számnak kell lennie!")
        logging.error(f"ValueError a törlésnél, input: '{task_id}'")


def display_menu():
    """Kiprinteli a menüpontokat."""
    print("\n=== Feladatkezelő ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    # Programindításkor automatikus beolvasás file-ból
    tasks = read_tasks()

    while True:
        display_menu()
        choice = input("Válassz egy opciót (1-4): ").strip()

        if choice == "1":
            new_task = input("Add meg az új feladatot: ").strip()
            if new_task:
                add_task(tasks, new_task)
            else:
                print("Üres feladatot nem lehet hozzáadni!")
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                task_id = input("Add meg a törlendő feladat ID-jét: ").strip()
                remove_task(tasks, task_id)
        elif choice == "4":
            # Csak kilépéskor írjuk vissza a file-ba
            write_tasks(tasks)
            print("Viszlát!")
            logging.info("Program leállítva.")
            break
        else:
            print("Érvénytelen opció! 1, 2, 3 vagy 4 kell legyen.")
            logging.warning(f"Érvénytelen menüopció: '{choice}'")


if __name__ == "__main__":
    main()