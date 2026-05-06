import logging

# A logging modul beallitasa
# basicConfig-gal egyszerre tudunk konzolra es fajlba is logolni
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG szinttol logoljon mindent
    format="%(asctime)s - %(levelname)s - %(message)s",  # log uzenetek formatuma
    handlers=[
        logging.FileHandler("to_do.log"),  # fajlba iras
        logging.StreamHandler()            # konzolra iras
    ]
)

# Ez a lista tarolja a feladatokat a program futasa kozben (memoria)
# Indulaskor ures, majd read_tasks() feltolti a fajlbol
tasks = []


# --- FUGGVENYEK DEFINIALASA ---
# A fuggvenyeket elobb kell definialani, mint ahogy meghivjuk oket!
# Ezert kerulnek a kod elejere, a fo program logika a2
# vege fele lesz.


# Ez a fuggveny beolvassa a feladatokat a tasks.txt fajlbol
# es beleteszi a tasks listaba
# Automatikusan lefut a program indulasakor
def read_tasks():
    try:
        file = open("tasks.txt", "r")  # fajl megnyitasa olvasasra
        for line in file:
            tasks.append(line.strip())  # strip() levagja a sorvegi \n karaktert
        file.close()
        logging.info("Feladatok beolvasva")
    except:
        # Ha a fajl meg nem letezik (pl. elso inditas), nem gond, csak logoljuk
        logging.warning("Nem sikerult beolvasni a fajlt, vagy meg nem letezik")


# Ez a fuggveny kiirja a tasks lista tartalmat a tasks.txt fajlba
# Csak akkor hivodik meg, amikor a felhasznalo az "Exit" opciоt valasztja
def write_tasks():
    try:
        file = open("tasks.txt", "w")  # "w" mod: felulirja a fajl tartalmat
        for task in tasks:
            file.write(task + "\n")  # minden feladat uj sorba kerul
        file.close()
        logging.info("Feladatok elmentve")
    except:
        logging.error("Nem sikerult elmenteni a fajlt")


# Ez a fuggveny kiirja a konzolra a tasks lista aktualis tartalmat
# Ha ures a lista, azt is jelzi
def display_tasks():
    if len(tasks) == 0:
        print("Nincsenek feladatok")
    else:
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])  # sorszammal egyutt irja ki


# Ez a fuggveny hozzaad egy uj feladatot a tasks listahoz
# A "task" parameter az add_task() hivas soran kap erteket
def add_task(task):
    tasks.append(task)  # lista vegere fűzi az uj feladatot
    logging.info("Feladat hozzaadva: " + task)


# Ez a fuggveny kitorli a megadott feladatot a tasks listabol
# A "task" parameter az remove_task() hivas soran kap erteket
def remove_task(task):
    if task in tasks:  # ellenorzi, hogy benne van-e egyaltalan a listaban
        tasks.remove(task)
        logging.info("Feladat torolve: " + task)
    else:
        print("Nincs ilyen feladat")
        logging.warning("Nem talalhato feladat: " + task)


# Ez a fuggveny csak kiirja a menu opcioikat a konzolra
def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


# --- FO PROGRAM ---

# Eloszor beolvassuk a fajlbol a korabbi feladatokat (ha van)
read_tasks()

# Vegtelen ciklus: addig fut, amig a felhasznalo ki nem lep (4. opcio)
while True:

    # Minden kor elején kiirjuk a menüt
    display_menu()
    choice = input("Valasszon: ")

    # Ellenorizzuk, hogy a felhasznalo 1, 2, 3 vagy 4-et adott-e meg
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Hibas opcio, probalja ujra")
        logging.warning("Hibas menu opcio: " + choice)

    elif choice == "1":
        # Bekerjuk az uj feladat nevet, majd meghivjuk az add_task() fuggvenyt
        task = input("Adja meg a feladatot: ")
        add_task(task)

    elif choice == "2":
        # Meghivjuk a display_tasks() fuggvenyt, ami kilistazza a feladatokat
        display_tasks()

    elif choice == "3":
        # Bekerjuk a torlendo feladat nevet, majd meghivjuk a remove_task() fuggvenyt
        task = input("Melyik feladatot szeretne torolni: ")
        remove_task(task)

    elif choice == "4":
        # Kilepes elott elmentjuk a feladatokat a fajlba
        write_tasks()
        print("Viszlat!")
        logging.info("Program leallitva")
        break  # kilep a while ciklusbol, ezzel a program veget er