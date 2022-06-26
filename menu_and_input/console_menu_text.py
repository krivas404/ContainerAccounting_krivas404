
def print_text_main_menu():
    print("Меню:\n" +
        "1 - выдача контейнеров/приём контейнеров\n" +
        "2 - Вывести все контейнеры на руках курьеров\n" +
        "3 - Поиск по контейнеру или курьеру\n" +
        "4 - вывод информации о контейнерах на руках курьеров\n" +
        "5 - вывод отчёта об отданных/принятых контейнерах за сутки по фио курьеров\n" +
        "6 - тест сканера и штрихкодов\n" + "Введите цифру пункта меню, и нажмите Enter\n" +
        "Из любого меню можно выйти назад, нажав Q\n"
          )

def print_text_submenu_1_give_take_containers():
    print(
        "ШК = Штрих или QR код\n" +
        "Отсканируйте один или несколько ШК контейнеров, затем отсканируйте ШК сотрудника\n" +
        "Далее отсканируйте ШК 'Выдать' чтобы провести выдачу контейнеров на руки сотрудника\n" +
        "Либо отсканируйте ШК 'Принять' чтобы принять контейнеры на склад\n" +
        "Отсканируйте ШК 'Сброс' чтобы обнулить сбросить все просканированные ШК, и начать операцию\n" +
        "выдачи или получения заново"
    )


def print_text_submenu_2_info_about_handon_containers():
    print(
        "Ниже вы видете все контейнеры, которые сейчас числятся на руках у курьеров\n"
    )


def print_text_submenu_3_search_info_about_couriers_or_containers():
    print(
        "Введите id контейнера, для поиска места, где сейчас находится контейнер\n" +
        "Введите id курьера, для поиска всех контейнеров у него на руках\n" +
        "Введите q для выхода в предыдущее меню\n"
    )


def print_text_submenu_4_report_about_containers_today():
    """print menu for report about all give on/take back operations with containers"""
    print(
        "1 - создать отчёт за сутки\n" +
        "2 - дата последнего вывода отчёта\n" +
        "3 - вывод всей информации о контейнере/сотруднике за неделю\n"
    )


def print_text_submenu_5_testmenu():
    '''print menu for test'''
    print(
        "Отсканируйте любой штрих-код, и на экране появится вся известная информация:\n" +
        "что отсканировано, и какие записи об этом коде лежат в памяти программы или в базе данных\n"
    )