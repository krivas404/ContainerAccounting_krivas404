from menu_and_input.main_menu import start_main_menu
from exceptions import LenghtInputError


def main():
    while True:
        try:
            start_main_menu()
        except LenghtInputError:
            start_main_menu()



if __name__ == "__main__":
    main()
