""" Functions and concepts of 4 in a row """

# some variables

PLAYER = 1
cas = 0

# board: a 7x6 array

board = [["0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0"]]


def printer(matrix):  # Prints the board
    for j in range(len(board)):
        for i in range(len(board[0])):
            print(matrix[j][i], end=" ")
        print("")


def cleaner():  # Erase the options into the board
    for j in range(len(board[0])):
        for i in range(len(board)):
            if board[i][j] in [1, 2, 3, 4, 5, 6, 7]:
                board[i][j] = "0"


def options(count):  # Options for put a mark into the board
    for i in range(len(board[0])):
        for j in range(len(board)):
            if j == len(board) - 1:
                if board[j][i]  == "0":
                    board[j][i] = count + 1 
                    count = count + 1
            elif board[j+1][i] in ["X", "O"] and board[j][i] in ["0"]:
                    board[j][i] = count + 1 
                    count = count + 1
            if count == len(board[0]):
                break
        if count == len(board[0]):
            break

def draw(zero):  # in one hand Prove that the game can continue, on the other handend the game in a draw
    for j in range(4):
        for i in range(4):
            if board[i][j] == "0":
                zero = zero + 1
    if zero == 0:
        return 1
    else:
        return 0


def checker(board):  # Checks the situation of the game
    for j in range(6):
        for i in range(7):
            if ((str(board[j][i]) in ["X", "O"]) and
                (winLinesHorizontal(j, i, board[j][i]) == 0 or
                 winLinesVertical(j, i, board[j][i]) == 0 or
                 winLinesDiagOne(j, i, board[j][i]) == 0 or
                 winLinesDiagTwo(j, i, board[j][i]) == 0)):

                sweetVictory(board[j][i])

                return 1

    if draw(0) == 1:
        print("Draw!!")
        return 4
    else:
        return 0


# finds a winning position in Horizontal
def winLinesHorizontal(x=int, y=int, symbol=str):
    if y+1 < len(board[0]):
        if board[x][y+1] == symbol:
            if y+2 < len(board[0]):
                if board[x][y+2] == symbol:
                    if y+3 < len(board[0]):
                        if board[x][y+3] == symbol:
                            return 0


# finds a winning position in Horizontal
def winLinesVertical(x=int, y=int, symbol=str):
    if x+1 < len(board):
        if board[x+1][y] == symbol:
            if x+2 < len(board):
                if board[x+2][y] == symbol:
                    if x+3 < len(board):
                        if board[x+3][y] == symbol:
                            return 0


# finds a winning position in left-right diagonals
def winLinesDiagOne(x=int, y=int, symbol=str):
    if x+1 < len(board) and y+1 < len(board[0]):
        if board[x+1][y+1] == symbol:
            if x+2 < len(board) and y+2 < len(board[0]):
                if board[x+2][y+2] == symbol:
                    if x+3 < len(board) and y+3 < len(board[0]):
                        if board[x+3][y+3] == symbol:
                            return 0


# finds a winning position in right-left diagonals --- REVISARa   s
def winLinesDiagTwo(x=int, y=int, symbol=str):
    if x-1 > 0 and y+1 < len(board[0]):
        if board[x-1][y+1] == symbol:
            if x-2 > 0 and y+2 < len(board[0]):
                if board[x-2][y+2] == symbol:
                    if x-3 > 0 and y+3 < len(board[0]):
                        if board[x-3][y+3] == symbol:
                            return 0


def sweetVictory(symbol=str):  # Victoty Visualizer
    print("win for", symbol, "!!")
