import random
def initialize_board(length,complex):
    amount_mine=length*length*complex//10
    board = []
    for i in range(length):
        row = [0]*length
        board.append(row)
    while amount_mine>0:
        row = random.randint(0,length-1)
        col = random.randint(0,length-1)
        if board[row][col]==0:
            board[row][col]=9
            amount_mine-=1
    for row in range(length):
        for col in range(length):
            if board[row][col]!=9:
                count = 0
                for i in range(row-1,row+2):
                    for r in range(col-1,col+2):
                        if i>=0 and r>=0 and i<length and r<length and (i!=row or r!=col):
                            if board[i][r]==9:
                                count+=1
                board[row][col]=count
    return board
def open(board_open,board,row,col):
    board_open[row][col]=1
    if board[row][col]!=0:
        return
    if row < len(board_open)-1 and board_open[row+1][col]==0 and board[row+1][col]!=9:
        open(board_open,board,row+1,col)
    if row > 0 and board_open[row-1][col]==0 and board[row-1][col]!=9:
        open(board_open,board,row-1,col)
    if col < len(board_open)-1 and board_open[row][col+1]==0 and board[row][col+1]!=9:
        open(board_open,board,row,col+1)
    if col > 0 and board_open[row][col-1]==0 and board[row][col-1]!=9:
        open(board_open,board,row,col-1)
    if row < len(board_open)-1 and col < len(board_open)-1 and board_open[row+1][col+1]==0 and board[row+1][col+1]!=9:
        open(board_open,board,row+1,col+1)
    if row < len(board_open)-1 and col > 0 and board_open[row+1][col-1]==0 and board[row+1][col-1]!=9:
        open(board_open,board,row+1,col-1)
    if row > 0 and col < len(board_open)-1 and board_open[row-1][col+1]==0 and board[row-1][col+1]!=9:
        open(board_open,board,row-1,col+1)
    if row >0 and col > 0 and board_open[row-1][col-1]==0 and board[row-1][col-1]!=9:
        open(board_open,board,row-1,col-1)
def print_game(board_open,board,board_flag):
    for i in range(len(board)):
        for r in range(len(board)):
            if board_open[i][r]==1:
                if board[i][r]!=9:
                    print(board[i][r],end="")
                else:
                    print("*",end="")
            elif board_flag[i][r]==1:
                print("F",end="")
            else:
                print("#",end="")
        print()
def open_mines(board_open,board):
    for i in range(len(board)):
        for r in range(len(board)):
            if board[i][r]==9:
                board_open[i][r]=1

def check_win(board_open,board):
    count_open = 0
    count_mines = 0
    for i in range(len(board)):
        for r in range(len(board)):
            if board_open[i][r]==1:
                count_open+=1
            if board[i][r]==9:
                count_mines+=1
    if count_open+count_mines==len(board)*len(board):
        return True
    return False
def initialize_open_flag(length):
    board = []
    for i in range(length):
        row = [0]*length
        board.append(row)
    return board
def game():
    length = int(input("Enter length 10-50 "))
    while length>50 or length<10:
        length = int(input("Enter length 10-50 "))
    complexity = int(input("Enter complexity 1-5 1=eazy 5=hard "))
    while complexity>5 or complexity<1:
        complexity = int(input("Enter complexity 1-5 1=eazy 5=hard "))
    board_open = initialize_open_flag(length)
    board = initialize_board(length,complexity)
    board_flag = initialize_open_flag(length)
    print_game(board_open,board,board_flag)
    while True:
        o = int(input("Open cell or put or remove flag 1-3 "))
        while o>3 or o<1:
            o = int(input("Open cell or put or remove flag 1-3 "))
        row = int(input("Enter row 0-"+str(length-1)+" "))
        while row>=length or row<0:
            row = int(input("Enter row 0-"+str(length-1)+" "))
        col = int(input("Enter col 0-"+str(length-1)+" "))
        while col>=length or col<0:
            col = int(input("Enter col 0-"+str(length-1)+" "))
        if o==1:
            if board[row][col]==9:
                open_mines(board_open,board)
                print_game(board_open,board,board_flag)
                print("You Lose")
                return
            open(board_open,board,row,col)
            print_game(board_open,board,board_flag)
            if check_win(board_open,board):
                print("You Win")
                return
            continue
        elif o==2:
            board_flag[row][col]=1
        else:
            board_flag[row][col]=0
        print_game(board_open,board,board_flag)
game()