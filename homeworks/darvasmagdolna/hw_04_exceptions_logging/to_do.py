import logging

# logging beállítása
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# konzolra logolás
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

# fájlba logolás
fileHandler = logging.FileHandler("todo.log", mode="a", encoding="utf-8")
fileHandler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)




def read_tasks(tasks, filename="tasks.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip())
        logger.info("Tasks loaded successfully.")
    except FileNotFoundError:
        logger.warning("tasks.txt not found. Starting with an empty task list.")
    except Exception as e:
        logger.error(f"Error while reading tasks: {e}")


def write_tasks(tasks, filename="tasks.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info("Tasks saved successfully.")
    except Exception as e:
        logger.error(f"Error while saving tasks: {e}")


def display_tasks(tasks):
    if not tasks:
        print("\nThere are no tasks.\n")
        return

    print("\n--- TASKS ---")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")
    print()


def add_task(tasks, task):
    tasks.append(task)


def remove_task(tasks, index):
    try:
        removed = tasks.pop(index - 1)
        return removed
    except IndexError:
        print("Invalid task number.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def display_menu():
    print("----- TO-DO MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("Exit")
    print("----------------------")


def main():
    tasks = []
    read_tasks(tasks)
    pending_log = None

    while True:
        if pending_log:
            logger.info(pending_log)
            pending_log = None
            print()

        display_menu()
        choice = input("Select an option (1–3 or 'exit'): ").strip().lower()

        if choice == "exit":
            write_tasks(tasks)
            print("Exit... Tasks saved.")
            return False

        if choice not in ("1", "2", "3"):
            print("Invalid selection! You can only choose 1–3 or 'exit'.")
            continue

        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
            pending_log = f"Task added: {task}"
            continue

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            try:
                index = int(input("Enter the number of the task to be deleted: "))
                removed = remove_task(tasks, index)
                if removed:
                    pending_log = f"Task removed: {removed}"
            except ValueError:
                print("You must enter a number.")
            continue


if __name__ == "__main__":
    main()
