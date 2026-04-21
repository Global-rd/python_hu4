'''
FELADAT 2:

    while és for loop használata

    Hozz létre egy rock_paper_scissors.py nevű file-t, és kódold le a
    következő feladat megoldását:                                          (OK)

    Írj egy python programot ami levezényli a kő-papír-olló játékot két
    játékos között.

    A program kérje be, hogy hány kört akarnak játszani a játékosok. Figyelj
    oda, hogy olyan számot kell megadnia a felhasználónak ami mellett nem
    tudnak döntetlent játszani!

    Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a
    körök számát amíg páratlan számot nem ad meg.

    Ezután a program felváltva kérje be az első és második játékos válaszát,
    ami kizárólag a következő stringek valamelyik lehet:

        "rock", "paper", "scissors".

    Ellenkező esetben kezeld úgy a hibát ahogy a körök számánál.
    Egy adott kör addig ne érjen véget, amíg valaki nem nyer (döntetlen esetén
    az adott kört újra kell játszani).

    Tárold a nyertesek pontjait, és minden kör végén növeld az aktuális
    játékos pontszámát. A végén printeld ki ki nyert, és hány ponttal.
'''

rounds: (int) = 0
player_one_points: (int) = 0
player_two_points: (int) = 0
good_answers: (set) = {'rock', 'paper', 'scissors'}

while rounds % 2 == 0:
    rounds = int(input('How many rounds would you like to play? '))
    if rounds % 2 == 0:
        print(f'{rounds}? Unfortunately, this way the game can end in a draw.')
        print('You need to enter an odd number of rounds!\n')

while rounds > 0:
    print(f'\nNumber of remaining rounds: {rounds}')
    print(f'  Choose from the available options: {str(good_answers)[1:-1]}.')

    player_one = input('  Player one, what do you choose? ').lower()
    player_two = input('  Player two, what do you choose? ').lower()

    if {player_one, player_two} - good_answers:
        print('You entered an invalid option! Try to be more mindful!')
        continue

    if player_one == player_two:
        print("Same choices — it’s a draw! Let’s replay the round!")
        continue

    if (
       player_one == 'rock' and player_two == 'paper' or
       player_one == 'paper' and player_two == 'scissors' or
       player_one == 'scissors' and player_two == 'rock'
       ):
        player_two_points += 1
    else:
        player_one_points += 1

    rounds -= 1

text = 'two' if player_one_points < player_two_points else 'one'
print(f'\nPlayer {text} is the winner! Final result: {player_one_points}:'
      f'{player_two_points}. '
      f'Win by {abs(player_one_points - player_two_points)} points.')
