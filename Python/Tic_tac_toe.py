# Defining functions
def print_board(brd) :
    print(brd[0], brd[1], brd[2], "      ", "1 2 3")
    print(brd[3], brd[4], brd[5], "      ", "4 5 6")
    print(brd[6], brd[7], brd[8], "      ", "7 8 9")
# Defining variables
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win = "n"
counter = 0
# Main game loop
while True :
    print_board(board)
    counter += 1
    if board[0] == board[1] == board[2] != " " :
        win = board[0]
        break
    elif board[3] == board[4] == board[5] != " " :
        win = board[3]
        break
    elif board[6] == board[7] == board[8] != " " :
        win = board[6]
        break
    elif board[0] == board[3] == board[6] != " " :
        win = board[0]
        break
    elif board[1] == board[4] == board[7] != " " :
        win = board[1]
        break
    elif board[2] == board[5] == board[8] != " " :
        win = board[2]
        break
    elif board[0] == board[4] == board[8] != " " :
        win = board[0]
        break
    elif board[2] == board[4] == board[6] != " " :
        win = board[2]
        break
    elif " " not in board :
        win = "n"
        break
# Gathering input
    if counter % 2 == 0 :
        while True :
            try :
                x = int(input("Enter the position for O : "))
                if not x < 1 and board[x - 1] == " " :
                    board[x - 1] = "O"
                    break
                else :
                    print("Invalid position!")
            except :
                print("Invalid position!")
    else :
        while True :
            try :
                x = int(input("Enter the position for X : "))
                if not x < 1 and board[x - 1] == " " :
                    board[x - 1] = "X"
                    break
                else :
                    print("Invalid position!")
            except :
                print("Invalid position!")
# Printing winner
if win != "n" :
    print(win, "has won the game!")
else :
    print("It's a Tie!")
