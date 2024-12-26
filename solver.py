from math import *

print("=============================")

M_Line = [
    [1,3,3,0,0,3,0,3,0,3,0,0]
]

M_Line_Solved = [
    [1,0,1,0,0,1,0,1,0,1,0,0]
]

M_Line_1 = [
    [3,0,3,0,3,1,1,3,1,1,3,3]
]

M_Line_Solved_1 = [
    [3,0,1,0,0,1,1,0,1,1,0,3]
]

M_Line_2 =[
    [1,3,0,3,1,1]
]

M_Line_Solved_2 =[
    [1,1,0,0,1,1]
]

M1 = [
    [1,1,3],
    [0,3,0],
    [1,1,3],
    [0,0,3],
    [1,1,3],
    [3,1,1],
    [0,0,3]
]

M1_solved = [
    [1,1,0],
    [0,1,0],
    [1,1,0],
    [0,0,1],
    [1,1,0],
    [0,1,1],
    [0,0,1]
]


M2 = [
    [1,3,0,0],
    [3,0,3,1],
    [1,1,3,1],
    [0,3,0,3]
]

M2_solved = [
    [1,1,0,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,0,0]
]

M_Colum = [

    [0],
    [3],
    [1],
    [3],
    [0],
    [3],
    [1],
    [1]
]

M_Colum_solved = [

    [0],
    [0],
    [1],
    [1],
    [0],
    [0],
    [1],
    [1]
]


M3 = [
    [1,1,3,3,0,1],
    [1,3,3,1,3,3],
    [1,3,3,1,3,3],
    [1,1,0,3,3,0],
    [1,0,3,3,3,0],
    [3,0,3,3,0,3]
]

M3_solved = [
    [1,1,3,3,0,1],
    [1,3,3,1,3,0],
    [1,3,3,1,3,1],
    [1,1,0,3,3,0],
    [1,0,3,3,3,0],
    [3,0,3,3,0,1]
]
def make_line_str(Line:list,nbCol:int,indication=None):

    string_line = "["

    for c in range(nbCol):
        symbol = " "
        if (Line[c] != 3):
            symbol = str(Line[c])
        string_line += symbol

        separator = ""
        if (c+1 != nbCol):
            separator = "|"

        string_line += separator

    string_line += "]"
    
    string_line += indication

    return string_line


def print_grid(M,name=None,M_result=None,M_result_name=None):   #print the matrix

    nbLine = len(M)
    nbCol = len(M[0])
    
    if name == None:
        name = "No named"

    print("")
    for i in range(nbLine):
        print(f"  {i+1}-",end="")
        
        indication = f" --> {name}    "
        if (i != nbLine//2):
            indication = len(indication)*" "

        string_line = make_line_str(M[i],nbCol,indication)  

        string_line_result = ""

        indication = f" --> {M_result_name}    "
        if (i != nbLine//2):
            indication = len(indication)*" "

        if (M_result != None):
            string_line_result = f"{i+1}-" + make_line_str(M_result[i],nbCol,indication)

        string_line += string_line_result

        print(string_line)

    print("")

global_edited = True

def three_symbols_resolve(a:int,b:int,c:int):

    sum = a+b+c 
    if (sum & 3 == 3 or sum & 5 == 5):

        global global_edited 
        global_edited = True

        if (a == b):
            return (a,b,abs(a-1))
        elif (b == c):
            return (abs(b-1),b,c)
        else:
            return (a,abs(a-1),c)
    
    return (a,b,c)

def line_solver(Line:list):

    size = len(Line)

    for i in range(size-2):

        (Line[i],Line[i+1],Line[i+2]) = three_symbols_resolve(Line[i],Line[i+1],Line[i+2])

    for j in range(size-2):

        a,b,c = Line[size-1-j],Line[size-2-j],Line[size-3-j]
        (Line[size-3-j],Line[size-2-j],Line[size-1-j]) = three_symbols_resolve(c,b,a) 


def colum_solver(M,j_col):

    col = [row[j_col] for row in M]

    line_solver(col)

    for i in range(len(col)):
        
        M[i][j_col] = col[i]

    return col

def all_lines_solver(M):

    for l in M:
        line_solver(l)

def all_colums_solver(M):

    for c in range(len(M[0])):
        colum_solver(M,c)

def symbols_filling(M):

    filled = False

    nbLine = len(M)
    nbCol = len(M[0])

    for l in M:

        count_one = 0
        count_zero = 0

    return filled

solved = False

def main(M):

    print("Matrix selected :")

    print_grid(M,"Initial Matrix")
  
    global global_edited

    global solved

    while(not solved):
    
        while(global_edited):

            global_edited = False

            all_lines_solver(M)
            
            all_colums_solver(M)

        
    
    print_grid(M,"Final Matrix",M2_solved,"Matrix Solved")

main(M2)

print("=============================")