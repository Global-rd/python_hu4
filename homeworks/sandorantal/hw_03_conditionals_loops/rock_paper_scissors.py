rounds = 0
while rounds % 2 == 0 or rounds <= 0:
    try:
        rounds = int(input("How many rounds would you like to play? (Enter an odd number!): "))
        if rounds % 2 == 0:
            print("Error: Even numbers can result in a draw. Please enter an odd number!")
    except ValueError:
        print("Error: Please enter a number!")
    
player1_score = 0
player2_score = 0
needed_to_win = (rounds // 2) + 1

while player1_score < needed_to_win and player2_score < needed_to_win:
    print(f"\n--- Position: Player1: {player1_score} | Player2: {player2_score} ---")
    
    round_winner = None
    
    while round_winner is None:
        choices = ["rock", "paper", "scissors"]
        
        p1_choice = ""
        while p1_choice not in choices:
            p1_choice = input("Player 1 (rock/paper/scissors): ").lower()
            if p1_choice not in choices:
                print("Error: You can only use the words 'rock', 'paper' or 'scissors'!")

        p2_choice = ""
        while p2_choice not in choices:
            p2_choice = input("Player 2 (rock/paper/scissors): ").lower()
            if p2_choice not in choices:
                print("Error: You can only use the words 'rock', 'paper' or 'scissors'!")

        if p1_choice == p2_choice:
            print("Draw! This round must be replayed.")
        elif (p1_choice == "rock" and p2_choice == "scissors") or \
             (p1_choice == "paper" and p2_choice == "rock") or \
             (p1_choice == "scissors" and p2_choice == "paper"):
            print("Player 1 won this round!")
            player1_score += 1
            round_winner = "P1"
        else:
            print("This round was won by Player 2.!")
            player2_score += 1
            round_winner = "P2"

print("\n" + "="*20)
if player1_score > player2_score:
    print(f"THE GAME WAS WON BY PLAYER 1! Score: {player1_score}")
else:
    print(f"THE GAME WAS WON BY PLAYER 2! Score: {player2_score}")
print("="*20)