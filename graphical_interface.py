import os
from math import *
import grid_storage
import solver
import introduction_board
import random
from colorama import Fore, Back, Style
from termcolor import colored
from time import sleep
from pynput.keyboard import Key, Listener 

def cursor_show():
    print('\033[? 25h', end="")

def cursor_hide():
    print('\033[? 25l', end="")

intro_margin_right = " "*10
intro_margin_top = "\n"*1

#33 = 0r
#10 = 0c

def colorise_vertical_side(start, end, i, reset, color=None):
   
    for j in range(start, end + 1):

        c = introduction_board.G_intro_board[j][i] 
        if reset:
            Fore.WHITE  + introduction_board.G_intro_board[j][i] + Style.RESET_ALL
        else:
            introduction_board.G_intro_board[j][i] = colored(c, color)

def colorise_horizontal_side(reset, start, end, j, color=None):

    for i in range(start, end + 1):

        c = introduction_board.G_intro_board[j][i]  

        introduction_board.G_intro_board[j][i] = colored(c, "black") if reset else colored(c, color)
        

def big_rec_edit(reset:bool,color=None):

    tl_corner = [3, 17]
    tr_corner = [3, 33]
    bl_corner = [7, 17]
    br_corner = [7, 33]

    colorise_horizontal_side(reset, tl_corner[1], tr_corner[1], tl_corner[0], color)  # Top side
    colorise_horizontal_side(reset, bl_corner[1], br_corner[1], bl_corner[0], color)  # Bottom side

    colorise_vertical_side(tl_corner[0], bl_corner[0], tl_corner[1], reset, color)  # Left side
    colorise_vertical_side(tr_corner[0], br_corner[0], tr_corner[1], reset, color)  # Right side

    return

def small_rec_edit(color):
    return

def random_symbols():

    return random.choice([' ',' ',' ',' ','1','0'])

def line_void_check(row,start,jump,end):

    for i in range(start,end,jump):

        if row[i] != ' ':
            return False

    return True

def random_line_filling(row,start,jump,end,random,char=None):

    for i in range(start,end,jump):

        random_symbol = random_symbols()
        c =  colored(random_symbol, "yellow") if random_symbol == '1' else colored(random_symbol, "cyan")
        row[i] = c

def intro_grid_fill(random:bool,char=None):

    r = 35
    c = 11
    end_row = 47
    end_col= 17

    while (c <= end_col):
        
        random_line_filling(introduction_board.G_intro_board[c],r,4,end_row,random,char)
        
        if line_void_check(introduction_board.G_intro_board[c],r,4,end_row):
           
            random_line_filling(introduction_board.G_intro_board[c],r,4,end_row,random,char)
            
        r = 35
        c += 2

def intro_display():

    print(intro_margin_top)
    
    for row in introduction_board.G_intro_board:
        
        print(intro_margin_right +  "".join(row))

    print(intro_margin_top)


def intro():
    
    os.system('clear')

    #small_rec_edit('yellow')

    intro_grid_fill(False,' ')
    big_rec_edit(False,"grey")
    
    intro_display()

    
    sleep(1)

    os.system('clear')

    #small_rec_edit('white')

    big_rec_edit(True)
    intro_grid_fill(True)
    intro_display()
    
    
    sleep(1)    



   
grid_list = ["  6x6  ","  8x8  "," 10x10 "," 12x12 "," 14x14 "]

grid_list_size = len(grid_list)

current_grid = 0

dimensions_string = "\n  "

def display_menu():

    os.system("clear")
    print("\n     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n     ┃ Choose the grid dimension: ┃\n     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n")

    
def display_grid_lists(current_grid,select:bool):

    current_grid_copy = grid_list[current_grid]
    global dimensions_string

    if select:
        dimensions_string = "  " + " "*9*current_grid + "┌───────┐" +"\n  "

        for i in range(grid_list_size):

            if i == current_grid:
                grid_list[i] = "│" + grid_list[i] + "│"
        
            dimensions_string +=  grid_list[i]  +  "  "
        dimensions_string += "\n  " + " "*9*current_grid + "└───────┘"

    print(dimensions_string, end="\n"*5)
    grid_list[current_grid] = current_grid_copy

def grid_dimension():

    display_menu()
    display_grid_lists(current_grid,True)

    def on_press(key):

        global current_grid
        try:
            if key == Key.left:
                
                if current_grid != 0:
                    current_grid = current_grid-1
                display_menu()
                display_grid_lists(current_grid,True)

           
            elif key == Key.right:
                'green'
                if current_grid != grid_list_size-1:
                    current_grid += 1
                display_menu()
                display_grid_lists(current_grid,True)
               
            
            elif key == Key.enter:
                return False
           
            elif key.char == 'q':

                current_grid = -1
                return False
            
            else:
                display_menu()
                display_grid_lists(current_grid,False)

            
        except AttributeError:
            
            pass
            
    with Listener(on_press = on_press) as listener:
        listener.join()

    return current_grid

#Dublin Est

grids = [grid_storage.grid_6x6,grid_storage.grid_8x8,grid_storage.grid_10x10,grid_storage.grid_12x12]

grids_name = ["6x6","8x8","10x10","12x12"]

grid_size = [5,7,9,11]

i = 14
i_prev = 2
i_next = 6
j = 5
j_next = 7
j_prev = 3

grid_sets = []

def init_matrix(size):

    return [[3 for _ in range(size)] for _ in range(size)]


def grid_reading(num_grid):

    M = init_matrix(grid_size[num_grid]+1)

    i = 0
    j = 0

    for row in range(1, len(grids[num_grid]) - 1, 2): 
        
        j = 0
        for col in range(2, len(grids[num_grid][row]) - 2, 4):  
            
            digit = grids[num_grid][row][col]
            if digit != ' ':
            
                M[i][j] = int(digit)
            j += 1
        i += 1
             
    return M


def grid_writing(M, num_grid):
  
    size = len(M)

    if size != len(M[0]):
        raise TypeError("Matrix width different from height.")

    for i in range(size):

        for j in range(size):

            value = ' ' if  M[i][j] == 3 else str(M[i][j]) 

            grids[num_grid][(i*2)+1][(j*4)+2] = value

    return grids[num_grid]


def clear_colum(num_grid):

    l = 1
    end = grid_size[num_grid]
    while((l-1)//2 <= end):
        
        grids[num_grid][l][i] = ' '   
        l += 2

def clear_line(num_grid):

    c = 2
    end = grid_size[num_grid]
    while((c-2)//4 <= end):
        
        grids[num_grid][j][c] = ' '   
        c += 4
        
def clear_grid(num_grid):
    
    for row in range(1, len(grids[num_grid]) - 1, 2): 
        
        for col_index in range(2, len(grids[num_grid][row]) - 2, 4):  
            grids[num_grid][row][col_index] = ' '

 
example_sets = [
                [grid_storage.G_6x6_EASY_1,grid_storage.G_6x6_EASY_2,grid_storage.G_6x6_EASY_3],
                [grid_storage.G_8x8_EASY_1,grid_storage.G_8x8_EASY_2],
                [grid_storage.G_10x10_EASY_1,grid_storage.G_10x10_EASY_2,grid_storage.G_10x10_EASY_3],
                [grid_storage.G_12x12_EASY_1,grid_storage.G_12x12_EASY_2,grid_storage.G_12x12_EASY_3]
            ]
e = 0

def example_set(num_grid):

    global e
    
    os.system('clear')

    random_grid = example_sets[num_grid][e]

    grids[num_grid] = grid_writing(random_grid,num_grid)


    display_grid(num_grid)

    e = (e + 1)%len(example_sets[num_grid])
  
    return

helpful_sentences = ["┌──────────────────────────────────┐","│  Press 'x' to set '1'            │","│  Press 'c' to set '0'            │","│  Press 'v' to delete             │","│  Press 'b' to clear the line     │","│  Press 'g' to clear the colum    │","│  Press 'j' to clear the grid     │","│  Press 'e' to display an example │","│  Press 'ENTER' to Solve          │","│  Press 'q' to Quit               │","└──────────────────────────────────┘"]
nb_space = 6
space_between = " "*nb_space

def display_grid(num_grid,example=None):

    os.system("clear") 

    if example != None:
        
        print(f"{space_between}┏━━━━━━━━━━━━━┓\n{space_between}┃ Example : {example} ┃\n{space_between}┗━━━━━━━━━━━━━┛")
        

    grids[num_grid][j][i_next-1] = ' ' 
    grids[num_grid][j][i_next+1] = ' '
    grids[num_grid][j][i_prev-1] = ' '
    grids[num_grid][j][i_prev+1] = ' ' 

    grids[num_grid][j_prev][i-1] = ' ' 
    grids[num_grid][j_prev][i+1] = ' '   
    grids[num_grid][j_next][i-1] = ' ' 
    grids[num_grid][j_next][i+1] = ' '   
    
    grids[num_grid][j][i-1] = '▸' 
    grids[num_grid][j][i+1] = '◂'
 
    s = len(grids[num_grid])

    information = f"\n                        ┌───┐\n      Current Cellule : │ {grids[num_grid][j][i]} │\n                        └───┘"
    
    sentence = 0
    sentences_nb = len(helpful_sentences)
    if (example == None):
        up_border,down_border = "━"*(len(grids_name[num_grid])+7),"━"*(len(grids_name[num_grid])+7)                                                                                  
        print(f"{space_between}┏"+up_border+f"┓\n{space_between}┃ {grids_name[num_grid]} grid ┃\n{space_between}┗"+down_border+"┛")

    for r in range(s):
        
        supp = "" 

        if sentence < sentences_nb:

   
            supp = helpful_sentences[sentence] if r % 2 == 0 else "│                                  │"
            
            sentence = sentence+1 if  r % 2 == 0 else sentence
            

        print(space_between + "".join(grids[num_grid][r]) + space_between + supp)
  
    if (sentence < sentences_nb):

        mg = len(grids[num_grid][0]) + 2*nb_space
        while (sentence < sentences_nb):
            
            print(" "*mg +"│                                  │")
            print(" "*mg + f"{helpful_sentences[sentence]}")
            sentence += 1

        
    print(information)

    if (example != None):
        sleep(1.5)
    
    return

def grid_filling(num_grid):

    display_grid(num_grid)

    def arrow_press(key):

        global i
        global i_prev
        global i_next

        global j
        global j_prev
        global j_next

        try:
            if key == Key.left:
                
                i_next = i
                if i != 2:
                    i -= 4
                    
                
            elif key == Key.right:
                
                i_prev = i
                if (i-2)//4 != (grid_size[num_grid]):
                    i += 4

            elif key == Key.up:
                
                j_prev = j
                if j != 1:
                    j -= 2

            elif key == Key.down:

                j_next = j
                if (j-1)//2 != (grid_size[num_grid]):
                    j += 2

            elif key == Key.enter:
                
                os.system('clear')

                M = grid_reading(num_grid)
                solver.main(M)

                sleep(4)

                grids[num_grid] = grid_writing(M,num_grid)


            elif key.char == '1' or key.char == 'x':
                grids[num_grid][j][i] = '1'

            elif key.char == '0' or key.char == 'c':
                grids[num_grid][j][i] = '0'
            
            elif key.char == '2' or key.char == 'v':
                grids[num_grid][j][i] = ' '
            
            elif key.char == 'b':
                clear_line(num_grid)
            
            elif key.char == 'g':
                clear_colum(num_grid)

            elif key.char == 'j':
                clear_grid(num_grid)

            elif key.char == 'e':
                clear_grid(num_grid)
                display_grid(num_grid,e+1)
                example_set(num_grid)
                
       
            elif key.char == 'q' or key.char == 'a':

                os.system('clear')
                return False

            display_grid(num_grid)
            
        except AttributeError:
            
            pass
            
    with Listener(on_press = arrow_press) as listener:
        listener.join()

    return num_grid



#user_grid = 