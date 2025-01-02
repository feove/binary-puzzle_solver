import os
from time import sleep

press_string = "          ▁▁▁               ▁▁▁\n    Press ▎s ▎  to start or ▎q ▎ to quit.\n          ▔▔▔               ▔▔▔"


def print_start():
    print("\n\n        ┏━━━━━━━━━━━━━━┓\n        ┃     START    ┃\n        ┗━━━━━━━━━━━━━━┛\n\n\n")

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
    loader = "\n    ═"

    #id = os.fork()

    for t in range(len("Press ┃s┃ to start or ┃q┃ to quit.")):

        os.system('clear')
        print_start()
        print(press_string + loader,end="\n\n\n\n\n\n")
       
        loader += '═'
        
        sleep(0.2)
    sleep(1)
   
    print('\033[? 25h', end="")

