'''
FELADAT 1:
    Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra
    (if-elif-else, operátorok)

    Hozz létre egy flat_finder.py nevű file-t, és kódold le a következő feladat
    megoldását:                                                            (OK)

    A feladat célja, hogy elsajátítsd azt a képességet hogy hétköznapi módon
    megfogalmazott feladatokat fordítasz le python-ra. Sarah-nak kell segítened
    a lakáskeresésben, a következőket tudjuk:

    -   Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban
        kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD
        havonta.

    -   Gyűlöli Washington-t, és semmi pénzért nem lakna ott

    -   Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit
        megadna azért hogy ott lakhasson

    -   Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
        ellenében költözne oda.

    Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
    Ezután a fentiek alapján printeld ki egy f-string használatával hogy az
    adott feltételek (város és albérlet ára) mellett be tudna e költözni az
    adott helyre.
'''

city: str = input('Please provide the location of the property; in which'
                  ' city is it located: ').title()
rental_fee: str = input('Please provide the monthly rental fee of the '
                        'property: ')

if rental_fee.isnumeric():
    rental = int(rental_fee)
    is_moving = False

    if (
       (city in ['New York', 'San Francisco'] and rental < 4000)
       or city == 'Chicago'
       or rental <= 3000
       ):
        is_moving = True

    if city == 'Washington':
        is_moving = False

    print(f"Under the given conditions ({city} and {rental}USD/month), Sarah"
          f" can{"" if is_moving else "'t"} move to the city.")

else:
    print('Please provide a numeric value!')
