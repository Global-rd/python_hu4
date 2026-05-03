"""
Feladatkezelő alkalmazás amellyel egy teendő listát lehet karbantartani, és text fájlba menteni.

"""
from pathlib import Path
import logging

# Globális változók beállítása
hw04_path = Path("homeworks") / "szokesandor"/ "hw_04_exceptions_logging" # A házi feladat mappa elérési útja. Ide kerül a log fájl és a txt fájl
log_file_name = "app.log"                                                 # Log fájl megnevezése
to_do_list_file_name = "to_do_list.txt"                                   # Feladat lista fájl
menu_list = ("Add Task", "View Tasks", "Remove Task", "Exit")             # Ezek a menük jelennek meg

# Formatter, handler és logger beállítása és egymáshoz rendelése

# Formatter létrehozása
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Handler a log fájlhoz
file_handler = logging.FileHandler(hw04_path / log_file_name, encoding="utf-8") # Az encoding="utf-8" argument nélkül, ha magyar ékezetes szavakat adtam meg, akkor ákombákomok kerültek a log fájlba.
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

# Handler a log bejegyzés konzolon való megjelenítéséhez
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

# Logger létrehozása, handler-ek hozzárendelése
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

# --------------------------------------------------------------------------------------------------
#
# Függvények
#
# --------------------------------------------------------------------------------------------------

# Egy feladat hozzáadása a listához
def add_task(task_list, task):
    """
    Adding a task to the task list
    """
    if task in task_list:
        # Ha a feladat már szerepel a listában, akkor egy warning kerül a log-ba
        logger.warning(f"{task} task is already in the list. No new task added.")
    else:
        # Ha a feladatot még nem tartalmazza a lista, akkor hozzáadjuk, és egy info-t loggolunk.
        task_list.append(task)
        logger.info(f"New task added to the list: {task}")

# Egy feladat törlése a listából
def remove_task(task_list, task):
    """
    Removing a task from the task list
    """
    if task in task_list:
        # Ha a feladatot tartalmazza a lista, akkor eltávolítjuk, és egy info-t loggolunk.
        task_list.remove(task)
        logger.info(f"Task removed from the list: {task}")
    else:
        # Ha a feladat nem szerepel a listában, akkor egy warning kerül a log-ba
        logger.warning(f"{task} task is not in the list. No task removed.")

# A lista tartalmának megjelenítése a konzolon
def display_all_tasks(task_list):
    """
    Displays all tasks
    """
    logger.info("Displaying all tasks") # Egy info bejegyzése a logba, amely a lista megjelenítésének tényét rögzíti (a konkrét tartalmat nem).
    print()
    if task_list:
        print("Tasks to be accomplished:")
        for task in task_list:
            print(f" - {task}")
    else:
        print("The tasks list is empty!") # Ha nincsenek feladatok a listában, akkor más felirat jelenik meg.

# A lista tartalmának text fájlba mentése
def save_tasks(task_list):
    """
    Writting all tasks to the to_do_list file
    """
    logger.info(f"Saving tasks to file: {to_do_list_file_name}") # Loggoljuk a tényt és a fájl nevét.
    try:
        with open(hw04_path / to_do_list_file_name, "w", encoding="utf-8") as file:    # Az encoding="utf-8" itt is szükséges, mert egyébként a magyar ékezetes karakterek nem megfelelő kódolással kerülnek a fájlba.
            for task in task_list:
                file.write(f"{task}\n")  #Egy sor, egy feladat
    except Exception as e:
        logger.error(f"Error occurred while saving tasks: {e}")  # Ha a fájl megnyitása és az adatok mentése során hiba lép fel, akkor azt a log-ba írjuk.

# A lista text fájlból való betöltése
def load_tasks(task_list):
    """
    Reading tasks from to_do_list file
    """
    logger.info(f"Loading tasks from file: {to_do_list_file_name}") # Loggoljuk a tényt és a fájl nevét.
    try:
        task_list.clear()
        with open(hw04_path / to_do_list_file_name, "r", encoding='utf-8') as file:
            for line in file.readlines():
                task = line.strip()
                # Az üres sorokat kihagyjuk, és ha egy sor csak szóközöket tartalmaz, akkor az sem kerül be a listába
                if len(task):            
                    task_list.append(task)  
    except FileNotFoundError:
        pass # Ha a txt fájl még nem letezik, akkor nincs teendő. A task_list üres marad, és a txt fájl a kilépéskor lefutó mentéskor létre fog jönni.
    except Exception as e:
        logger.error(f"Error occurred while reading tasks: {e}") # Ha a fájl megnyitása és a feladatok beolvasása során hiba lép fel, akkor azt a log-ba írjuk.
    # A beolvasott feladatok számának log-ba írása
    if task_list:
        logger.info(f"{len(task_list)} task(s) read.")
    else:
        logger.info(f"The {to_do_list_file_name} file is empty or does not exist! No task is read.") # Ha nincsenek beolvasott (nem üres) feladatok, akkor más felirat jelenik meg.

# A konzolon megjeleníti a sorszámmal ellátott menüt
def display_menu():
    """
    Displays a menu on the console
    """
    print()
    for id, menu_item in enumerate(menu_list, 1):
        print(f"{id}. {menu_item}")

# A felhasználó megadja, hogy a menü melyik pontját szeretné végrehajtani.
# Az 1 ... 4 számok mellett a 0 -át is megadhatja, amellyel kérheti a menü ismételt megjelenítését, ha nem lenne látható vagy már elfelejtette volna a pontokat.
def choose_menu():
    """
    Retrieves the menu item selected by the user
    """
    menu_number_list = range(len(menu_list) + 1)
    while True:  # A ciklus addig fut, amíg 0-tól 4-ig eső számot meg nem ad.
        print()
        try:
            menu_number = int(input("Enter the number of the selected menuitem (or enter 0 to show the menu): "))
        except ValueError:
            # Ha nem számot adtak meg, akkor az exception-t lekezeljük, és újra kezdődik a ciklus
            menu_number = None
        if menu_number in menu_number_list:
            # Ha 0-tól 4ig tejedő számot adtak meg, akkor minden frankó, így visszatérünk.
            return menu_number
        else:
            # Ha nem szám vagy nem megfelelő érték érkezett, akkor hibaüzenet jelenik meg.
            print("Invalid input!")

# Ha az 1. vagy 3. menüpontot választották, akkor egy feladat megnevezésre is szükségünk van. A feladatot ez a függvény kéri be.
def read_task(goal):
    """
    Retrieves a task string from the console
    """
    while True: # Addig kéregeti a felhasználót, ameddig nullánál hosszabb szöveget meg nem ad.
        print()
        task = input(f"Enter the task to {goal} (or enter 0 to go back): ").strip().lower()
        # Ha a kezdő és záró szóközök eltávolítása után nullánál hosszabb string érkezett, akkor rendben vagyunk, és visszatérünk
        if len(task):
            print()  
            return task

# Fő belépési pont
def main():
    """
    Main function of the program
    """
    logger.info("Program started.") # Log-ba írjuk a kezdés időpontját
    tasks = []  # Ez a változó tárolja a feladatok listáját
    load_tasks(tasks) # Feladatok betöltése txt fájlból

    # Fő ciklus, ami addig fut amíg a "4. Exit" menüpontot nem választják
    display_menu()
    while True:
        menu_to_execute = choose_menu()
        if menu_to_execute == 0:
            display_menu()
        elif menu_to_execute == 1:
            task = read_task("add")
            if task != "0":
                add_task(tasks, task)
        elif menu_to_execute == 2:
            display_all_tasks(tasks)
        elif menu_to_execute == 3:
            task = read_task("remove")
            if task != "0":
                remove_task(tasks, task)
        elif menu_to_execute == 4:
            print()
            break
    # 4. menüpontot választották, a ciklus megszakítva
    save_tasks(tasks) # Feladatlista mentése txt fájlba
    logger.info("Program successfully ended.") # Log-ba írjuk a befejezés időpontját

# --------------------------------------------------------------------------------------------------
#
# Modul
#
# --------------------------------------------------------------------------------------------------

main()
