import random

print("Rock-Paper-Scissors Game 😊")
print("----------------------------")

while True:
    # --- Number of rounds ---
    rounds_input = input("Please enter the number of rounds (it can only be an odd number): ").strip()

    if not rounds_input.isdigit():
        print("\nData entry error: Please enter the number of rounds by digits.: ")
        continue

    rounds = int(rounds_input)

    if rounds % 2 == 0:
        print("\nThe number of games must be odd to declare a winner.")
        continue

    print(f"\nOkay, {rounds} round(s) to go!\n")

    # --- pontszámok ---
    user_score = 0
    comp_score = 0

    options = ["rock", "paper", "scissors"]

    # --- Number of cycles of games ---
    for i in range(1, rounds + 1):
        print(f"Round-{i}. :")

        user = input("Your choice (rock / paper / scissors): ").strip().lower()
        if user not in options:
            print("Invalid character choice, you lost this round 😅\n")
            comp_score += 1
            continue

        comp = random.choice(options)
        print(f"The choice of computer: {comp}")

        # --- Determining the winner in round ---
        if user == comp:
            print("This round is a draw!\n")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You won this round!\n")
            user_score += 1
        else:
            print("The computer won this round!\n")
            comp_score += 1

    # --- Summary of the results of the rounds ---
    print("=== GAME RESULTS ===")
    print(f"You scored: {user_score} point(s)")
    print(f"Computer scored: {comp_score} point(s)")

    if user_score == comp_score:
        print("⚓️ No winner, the players' scores are equal!")
    elif user_score > comp_score:
        print("😊 You won this game!\n")
    else:
        print("🤖 Computer won this game!\n")

    # --- New game? ---
    new_game = input("Would you like to play again?? (Y/N): ").strip().upper()
    if new_game != "Y":
        print("\nThanks for playing! 🥂")
        print("**************************")
        break

    print("\nNew game starts! ✂\n")