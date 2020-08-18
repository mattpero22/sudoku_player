list=[(0,0)]
board= [[8,7,0,1,0,2,0,6,9],
        [0,6,1,5,0,8,7,2,0],
        [5,0,4,7,0,0,0,0,0],
        [3,0,6,2,0,0,0,9,1],
        [0,0,0,0,9,0,6,0,7],
        [0,5,0,6,0,1,0,4,0],
        [2,0,0,8,1,7,0,0,0],
        [0,0,0,0,0,0,1,7,2],
        [0,1,0,0,2,4,9,0,0]]
is_valid=True

def display():
    print("\n")
    for i in range(9):
        if(i==3 or i==6):
            print("- - - - - - - - - - - - - - - ")
        for j in range(9):
            print(' %d ' % (board[i][j]), end="")
            if(j==2 or j==5):
                print("|",end="")
            if(j==8):
                print("\n",end="")

def checkrow(i,n):
    for col in range(9):
        if(board[i][col]==n):
            return False
    return True

def checkcol(j,n):
    for row in range(9):
        if(board[row][j]==n):
            return False
    return True

def checkzone(i,j,n):
    if(i>=0 and i<=2 and j>=0 and j<=2): #NW cell
            for row in range(3):
                for col in range(3):
                    if(board[row][col]==n):
                        return False
    if(i>=0 and i<=2 and j>=3 and j<=5): #N cell
            for row in range(3):
                for col in range(3):
                    if(board[row][col+3]==n):
                        return False
    if(i>=0 and i<=2 and j>=6 and j<=8): #NE cell
            for row in range(3):
                for col in range(3):
                    if(board[row][col+6]==n):
                        return False
    if(i>=3 and i<=5 and j>=0 and j<=2): #W cell
            for row in range(3):
                for col in range(3):
                    if(board[row+3][col]==n):
                        return False
    if(i>=3 and i<=5 and j>=3 and j<=5): #C cell
            for row in range(3):
                for col in range(3):
                    if(board[row+3][col+3]==n):
                        return False
    if(i>=3 and i<=5 and j>=6 and j<=8): #E cell
            for row in range(3):
                for col in range(3):
                    if(board[row+3][col+6]==n):
                        return False
    if(i>=6 and i<=8 and j>=0 and j<=2): #SW cell
            for row in range(3):
                for col in range(3):
                    if(board[row+6][col]==n):
                        return False
    if(i>=6 and i<=8 and j>=3 and j<=5): #S cell
            for row in range(3):
                for col in range(3):
                    if(board[row+6][col+3]==n):
                        return False
    if(i>=6 and i<=8 and j>=6 and j<=8): #SE cell
            for row in range(3):
                for col in range(3):
                    if(board[row+6][col+6]==n):
                        return False
    return True

def solve_cell(i,j):
    n= board[i][j]+1
    while(n<10):
        is_valid=checkrow(i,n)
        if(is_valid==True):
            is_valid=checkcol(j,n)
            if(is_valid==True):
                checkzone(i,j,n)
        if(is_valid):
            board[i][j]=n
            find_zero()
            return
        if(not(is_valid)):
            n+=1
    board[i][j]=0
    list.pop(-1)
    previously_solved=list[-1]
    prev_x = previously_solved[0]
    prev_y = previously_solved[1]
    solve_cell(prev_x,prev_y)

def find_zero():
    for i in range(9):
        for j in range(9):
            if (board[i][j]==0):
                list.append((i,j))
                solve_cell(i,j)

display()
find_zero()
display()
