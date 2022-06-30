from database.dbsession import Courier, Session

def create_new_courier():
    '''
    Function ask user to enter couriers name and call creating new Courier object,
    then push Courier to database
    '''
    courier_last_name = input("Введите фамлию: ")
    courier_first_name = input("Введите имя: ")
    courier_name_from_father = input("Введите отчество: ")
    print(f'Будет добавлен курьер со следующими ФИО: '
          f'{courier_last_name} {courier_first_name} {courier_name_from_father}'
          )
    keyboard = input(f'\n Если всё верно, введите "Д". Если требуется изменить данные, введите "Н",'
                     f'или введите "Q" для выхода: ')
    keyboard = keyboard.lower()
    if keyboard == "y" or keyboard == 'д':
        session = Session()
        new_courier = Courier(courier_first_name, courier_last_name, courier_name_from_father)
        session.add(new_courier)
        session.commit()
        session.flush()
        session.close()

    elif keyboard == "n" or keyboard == 'н':
        create_new_courier()
    elif keyboard == "q" or keyboard == 'в':
        return
    return
