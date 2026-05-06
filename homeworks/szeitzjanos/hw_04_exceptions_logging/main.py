'''
FELADAT:
    Hozz létre egy to_do.py nevű file-t, és kódold le a következő feladat
    megoldását:

    Készíts egy Feladatkezelő alkalmazást!
        Definiálj 5 függvényt a következőkre: feladatok olvasása, feladatok
        írása, feladatok megjelenítése, egy feladat hozzáadása, egy feladat
        törlése

        Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges
        opciókat:

            1. Add Task
            2. View Tasks
            3. Remove Task
            4. Exit

    Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok
    közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt.

    A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! Ha az
    1-es vagy 3-as opciót választja, mindkét esetben paramétert kell átadnod a
    megfelelő függvénynek. “Exit”-re lépjen ki a program.

    Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve
    használd a logging module-t. Egyszerre logolj a konzolra és egy .log
    file-ba. A .txt file legyen része a pull request-nek.

TIPP:
    A program futása során a feladatokat memóriában (egy listában) tartsd
    nyilván (itt adj hozzá vagy törölj elemeket a function hívásoknál).

    A file-ból való olvasás automatikusan történjen meg a program indulásakor.
    A fájlba írás csak a program befejezésekor (“Exit” opció választásakor)
    történjen meg, ekkor a program írja felül a korábbi feladatlistát a
    módosított tartalommal (nem kell minden Add Task vagy Remove Task opciónál
    módosítani a file-t).
'''

# IMPS and DEFS
import logging
import sei_defs as sd
import sei_init as si


def main():
    todo_list: list = sd.todo_fileread()
    user_choice: int = 0

    while user_choice != 4:
        sd.display_menu(si.avaiable_choices)
        user_choice = sd.get_user_answer()

        if user_choice == None:
            continue

        if user_choice not in range(1, 5):
            si.logger.warning(si.messages['war_choose'])
            continue

        if user_choice == 1:
            si.logger.info(si.messages['inf_adding'])
            todo_list = sd.todo_append(todo_list)
            print('The list has been extended.')

        elif user_choice == 2:
            si.logger.info(si.messages['inf_show'])
            sd.todo_show(todo_list)

        elif user_choice == 3:
            si.logger.info(si.messages['inf_remove'])
            todo_list = sd.todo_delete(todo_list)

        else:
            sd.todo_filewrite(todo_list)
            si.logger.info(si.messages['inf_leave'])
            print('Bye!')


if __name__ == "__main__":
    main()
