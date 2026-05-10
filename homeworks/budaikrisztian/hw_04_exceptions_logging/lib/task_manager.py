"""
Task manager class for the to-do application.
"""

import logging

from lib.log_messages import LogMessage


class TaskManager:
    """Manage task list operations."""

    def __init__(self, tasks: list[str]) -> None:
        """Initialize the task manager with the task list."""
        self.tasks = tasks

    def display_tasks(self) -> None:
        """Print the current tasks."""
        if len(self.tasks) == 0:
            logging.info(LogMessage.TASK_LIST_EMPTY.get_message())
            return

        print("Current tasks:")

        for task_number, task in enumerate(self.tasks, start=1):
            print(f"{task_number}. {task}")

        print("\n" + "-" * 100 + "\n")

        print(f"Total tasks: {len(self.tasks)}\n")
        logging.info(LogMessage.TASK_LIST_DISPLAYED.get_message())

    def add_task(self, task: str) -> None:
        """Add a task to the task list."""
        self.tasks.append(task)
        logging.info(LogMessage.TASK_ADDED.get_message(), task)

    def remove_task(self, task_number: int) -> None:
        """Remove a task from the task list by its number."""
        task_index: int = task_number - 1

        if task_index < 0 or task_index >= len(self.tasks):
            logging.error(
                LogMessage.TASK_NUMBER_NOT_FOUND.get_message(),
                task_number,
            )
            return

        removed_task: str = self.tasks.pop(task_index)
        logging.info(LogMessage.TASK_REMOVED.get_message(), removed_task)
