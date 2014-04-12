from numpy import matrix
import random

row1 = [0,0,0,0]
row2 = [0,0,0,0]
row3 = [2,0,0,0]
row4 = [0,0,2,0]
grid = matrix([row1, row2, row3, row4])
def addnum():
    numList = random.sample([2,2,2,2,2,2,2,2,2,4],1)
    s = ''.join(map(str, numList))
    return int(s)
def pickrow(rowlist):
    rowlist = random.sample(rowlist,1)
    s = ''.join(map(str, rowlist))
    return int(s)
def moveleft(grid):

    possible_adds = []

    for h in range(4):



        row = grid.tolist()[h]



        for x in range(3,0,-1):



            while row[x-1] == 0 and row[x] != 0:
                row[x-1] = row[x]
                row[x] = 0






        for x in range(1,4):
            if row[x] == row[x-1] and row[x] != 0:
                row[x-1] *=2
                row[x] = 0

        for x in range(3,0,-1):



            while row[x-1] == 0 and row[x] != 0:
                row[x-1] = row[x]
                row[x] = 0

        if row[3] == 0:
            possible_adds.append(h)

        grid[h] = row
    row_index = pickrow(possible_adds)

    chosen_row = grid.tolist()[row_index]

    chosen_row[3] = addnum()
    grid[row_index] = chosen_row




def moveright(grid):
    possible_adds = []


    for h in range(4):

        row = grid.tolist()[h]

        for x in range(3):

            while row[x+1] == 0 and row[x] != 0:
                row[x+1] = row[x]
                row[x] = 0






        for x in range(-2,-5,-1):
            if row[x] == row[x+1] and row[x] != 0:
                row[x+1] *=2
                row[x] = 0

        for x in range(3):

            while row[x+1] == 0 and row[x] != 0:
                row[x+1] = row[x]
                row[x] = 0


        if row[0] == 0:
            possible_adds.append(h)



        grid[h] = row

    row_index = pickrow(possible_adds)

    chosen_row = grid.tolist()[row_index]
    chosen_row[0] = addnum()
    grid[row_index] = chosen_row



def moveup(grid):
    grid = grid.transpose()
    moveleft(grid)



def movedown(grid):
    grid = grid.transpose()
    moveright(grid)


# print(grid)
# moveright(grid)
# print(grid)

