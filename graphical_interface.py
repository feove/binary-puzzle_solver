import os
from time import sleep
import cursor

press_string = "\n    Press 's' to start or 'q' to quit."


def print_start():

    print("\n\n        ┏━━━━━━━━━━━━━━┓\n        ┃     START    ┃\n        ┗━━━━━━━━━━━━━━┛\n\n\n")

def intro():

    os.system('clear')
    sleep(0.3)
    print_start()
    print(press_string)
    sleep(0.3)
    loader = "\n    ═"

    #id = os.fork()
    cursor.show()

    for t in range(len("Press 's' to start or 'q' to quit.")):

        os.system('clear')
        print_start()
        print(press_string + loader,end="\n\n\n\n\n\n")

        loader += "═"

        sleep(0.1)
    
 
   

