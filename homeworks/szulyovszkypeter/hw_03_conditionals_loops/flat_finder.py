'''
Feladat 1: Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra (if-elif-else, operátorok)
Hozz létre egy fl at_fi nder.py nevű fi le-t, és kódold le a következő feladat megoldását:
A feladat célja, hogy elsajátítsd azt a képességet hogy hétköznapi módon megfogalmazott feladatokat fordítasz
 le python-ra. Sarah-nak kell segítened a lakáskeresésben, a következőket tudjuk:
● Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne egy lakást, 
  ha az albérlet ára kevesebb mint 4000 USD havonta.
● Gyűlöli Washington-t, és semmi pénzért nem lakna ott
● Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért hogy ott lakhasson
● Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér ellenében költözne oda.
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát. 
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
'''
# két változatott csinálok, hogy gyakoroljak
print('Sarah lakáskeresésének segítése:')
#Város és a lakbér árának bekérése
city = input("Add meg a várost, ahova költözni szeretnél: ").title()
rent = input("Add meg a havi lakbér árát (USD): ")
# ez egy kicsit hosszabb, személyesebb változat 
print('Első változat')
if rent.isdigit():
    rent = int(rent)
    in_message = f"Be tudsz költözni {city} városba a(z) {rent} USD-os lakbérrel!"
    not_in_message = f"Nem tudsz {city} városába költözni a(z) {rent} USD-os lakbérrel!"
    if city == "New York" or city == "San Francisco": #ez lehet in is, így a hagyományos
        if rent < 4000:
            print(in_message)
        else:
            print(not_in_message)
    elif city == "Washington":
        print(f"Nem akarsz {city} városába költözni! Elfelejteted?")
    elif city == "Chicago":
        print(f"{in_message} Bármennyit fizethetek, mert imádod! ")
    else:
        if rent <= 3000:
            print(in_message)
        else:
            print(not_in_message)
else:
    print(f"A lakbér árának \"{rent}\" egész számnak kell lennie!")

print('Második változat')
rent = str(rent)  #ez csak azért, hogy ne akadjon ki a második változatban, mert mert az elsőben már int lett 
if rent.isdigit():
    rent = int(rent) 
    if city in ["New York", "San Francisco"]:
        can_move = rent<4000
    elif city == "Chicago":
        can_move = True
    elif city == "Washington":
        can_move = False
    else:
        can_move = rent<=3000
    if can_move:
        print(f"Be tudsz {city} városába költözni a(z) {rent} USD-os lakbérrel!")
    else:
        print(f"Nem tudsz {city} városába költözni a(z) {rent} USD-os lakbérrel!")
    print('---------------')
    # egy másik változa csak a teszt kedvéért
    prefix = "Be" if can_move else "Nem"
    print(f"{prefix} tudsz {city} városába költözni a(z) {rent} USD-os lakbérrel!")
    print('---------------')
    # na még egy változat, hogy ez is személyesebb legyen
    was_chi = f"{" Mert utálod Washingtont! " if city == "Washington" else ""}{" Bármennyit fizethetek, mert imádod!! " if city == "Chicago" else ""}"
    print(f"{"Be" if can_move else "Nem"} tudsz {city} városába költözni a(z) {rent} USD-os lakbérrel!"+was_chi ) 
else:
    print(f"A lakbér árának \"{rent}\" egész számnak kell lennie!")

