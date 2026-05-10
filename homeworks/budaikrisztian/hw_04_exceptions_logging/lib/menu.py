"""
Menu handling for the to-do application.
"""

from enum import Enum


class InvalidMenuOptionError(Exception):
    """Custom exception for invalid menu options."""


class MenuOption(Enum):
    """Menu options for the to-do application."""

    ADD_TASK = "1"
    VIEW_TASKS = "2"
    REMOVE_TASK = "3"
    EXIT = "4"

    @classmethod
    def from_option_number(cls, option_number: str) -> "MenuOption":
        """Return the menu option matching the given number."""
        for option in cls:
            if option.value == option_number:
                return option

        raise InvalidMenuOptionError(
            "Invalid menu option. Please choose 1, 2, 3 or 4."
        )


class Menu:
    """Display and validate menu options."""

    OPTION_LABELS: dict[MenuOption, str] = {
        MenuOption.ADD_TASK: "Add Task",
        MenuOption.VIEW_TASKS: "View Tasks",
        MenuOption.REMOVE_TASK: "Remove Task",
        MenuOption.EXIT: "Exit",
    }

    def __init__(self, section_separator: str) -> None:
        """Initialize the menu."""
        self.section_separator: str = section_separator

    def display(self) -> None:
        """Print the available menu options."""
        print(self.section_separator)

        for option in MenuOption:
            print(f"{option.value}. {self.OPTION_LABELS[option]}")

    def get_option(self) -> MenuOption:
        """Ask for a valid menu option or raise an error."""
        menu_option: str = input("Choose an option: ").strip()

        print(self.section_separator)

        return MenuOption.from_option_number(menu_option)
