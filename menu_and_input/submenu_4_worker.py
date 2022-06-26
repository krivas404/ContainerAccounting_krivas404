from menu_and_input.input_parser import parse_input
from database.current_db_courier_and_containers_info import query_container_all_last_places, query_courier_all_last_containers


def submenu_4_worker():
    while True:
        _parsed_input = parse_input()
        _prefix = _parsed_input[0]
        _code = _parsed_input[1]

        if _code == 'q':
            return 'quit'
        if _prefix == 'menu':
            if _code == '1':
                submenu_4_1()
            if _code == '2':
                submenu_4_2()
            if _code == '3':
                submenu_4_3()
        return


def submenu_4_1():
    """Creating daily report about containers in/out"""
    querydb_all_containeers_movement()
    pass


def submenu_4_2():
    """Printing last report date and time"""
    querydb_last_report_datetime()
    pass


def submenu_4_3():
    """Print weekly report about courier or container"""
    _parsed_input = parse_input()
    _prefix = _parsed_input[0]
    _code = _parsed_input[1]

    if _code == 'q':
        return 'quit'
    if _prefix == 'digits':
        print_container_last_places(_code, 'week')
        return
    if _prefix == 'hm':
        print_courier_last_containers(_code, 'week')
        return
    pass


def print_container_last_places(container_code, data):
    query = query_container_all_last_places(container_code, data)
    print(query)
    return

def print_courier_last_containers(courier_code, data):
    query = query_courier_all_last_containers(courier_code, data)
    print(query)
    return