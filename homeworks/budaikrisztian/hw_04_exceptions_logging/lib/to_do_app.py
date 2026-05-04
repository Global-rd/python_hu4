"""
Main to-do application class.
"""

import logging
import logging.config
from pathlib import Path

from lib.file_handler import FileHandler
from lib.menu import InvalidMenuOptionError, Menu, MenuOption
from lib.task_manager import TaskManager


class ColoredFormatter(logging.Formatter):
    """Add colors to log level names for console output."""

    COLORS: dict[str, str] = {
        "DEBUG": "\033[37m",
        "INFO": "\033[32m",
        "WARNING": "\033[33m",
        "ERROR": "\033[31m",
        "CRITICAL": "\033[35m",
    }
    RESET: str = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        """Format a log record with a colored level name."""
        original_levelname: str = record.levelname
        color: str = self.COLORS.get(record.levelname, self.RESET)

        try:
            record.levelname = f"{color}{record.levelname}{self.RESET}"
            return super().format(record)
        finally:
            record.levelname = original_levelname


class TodoApp:
    """Run the to-do application flow."""

    TASKS_FILE_PATH: Path = Path(__file__).parent.parent / "tasks.txt"
    LOG_FILE_PATH: Path = Path(__file__).parent.parent / "to_do.log"

    SECTION_SEPARATOR: str = f"\n{'=' * 100}\n"

    def __init__(self) -> None:
        """Initialize the application dependencies."""
        self.setup_logging()
        logging.info("To-do application started.")

        self.file_handler = FileHandler(self.TASKS_FILE_PATH)
        self.menu = Menu(self.SECTION_SEPARATOR)
        self.tasks: list[str] = self.file_handler.read_tasks()
        self.task_manager = TaskManager(self.tasks)

    def get_new_task(self) -> str:
        """Ask for a new task until the user gives a non-empty value."""
        while True:
            task: str = input("Enter the new task: ").strip()

            if task != "":
                return task

            logging.error("Empty task input.")
            print(self.SECTION_SEPARATOR)

    def get_task_number(self) -> int:
        """Ask for the task number to remove."""
        return int(input("Enter the task number to remove: "))

    def handle_add_task(self) -> None:
        """Get a new task from the user and add it to the task list."""
        task: str = self.get_new_task()
        self.task_manager.add_task(task)

    def handle_remove_task(self) -> None:
        """Get a task number from the user and remove that task."""
        try:
            task_number: int = self.get_task_number()
            self.task_manager.remove_task(task_number)
        except ValueError:
            logging.error("Invalid task number input.")
            print(self.SECTION_SEPARATOR)

    def setup_logging(self) -> None:
        """Set up logging to the console and to a log file."""
        logging.config.dictConfig(
            {
                "version": 1,
                "disable_existing_loggers": False,
                "formatters": {
                    "default": {
                        "format": (
                            "%(asctime)s [%(levelname)s] "
                            "%(name)s:%(lineno)d | %(message)s"
                        )
                    },
                    "simple": {
                        "()": ColoredFormatter,
                        "format": "%(levelname)s - %(message)s",
                    },
                },
                "handlers": {
                    "console": {
                        "class": "logging.StreamHandler",
                        "formatter": "simple",
                        "level": "INFO",
                    },
                    "file": {
                        "class": "logging.handlers.RotatingFileHandler",
                        "filename": self.LOG_FILE_PATH,
                        "maxBytes": 10_000_000,
                        "backupCount": 5,
                        "formatter": "default",
                        "level": "DEBUG",
                    },
                },
                "root": {
                    "handlers": ["console", "file"],
                    "level": "DEBUG",
                },
            }
        )

    def run(self) -> None:
        """
        Run the main to-do application flow.

        To-do app flow tasks:
        - Ask the user what they want to do until they choose Exit.
        - Write the updated task list to the text file before exiting.
        """
        while True:
            self.menu.display()

            try:
                menu_option: MenuOption = self.menu.get_option()
            except InvalidMenuOptionError as error:
                logging.error(error)
                continue

            if menu_option == MenuOption.ADD_TASK:
                self.handle_add_task()
            elif menu_option == MenuOption.VIEW_TASKS:
                self.task_manager.display_tasks()
            elif menu_option == MenuOption.REMOVE_TASK:
                self.handle_remove_task()
            else:
                self.file_handler.write_tasks(self.tasks)
                logging.info("To-do application closed.")
                print(self.SECTION_SEPARATOR)
                print("Goodbye!\n")
                break
