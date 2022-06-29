from database.models import Courier

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
    keyboard = input(f'\n Если всё верно, введите "Y", если требуется изменить данные, введите "N",'
                     f'или введите "Q" для выхода: ')
    keyboard = keyboard.lower()
    if keyboard == "y":
        new_courier = Courier(courier_first_name, courier_last_name, courier_name_from_father)
        new_courier.
    elif keyboard == "n":
        create_new_courier()
    elif keyboard == "q":
        return
    return
