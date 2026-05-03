import sei_init as si


def todo_fileread() -> list:
    '''
    Attempts to open the saved to-do list.
    '''
    todo_list: list = []
    try:
        with open(si.WORKING_DIR / 'todo_list.txt', 'r', encoding='utf-8') as file:
            for todo in file:
                todo_list.append(todo.strip())

    except FileNotFoundError:
        si.logger.error(si.messages['err_source'])

    return todo_list


def todo_filewrite(todo_list: list) -> None:
    '''
    Writing a to-do list to a file
    '''
    si.logger.info(si.messages['inf_write'])
    with open(si.WORKING_DIR / 'todo_list.txt', 'w', encoding='utf-8') as file:
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
        si.logger.error(si.messages['err_notexi'])
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
        si.logger.warning(si.messages['war_choose'])
        return None

    except KeyboardInterrupt:
        si.logger.error(si.messages['err_unauth'])
        return None
