from menu_and_input.input_parser import parse_input
from database.dbsession import Container, Session


def submenu_3_worker():
    while True:
        _parsed_input = parse_input()
        _prefix = _parsed_input[0]
        _code = _parsed_input[1]

        if _code == 'q':
            return 'quit'
        if _prefix == 'digits':
            print_container_last_places(_code, '3 days')
            return
        if _prefix == 'hm':
            print_courier_last_containers(_code,'3 days')
            return
    return


def query_container_all_last_places(container_code, data):
    session = Session()
    query = session.query(Container).filter(Container.container_id == container_code)
    print(query)


def print_container_last_places(container_code, data):
    query = query_container_all_last_places(container_code, data)
    print(query)
    return


def query_courier_all_last_containers(courier_code, data):
    session = Session()
    query = session.query(Container).filter(Container.container_id == courier_code)
    print(query)


def print_courier_last_containers(courier_code, data):
    return