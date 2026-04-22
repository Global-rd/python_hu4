# ROCK PAPER SCISSORS

# KÖRÖK SZÁMA
rounds = int(input("How many rounds do you want to play? "))
while rounds % 2 == 0:
    print("Please enter an odd number to avoid a draw!")
    rounds = int(input("How many rounds do you want to play? "))

# PONTOK
player1_score = 0
player2_score = 0

# JÁTÉK
for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num} ---")
    
    while True:
        p1 = input("Player 1 - rock, paper or scissors? ").strip().lower()
        if p1 not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please enter rock, paper or scissors.")
            continue
        
        p2 = input("Player 2 - rock, paper or scissors? ").strip().lower()
        if p2 not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please enter rock, paper or scissors.")
            continue
        
        if p1 == p2:
            print("Draw! Play again.")
            continue
        
        if (p1 == "rock" and p2 == "scissors") or \
           (p1 == "paper" and p2 == "rock") or \
           (p1 == "scissors" and p2 == "paper"):
            print("Player 1 wins this round!")
            player1_score += 1
        else:
            print("Player 2 wins this round!")
            player2_score += 1
        
        break

# VÉGEREDMÉNY
print(f"\n=== GAME OVER ===")
print(f"Player 1: {player1_score} points")
print(f"Player 2: {player2_score} points")

if player1_score > player2_score:
    print(f"Player 1 wins with {player1_score} points!")
else:
    print(f"Player 2 wins with {player2_score} points!")