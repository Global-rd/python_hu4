import pathlib
import logging.config


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

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

avaiable_choices: list = [
    '\n\t1. Add Task',
    '\t2. View Task',
    '\t3. Remove Task',
    '\t4. Exit'
]

messages: dict = {
    'inf_show': 'Show the todo list',
    'inf_write': 'Writing a list to a file',
    'inf_leave': 'Leave the Matrix',
    'inf_adding': 'Adding items to the to‑do list',
    'inf_remove': 'Removing an item from a list',
    'err_unauth': 'Unauthorized exit is not allowed!',
    'err_source': 'The source file cannot be found! An empty to-do list has been created.',
    'err_notexi': 'The specified activity does not exist.',
    'war_choose': 'Please choose a number from the following options: 1, 2, 3, 4.'
}
