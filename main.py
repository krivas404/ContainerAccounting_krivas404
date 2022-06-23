from menu_and_input.console_menu_text import
from menu_and_input.main_menu import start_main_menu
from exceptions import LenghtInputError


def main():
    try:
        start_main_menu()
    except LenghtInputError:
        start_main_menu()



if __name__ == "__main__":
    main()
