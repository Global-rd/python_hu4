# Feladat 2: Kő-papír-olló játék

# Körök számának bekérése - csak páratlan szám
while True:
    rounds = int(input("Hány kört szeretnétek játszani? (páratlan szám): "))
    if rounds % 2 != 0:
        break
    print("Hibás szám! Csak páratlan számot adhatsz meg!")

# Pontszámok
player1_score = 0
player2_score = 0

# Játék
for round_num in range(1, rounds + 1):
    print(f"\n--- {round_num}. kör ---")

    while True:
        p1 = input("1. játékos (rock/paper/scissors): ").strip().lower()
        if p1 in ["rock", "paper", "scissors"]:
            break
        print("Hibás! Csak rock, paper vagy scissors lehet!")

    while True:
        p2 = input("2. játékos (rock/paper/scissors): ").strip().lower()
        if p2 in ["rock", "paper", "scissors"]:
            break
        print("Hibás! Csak rock, paper vagy scissors lehet!")

    if p1 == p2:
        print("Döntetlen! A kört újra kell játszani!")
        continue
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        print("1. játékos nyerte a kört!")
        player1_score += 1
    else:
        print("2. játékos nyerte a kört!")
        player2_score += 1

# Végeredmény
print(f"\n=== VÉGEREDMÉNY ===")
print(f"1. játékos: {player1_score} pont")
print(f"2. játékos: {player2_score} pont")

if player1_score > player2_score:
    print("Az 1. játékos nyerte a játékot!")
else:
    print("A 2. játékos nyerte a játékot!")