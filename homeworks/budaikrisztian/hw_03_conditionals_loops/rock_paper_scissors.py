"""
Homework 3.2: While and for loop usage.
Author: Budai Krisztián
"""

from typing import TypedDict

section_separator: str = f"\n{'=' * 100}\n"

"""
Rock, paper, scissors tasks:
- Ask the players how many rounds they want to play.
- The number of rounds must be odd, so the final result cannot be a tie.
- Ask both players for their choice in every round.
- Valid choices are: "rock", "paper" and "scissors".
- If a round is a tie, replay the same round.
- Store both players' scores.
- Print the winner and the final score.
"""

# Store the valid choices in a list, so they can be checked easily.
valid_choices: list[str] = ["rock", "paper", "scissors"]


class PlayerData(TypedDict):
    name: str
    score: int
    choices: list[str]


def get_player_name(default_name: str) -> str:
    """Ask for a player's name or return the default name for empty input."""
    player_name: str = input(
        f"Enter {default_name}'s name or press enter to keep the default: "
    ).strip()

    if player_name == "":
        return default_name

    return player_name


def get_round_count() -> int:
    """Ask for the number of rounds until the user gives an odd number."""
    round_count: int = int(input("How many rounds do you want to play? "))

    while round_count % 2 == 0:
        print("Invalid number. Please enter an odd number of rounds.")
        round_count = int(input("How many rounds do you want to play? "))

    return round_count


def get_player_choice(player_name: str) -> str:
    """Ask one player for a valid rock, paper or scissors choice."""
    player_choice: str = (
        input(f"{player_name}, choose rock, paper or scissors: ")
        .lower()
        .strip()
    )

    while player_choice not in valid_choices:
        print("Invalid choice. Please choose rock, paper or scissors.")
        player_choice = (
            input(f"{player_name}, choose rock, paper or scissors: ")
            .lower()
            .strip()
        )

    return player_choice


def get_round_winner(
    player_one: PlayerData,
    player_two: PlayerData,
) -> PlayerData | None:
    """Return the winner of the current round or None for a tie."""
    player_one_choice: str = player_one["choices"][-1]
    player_two_choice: str = player_two["choices"][-1]

    if player_one_choice == player_two_choice:
        return None

    player_one_wins: bool = (
        player_one_choice == "rock"
        and player_two_choice == "scissors"
        or player_one_choice == "paper"
        and player_two_choice == "rock"
        or player_one_choice == "scissors"
        and player_two_choice == "paper"
    )

    return player_one if player_one_wins else player_two


def print_current_score(
    player_one: PlayerData,
    player_two: PlayerData,
) -> None:
    """Print the current score after a finished round."""
    print(
        f"Current score: {player_one['name']} - {player_one['score']}, "
        f"{player_two['name']} - {player_two['score']}"
    )


def print_final_result(
    player_one: PlayerData,
    player_two: PlayerData,
) -> None:
    """Print the winner and the final score."""
    winner: PlayerData = (
        player_one if player_one["score"] > player_two["score"] else player_two
    )

    print(f"{winner['name']} won the game with {winner['score']} points.")


def print_round_result(
    round_number: int,
    round_winner: PlayerData,
    player_one: PlayerData,
    player_two: PlayerData,
) -> None:
    """Print the winner and current score after a finished round."""
    print(f"{round_winner['name']} won round {round_number}.")
    print_current_score(player_one, player_two)
    print(section_separator)


def play_round(
    round_number: int,
    player_one: PlayerData,
    player_two: PlayerData,
) -> None:
    """Play one round until one of the players wins it."""
    print(f"Round {round_number}")

    round_winner: PlayerData | None = None

    # Repeat the current round until one of the players wins it.
    while round_winner is None:
        player_one["choices"].append(
            get_player_choice(player_one["name"])
        )
        player_two["choices"].append(
            get_player_choice(player_two["name"])
        )
        round_winner = get_round_winner(player_one, player_two)

        if round_winner is None:
            print("This round is a tie. Replay the round.")

    round_winner["score"] += 1
    print_round_result(round_number, round_winner, player_one, player_two)


def main() -> None:
    """
    Run the main game flow.

    Game flow tasks:
    - Get the valid number of rounds.
    - Use a for loop to play all rounds.
    - Use a while loop to replay tied rounds.
    - Increase the winner's score after every finished round.
    """
    # Get the names and store the score of both players.
    player_one: PlayerData = {
        "name": get_player_name("Player 1"),
        "score": 0,
        "choices": [],
    }
    player_two: PlayerData = {
        "name": get_player_name("Player 2"),
        "score": 0,
        "choices": [],
    }

    # Get the number of rounds, ensuring it is an odd number.
    round_count: int = get_round_count()

    print(section_separator)

    # Play the selected number of rounds.
    for round_number in range(1, round_count + 1):
        play_round(round_number, player_one, player_two)

    # Print the winner and the final score.
    print_final_result(player_one, player_two)


main()
