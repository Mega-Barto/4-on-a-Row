""" Functions and of 4 in a row """

# some variables

PLAYER = 1
cas = 0

board = [["0", "0", "0", "0"], ["0", "0", "0", "0"],  # Original Board
         ["0", "0", "0", "0"], ["0", "0", "0", "0"]]


def printer(matrix):  # Prints the board
    for j in range(4):
        for i in range(4):
            print(matrix[j][i], end=" |")
        print("")


def cleaner():  # Erase the options into the board
    for j in range(4):
        for i in range(4):
            if board[i][j] in [1, 2, 3, 4]:
                board[i][j] = "0"


def options(count):  # Options for put a mark into the board
    for j in range(4):
        if board[3][j] == "0":
            board[3][j] = count + 1
            count = count + 1
            if count == 4:
                break
    if count < 4:
        for i in range(4):
            for j in range(3):
                if board[j+1][i] in ["X", "O"] and board[j][i] in ["0"]:
                    board[j][i] = count + 1
                    count = count + 1
                    if count == 4:
                        break


def draw(zero):# in one hand Prove that the game can continue, on the other handend the game in a draw 
    for j in range(4):
        for i in range(4):
            if board[i][j] == "0":
                zero = zero + 1
    if zero == 0:
        return 1
    else:
        return 0


def checker():  # Combinations for victory
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" and board[3][3] == "X":  # win for 1
        print("victory for 1")
        return 1
    elif board[0][3] == "X" and board[1][2] == "X" and board[2][1] == "X" and board[3][0] == "X":
        print("victory for 1")
        return 1
    elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" and board[0][3] == "X":
        print("victory for 1")
        return 1
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X":
        print("victory for 1")
        return 1
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" and board[2][3] == "X":
        print("victory for 1")
        return 1
    elif board[3][0] == "X" and board[3][1] == "X" and board[3][2] == "X" and board[3][3] == "X":
        print("victory for 1")
        return 1
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" and board[3][0] == "X":
        print("victory for 1")
        return 1
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" and board[3][1] == "X":
        print("victory for 1")
        return 1
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" and board[3][2] == "X":
        print("victory for 1")
        return 1
    elif board[0][3] == "X" and board[1][3] == "X" and board[2][3] == "X" and board[3][3] == "X":
        print("victory for 1")
        return 1

    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" and board[3][3] == "O":  # win for 2
        print("victory for 2")
        return 2
    elif board[0][3] == "O" and board[1][2] == "O" and board[2][1] == "O" and board[3][0] == "O":
        print("victory for 2")
        return 2
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" and board[0][3] == "O":
        print("victory for 2")
        return 2
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" and board[1][3] == "O":
        print("victory for 2")
        return 2
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" and board[2][3] == "O":
        print("victory for 2")
        return 2
    elif board[3][0] == "O" and board[3][1] == "O" and board[3][2] == "O" and board[3][3] == "O":
        print("victory for 2")
        return 2
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" and board[3][0] == "O":
        print("victory for 2")
        return 2
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" and board[3][1] == "O":
        print("victory for 2")
        return 2
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O" and board[3][2] == "O":
        print("victory for 2")
        return 2
    elif board[0][3] == "O" and board[1][3] == "O" and board[2][3] == "O" and board[3][3] == "O":
        print("victory for 2")
        return 2
    elif draw(0) == 1:#The board is full without an winner combination
        print("Draw!")  
        return 4
    else:
        return 0#The game can continue
