# 2 feladat

korok_szama = int(input("Add meg hány körből álljon a játék: "))

j1_pont = 0
j2_pont = 0

while korok_szama % 2 != 1:
    korok_szama = int(input("Csak páratlan számot adját meg: "))

for i in range(1, korok_szama + 1):
    print(f"----{i}. kör----")
    nyertes = 0
    while nyertes == 0:
        jatekos1 = input("játékos1 válassz egyet: kő(k), papír(p), olló(o): ")
        jatekos2 = input("Játékos2 válassz egyet: kő(k), papír(p), olló(o): ")
        # while jatekos1 != "k" or jatekos1 != "p" or jatekos1 != "o":
        #     jatekos1 = input("játékos1 válassz egyet: kő(k), papír(p), olló(o): ")
        print(f"Játékos választása: {jatekos1}")

        # while jatekos2 != "k" or jatekos2 != "p" or jatekos2 != "o":
        #     jatekos2 = input("Játékos2 válassz egyet: kő(k), papír(p), olló(o): ")
        print(f"Játékos választása: {jatekos2}")

        if jatekos1 == jatekos2:
            print("Döntetlen")
            nyertes = 0
        elif (jatekos1 == "k" and jatekos2 == "o") or \
                (jatekos1 == "p" and jatekos2 == "k") or \
                (jatekos1 == "o" and jatekos2 == "p"):
            print(f"{i}. kör nyertese: {jatekos1}")
            nyertes = 1
        else:
            print(f"{i}. kör nyertese: {jatekos2}")
            nyertes = 2

        if nyertes == 1:
            j1_pont += 1
        else:
            j2_pont += 1

print("=====Játék vége=====")
print(f"1. játékos pontjai: {j1_pont}")
print(f"2. játékos pontjai: {j2_pont}")

if j1_pont > j2_pont:
    print("Az 1. játékos nyert!")
else:
    print("A 2. játékjos nyert!")
        


