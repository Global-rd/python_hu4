print("----------------------------------")  
print("ROCK, PAPER, SCISSORS GAME")
print("----------------------------------")  

score_player_1=0
score_player_2=0
current_round=1
result_1=0
result_2=0

n=int(input("Add meg, hány kört szeretnél játszani: "))

while n%2==0:
        n=int(input("Hibás adat, add meg újra hány kört szeretnél játszani: "))

print("----------------------------------")     
print(f" Tehát a körök száma {n}. A döntetlen eredmény nem számítódik be a körök számába.")

print("----------------------------------")

while score_player_1+score_player_2<n:  
    

       
    print(f"{current_round}. kör")
   
    player_1=input("Add meg első játékos: rock, paper, scissors: ").strip().lower()
    
    while player_1 not in ["rock", "scissors","paper"]:
        print("Nem jó")
        player_1=input("Add meg az új adatot: rock, paper, scissors: ").strip().lower()
        print(f"Az első játékos: {player_1}")
       
    
    player_2=input("Add meg második játékos: rock, paper, scissors: ").strip().lower()
        
    while player_2 not in ["rock", "scissors","paper"]:
        print("Nem jó")
        player_2=input("Add meg az új adatot: rock, paper, scissors: ").strip().lower()
        print(f"Az második játékos: {player_2}")
    

    if player_1==player_2:
        print(f"A(z) {current_round}. kör eredméyne döntetlen. Újraszámolás indul.")
        print("----------------------------------")
        continue

    
    elif(player_1=="rock" and player_2=="scissors") or(player_1=="paper" and player_2=="rock")or(player_1=="scissors" and player_2=="paper"):
        print(f"{player_1} nyerte a(z) {current_round}. kört")
        score_player_1+=1
        current_round+=1

    else:
        print(f"{player_2} nyerte a(z) {current_round}. kört")
        score_player_2+=1
        current_round+=1

print("----------------------------------")   

if score_player_1>score_player_2:
    print("Végeredmény: Az első játékos nyert.")
    
    print(f"{score_player_1-score_player_2} ponttal többett szerzett, mint a második játékos.")
    print("----------------------------------")  
else:
    print("Végeredmény: A második játékos nyert.")
    
    print(f"{score_player_2-score_player_1} ponttal többet szerzett, mint az első játékos.")
    print("----------------------------------")  

