from random import randrange

board = [[[],[],[]], [[],[],[]], [[],[],[]]]
count = 0
for i in range (3):
    for j in range(3):
        count += 1
        board[i][j] = count

print(board)

sign = "X"

def display_board(board):
    print("+-------" * 3, "+", sep = (""))

    for row in range(3):
        print("|", "      |", "      |","      |" )
        for collumn in range(3):
            print("|  ", str(board[row][collumn]), "  ", end=(""))
        print("|")
        print("|", "      |", "      |", "      |")
        print("+-------" * 3, "+", sep = (""))
        
def enter_move(board):

    board[1][1] = "X"
                
    var = int(input("Enter your move: "))

    if var < 1 or var > 9:
        print("Enter a number between 1 and 9")
        var = int(input("Enter your move: "))
    else:
        for i in range(3):
            for j in range(3):
                if var == board[i][j]:
                    board[i][j] = "O"


def make_list_of_free_fields(board):
    tup = ()
    lisT = []

    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                continue
            else:
                tup = (i, j)
                lisT.append(tup)
    return lisT


def draw_move(board):

    var = randrange(1, 10)
    hlp = True

    while (hlp):
        for i in range(3):
            for j in range(3):
                if board[i][j] == var:
                    board[i][j] = "X"
                    hlp = False
                else:
                    var = randrange(1, 10)       
    return board
    
            

def victory_for(board, sign):
    lX = ["X", "X", "X"]
    lO = ["O", "O", "O"]

    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == lX[j]:
                count += 1
                if count == 3:
                    break
    print("X wins!")
    return True
    

    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == lO[j]:
                count += 1

            elif count == 3:
                break
    print("O wins!")
    return True


while(True):
    display_board(board)
    enter_move(board)
    draw_move(board)
    print(board)
