"""
A program Sarahnak segít lakás keresésben
több városban, különböző árakkal, amiket Sarah elfogadna.
"""


#Bekérem azt, hogy hol van a lakás amit bérelni szeretne?
city = input("In which city is the apartment located?").strip().title() 
rent = int(input("Monthly rental fee (USD):? "))

# Meghatározom az eredméynt az igények alapján 
if city == "Washington":
    suitable = False
elif city == "Chicago":
    suitable = True
elif city in ["New York", "San Francisco"]:
    suitable = rent < 4000
else:
    suitable = rent <= 3000

# A megadott adatok alapján kiírom egy f stringben, hogy az adott városban adott ár mellett megfelele-e Sarah feltételeinek vagy sem. 
print(f"The apartment in {city} for {rent} USD/month {'is' if suitable else 'is not'} suitable for Sarah.")