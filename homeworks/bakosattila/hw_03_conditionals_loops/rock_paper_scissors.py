
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
    
    # Addig játszunk amíg valaki nem nyer (döntetlen esetén újra)
    while True:
        # Játékosok beírása
        while True:
            move1 = input("Játékos 1, add meg a lépésed (rock/paper/scissors): ").lower().strip()
            if move1 not in ["rock", "paper", "scissors"]:
                print("Hibás input! Csak a rock, paper vagy scissors lehetséges!")
                continue
            break
        
        while True:
            move2 = input("Játékos 2, add meg a lépésed (rock/paper/scissors): ").lower().strip()
            if move2 not in ["rock", "paper", "scissors"]:
                print("Hibás input! Csak a rock, paper vagy scissors lehetséges!")
                continue
            break
        
        # Eredmény meghatározása
        if move1 == move2:
            print(f"Döntetlen! ({move1} vs {move2}) Újra játsszatok!")
        elif (move1 == "rock" and move2 == "scissors") or \
             (move1 == "paper" and move2 == "rock") or \
             (move1 == "scissors" and move2 == "paper"):
            print(f"Játékos 1 nyert! ({move1} vs {move2})")
            player1_score += 1
            break
        else:
            print(f"Játékos 2 nyert! ({move2} vs {move1})")
            player2_score += 1
            break
    
    round_num += 1


print("\n" + "="*40)
print("VÉGEREDMÉNY")
print("="*40)
print(f"Játékos 1: {player1_score} pont")
print(f"Játékos 2: {player2_score} pont")

if player1_score > player2_score:
    print(f"\n🎉 Játékos 1 nyert {player1_score - player2_score} ponttal!")
else:
    print(f"\n🎉 Játékos 2 nyert {player2_score - player1_score} ponttal!")