from database.models import Courier

def create_new_courier():
    Courier.last_name = input("Введите фамлию: ")
    Courier.first_name = ("Введите имя: ")
    Courier.name_from_father = input("Введите отчество: ")
    #push to database

    return