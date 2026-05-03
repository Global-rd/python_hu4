from pathlib import Path
import logging

#logging module
BASE_DIR = Path(__file__).parent
log_path = BASE_DIR / "program.log"

file_handler = logging.FileHandler(log_path)
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG)

#a PATH változóval a lista.txt elérési útvonala
file_path = Path("to_do_list.txt") 

#1. függvény a lista olvasásához
def task_reading():
    try:
        with open(file_path, "r") as file:   
            lines = file.readlines()
            new_lines = []
            for line in lines:
                new_lines.append(line.strip()) 
        return new_lines
    except FileNotFoundError as e:
        logging.warning(f"A fájl még nem létezett, ezért létrehozva: {e}")
        with open(file_path, "w") as file:
            pass
        return []  
    
#a new_lines változó definiálása a tas_reading függvénnyel
new_lines = task_reading() 

#2. függvény a fájlba íráshoz
def task_writing(new_lines):
    try: 
        with open(file_path, "w") as file:
            for line in new_lines:
               file.write(line + "\n")
    except OSError as e: 
        logging.error(f"A lemez megtelt: {e}")

#3. függvény a lista megjelenítéséhez
def task_display(new_lines): 
    for line in new_lines:
            print(line)
            print("---------------")

#4. függvény 1 feladat hozzáadásához
def task_add(new_lines, new_task):
    new_lines.append(new_task.strip())

#5. függvény 1 feladat törléséhez
def task_remove(new_lines, del_task):
    new_lines.remove(del_task)

#opciók kiprintelése
def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

#feladat kiválasztása és annak végrehajtása függvényekkel
while True:
    display_menu()
    answer = input("Add meg a feladat számát, pont nélkül: ")
    if answer not in ["1","2","3","4"]:
       print("Érvénytelen szám. Válassz újra!")
       continue
    else:
        answer = int(answer)
    if answer == 1:
        new_task = input("Add meg az új feladatot: ")
        task_add(new_lines, new_task)
    elif answer == 2:
        task_display(new_lines)
    elif answer == 3:
        del_task = input("Melyik feladatot akarod törölni? ")
        task_remove(new_lines, del_task) 
    elif answer == 4:
        task_writing(new_lines)
        break