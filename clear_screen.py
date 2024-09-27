import os

def clear_screen():
    if os.system == 'nt': #windows
        os.system('cls')
    else:
        os.system('clear')

