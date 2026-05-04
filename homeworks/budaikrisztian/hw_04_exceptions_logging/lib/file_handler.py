"""
Task file handling for the to-do application.
"""

import logging
from pathlib import Path


class FileHandler:
    """Handle task file operations."""

    def __init__(self, tasks_file_path: Path) -> None:
        """Initialize the file handler with the task file path."""
        self.tasks_file_path = tasks_file_path

    def read_tasks(self) -> list[str]:
        """Read tasks from the text file."""
        try:
            with open(self.tasks_file_path, encoding="utf-8") as tasks_file:
                tasks: list[str] = [
                    task.strip()
                    for task in tasks_file.readlines()
                    if task.strip() != ""
                ]

            logging.info("Tasks read from file.")
            return tasks
        except FileNotFoundError:
            logging.warning("Task file does not exist yet. Starting empty.")
            return []
        except OSError as error:
            logging.error("Could not read tasks from file: %s", error)
            return []

    def write_tasks(self, tasks: list[str]) -> None:
        """Write tasks to the text file."""
        try:
            with open(
                self.tasks_file_path, "w", encoding="utf-8"
            ) as tasks_file:
                for task in tasks:
                    tasks_file.write(f"{task}\n")

            logging.info("Tasks written to file.")
        except OSError as error:
            logging.error("Could not write tasks to file: %s", error)
