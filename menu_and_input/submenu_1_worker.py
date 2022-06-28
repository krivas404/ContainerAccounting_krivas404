from menu_and_input.input_parser import parse_input


menu_command_push_to_db = '000001'
menu_command_del_from_db = '000002'
menu_command_clean_input = '000003'

def main():
    if parsed_input[1] == 'q':
        return
    

def submenu_1_worker():
    """take types and codes. stuck it until take command for clear stack or push to database"""
    human = ''
    containeers = []
    command = 0

    while True:
        _parsed_input = parse_input()  # take parsed input from user
        _prefix = _parsed_input[0]  # split input on prefix and code
        _code = _parsed_input[1]  # split input on prefix and code

        print(
            'Тестовая информация. Последний ввод: ', _parsed_input,
            '\nТекущие используемые данные: ' +
            '\nСотрудник: ', human,
            '\nКонтейнер: ', containeers
              )

        if _code == 'q':
            return 'quit'
        if _prefix == 'hm':
            human = _code
            continue
        if _prefix == 'digits':
            containeers.append(_code)
            continue
        if _prefix == 'cm':
            command = _code
            do_command(human, containeers, command)  # use inputed data to add/del data in database

            human = ''          # reset value variables to empty
            containeers = []    # reset value variables to empty
            command = 0         # reset value variables to empty

            continue
        print('Команда не опознана, попробуйте ещё раз')
    return

def do_command(human, containers, command):
    if command == menu_command_push_to_db:
        push_human_and_containers_to_database(human, containers)
        return
    if command == menu_command_del_from_db:
        delete_human_and_containers_from_database(human, containers)
        return
    if command == menu_command_clean_input:  # do nothing, variables value resetting not here
        print(
            'Сотрудник: ' + human + '\nКонтейнеры: ' + '\n' + containers + '\n КОД - обнулить введённые данные \nтест')
        return


def push_human_and_containers_to_database(human, containers):
    print('Сотрудник: ', human, '\nКонтейнеры: ', '\n, containers' + '\nКОД - выдать контейнеры сотруднику \nтест')
    pass

def delete_human_and_containers_from_database(human, containers):
    print('Сотрудник: ', human, '\nКонтейнеры: \n', containers, '\n КОД - принять контейнеры на склад \nтест')
    pass