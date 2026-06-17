import json
import logging
from pathlib import Path

# Logging beállítás
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler
log_file = Path(__file__).parent / "task_manager.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Logger-hez handlerek hozzáadása
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Globális task lista
tasks = []
TASKS_FILE = Path(__file__).parent / "tasks.txt"


def read_tasks():
    """Feladatok beolvasása a file-ból."""
    global tasks
    try:
        if TASKS_FILE.exists():
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    tasks = json.loads(content)
                    logger.info(f"Feladatok sikeresen beolvasva. Feladatok száma: {len(tasks)}")
                else:
                    tasks = []
                    logger.info("A tasks file üres, üres lista inicializálva.")
        else:
            tasks = []
            logger.info("Tasks file nem létezik, üres lista inicializálva.")
    except json.JSONDecodeError as e:
        logger.error(f"JSON dekódolási hiba a tasks file-ból: {e}")
        tasks = []
    except IOError as e:
        logger.error(f"File olvasási hiba: {e}")
        tasks = []


def write_tasks():
    """Feladatok írása a file-ba."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
        logger.info(f"Feladatok sikeresen mentve. Feladatok száma: {len(tasks)}")
    except IOError as e:
        logger.error(f"File írási hiba: {e}")


def display_tasks():
    """Feladatok megjelenítése."""
    if not tasks:
        logger.info("Nincsenek feladatok a listában.")
        print("\n Nincsenek feladatok a listában.\n")
    else:
        print("\n A feladatok listája:")
        print("-" * 50)
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print("-" * 50 + "\n")
        logger.info(f"Feladatok megjeleníve. Összes feladat: {len(tasks)}")


def add_task(task_name):
    """Egy feladat hozzáadása a listához."""
    if not task_name.strip():
        logger.warning("Üres feladat nem adható hozzá.")
        print("  A feladat nem lehet üres!\n")
        return
    
    tasks.append(task_name)
    logger.info(f"Feladat hozzáadva: '{task_name}'")
    print(f" Feladat hozzáadva: '{task_name}'\n")


def remove_task(task_index):
    """Egy feladat törlése a listából."""
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            logger.info(f"Feladat törölve: '{removed_task}'")
            print(f" Feladat törölve: '{removed_task}'\n")
        else:
            logger.warning(f"Érvénytelen feladat index: {task_index}")
            print(f"  Érvénytelen feladat index! Kérlek, válassz 1 és {len(tasks)} közül.\n")
    except ValueError:
        logger.error("A feladat index nem számérték.")
        print("  A feladat index szám kell, hogy legyen!\n")


def display_menu():
    """A menü opcióinak megjelenítése."""
    print("\n" + "=" * 50)
    print(" FELADATKEZELŐ ALKALMAZÁS ")
    print("=" * 50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("=" * 50 + "\n")


def main():
    """A főprogram."""
    logger.info("Feladatkezelő alkalmazás elindítva.")
    
    # Feladatok beolvasása az induláskor
    read_tasks()
    
    while True:
        display_menu()
        user_input = input("Kérlek, válassz egy opciót (1-4): ").strip()
        
        if user_input == "1":
            # Add Task
            task_name = input("Add meg az új feladatot: ").strip()
            add_task(task_name)
        
        elif user_input == "2":
            # View Tasks
            display_tasks()
        
        elif user_input == "3":
            # Remove Task
            display_tasks()
            if tasks:
                task_index = input("Add meg a törlendő feladat sorszámát: ").strip()
                remove_task(task_index)
        
        elif user_input == "4":
            # Exit
            logger.info("Feladatok mentése és program bezárása...")
            write_tasks()
            logger.info("Feladatkezelő alkalmazás leállítva.")
            print("\nViszlát!\n")
            break
        
        else:
            logger.warning(f"Érvénytelen opció: '{user_input}'")
            print("Érvénytelen opció! Kérlek, válassz 1, 2, 3 vagy 4 közül.\n")


if __name__ == "__main__":
    main()
