"""
Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. A
program kérje be, hogy hány kört akarnak játszani a játékosok. Figyelj oda, hogy
olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent
játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a
körök számát amíg páratlan számot nem ad meg. Ezután a program felváltva kérje
be az első és második játékos válaszát, ami kizárólag a következő stringek
valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát
ahogy a körök számánál. Egy adott kör addig ne érjen véget, amíg valaki nem nyer 
(döntetlen esetén az adott kört újra kell játszani). Tárold a nyertesek pontjait, és
minden kör végén növeld az aktuális játékos pontszámát. A végén printeld ki ki
nyert, és hány ponttal.
"""

score_player1 = 0
score_player2 = 0
valid_moves = ["rock", "paper", "scissors"]

while True:
    rounds = int(input("How many rounds do you want to play? "))
    if rounds % 2 == 1:
        break
    else:
        print("Please enter an odd number!")

for n in range(rounds):
    print(f"Round {n+1}")
    
    while True:
        # Player 1 input
        while True:
            player1 = input("Player 1 (rock/paper/scissors): ").lower()
            if player1 in valid_moves:
                break
            else:
                print("Invalid input, try again!")
        
        # Player 2 input
        while True:
            player2 = input("Player 2 (rock/paper/scissors): ").lower()
            if player2 in valid_moves:
                break
            else:
                print("Invalid input, try again!")
        
    
        if player1 == player2:
            print("It's a draw! Replay the round.")
            continue
        elif ((player1 == "rock" and player2 == "scissors") or
             (player1 == "scissors" and player2 == "paper") or
             (player1 == "paper" and player2 == "rock")): 
            print("Player 1 wins this round!")
            score_player1 += 1
            break               
        else:
            print("Player 2 wins this round!")
            score_player2 += 1
            break


print("Final Results:")
print(f"Player 1: {score_player1} | Player 2: {score_player2}")

if score_player1 > score_player2:
    print("Player 1 wins the game!")
elif score_player2 > score_player1:
    print("Player 2 wins the game!")
else:
    print("It's a draw!")  