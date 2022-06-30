from exceptions import NotMenuError
from menu_and_input.console_menu_text import *
from menu_and_input.submenu_1_worker import submenu_1_worker
from menu_and_input.submenu_2_worker import submenu_2_worker
from menu_and_input.submenu_3_worker import submenu_3_worker
from menu_and_input.submenu_4_worker import submenu_4_worker
from menu_and_input.submenu_5_worker import submenu_5_worker
from menu_and_input.submenu_6_worker import submenu_6_worker


def start_submenu_1():
    print_text_submenu_1_give_take_containers()
    submenu_1_worker()  # User must enter or scan some codes

def start_submenu_2():
    print_text_submenu_2_info_about_handon_containers()
    submenu_2_worker()  # User must enter or scan some codes

def start_submenu_3():
    print_text_submenu_3_search_info_about_couriers_or_containers()
    submenu_3_worker()  # User must enter or scan some codes

def start_submenu_4():
    print_text_submenu_4_report_about_containers_today()
    submenu_4_worker()  # User must enter or scan some codes

def start_submenu_5():
    print_text_submenu_5_testmenu()
    submenu_5_worker()  # User must enter or scan some codes

def start_submenu_6():
    print_text_submenu_6_newcourier()
    submenu_6_worker()


def call_submenu(type, code):
    if type != 'menu':
        raise NotMenuError
    if code == 1:
        start_submenu_1()
    if code == 2:
        start_submenu_2()
    if code == 3:
        start_submenu_3()
    if code == 4:
        start_submenu_4()
    if code == 5:
        start_submenu_5()
    if code == 6:
        start_submenu_6()
