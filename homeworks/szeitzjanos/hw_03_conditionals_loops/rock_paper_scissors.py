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

# INITS
rounds: int = 0
player_one_points: int = 0
player_two_points: int = 0
good_answers: list = ['rock', 'paper', 'scissors']


# DEFS
def get_rounds() -> int:
    # Bekéri a játékkörök számát.

    return int(input('How many rounds would you like to play? '))


def warning_rounds() -> None:
    # Figyelmeztet, ha páros számú a játékmenet.

    print(f'{rounds}? Unfortunately, this way the game can end in a draw.')
    print('You need to enter an odd number of rounds!\n')


def print_rounds(rounds: int) -> None:
    # Kiírja körök számát és a választási lehetőségeket.

    print(f'\nNumber of remaining rounds: {rounds}')
    print(f'  Choose from the available options: {str(good_answers)[1:-1]}.')


def get_player_choose(player: int) -> int:
    # Bekéri a játékos tippjét.

    print(f'  Player {player}, what do you choose? ', end='')
    return input().lower()


def is_correct_answer(answer: str) -> bool:
    # Ellenőrzi a helyes opciók közül a tippet.

    if answer in good_answers:
        return True
    else:
        return False


def warning_player(player: str) -> None:
    # Figyelmeztet hibás tipp esetén.

    print(f'Player {player} entered an invalid option! Try again!')


def is_players_draw(player_one: str, player_two: str) -> bool:
    # Ellenőrzi a tipp egyezőséget.

    return player_one == player_two


def warning_draw() -> None:
    # Figyelmeztet tipp egyezőség esetén.

    print("Same choices — it’s a draw! Let’s replay the round!")


def is_player_one_the_round_winner(player_one: str, player_two: str) -> bool:
    # Eldönti, melyik játékos tippje az erősebb.

    if (
       player_one == 'rock' and player_two == 'paper' or
       player_one == 'paper' and player_two == 'scissors' or
       player_one == 'scissors' and player_two == 'rock'
       ):
        return False
    else:
        return True


def print_resoult(player_one_points: int, player_two_points: int) -> None:
    # A végerdmény kiíratása.

    text = 'two' if player_one_points < player_two_points else 'one'
    print(f'\nPlayer {text} is the winner! Final result: {player_one_points}:'
          f'{player_two_points}. '
          f'Win by {abs(player_one_points - player_two_points)} points.')


# CODE
while rounds % 2 == 0:
    rounds = get_rounds()
    if rounds % 2 == 0:
        warning_rounds()

while rounds > 0:
    print_rounds(rounds)

    is_player_one_correct_answer = False
    is_player_two_correct_answer = False

    while not is_player_one_correct_answer:
        player = get_player_choose('one')
        if is_correct_answer(player):
            player_one = player
            is_player_one_correct_answer = True
        else:
            warning_player('one')

    while not is_player_two_correct_answer:
        player = get_player_choose('two')
        if is_correct_answer(player):
            player_two = player
            is_player_two_correct_answer = True
        else:
            warning_player('two')

    if is_players_draw(player_one, player_two):
        warning_draw()
        continue

    if is_player_one_the_round_winner(player_one, player_two):
        player_one_points += 1
    else:
        player_two_points += 1

    rounds -= 1

print_resoult(player_one_points, player_two_points)
