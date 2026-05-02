
# A tennivalókat tartalmazó .txt fájl betöltése
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log", mode="a"),
        logging.StreamHandler()
    ]
)
''' logging.basicConfig: alapbeállítás);
level = milyen részletességű logokat alkalmazunk (DEBUG, INFO, WARNING, ERROR, CRITICAL); format: hogyan nézzen ki az üzenet
Ha INFO a beállítás: minden INFO, WARNING, ERROR, CRITICAL átmegy (látni a hibákat is);
fileHandler: log a fájlba; StreamHandler: log a konzolra;
%(asctime)s - időbélyeg,
%(levelname)s → INFO / WARNING / ERROR,
%(message)s → amit a kódoló ír a logba;
mode="a": hozzáfűzés (append), nem pedig törlés'''

def loading_tasks(filename):
    try:
        with open(filename, "r") as user_do:
            tasks_todo = user_do.read().splitlines() # minden listaelem új sorba
        logging.info(f"\nTasks completed successfully: {filename}")    
        return tasks_todo
    except FileNotFoundError:
        # Ha nincs fájl, hozzuk létre üresen
        logging.warning(f"File does not exist; empty file created: {filename}")
        with open(filename, "w") as f:
            pass  # csak létrehozza az üres fájlt
        return [] # üres fájl 
    except Exception as err:
        logging.error(f"\nAn error occurred while reading the file.: {err}")
        return []
    
def query_tasks(tasks_todo):
    if not tasks_todo:
        print("There is no single task.")
    else:
        print("\n--- TASKS TO DO ---")
        for f in tasks_todo:
            print("-", f)        

def add_task(tasks_todo): # Egy új feladat felvétele a listába
    newtask = input("Enter the new task: ")
    tasks_todo.append(newtask)
    print("New task added.")

def delete_task(tasks_todo):
    deltask = input("Which task would you like to delete? : ")
    if deltask in tasks_todo:
        tasks_todo.remove(deltask)
        print("Task deleted.")
    else:
        print("There is no such task in the list..") 

# Kilépéskor a .txt fájl tartalma felülíródik:
def saving_tasks(filename, tasks_todo):
    try:
        with open(filename, "w") as fajl:
            for task in tasks_todo:
                fajl.write(task + "\n")
        logging.info(f"\nTasks saved successfully: {filename}")

    except Exception as err: # Exception: minden általános hibatípus
        logging.error(f"An error occurred while writing the file.: {err}")

# Feladatkezelő display menü
def display_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Add task")
    print("2. Query tasks")
    print("3. Deleting tasks")
    print("4. Exit")

def main():
    filename = "tasks.txt"
    tasks_todo = loading_tasks(filename)

    while True:
        display_menu()
        choice = input("Válassz egy menüpontot (1-4): ")

        if choice == "1":
            add_task(tasks_todo)
        elif choice == "2":
            query_tasks(tasks_todo)
        elif choice == "3":
            delete_task(tasks_todo)
        elif choice == "4":
            print("Saving tasks and exit...")
            saving_tasks(filename, tasks_todo)
            break
        else:
            print("invalid choice (please enter 1/2/3/4): ")

# Program indítása
main()