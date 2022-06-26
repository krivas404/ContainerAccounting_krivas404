from menu_and_input.console_menu_text import *
from exceptions import NotMenuError
from menu_and_input.input_parser import parse_input
from menu_and_input.submenu import call_submenu


def start_main_menu():
    try:
        print_text_main_menu()
        _input = parse_input() #User must enter number of menu item, then string will be parsed
        print('главное_меню_инпут: ', *_input)
        call_submenu(*_input)  # Function take 2 position args
    except NotMenuError:
        print('Ошибка, вы ввели не пункт меню. Попробуйте ещё раз.')
        print_text_main_menu()
        _input = parse_input()
        call_submenu(*_input)  # Function take 2 position args
