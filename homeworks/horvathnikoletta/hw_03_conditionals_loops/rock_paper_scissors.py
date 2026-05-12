#körök számána bekérése, hibára fut, ha páros szám
while True:
    rounds= int(input("Please enter the number of rounds:"))
    if rounds % 2 != 0:
        break
    print("Please enter an odd number!")

# pont és körszámlálók
player1_score =0
player2_score =0
played_rounds =0

#megadjuk hanyadik körnél járunk
while played_rounds < rounds:
    print(f"Round {played_rounds+1} of {rounds}")

#1. és 2. játékos inputjának bekérése, hibára fut ha mást adnak meg
    while True:
        player1 = input("1. player: Please enter rock/paper/scissors:").lower()
        if player1 in ["rock", "paper", "scissors"]:
            break
        print ("Invalid input! Please enter only rock/paper/scissors!")

    while True:
        player2 = input("2. player: Please enter rock/paper/scissors:").lower()
        if player2 in ["rock", "paper", "scissors"]:
            break
        print ("Invalid input! Please enter only rock/paper/scissors!")

    if player1 == player2:
        print("It's a tie!Replaying this round")
        continue
    elif (player1== "rock" and player2== "scissors") or (player1== "paper" and player2== "rock") or (player1== "scissors" and player2== "paper"):
        print("Player1 won at this round")
        player1_score += 1
    else:
        print("Player2 won at this round")
        player2_score += 1
    played_rounds +=1

#a jaték végén a nyertes kiírása pontokkal
if player1_score > player2_score:
    print(f"The winner is player1 with {player1_score} points")
else:
    print(f"The winner is player2 with {player2_score} points")
