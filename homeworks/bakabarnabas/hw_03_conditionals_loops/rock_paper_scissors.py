"""
Kő-papír-olló játék két játékos között
"""
#Körök Számának bekérése ( csak páratlan szám fogadható el)
while True:
    rounds = int (input ("How many rounds would you like to play? "))
    if rounds % 2 == 1:
        break
    print("Error: please enter an odd number to avoid a draw!")

valid_choices = ["rock", "paper", "scissors"]

#pontok tárolása
player1_score = 0
player2_score = 0

#játék szabályainak betartása, mikor ki nyer
def get_winner(p1,p2):
    if p1 == p2:
        return "draw"
    elif (p1 == "rock" and p2 == "scissors" )or \
      (p1 == "scissors" and p2 == "paper") or \
      (p1 == "paper" and p2 == "rock"):
        return "player1"
    else:
        return "player2" 
round_num = 1 
#körök lejátszása
while round_num <= rounds:
    print(f"\n--- Round {round_num} ---")
    #Player 1 választása
    while True:
        p1_choice = input("Player 1 (rock/paper/scissors): ").strip().lower()
        if p1_choice in valid_choices:
            break
        print("Error: please enter 'rock', 'paper' or 'scissors'!")

        # Player 2 választása
    while True:
        p2_choice = input("Player 2 (rock/paper/scissors): ").strip().lower()
        if p2_choice in valid_choices:
            break
        print("Error: please enter 'rock', 'paper' or 'scissors'!")

    #Kör eredménye
    result = get_winner(p1_choice,p2_choice)
    
    if result == "draw":
        print("Draw! Play again.")
        continue
    elif result == "player1":
        player1_score += 1
        print(f"Player 1 wins this round! ({p1_choice} beats {p2_choice})")
    else:
        player2_score += 1
        print(f"Player 2 wins this round! ({p2_choice} beats {p1_choice})")
        
        round_num += 1
    #Végeredmény
print(f"Player 1 wins the game with {player1_score} points!")
print(f"Player 1: {player1_score} points")
print(f"Player 2: {player2_score} points!")
if player1_score > player2_score:
    print(f"Player 1 wins the game with {player1_score} points!")
else:
    print(f"Player 2 wins the game with {player2_score} points!")

