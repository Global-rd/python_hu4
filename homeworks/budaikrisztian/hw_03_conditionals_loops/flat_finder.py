"""
Homework 3.1: Conditionals, operators and f-string usage.
Author: Budai Krisztián
"""

from typing import TypedDict

section_separator: str = f"\n{'=' * 100}\n"


class FlatRule(TypedDict):
    cities: list[str]
    can_move: bool
    max_rent: int | None
    is_default: bool


flat_rules: list[FlatRule] = [
    {
        "cities": ["Washington"],
        "can_move": False,
        "max_rent": None,
        "is_default": False,
    },
    {
        "cities": ["Chicago"],
        "can_move": True,
        "max_rent": None,
        "is_default": False,
    },
    {
        "cities": ["New York", "San Francisco"],
        "can_move": True,
        "max_rent": 3999,
        "is_default": False,
    },
    {
        "cities": [],
        "can_move": True,
        "max_rent": 3000,
        "is_default": True,
    },
]

"""
Flat finder tasks:
- Help Sarah decide whether she would move into a flat.
- Ask the user for the city where the flat is located.
- Ask the user for the monthly rent in USD.
- Sarah loves New York and San Francisco, but only below 4000 USD.
- Sarah hates Washington and would never live there.
- Sarah loves Chicago so much that the price does not matter.
- In any other city, Sarah would move in for 3000 USD or less.
- Print the decision using an f-string.
"""


def get_city() -> str:
    """Ask for the city and normalize its format."""
    return input("Which city is the flat in? ").title().strip()


def get_monthly_rent() -> int:
    """Ask for the monthly rent and convert it to an integer."""
    return int(input("How much is the monthly rent in USD? "))


def rule_matches_city(flat_rule: FlatRule, city: str) -> bool:
    """Return whether a flat rule matches the city."""
    return city in flat_rule["cities"] or flat_rule["is_default"]


def can_move_by_rule(flat_rule: FlatRule, monthly_rent: int) -> bool:
    """Return whether Sarah can move based on one matching rule."""
    if flat_rule["max_rent"] is None:
        return flat_rule["can_move"]

    return flat_rule["can_move"] and monthly_rent <= flat_rule["max_rent"]


def can_sarah_move(city: str, monthly_rent: int) -> bool:
    """Return whether Sarah can move into the flat."""
    for flat_rule in flat_rules:
        if rule_matches_city(flat_rule, city):
            return can_move_by_rule(flat_rule, monthly_rent)

    return False


def print_final_result(
    city: str,
    monthly_rent: int,
    can_move: bool,
) -> None:
    """Print the final decision."""
    moving_decision: str = "can" if can_move else "cannot"

    print(
        f"The flat is in {city} and costs {monthly_rent} USD per month.\n"
        f"Sarah {moving_decision} move into this flat."
    )


def main() -> None:
    """
    Run the main flat finder flow.

    Flat finder flow tasks:
    - Get the city from the user.
    - Get the monthly rent from the user.
    - Check Sarah's preferences based on the flat rules.
    - Print the final decision.
    """
    city: str = get_city()
    monthly_rent: int = get_monthly_rent()

    print(section_separator)

    can_move: bool = can_sarah_move(city, monthly_rent)
    print_final_result(city, monthly_rent, can_move)


main()
