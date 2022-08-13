from os import system
from game_mechs import *

so = 0

while not(so in ["clear", "cls"]):
    so = int(input("Choose your O.S. (1. Win, 2. Linux):"))
    if so == 1:
        so = "cls"
    elif so == 2:
        so = "clear"
    else:
        print("select a valid option")

while checker() == 0:
    options(0)
    printer(board)
    cas = int(input("--> "))

    for i in range(4):
        for j in range(4):
            if board[i][j] == cas:
                if turno == 1:
                    board[i][j] = "X"
                elif turno == 2:
                    board[i][j] = "O"
                break

    if turno == 1:
        turno = 2
    elif turno == 2:
        turno = 1
    cleaner()
    system(so)
    
