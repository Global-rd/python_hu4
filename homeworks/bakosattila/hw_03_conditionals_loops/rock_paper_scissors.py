
# Körök számának bekérése (páratlan számnak kell lennie)
while True:
    try:
        rounds = int(input("Hány kört akartok játszani? "))
        if rounds % 2 == 0:
            print("Hibás input! A körök száma páratlan kell hogy legyen!")
            continue
        break
    except ValueError:
        print("Hibás input! Számot adj meg!")


player1_score = 0
player2_score = 0
round_num = 1

# Játék kezdete
while round_num <= rounds:
    print(f"\n--- {round_num}. kör ---")
    
    # Játékosok beírása
    while True:
        move1 = input("Player 1, add meg a lépésed (rock/paper/scissors): ").lower()
        if move1 not in ["rock", "paper", "scissors"]:
            print("Hibás input! Csak a rock, paper vagy scissors lehetséges!")
            continue
        break
    
    while True:
        move2 = input("Player 2, add meg a lépésed (rock/paper/scissors): ").lower()
        if move2 not in ["rock", "paper", "scissors"]:
            print("Hibás input! Csak a rock, paper vagy scissors lehetséges!")
            continue
        break