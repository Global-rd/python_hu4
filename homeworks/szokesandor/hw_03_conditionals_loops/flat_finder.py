"""
A program Sarah-nak nyújt segítséget a lakáskeresésben.

"""
# Kiírjuk, hogy a program mire használható
print("Let's help Sarah decide if the apartment is right for her.")

# Ciklust alkalmazunk, hogy több vizsgálatra is legyen lehetőség.
answer = "Y"
while answer in ["Y", "YES"]:
    #Bekérjük az adatokat
    print("Enter the details: ")
    city=input(" - in which city is the apartment located? ").strip().title() # A kezdő és záró szóközöket levágjuk és az inputot nagy kezdőbetűs szavakra konvertáljuk, hogy az összehasonlítás ne legyen kis- nagybetű érzékeny.
    rental_fee=int(input(" - monthly rental fee (USD): ")) # A havi albérleti díj összege

    # Eldöntjük, hogy a megadott városban az adott bérleti díjért megfelelő-e a lakás?
    if city in ["New York", "San Fransisco"] and rental_fee <= 4000:
        suitable_flat = True
    elif city == "Washington":
        suitable_flat = False
    elif city == "Chicago":    
        suitable_flat = True
    elif rental_fee <= 3000:
        suitable_flat = True
    else:
        suitable_flat = False

    """
    A fenti, több soros if utasítást szerintem ki lehetne váltani egy egy soros logikai értékadással, az alábbiak szerint. (Persze ez nem annyira átlátható.)

    suitable_flat = city in ["New York", "San Fransisco"] and rental_fee <= 4000  or city == "Chicago" or rental_fee <= 3000 and city != "Washington"
    """
    
    # Kiírjuk a választ
    print(f"The apartment in {city} for {rental_fee} USD is {"" if suitable_flat else "not "}right for her.")

    # Megkérdezzük, szeretne-e további esetet megadni?
    answer = input("Would you like to check another apartment? (y/n) ").strip().upper() # A kezdő és záró szóközöket levágjuk és a választ nagybetűre alakítjuk, hogy vizsgálat ne legyen kis- nagybetű érzékeny.
    print()


