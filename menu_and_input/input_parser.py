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

