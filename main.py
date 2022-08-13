# Main file of the program

from os import system
from game_mechs import *

so = 0

while not(so in ["clear", "cls"]):#this is a method for select an clear command for each O.S.
    so = int(input("Choose your O.S. (1. Win, 2. Linux):")) 
    if so == 1:
        so = "cls"
    elif so == 2:
        so = "clear"
    else:
        print("select a valid option")

while checker() == 0 and checker() != 4: #From game_mechs
    print("Turn of",PLAYER)#Prints turns
    options(0) #First place the possible options for put a mark
    printer(board) #Next is print the board
    cas = int(input("--> ")) #Now an input for select a place for put a mark

    for i in range(4): #The program find in the board/array if the number is valid
        for j in range(4):
            if board[i][j] == cas: #if a match is found, the program will put the correspondent mark in his place
                if PLAYER == 1:
                    board[i][j] = "X" 
                elif PLAYER == 2:
                    board[i][j] = "O"
                break

    if PLAYER == 1: #Change of turn
        PLAYER = 2
    elif PLAYER == 2:
        PLAYER = 1
    cleaner() #Clear the options on the board
    system(so) #Clear the screen
    
printer(board)#Prints the last board
