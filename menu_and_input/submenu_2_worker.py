from menu_and_input.input_parser import parse_input
from database.dbsession import Container, Session

"""menu 2 - id контейнера или курьера -> узнать все привязки в базе данных по введённому id"""

def submenu_2_worker():
    while True:
        _parsed_input = parse_input()
        _prefix = _parsed_input[0]
        _code = _parsed_input[1]

        if _code == 'quit':
            return 'quit'

        print_all_containeers_on_hands(_parsed_input)


def print_all_containeers_on_hands(prefix, code):
    """send request to database to print on the screen all containeers what couriers have on hands"""
    if prefix == 'digits':
        session = Session()
        query = session.query(Container).filter(Container.container_id == code)
        print(query)
    if prefix == 'hm':
        code = prefix + code
        session = Session()
        query = session.query(Container).filter(Container.container_id == code)


def print_query(query):
    pass