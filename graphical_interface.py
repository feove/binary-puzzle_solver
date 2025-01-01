import os
from time import sleep

press_string = "\n    Press 's' to start or 'q' to quit.\n"

def intro():

    os.system('clear')
    sleep(0.3)

    print(press_string)
    sleep(0.3)
    loader = "\n    ━"

    for t in range(len("Press 's' to start or 'q' to quit.")):
        os.system('clear')
        print(press_string + loader)

        loader += "━"
        sleep(0.1)
    sleep(0.4)
 
   

