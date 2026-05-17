game_list = ["rock", "paper", "scissor"]

def determine_winner(player_01_input, player_02_input):
        if player_01_input == player_02_input:
            return "It's a tie!"
        elif (player_01_input.lower() == game_list[0] and player_02_input.lower() == game_list[2]) or (player_01_input.lower() == game_list[1] and player_02_input.lower() == game_list[0]) or (player_01_input.lower() == game_list[2] and player_02_input.lower() == game_list[1]):
            return "Player_01 wins!"
        else:
            return "Player_02 wins!"

while True:
    rounds_no = int(input("How many rounds do you want to play?: "))
        
    if rounds_no > 0 and rounds_no % 2 != 0:
            break
    else:
            print("Please enter a positive odd number.")
print (f"You have chosen to play {rounds_no} rounds. Let's start the game!")
player_01_points = 0
player_02_points = 0
for round in range(rounds_no) :
    print(f"Round {round + 1}")
    player_01_input = input("Player_01, please enter rock, paper or scissor: ")
    player_02_input = input("Player_02, please enter rock, paper or scissor: ")
 
    result = determine_winner(player_01_input, player_02_input)
    while result == "It's a tie!":
        print("It's a tie! Please play again.")
        player_01_input = input("Player_01, please enter rock, paper or scissor: ")
        player_02_input = input("Player_02, please enter rock, paper or scissor: ")
        result = determine_winner(player_01_input, player_02_input)
    else:
        result = determine_winner(player_01_input, player_02_input)
    print(result)
    if result == "Player_01 wins!":
        player_01_points += 1
    elif result == "Player_02 wins!":
        player_02_points += 1
    print(f"Current score: Player_01: {player_01_points} - Player_02: {player_02_points}")
if player_01_points > player_02_points:
    print("Player_01 is the overall winner!")
elif player_01_points == player_02_points:
    print("The game is a tie!")
else:   print("Player_02 is the overall winner!")