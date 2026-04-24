#bekérem a körök számát. Biztos integer legyen.
requested_round_number = int(input("Hány kört szeretnétek játszani? Adjatok meg egy számot: "))

#ellenőrzöm, hogy páratlan számot adnak-e meg. Ha nem, addig kérem újra a számot, amíg az páratlan nem lesz.
while True:

        if requested_round_number % 2 != 0:
           print("Kezdhetjük a játékot!")
           break
        else:
           #print("Így nem biztos, hogy tudunk győztest hirdetni")
           requested_round_number = int(input("Így nem biztos, hogy tudunk győztest hirdetni. Adjatok meg egy ÚJ számot: "))

#létrehozok változókat a pontok regisztrálásához
score_player1 = 0
score_player2 = 0

#annyi kör lesz, ahányat a játékosok meghatároztak
for _ in range(requested_round_number):
      
      #minden körön belül elvégzek ellenőrzéseket, illetve megállapítok győztest
      while True:
            
            answer_player1 = input("Az első játékos válasza (kő, papír, olló): ").lower().strip()
            answer_player2 = input("A második játékos válasza(kő, papír, olló): ").lower().strip() 

            #vizsgálom a szó érvényességét. Ha nem érvényes bármelyik játékostól kapott szó, akkor újra bekérem a szavakat.
            if (answer_player1 not in ["kő", "papír", "olló"]) or (answer_player2 not in ["kő", "papír", "olló"]):
                print("Érvénytelen szó! Újra")
                continue 
            
            #ha ugyanazt a szót adják meg, érvénytelen a kör és újráztatok
            elif answer_player1 == answer_player2:
               print("Ez bizony most döntetlen! Újra!") 
               continue
               #ebben az esetben nem kap senki pontot   
        
            #a 3 elif-ben megadom mikor nyer az első játékos
            elif answer_player1 == "kő" and answer_player2 =="olló":
               print("A pont az első játékosé")
               score_player1 += 1
               break

            elif answer_player1 == "olló" and answer_player2 =="papír":
               print("A pont az első játékosé")
               score_player1 += 1
               break
        
            elif answer_player1 == "papír" and answer_player2 =="kő":
               print("A pont az első játékosé")
               score_player1 += 1
               break
        
            #az összes többi esetben a 2. játékos nyer
            else:
               print("A pont a második játékosé")
               score_player2 += 1
               break

#a result változóban eltárolom a győztes nevét és az eredmény alakulását
result = f"Első játékos nyert, {score_player1} : {score_player2} arányban." if score_player1 > score_player2 else f"Második játékos nyert, {score_player2} : {score_player1} arányban."

#kiprintelem az eredményt
print(result)