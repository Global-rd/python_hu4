import logging
import sys

logger = logging.getLogger("ToDoApp")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Fájl handler (todo_app.log fájlba ír)
file_handler = logging.FileHandler('todo_app.log', encoding='utf-8')
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# --- 2. GLOBÁLIS VÁLTOZÓK ---
tasks = []
FILENAME = "tasks.txt"

# --- 3. FÜGGVÉNYEK DEFINIÁLÁSA ---

def load_tasks():
    """1. függvény: Feladatok olvasása a fájlból"""
    global tasks
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
        logger.info(f"Sikeres betöltés: {len(tasks)} feladat beolvasva.")
    except FileNotFoundError:
        logger.warning("A feladatfájl még nem létezik. Új lista indul.")
    except Exception as e:
        logger.error(f"Hiba történt a fájl olvasásakor: {e}")

def save_tasks(task_list):
    """2. függvény: Feladatok írása (mentés a program végén)"""
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            for task in task_list:
                f.write(task + "\n")
        logger.info("Adatok sikeresen mentve a fájlba.")
    except Exception as e:
        logger.error(f"Hiba történt a fájlba íráskor: {e}")

def show_tasks():
    """3. függvény: Feladatok megjelenítése"""
    print("\n" + "="*20)
    if not tasks:
        print("A feladatlista jelenleg üres.")
    else:
        print("AKTUÁLIS FELADATOK:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("="*20)

def add_task(new_task):
    """4. függvény: Egy feladat hozzáadása (paraméterrel)"""
    if new_task:
        tasks.append(new_task)
        logger.info(f"Feladat hozzáadva: {new_task}")
    else:
        print("Hiba: Üres feladat nem adható hozzá!")

def remove_task(index):
    """5. függvény: Egy feladat törlése (paraméterrel)"""
    try:
        removed = tasks.pop(index - 1)
        logger.info(f"Feladat eltávolítva: {removed}")
    except (IndexError, ValueError):
        logger.error(f"Sikertelen törlés. Érvénytelen index: {index}")
        print("Error: No task with this number exists.!")

def display_menu():
    """Bonus function: Display menu"""
    print("\n--- MENÜ ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    load_tasks()  
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            task_name = input("Enter the new task: ")
            add_task(task_name)
            
        elif choice == '2':
            show_tasks()
            
        elif choice == '3':
            show_tasks()
            if tasks:
                try:
                    idx = int(input("Enter the number of the task you want to delete.: "))
                    remove_task(idx)
                except ValueError:
                    print("Error: Please enter a number!")
            
        elif choice == '4':
            save_tasks(tasks) 
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()