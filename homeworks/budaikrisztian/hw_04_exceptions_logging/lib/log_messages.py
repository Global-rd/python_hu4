"""
Log message keys and message lookup for the to-do application.
"""

from enum import Enum


class LogMessage(Enum):
    """Log message keys for the to-do application."""

    APP_STARTED = "app_started"
    APP_CLOSED = "app_closed"
    EMPTY_TASK_INPUT = "empty_task_input"
    INVALID_TASK_NUMBER_INPUT = "invalid_task_number_input"
    TASKS_READ = "tasks_read"
    TASK_FILE_MISSING = "task_file_missing"
    TASK_READ_ERROR = "task_read_error"
    TASKS_WRITTEN = "tasks_written"
    TASK_WRITE_ERROR = "task_write_error"
    TASK_LIST_EMPTY = "task_list_empty"
    TASK_LIST_DISPLAYED = "task_list_displayed"
    TASK_ADDED = "task_added"
    TASK_NUMBER_NOT_FOUND = "task_number_not_found"
    TASK_REMOVED = "task_removed"

    def get_message(self) -> str:
        """Return the log message for this key."""
        if self not in LOG_MESSAGES:
            raise ValueError(
                f"Missing log message for key: {self.value}"
            )

        return LOG_MESSAGES[self]


LOG_MESSAGES: dict[LogMessage, str] = {
    LogMessage.APP_STARTED: "To-do application started.",
    LogMessage.APP_CLOSED: "To-do application closed.",
    LogMessage.EMPTY_TASK_INPUT: "Empty task input.",
    LogMessage.INVALID_TASK_NUMBER_INPUT: "Invalid task number input.",
    LogMessage.TASKS_READ: "Tasks read from file.",
    LogMessage.TASK_FILE_MISSING: (
        "Task file does not exist yet. Starting empty."
    ),
    LogMessage.TASK_READ_ERROR: "Could not read tasks from file: %s",
    LogMessage.TASKS_WRITTEN: "Tasks written to file.",
    LogMessage.TASK_WRITE_ERROR: "Could not write tasks to file: %s",
    LogMessage.TASK_LIST_EMPTY: "Task list displayed. The list is empty.",
    LogMessage.TASK_LIST_DISPLAYED: "Task list displayed.",
    LogMessage.TASK_ADDED: "Task added: %s",
    LogMessage.TASK_NUMBER_NOT_FOUND: (
        "Task number does not exist: %s"
    ),
    LogMessage.TASK_REMOVED: "Task removed: %s",
}
