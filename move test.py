testrow1 = [8,8,None,2]
testrow2 = [8,4,2,2]
testrow3 = [4,8,None,None]
testrow4 = [2,8,None,2]
testcolumn1 = [testrow1[0],testrow2[0],testrow3[0],testrow4[0]]
testcolumn2 = [testrow1[1],testrow2[1],testrow3[1],testrow4[1]]
testcolumn3 = [testrow1[2],testrow2[2],testrow3[2],testrow4[2]]
testcolumn4 = [testrow1[3],testrow2[3],testrow3[3],testrow4[3]]
testgrid = [testrow1,testrow2,testrow3,testrow4]

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
    print(row)
def moveright(row):


    for x in range(-2,-5,-1):

        while row[x+1] == None and row[x] != None:
            row[x+1] = row[x]
            row[x] = None
            x+=1




    for x in range(-2,-5,-1):
        if row[x] == row[x+1] and row[x] != None:
            row[x+1] *=2
            row[x] = None

    for x in range(-2,-5,-1):

            while row[x+1] == None and row[x] != None:
                row[x+1] = row[x]
                row[x] = None
                x+=1

    print(row)
def moveup(column):
    moveleft(column)
def movedown(column):
    moveright(column)

def update():
    pass
print(testgrid)
moveup(testcolumn1)
print(testgrid)

