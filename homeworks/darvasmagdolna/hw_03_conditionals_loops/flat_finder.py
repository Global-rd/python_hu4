# 1 feladat

varos = input ("Add meg milyen városban szeretnél lakni: ")
lakber = int(input("Add meg mennyi lakbért fiztenél: "))

if (varos == "New York" or varos == "San Fransico") and lakber < 4000: 
    print(f"{varos}-ba költözik {lakber}-USD lakbér")
elif varos == "Washington":
    print ("Semmi pénzért nem költözik oda")
elif varos == "Chicago": 
    print("Bármennyi pénzért odaköltözne")
elif lakber <= 3000:
    print(f"{varos}-ba odaköltözne")
else: 
    print("Nem költözik el.")

