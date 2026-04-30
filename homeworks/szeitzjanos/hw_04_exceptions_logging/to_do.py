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
import logging.config
import pathlib


def todo_fileread() -> list:
    '''
    Attempts to open the saved to-do list.
    '''
    todo_list: list = []
    try:
        with open(WORKING_DIR / 'todo_list.txt', 'r', encoding='utf-8') as file:
            for todo in file:
                todo_list.append(todo.strip())

    except FileNotFoundError:
        logger.error(error_messages[1])

    return todo_list


def todo_filewrite(todo_list: list) -> None:
    '''
    Writing a to-do list to a file
    '''
    logger.info(info_messages[1])
    with open(WORKING_DIR / 'todo_list.txt', 'w', encoding='utf-8') as file:
        for todo in todo_list:
            file.write(todo + '\n')


def todo_show(todo_list: list) -> None:
    '''
    Showing a to-do list
    '''
    print('\nThe list contains the following tasks:')
    for index, todo in enumerate(todo_list):
        print(f'\t {index + 1} - {todo}')


def todo_append(todo_list: list) -> list:
    '''
    Adding items to the to-do list
    '''
    todo = input('Enter the activity to add to the list: ')
    todo_list.append(todo)
    return todo_list


def todo_delete(todo_list: list) -> list:
    '''
    Removing an item from a list
    '''
    todo = input('Enter the activity you want to remove from the list: ')
    try:
        todo_list.remove(todo)
        print(f'OK, {todo} removed!')

    except ValueError:
        logger.error(error_messages[2])
        print(f'ERROR: {todo} not exist!')

    return todo_list


def display_menu(choices: list) -> None:
    '''
    Printing a menu and listing the available choices
    '''
    print('----------------------------------------------')
    for choice in choices:
        print(choice)


def get_user_answer() -> int:
    '''
    It prompts the user for input.
    '''
    try:
        return int(input('\nPlease select one of the options above! '))

    except ValueError:
        logger.warning(warning_messages[0])
        return None

    except KeyboardInterrupt:
        logger.error(error_messages[0])
        return None


# INITS
WORKING_DIR: str = pathlib.Path('homeworks') / 'szeitzjanos' / \
    'hw_04_exceptions_logging'

LOGGING_DIR: str = pathlib.Path(WORKING_DIR) / 'logs'
LOGGING_DIR.mkdir(exist_ok=True)

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'classic': {
            'format': '%(asctime)s • %(levelname)s • %(message)s',
            'datefmt': '%Y-%m-%d • %H:%M:%S'
        },
        'minimal': {
            'format': '%(asctime)s • %(message)s',
            'datefmt': '%m-%d • %H:%M'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'classic',
            'level': 'INFO'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': LOGGING_DIR / 'todo_list.log',
            'mode': 'a',
            'encoding': 'utf-8',
            'formatter': 'classic',
            'level': 'INFO'
        }
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO'
    }
}

avaiable_choices: list = [
    '\n\t1. Add Task',
    '\t2. View Task',
    '\t3. Remove Task',
    '\t4. Exit'
]

info_messages: list = [
    'Show the todo list',
    'Writing a list to a file',
    'Leave the Matrix',
    'Adding items to the to‑do list',
    'Removing an item from a list'
]

error_messages: list = [
    'Unauthorized exit is not allowed!',
    'The source file cannot be found! An empty to-do list has been created.',
    'The specified activity does not exist.'
]

user_choice: int = 0

warning_messages: list = [
    'Please choose a number from the following options: 1, 2, 3, 4.'
]


# CODE
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

todo_list = todo_fileread()

while user_choice != 4:
    display_menu(avaiable_choices)
    user_choice = get_user_answer()

    if user_choice == None:
        continue

    if user_choice not in range(1, 5):
        logger.warning(warning_messages[0])
        continue

    if user_choice == 1:
        logger.info(info_messages[3])
        todo_list = todo_append(todo_list)
        print('The list has been extended.')

    elif user_choice == 2:
        logger.info(info_messages[0])
        todo_show(todo_list)

    elif user_choice == 3:
        logger.info(info_messages[4])
        todo_list = todo_delete(todo_list)

    else:
        todo_filewrite(todo_list)
        logger.info(info_messages[2])
        print('Bye!')
