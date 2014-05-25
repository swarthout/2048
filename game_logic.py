from numpy import matrix
import random

row1 = [0,0,0,0]
row2 = [0,0,0,0]
row3 = [0,0,0,0]
row4 = [0,0,0,0]
grid = matrix([row1, row2, row3, row4])
score = 0

def newboard():
    for i in range(2):
        row_index = pickone([0,1,2,3])
        tile_index = pickone([0,1,2,3])

        chosen_row = grid.tolist()[row_index]
        while chosen_row[tile_index] != 0:
            tile_index = pickone([0,1,2,3])

        chosen_row[tile_index] = addnum()
        grid[row_index] = chosen_row



def addnum():
    numList = random.sample([2,2,2,2,2,2,2,2,2,4],1)
    s = ''.join(map(str, numList))
    return int(s)



def pickone(rowlist):
    rowlist = random.sample(rowlist,1)
    s = ''.join(map(str, rowlist))
    return int(s)

def removezero(the_list):
            return [value for value in the_list if value != 0]

def moveleft(grid):

    possible_adds = []

    for h in range(4):

        row = grid.tolist()[h]
        row = removezero(row)

        z = 0

        while z < (len(row)-1):
                    if row[z+1] == row[z]:
                        row[z] *= 2
                        del row[z+1]


                    z += 1
        for count in range(-len(row) + 4):
            row.append(0)





        if row[3] == 0:
            possible_adds.append(h)

        grid[h] = row
    row_index = pickone(possible_adds)

    chosen_row = grid.tolist()[row_index]

    chosen_row[3] = addnum()
    grid[row_index] = chosen_row



def moveright(grid):
    possible_adds = []

    for h in range(4):

        row = grid.tolist()[h]

        row = row[::-1]

        row = removezero(row)

        z = 0

        while z < (len(row)-1):
                    if row[z+1] == row[z]:
                        row[z] *= 2
                        del row[z+1]


                    z += 1
        for count in range(-len(row) + 4):
            row.append(0)





        if row[3] == 0:
            possible_adds.append(h)


        row = row[::-1]

        grid[h] = row
    row_index = pickone(possible_adds)

    chosen_row = grid.tolist()[row_index]

    chosen_row[0] = addnum()

    grid[row_index] = chosen_row





def moveup(grid):
    grid = grid.transpose()
    moveleft(grid)



def movedown(grid):
    grid = grid.transpose()
    moveright(grid)


