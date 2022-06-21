def main_menu():
    print(
        "Меню:\r"
        "1 - выдача контейнеров/приём контейнеров\r"
        "2 - Вывести все контейнеры на руках курьеров\r"
        "3 - Поиск по контейнеру или курьеру\r"
        "4 - вывод информации о контейнерах на руках курьеров\r"
        "5 - вывод отчёта об отданных/принятых контейнерах за сутки по фио курьеров\r"
        "6 - тест сканера и штрихкодов\r"
        "Введите цифру пункта меню, и нажмите Enter\r"
        "Из любого меню можно выйти назад, нажав Q\r"
          )

def submenu_1_give_take_containers():
    print(
        "ШК = Штрих или QR код"
        "Отсканируйте один или несколько ШК контейнеров, затем отсканируйте ШК сотрудника\r"
        "Далее отсканируйте ШК 'Выдать' чтобы провести выдачу контейнеров на руки сотрудника\r"
        "Либо отсканируйте ШК 'Принять' чтобы принять контейнеры на склад\r"
        "Отсканируйте ШК 'Сброс' чтобы обнулить сбросить все просканированные ШК, и начать операцию"
        "выдачи или получения заново"
    )


def submenu_2_info_about_handon_containers():
    print(
        "Ниже вы видете все контейнеры, которые сейчас числятся на руках у курьеров\r"
    )

def submenu_3_search_info_about_couriers_or_containers():
    print(
        "Введите id контейнера, для поиска места, где сейчас находится контейнер\r"
        "Введите id курьера, для поиска всех контейнеров у него на руках\r"
        "Введите q для выхода в предыдущее меню\r"
    )


def submenu_3_report_about_containers_today():
    """print menu for report about all give on/take back operations with containers"""
    print(
        "1 - печать отчёт"
        "2 - дата последнего вывода отчёта"
        "3 - "

    )
3.1 - дата последнего вывода отчёта
			3.2 - сохранение отчёта в файл
			3.3 вывод всей информации о контейнерах, полученных конкретным сотрудником за неделю
			3.4 вывод всей информации о сутрудниках, у которых был искомый контейнер




def submenu_4_testmenu():
    '''print menu for test'''
    print(
        "Отсканируйте любой штрих-код, и на экране появится вся известная информация:\r"
        "что отсканировано, и какие записи об этом коде лежат в памяти программы или в базе данных\r"
    )