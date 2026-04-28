
rounds = int(input("How many rounds? "))

p1_score = 0
p2_score = 0


#Loop 'til input is odd
while rounds % 2 == 0:
    rounds = int(input("Rounds should be odd: "))

roundsmax = rounds

while rounds > 0:

    print("Round ",rounds,"/",roundsmax)

    while True:                                    #Input has to be rock paper or scissor exactly
        move_1= input("Player1 next move: ")
        if move_1 in ["rock","paper","scissor"]:
            break

    while True:                                    #Input has to be rock paper or scissor exactly
        move_2 = input("Player2 next move: ")
        if move_2 in ["rock","paper","scissor"]:
            break

# If its a tie then again
    if move_1 == move_2:
        print("Tie, again!")
        rounds = rounds + 1

    if move_1 == "rock" and move_2 == "paper":
        p2_score +=1

    if move_1 == "paper" and move_2 == "rock":
        p1_score +=1
        
    if move_1 == "paper" and move_2 == "scissor": 
        p2_score +=1
        
    if move_1 == "scissor" and move_2 == "paper":    
        p1_score +=1

    if move_1 == "scissor" and move_2 == "rock":    
        p2_score +=1

    if move_1 == "rock" and move_2 == "scissor": 
        p1_score +=1
    

    rounds = rounds - 1

print("-----=============-----")
print("GAME OVER")
print("Player 1 score: ",p1_score)
print("Player 2 score: ",p2_score)

# Winner with point difference

if p1_score > p2_score:
    diff = p1_score - p2_score
    print("The winner is Player 1 by (",diff,") points!")
    
else:
    diff = p2_score - p1_score
    print("The winner is Player 2 by (",diff,") points!")