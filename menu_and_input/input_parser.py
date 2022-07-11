from menu_and_input.input import take_input
from exceptions import LenghtInputError


def parse_input():
    raw_input = take_input()

    if len(raw_input) == 1:  # Check if it's menu item
        # Now finding what is the menu item here
        if raw_input == '1':
            return 'menu', 1
        if raw_input == '2':
            return 'menu', 2
        if raw_input == '3':
            return 'menu', 3
        if raw_input == '4':
            return 'menu', 4
        if raw_input == '5':
            return 'menu', 5
        if raw_input == '6':
            return 'menu', 6
        if raw_input.lower() == 'q' or raw_input.lower('в'):
            return 'menu', 'quit'

    # If it's not menu item, than parse input for check other cases
    if raw_input.isdigit() and len(raw_input) == 6:  # In project architecture, all digits have 6 char codes
        return 'digits', raw_input

    # Input is not menu item, and it's not digits. Than, it's item code with prefix, or error
    # Now check lenght, it must be^ 2 chars from prefix + 6 digits from code = 8 chars.

    if len(raw_input) != 8:
        error_message = 'Введённое значение не распознано. Возможно, опечатка. Попробуйте ещё раз'
        print(error_message)
        raise LenghtInputError

    # Other errors checks will be done in functions who take return from menu's
    # Now just take prefix(first 2 chars) and code(6 digits) from input and return
    prefix = raw_input[:2]
    code = raw_input[2:]
    return prefix, code




import keyboard
from re import match
from string import ascii_lowercase, digits

key_press_log = ''  #global

keys_for_registration = ascii_lowercase + digits
human_regexp = r'hm\d{6}'
container_regexp = r'..5\d{5}'
quit_regexp = r'q'
command_regexp = r'cm\d{6}'

def is_code(user_input: str):
    last_8_chars = user_input[-8::]
    print(last_8_chars)
    if match(human_regexp, last_8_chars):
        return ''
    if match(container_regexp, last_8_chars):
        print('container')
    if match(quit_regexp, last_8_chars[-1]):
        print('menu')
    if match(command_regexp, last_8_chars):
        print('command')


def keypress_logging(key):
    f = open('logs.txt', 'w')
    f.write(key)
    f.close()

    global key_press_log
    if len(key_press_log) > 50:
        key_press_log = key_press_log[-10::]

def print_pressed_keys(e):
    key_pressed = e.name.lower()
    keypress_logging(key_pressed)
    print(key_pressed)
    global key_press_log
    if key_pressed in keys_for_registration:
        # print('match: ', key_pressed)
        key_press_log += key_pressed
        is_code(key_press_log)


print(keys_for_registration)
keyboard.on_press(print_pressed_keys)
keyboard.wait('esc')
# print('ending: ', key_press_log)
