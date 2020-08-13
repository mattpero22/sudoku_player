#######################################################################
#sample board
board= [[0,5,0,0,0,4,0,1,0],
        [0,0,3,0,0,1,0,0,9],
        [0,0,4,3,0,0,5,7,0],
        [2,0,0,8,9,0,0,5,0],
        [6,0,5,4,1,2,9,0,7],
        [0,7,0,0,5,3,0,0,2],
        [0,9,6,0,0,5,2,0,0],
        [5,0,0,2,0,0,8,0,0],
        [0,2,0,1,0,0,0,9,0]]
val=[1,2,3,4,5,6,7,8,9]
#########################################################################
#display in console
def display_unsolved():
    for i in range(9):
        if(i==3 or i==6):
            print("- - - - - - - - - - - - - - - ")
        for j in range(9):
            print(' %d ' % (board[i][j]), end="")
            if(j==2 or j==5):
                print("|",end="")
            if(j==8):
                print("\n",end="")
##########################################################################
#macroscopic location of cell for checking 3x3
def checkzone(val,i,j):
    if(i>=0 and i<=2 and j>=0 and j<=2): #NW cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x][y]!=0 and val.count(board[x][y])!=0):
                    val.remove(board[x][y])

    if(i>=0 and i<=2 and j>=3 and j<=5): #N cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x][y+3]!=0 and val.count(board[x][y+3])!=0):
                    val.remove(board[x][y+3])

    if(i>=0 and i<=2 and j>=6 and j<=8): #NE cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x][y+6]!=0 and val.count(board[x][y+6])!=0):
                    val.remove(board[x][y+6])

    if(i>=3 and i<=5 and j>=0 and j<=2): #W cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x+3][y]!=0 and val.count(board[x+3][y])!=0):
                    val.remove(board[x+3][y])

    if(i>=3 and i<=5 and j>=3 and j<=5): #C cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x+3][y+3]!=0 and val.count(board[x+3][y+3])!=0):
                    val.remove(board[x+3][y+3])


    if(i>=3 and i<=5 and j>=6 and j<=8): #E cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x+3][y+6]!=0 and val.count(board[x+3][y+6])!=0):
                    val.remove(board[x+3][y+6])

    if(i>=6 and i<=8 and j>=0 and j<=2): #SW cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x+6][y]!=0 and val.count(board[x+6][y])!=0):
                    val.remove(board[x+6][y])

    if(i>=6 and i<=8 and j>=3 and j<=5): #S cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x+6][y+3]!=0 and val.count(board[x+6][y+3])!=0):
                    val.remove(board[x+6][y+3])

    if(i>=6 and i<=8 and j>=6 and j<=8): #SE cell
        x=0
        y=0
        for x in range(3):
            for y in range(3):
                if(board[x+6][y+6]!=0 and val.count(board[x+6][y+6])!=0):
                    val.remove(board[x+6][y+6])
########################################################################
#check row digits
def checkrow(val,i):
    for x in range(9):
        if(board[i][x]!=0 and val.count(board[i][x])!=0):
            val.remove(board[i][x])
#########################################################################
#check column digits
def checkcol(val,j):
    for x in range(9):
        if(board[x][j]!=0 and val.count(board[x][j])!=0):
            val.remove(board[x][j])
#########################################################################
def checkall(val,i,j):
    checkrow(val,i)
    checkcol(val,j)
    checkzone(val,i,j)
    return val
#########################################################################
#function to solve puzzle
def solver(val):
    global board
    n=0
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                x=checkall(val,i,j)
                if(len(x)>0):
                    board[i][j]=x[n]
                else

##########################################################################
def main():
    display_unsolved()
    solver(val)
    print("\n")
    display_unsolved()

main()
