"""
Task manager class for the to-do application.
"""

import logging


class TaskManager:
    """Manage task list operations."""

    def __init__(self, tasks: list[str]) -> None:
        """Initialize the task manager with the task list."""
        self.tasks = tasks

    def display_tasks(self) -> None:
        """Print the current tasks."""
        if len(self.tasks) == 0:
            logging.info("Task list displayed. The list is empty.")
            return

        print("Current tasks:")

        for task_number, task in enumerate(self.tasks, start=1):
            print(f"{task_number}. {task}")

        print("\n" + "-" * 100 + "\n")

        print(f"Total tasks: {len(self.tasks)}\n")
        logging.info("Task list displayed.")

    def add_task(self, task: str) -> None:
        """Add a task to the task list."""
        self.tasks.append(task)
        logging.info("Task added: %s", task)

    def remove_task(self, task_number: int) -> None:
        """Remove a task from the task list by its number."""
        task_index: int = task_number - 1

        if task_index < 0 or task_index >= len(self.tasks):
            logging.error("Task number does not exist: %s", task_number)
            return

        removed_task: str = self.tasks.pop(task_index)
        logging.info("Task removed: %s", removed_task)
