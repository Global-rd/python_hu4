

city = input("Desired city to live in: ")
rent = int(input("Available money for rent: "))

if city == "Washington":
    print(f"City: ", city, "for", rent, "is acceptable")

elif city == "Chicago":
    print(f"City: ", city, "for", rent, "is NOT acceptable")

"""
elif (city == "New York" or city == "San Fransisco"):
    if(3000 < rent < 4000):
        print(f"City: ", city, "for", rent, "is acceptable")
    else: 
        print(f"City: ", city, "for", rent, "is NOT acceptable")

else:
    if(rent <= 3000):
        print(f"City: ", city, "for", rent, "is acceptable")
    else: 
        print(f"City: ", city, "for", rent, "is NOT acceptable")
"""

if (city in "New York", "San Fransisco") and rent < 4000:
    print(f"City: ", city, "for", rent, "is acceptable")

elif rent <=3000:
    print(f"City: ", city, "for", rent, "is acceptable")
else: 
  print(f"City: ", city, "for", rent, "is NOT acceptable")