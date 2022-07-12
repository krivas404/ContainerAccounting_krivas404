import keyboard
from re import match
from string import ascii_lowercase, digits


last_keys_pressed = ''  # global, here all last key inputs from user
keys_for_registration = ascii_lowercase + digits
human_regexp = r'hm\d{6}'
container_prefix5_regexp = r'..5\d{5}'
quit_regexp = r'q'
command_regexp = r'cm\d{6}'
menu_regexp = r'[1-9]'


# def take_menu_input(text_for_input_print='Напишите пункт меню и нажмите Enter, или отсканируйте ШК: '):
#     keyboard_input = input(text_for_input_print)
#     return keyboard_input


def start_code_input():
    """Take raw input and parse codes humans, commands, quit, containers"""
    keyboard.on_press(code_key_handler)
    keyboard.wait('esc')
    pass


def code_key_handler(key_object):
    pressed_key_name = key_object.name.lower()
    global last_keys_pressed

    if pressed_key_name in keys_for_registration:
        keypress_logging(pressed_key_name)
        last_keys_pressed += pressed_key_name
        input_code_parser(last_keys_pressed)


def input_code_parser(user_input: str):
    last_8_chars = user_input[-8::]

    if match(human_regexp, last_8_chars):
        prefix, code = 'hm', last_8_chars[-6::]

    elif match(container_prefix5_regexp, last_8_chars):
        prefix, code = 'digits', last_8_chars[-6::]

    elif match(quit_regexp, last_8_chars[-1]):
        prefix, code = 'menu', 'q'

    elif match(command_regexp, last_8_chars):
        prefix, code = 'cm', last_8_chars[-6::]

    else:
        prefix, code = None, None
    return prefix, code


def start_menu_input():
    """Take raw input and parse menu digits and quit"""
    keyboard.on_press(menu_key_handler)
    keyboard.wait('esc')
    pass


def menu_key_handler(key_object):
    pressed_key_name = key_object.name.lower()
    global last_keys_pressed

    if pressed_key_name in keys_for_registration:
        keypress_logging(pressed_key_name)
        last_keys_pressed += pressed_key_name
        input_menu_parser(last_keys_pressed)


def input_menu_parser(user_input: str):
    last_char = user_input[-1]
    if match(rf'{menu_regexp}|{quit_regexp}', last_char):
        prefix, code = 'menu', last_char
    else:
        return None, None
    #
    # elif match(quit_regexp, last_char):
    #     prefix, code = 'menu', last_char
    return prefix, code


def keypress_logging(key):
    file = open('logs.txt', 'a')
    file.write(key)
    file.close()

    global last_keys_pressed
    if len(last_keys_pressed) > 100:
        last_keys_pressed = last_keys_pressed[-30::]


# keyboard.on_press(parser_menu_input)
# keyboard.wait('esc')
# print('ending: ', key_press_log)
