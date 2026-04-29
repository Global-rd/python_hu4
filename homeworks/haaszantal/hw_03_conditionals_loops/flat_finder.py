#városnév bekérése, nagybetűsítés és szöközök eltávolítása a string elejéről és végéről
answered_city = input("Melyik városban szeretnél élni? ").upper().strip()

#összeg bekérése, a válasz integerré alakítása
answered_price = int(input("Mennyit USD-t szánsz a lakbérre? Add meg az összeget pont nélkül: "))

#moving változó definiálása
moving = False

#a feltételek vizsgálata
#if ((answered_city == "NEW YORK") or (answered_city == "SAN FRANCISCO")) and (answered_price < 4000): -- sok a zárójel.
#if (answered_city == "NEW YORK" or answered_city == "SAN FRANCISCO") and answered_price < 4000: -- ez így egyszerűbb
if answered_city in ["NEW YORK","SAN FRANCISCO"] and answered_price < 4000:
     moving = True
elif answered_city == "WASHINGTON":
     moving = False
elif answered_city == "CHICAGO":
     moving = True
#ezt össze lehet vonni:
#else:
#    if answered_price <= 3000:
#       moving = True
elif answered_price <= 3000: # Itt vontuk össze az else + if részt
    moving = True

#boolean típusú változó értékének szöveg megadása
result = "költözhetsz" if moving else "nem költözhetsz"

#a válasz kiprintelése
print (f"A megadott városba: ({answered_city}) {result}!")