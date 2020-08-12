import numpy

possible_numbers=[1,2,3,4,5,6,7,8,9]
hash=[0,0,0,0,0,0,0,0,0]
#######################################################################
#sample board
board= [[0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,5,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,3,0,0,0]]
########################################################################
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
#########################################################################
#check row digits
def checkrow(i):
    global hash
    for x in range(9):
        if(board[i][x]!=0):
            hash[(board[i][x])-1]=(board[i][x])
#########################################################################
#check column digits
def checkcol(j):
    global hash
    for x in range(9):
        if(board[x][j]!=0):
            hash[(board[x][j])-1]=(board[x][j])
#########################################################################
#check 3x3 zone digits(only the 4 remaining cells)
def checkzone(i,j):
    loc=""
    global hash
    if(i==0 or i==3 or i==6):
        loc=loc+"N"
    if(i==2 or i==5 or i==8):
        loc=loc+"S"
    if(j==0 or j==3 or j==6):
        loc=loc+"W"
    if(j==2 or j==5 or j==8):
        loc=loc+"E"

    print(loc)

    return
#########################################################################
#function to solve puzzle
def solver():
    global hash
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                checkrow(i)
                checkcol(j)
                checkzone(i,j)
                print(hash)
                hash=[0]*9      #reset hash table of valid digits

def main():
    display_unsolved()
    solver()
    return

main()
