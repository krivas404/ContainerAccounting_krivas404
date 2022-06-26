from menu_and_input.input_parser import parse_input


def submenu_4_worker():
    while True:
        _parsed_input = parse_input()
        _prefix = _parsed_input[0]
        _code = _parsed_input[1]

        if _code == 'q':
            return 'quit'