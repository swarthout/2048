class board():
    row1 = [2,4,8,8]
    row2 = [16,4,2,4]
    row3 = [2,2,8,4]
    row4 = [4,2,8,32]
    def __init__(self):
        pass
    def updateboard():

        grid = str(board.row1)+"\n" +str(board.row2)+ "\n" + str(board.row3) + "\n" + str(board.row4)
        return grid
    def moveleft(row):

        for x in range(1,4):


            while row[x-1] == None and row[x] != None:
                row[x-1] = row[x]
                row[x] = None
                x-=1




        for x in range(1,4):
            if row[x] == row[x-1] and row[x] != None:
                row[x-1] *=2
                row[x] = None
        for x in range(1,4):


            while row[x-1] == None and row[x] != None:
                row[x-1] = row[x]
                row[x] = None
                x-=1

game = board
print(game.updateboard())
game.moveleft(game.row1)

print(game.updateboard())






