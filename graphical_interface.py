import os
from math import *
from time import sleep
from pynput.keyboard import Key, Listener 

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


grid_list = ["6x6","10x10","12X12"]

grid_list_size = len(grid_list)

current_grid = 0

dimensions_string = "\n  "

def display_menu():

    os.system("clear")
    print("Choose the grid dimension:")

    
def display_grid(current_grid,select:bool):

    
    current_grid_copy = grid_list[current_grid]
    global dimensions_string

    if select:
        dimensions_string = "\n  "
        for i in range(grid_list_size):

            if i == current_grid:
                grid_list[i] = "|" + grid_list[i] + "|"
        
            dimensions_string +=  grid_list[i]  +  "  "

    print(dimensions_string)
    grid_list[current_grid] = current_grid_copy

def grid_dimension():



    display_menu()
    display_grid(current_grid,True)

    def on_press(key):

        global current_grid
        try:
            if key == Key.left:
                
                if current_grid != 0:
                    current_grid = current_grid-1
                display_menu()
                display_grid(current_grid,True)

           
            elif key == Key.right:
                
                if current_grid != grid_list_size-1:
                    current_grid += 1
                display_menu()
                display_grid(current_grid,True)
            
            elif key == Key.enter:
                return False
           
            elif key.char == 'q':

                current_grid = -1
                return False
            
            else:
                display_menu()
                display_grid(current_grid,False)

            
        except AttributeError:
            
            pass
            
    with Listener(on_press = on_press) as listener:
        listener.join()

    return current_grid

