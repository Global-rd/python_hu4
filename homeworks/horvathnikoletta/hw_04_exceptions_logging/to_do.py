import logging

file_handler = logging.FileHandler("app.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

tasks= []
tasks_file= "tasks.txt"

def read_tasks():
    try:
        with open (tasks_file, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        logger.warning("The file is not found.")
    return tasks

def write_tasks(tasks):
    try:
        with open(tasks_file, "w") as file:
            for task in tasks:
                file.write(task + "\n")

        logging.info("Tasks successfully saved.")

    except Exception as e:
        logging.error(f"Error while writing file: {e}")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.\n")
        return

    print("\nTasks:")

    for task in tasks:
        print(f"- {task}")

    print()

def add_tasks(task):
    tasks.append(task)
    logging.info(f"New task added: {task}")

def remove_tasks(task):
    try:
        if task in tasks:
            tasks.remove(task)
            logger.info(f"Task removed: {task}")
        else:
            print("Task not found in the list!")
            logger.warning(f"Failed to remove: {task} (not found)")
    except Exception as e:
        logger.error(f"Error during removal: {e}")

def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def choose_tasks():
    while True:
        display_menu()

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            task = input("Enter the new task: ")
            add_tasks(task)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            task = input("Enter the task to remove: ")
            remove_tasks(task)

        elif choice == "4":
            write_tasks(tasks)
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select a number between 1-4.")

read_tasks()
choose_tasks()