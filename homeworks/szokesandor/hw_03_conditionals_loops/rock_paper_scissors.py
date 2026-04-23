"""
Két játékos között a kő-papír-olló játék levezénylése

"""
# Kulcs-érték párok, amelyekben a kulcs megadja, hogy melyik értéket győzi le. (A key a nyerő a value-hoz képest)
stronger_item = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"}

# Egy tuple-ba kigyűjtjük a fenti kulcs mezőket, hogy kéznél legyen egy felsorolás az inputban megadható értékekről. (Elvileg nem lenne rá szükség, csak az átláthatóságot segíti.)
items = tuple(stronger_item.keys())

print()
print("Lets play rock paper scissors!")
print()

# Bekérjük, hány kört szeretnének játszani?
while True:
    max_rounds = int(input("How many rounds would you like to play? "))
    if max_rounds % 2 == 0:     # Csak páratlan számot fogadunk el!
        print("An odd number must be entered!") # Páros szám esetén hibaüzenet jelenik meg, és a ciklus folytatódik.
        print()
    else:
        print()
        break

# Az alábbi lista tartalmazza a játékosok megnevezését, valamint ebben tároljuk az egyes körökben az adott játékos által adott tippet ("bet"), és gyüjtjük a játékos pontszámát ("score")
player = [
    {"name":"First player", "bet":None, "score":0},
    {"name":"Second player", "bet":None, "score":0}]

# Kezdőértéket adunk a ciklusban használt változóknak
round = 1            # Hányadik körben járunk
winners_name = None  # A nyertes neve, aki az adott kört nyerte

while round <= max_rounds: # A ciklus addig fut, amíg a lejátszott körök száma el nem éri a program eljén megadott értéket. A round értéke csak akkor növekszik, ha volt nyertes. Ha ugyanazt tippelték, akkor a ciklus újra ugyanazzal a round értékkel fut le.
    if winners_name == "Nobody":  
        # Ha az előző körben nem volt nyertes, akkor ugyanaz a round fut újra, és ilyenkor nem írjuk ki mégegyszer, hogy hányadik körben járunk
        pass
    else:
        # Ha a winners_name még üres vagy nem "Nobody" az értéke, akkor az azt jelenti, az előző körben volt nyertes vagy éppen most indul az első kör. Ilyenkor kírjuk, hogy hányadik kör kezdődik.
        print(f"-------{ "-" * len(str(round)) }")
        print(f"Round: {round}")
        print(f"-------{ "-" * len(str(round)) }")
        print()

    # Bekérjük mindkét játékos tippjét
    for i in range(0,2):  # A ciklus kétszer fut le, mert két játékos játszik. Az i értéke 0 és 1 lesz
        while True: # A belső ciklus addig fut, ameddig a játékos a megfelelő választ nem adja
            player[i]["bet"] = input(f"{player[i]["name"]}'s bet ({'/'.join(items)}): ").strip().lower()
            if player[i]["bet"] in items:   # Csak a "rock", "paper", "scissors" válaszokat fogajuk el (nem kis- nagybetű érzékeny)
                print()
                break # Jó válasz esetén kilépünk a belső ciklusból
            else:
                print(f"Wrong word! Enter {'/'.join(items)} !")  # Ha nem megfelelő az input, akkor hibaüzenet jelenik meg
                print()

    # Mindkét játékos megadta a tippjét, ezután megvizsgáljuk ki nyert. (Ha nyert egyáltalán valaki.)
    winners_idx = None # A változó majd a player listának arra az elemére mutat, aki az aktuális kört megnyerte. Itt adunk neki egy kezdőértéket.

    if stronger_item[player[0]["bet"]] == player[1]["bet"]:  # Az első játékos által adott tippet a stronger_item dictionary kulcsaként vesszük figyelembe, és a dictionary ezen kulcsa alapján hivatkozunk az ahhoz tartozó value-ra. Ha a value egyenlő a második játékos tippjével, akkor az első játékos tippje volt az erősebb.
        winners_idx = 0   # Eltároljuk, hogy ebben a körben a player lista első eleme a nyertes.
    elif stronger_item[player[1]["bet"]] == player[0]["bet"]: # Megvizsgáljuk a második játékos tippjét. Ha az ő tippje az erősebb mint az első játékosé, akkor ő a nyertes
        winners_idx = 1   # Eltároljuk, hogy ebben a körben a player lista második eleme a nyertes

    # Ha fenti if egyik ágába se lépett be a program, vagyis sem az első sem a második játékos tippje nem volt erősebb a másikénál, akkor nincs nyertes. A winners_idx értéke ilyenkor maradt None.
    if winners_idx == None: 
        winners_name = "Nobody"  # A "Nevem: senki" Mármint a nyertes neve senki.
        # Mivel nem volt nyertes, a round változó értékét nem növeljük meg, és így a ciklus ugyanazon sorszámú körrel fogja újra lefutni.
    else:
        # A winners_idx értéket kapott, tehát van nyertes
        player[winners_idx]["score"] += 1             # A nyertesnek megfelelő listaelem "score" kulcsa alatt megnöveljük a pontokat.
        winners_name = player[winners_idx]["name"]    # Beállítjuk a nyertes nevét tartalmazó változót
        print(f"{round}. round: ", end = "")          # Kiirjuk, hogy hányadik körben vagyunk, amit éppen megnyertek.
        round += 1                                    # Volt nyertes, tehát léphetünk a következő körre.

    print(f"{winners_name} wins!", end = "")          # Kiírjuk a nyertes nevét. Ha senki sem nyert, akkor "Nobody" jelenik meg.
    print(" Try again!" if winners_name == "Nobody" else "")  # Csak egy kis szépészet. Ha nincs nyertes, akkor kiírjuk, hogy "Try again!"
    print()

# Lefutott az összes kör. Eredményhirdetés következik:
print("-------------")
print("Final result:")
print("-------------")
print()
print(f"{player[0]["name"]}: {player[0]["score"]} point(s)")
print(f"{player[1]["name"]}: {player[1]["score"]} point(s)")
print(f"THE WINNER IS: { player[0]["name"] if player[0]["score"] > player[1]["score"] else player[1]["name"] }")
print()
