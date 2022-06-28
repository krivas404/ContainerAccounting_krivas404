from menu_and_input.input_parser import parse_input


def submenu_5_worker():
    while True:
        _parsed_input = parse_input()
        _prefix = _parsed_input[0]
        _code = _parsed_input[1]

        print('В разработке. Пожалуйста, введите q чтобы выйти в главное меню.')

        if _code == 'q':
            return 'quit'