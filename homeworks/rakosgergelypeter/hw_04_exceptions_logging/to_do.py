import os
import sys
import logging
#global list
tasks=[]

#logger
file_handler = logging.FileHandler("homeworks/rakosgergelypeter/hw_04_exceptions_logging/tasks.log",mode="a")
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

def add_task(task):
    try:
        tasks.append(task)
        logger.info(f"Task hozzáadva:{task}")
    except MemoryError as e:
        logger.error(f"Nem sikerült a hozzáadás:{e} - task:{task}")

def remove_task(task):
    try:
        tasks.remove(task)
        logger.info(f"Task törölve:{task}")
    except ValueError as e:
        logger.error(f"Nem sikerült a törlés:{e} - task:{task}")

def view_tasks():
    for item in tasks:
        print(item)

def exit():
    print('Exit')
    sys.exit()

def read_tasks(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for item in lines:
                tasks.append(item.strip())
    except FileNotFoundError as e :
        logger.error(f"Nem sikerült a file olvasása:{e}")

def write_task(file_path): 
    with open(file_path, "w") as file:
        file.write("\n".join(item.strip() for item in tasks) + "\n")
        #file.writelines(item for item in tasks)

def display_menu():
    for key,value in menu_dict.items():
        if key in(1,2,3,4):
            print(str(key)+":"+value.__name__)

menu_dict={1:add_task,
           2:remove_task,
           3:view_tasks,
           4:exit,
           5:read_tasks,
           6:write_task,
           7:display_menu}

def choose_menu():
    while True:
        choosed=input("Kérem adja meg melyik menüt fogja választani:")
        try:
            choosed=int(choosed)
            if choosed in menu_dict.keys():
                if choosed in(1,2):# add task : need parameter
                    new_task=input("Kérem adja meg mi legyen az új task:" if choosed==1 else  "Kérem adja meg melyik taskot szeretné törölni:" ) 
                    menu_dict[choosed](new_task)
                elif choosed==3:
                    menu_dict[choosed]()
                else: 
                    return
        except ValueError:
            print(f"Nem jó a formátum: {choosed}")
            continue
        

def main():
    print(os.getcwd())
    read_tasks("homeworks/rakosgergelypeter/hw_04_exceptions_logging/tasks.txt")
    print(tasks)
    display_menu()
    choose_menu()
    write_task("homeworks/rakosgergelypeter/hw_04_exceptions_logging/tasks.txt")

if __name__ == "__main__":
    main()
