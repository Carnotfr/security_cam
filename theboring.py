def initialiseBoard():
    global board
    board = [[' ' for i in range(7) for j in range(6)]]

def print_board():
    global board
    for row in board:
        for col in row:
            print(col, end="")
        print()

def setUpGame():
    global isFinished, thisPlayer
    isFinished = False
    thisPlayer = 'X'

def thisPlayerMakesMove():
    global validCol, validRow
    validCol = thisPlayerMakesColum()
    validRow = findNextFreePositioncol()
    board[validRow][validCol] - thisPlayer

def thisPlayerMakesColum():
    global thisPlayer
    print("Player" , thisPlayer, "is playing")
    colOption = int(input("Column to play"))
    return colOption
def findNextFreePositioncol():
    global validCol, board
    for i in range(len(board)):
        if board[i][validCol] == " ":
            return i

initialiseBoard()
setUpGame()
print_board()
while  isFinished == False:
    thisPlayerMakesMove()
    print_board()