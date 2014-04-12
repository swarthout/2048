from numpy import matrix
import random

row1 = [0,0,0,0]
row2 = [0,0,0,0]
row3 = [2,2,0,0]
row4 = [0,0,0,0]
grid = matrix([row1, row2, row3, row4])
def addnum():
    numList = random.sample([2,2,2,2,2,2,2,2,2,4],1)
    s = ''.join(map(str, numList))
    return int(s)
def moveleft(grid):
    randrow = random.randrange(0,4)

    for h in range(4):



        row = grid.tolist()[h]



        for x in range(3,0,-1):



            while row[x-1] == 0 and row[x] != 0:
                row[x-1] = row[x]
                row[x] = 0
                # x+=1





        for x in range(1,4):
            if row[x] == row[x-1] and row[x] != 0:
                row[x-1] *=2
                row[x] = 0

        for x in range(3,0,-1):



            while row[x-1] == 0 and row[x] != 0:
                row[x-1] = row[x]
                row[x] = 0
                # x+=1
        if h == randrow:
            row[3] = addnum()

        grid[h] = row




def moveright(grid):
    randrow = random.randrange(0,4)

    for h in range(4):

        row = grid.tolist()[h]

        for x in range(3):

            while row[x+1] == 0 and row[x] != 0:
                row[x+1] = row[x]
                row[x] = 0
                # x-=1





        for x in range(-2,-5,-1):
            if row[x] == row[x+1] and row[x] != 0:
                row[x+1] *=2
                row[x] = 0

        for x in range(3):

            while row[x+1] == 0 and row[x] != 0:
                row[x+1] = row[x]
                row[x] = 0
                # x-=1
        if h == randrow:
            row[0] = addnum()

        grid[h] = row

def moveup(grid):
    grid = grid.transpose()
    moveleft(grid)



def movedown(grid):
    grid = grid.transpose()
    moveright(grid)



# print(grid)
# movedown(grid)
# print(grid)



