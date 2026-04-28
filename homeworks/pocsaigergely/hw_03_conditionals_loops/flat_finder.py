
newy = "New York"
sanf = "San Fransisco"
wash = "Washington"
chic = "Chicago"

city = input("Desired city to live in: ")
rent = int(input("Available money for rent: "))

if city == chic:
    print(f"City: ", city, "for", rent, "is acceptable")

elif city == chic:
    print(f"City: ", city, "for", rent, "is NOT acceptable")

elif (city == newy or city == sanf):
    if(3000 < rent < 4000):
        print(f"City: ", city, "for", rent, "is acceptable")
    else: 
        print(f"City: ", city, "for", rent, "is NOT acceptable")

else:
    if(rent <= 3000):
        print(f"City: ", city, "for", rent, "is acceptable")
    else: 
        print(f"City: ", city, "for", rent, "is NOT acceptable")