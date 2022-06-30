from menu_and_input.input_parser import parse_input

"""menu 2 - id контейнера или курьера -> узнать все привязки в базе данных по введённому id"""

def submenu_2_worker():
    print_all_containeers_on_hands()
    while True:
        _parsed_input = parse_input()
        _prefix = _parsed_input[0]
        _code = _parsed_input[1]

        if _code == 'q':
            return 'quit'
        return

def print_all_containeers_on_hands():
    """send request to database to print on the screen all containeers what couriers have on hands"""
    pass

