import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

tasks = []
FILE_NAME = "tasks.txt"


def load_tasks():
    """Reading tasks from file at program startup"""
    global tasks
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f.readlines()]
        logger.info("Tasks successfully loaded")
    except FileNotFoundError:
        logger.warning("tasks.txt not found, starting with an empty list")
        tasks = []
    except Exception as e:
        logger.error(f"An error occurred while scanning: {e}")

def save_tasks():
    """Feladatok kiírása a fájlba kilépéskor"""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(f"{task}\n")
        logger.info("Tasks saved to file")
    except Exception as e:
        logger.error(f"An error occurred while saving: {e}")

def display_tasks():
    """Display tasks on the screen"""
    if not tasks:
        print("\nThe list is currently empty")
    else:
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(new_task):
    """Add a new task to the list in memory"""
    tasks.append(new_task)
    logger.info(f"Added: {new_task}")

def remove_task(index):
    """Delete task based on index"""
    try:
        removed = tasks.pop(index - 1)
        logger.info(f"Deleted: {removed}")
    except IndexError:
        logger.error("Error: Invalid sequence number for deletion")
        print("There is no such task number!")

def display_menu():
    """The menu is displayed"""
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    load_tasks()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task_name = input("Enter the new task: ")
            add_task(task_name)
        
        elif choice == '2':
            display_tasks()
        
        elif choice == '3':
            display_tasks()
            if tasks:
                try:
                    idx = int(input("Which serial number should I delete? "))
                    remove_task(idx)
                except ValueError:
                    logger.error("Error: You did not enter a number to delete")
        
        elif choice == '4':
            save_tasks()
            logger.info("Exit the program")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()