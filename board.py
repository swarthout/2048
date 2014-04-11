from numpy import matrix


row1 = [0,0,0,4]
row2 = [16,4,2,4]
row3 = [2,2,8,4]
row4 = [4,2,8,32]
grid = matrix([row1, row2, row3, row4])

def moveleft(grid):
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

        grid[h] = row

def moveright(grid):
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



