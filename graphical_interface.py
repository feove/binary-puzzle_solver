import os
from time import sleep

press_string = "          ▁▁▁             ▁▁▁\n    Press ▎s ▎to start or ▎q ▎to quit\n          ▔▔▔             ▔▔▔\n\n\n"
                                                                            
def print_start():
    print("\n\n        ┏━━━━━━━━━━━━━━┓\n        ┃     START    ┃\n        ┗━━━━━━━━━━━━━━┛\n\n\n\n\n")

def cursor_show():
    print('\033[? 25h', end="")

def cursor_hide():
    print('\033[? 25l', end="")

def intro():

    cursor_hide()

    os.system('clear')
    
    print_start()
    sleep(0.3)
    print(press_string)
    loader = ""

    #id = os.fork()

    nb_char = len("Press ┃s┃ to start or ┃q┃ to quit      ")

    for t in range(nb_char):

        if t == nb_char-1 or t == 0:
            loader += '┃'

        else:
            loader += '='
        
        os.system('clear')
        print(loader)
        print_start()
        print(press_string)
        print(loader)

        sleep(0.1)
    

    sleep(0.5)
   
    print('\033[? 25h', end="")

