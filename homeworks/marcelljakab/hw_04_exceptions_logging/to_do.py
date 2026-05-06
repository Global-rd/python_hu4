import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("to_do.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_tasks():
    tasks = []
    try:
        with open("to_do.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                clean_line = line.strip()
                if clean_line:
                    tasks.append(clean_line)
        logger.info(f"{len(tasks)} feladat beolvasva.")
    except FileNotFoundError:
        logger.warning("to_do.txt nem talalhato. Ures listaval indulunk.")
    except Exception as e:
        logger.error(f"Hiba olvasaskor: {e}")
    return tasks


def write_tasks(tasks):
    try:
        with open("to_do.txt", "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info(f"{len(tasks)} feladat kiirva.")
    except Exception as e:
        logger.error(f"Hiba iraskor: {e}")


def display_tasks(tasks):
    if not tasks:
        print("Nincs meg feladat a listaban.")
        return
    print("\n--- Feladatok ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("-----------------\n")


def add_task(tasks, new_task):
    tasks.append(new_task)
    logger.info(f"Hozzaadva: '{new_task}'")
    print(f"'{new_task}' hozzaadva!")


def remove_task(tasks, task_to_remove):
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        logger.info(f"Torolve: '{task_to_remove}'")
        print(f"'{task_to_remove}' torolve!")
    else:
        logger.warning(f"Nem talalhato: '{task_to_remove}'")
        print(f"'{task_to_remove}' nincs a listaban.")


def display_menu():
    print("\n=== TO-DO MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    logger.info("Alkalmazas elindult.")
    tasks = read_tasks()

    while True:
        display_menu()
        choice = input("Valassz egy opciot (1-4): ").strip()

        if choice not in ["1", "2", "3", "4"]:
            print("Ervenytelen valasztas! Csak 1, 2, 3 vagy 4 lehet.")
            logger.warning(f"Ervenytelen valasztas: '{choice}'")
            continue

        if choice == "1":
            new_task = input("Add meg az uj feladatot: ").strip()
            if new_task:
                add_task(tasks, new_task)
            else:
                print("Ures feladat nem adhato hozza.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            task_to_remove = input("Add meg pontosan a torlendo feladatot: ").strip()
            remove_task(tasks, task_to_remove)

        elif choice == "4":
            write_tasks(tasks)
            logger.info("Alkalmazas kilep.")
            print("Viszlat!")
            break


if __name__ == "__main__":
    main()
    