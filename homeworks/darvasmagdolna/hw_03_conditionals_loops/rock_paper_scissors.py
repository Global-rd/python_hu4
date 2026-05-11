j1_score = 0
j2_score = 0

while played_rounds % 2 != 1:
    played_rounds = int(input("Please enter only odd numbers: "))

round = 0
while round < played_rounds:
    print(f"----{round + 1}. round----")

    player1 = input("Player 1, choose one: rock (r), paper (p), scissors (s): ")
    while player1 not in ["r", "p", "s"]:
        player1 = input("Player 1, choose one: rock (r), paper (p), scissors (s): ")

    player2 = input("Player 2, choose one: rock (r), paper (p), scissors (s): ")
    while player2 not in ["r", "p", "s"]:
        player2 = input("Player 2, choose one: rock (r), paper (p), scissors (s): ")

    if player1 == player2:
        print("Draw")
    elif (player1 == "r" and player2 == "s") or \
            (player1 == "p" and player2 == "r") or \
            (player1 == "s" and player2 == "p"):
        print(f"{round + 1}. round winner is Player 1: {player1}")
        j1_score += 1
        round += 1
    else:
        print(f"{round + 1}. round winner is Player 2: {player2}")
        j2_score += 1
        round += 1

print("=====GAME OVER=====")
print(f"Player 1's points: {j1_score}")
print(f"Player 2's points: {j2_score}")

if j1_score > j2_score:
    print("Player 1 won!")
else:
    print("Player 2 won!")

        


