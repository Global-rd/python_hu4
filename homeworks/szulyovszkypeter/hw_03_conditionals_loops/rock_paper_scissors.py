'''
Feladat 2: while és for loop használata
Hozz létre egy rock_paper_scissors.py nevű fi le-t, és kódold le a következő feladat megoldását: 
Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. 
A program kérje be, hogy hány kört akarnak játszani a játékosok. 
Figyelj oda, hogy olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent játszani! 
Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a körök számát amíg páratlan számot nem ad meg. 
Ezután a program felváltva kérje be az első és második játékos válaszát, ami kizárólag a következő stringek valamelyik lehet: "rock", "paper", "scissors". 
Ellenkező esetben kezeld úgy a hibát ahogy a körök számánál. 
Egy adott kör addig ne érjen véget, amíg valaki nem nyer
(döntetlen esetén az adott kört újra kell játszani). 
Tárold a nyertesek pontjait, és minden kör végén növeld az aktuális játékos pontszámát. 
A végén printeld ki ki nyert, és hány ponttal.
'''


# 1. Körök számának bekérése (Páratlan szám ellenőrzése)
rounds_to_win = 0
while True:
    try:
        rounds_to_win = int(input("Hány nyert körig menjen a játék? (Páratlan számot adj meg!): "))
        if rounds_to_win % 2 != 0 and rounds_to_win > 0:
            break
        else:
            print("Hiba: Páros számot adtál meg, vagy nullát! A döntetlen elkerülése végett páratlan kell.")
    except ValueError:
        print("Hiba: Kérlek, számot adj meg!")

player1_score = 0
player2_score = 0
current_round = 1

# 2. A fő játékciklus (Addig megy, amíg valaki el nem éri a szükséges pontot)
while player1_score < (rounds_to_win // 2 + 1) and player2_score < (rounds_to_win // 2 + 1):
    print(f"\n--- {current_round}. kör ---")
    print(f"Állás: 1. Játékos: {player1_score} - 2. Játékos: {player2_score}")
    
    round_winner = None
    
    # 3. Egy adott kör ciklusa (addig megy, amíg nincs döntés)
    while round_winner is None:
        choices = ["rock", "paper", "scissors"]
        
        # Bemenetek bekérése és ellenőrzése
        p1_choice = input("1. Játékos (rock/paper/scissors): ").lower()
        while p1_choice not in choices:
            p1_choice = input("Hiba! Csak 'rock', 'paper' vagy 'scissors' fogadható el: ").lower()
            
        p2_choice = input("2. Játékos (rock/paper/scissors): ").lower()
        while p2_choice not in choices:
            p2_choice = input("Hiba! Csak 'rock', 'paper' vagy 'scissors' fogadható el: ").lower()

        # Logika eldöntése
        if p1_choice == p2_choice:
            print("Döntetlen! Ezt a kört újra játsszuk.")
        elif (p1_choice == "rock" and p2_choice == "scissors") or \
             (p1_choice == "paper" and p2_choice == "rock") or \
             (p1_choice == "scissors" and p2_choice == "paper"):
            print("1. Játékos nyerte a kört!")
            player1_score += 1
            round_winner = "P1"
        else:
            print("2. Játékos nyerte a kört!")
            player2_score += 1
            round_winner = "P2"
            
    current_round += 1

# 4. Végeredmény hirdetése
print("\n" + "="*20)
if player1_score > player2_score:
    print(f"A JÁTÉK GYŐZTESE: 1. Játékos")
else:
    print(f"A JÁTÉK GYŐZTESE: 2. Játékos")
print(f"Végeredmény: {player1_score} - {player2_score}")
print("="*20)