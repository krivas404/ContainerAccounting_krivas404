import msvcrt
import sys

def take_input(text_for_input_print='Напишите пункт меню и нажмите Enter, или отсканируйте ШК: '):
    keyboard_input = input(text_for_input_print)
    return keyboard_input