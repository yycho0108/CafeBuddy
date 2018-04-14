import numpy as np

height = 5.8
pace = height * .46
print(pace)

cafHeight = int(63/pace)
cafWidth = int(63/pace)

print(cafHeight)
print(cafWidth)

numTables = 6

caf = np.zeros(shape=(cafWidth, cafHeight))


def mapTables(row, col, table, dim):
    if row + dim >= cafHeight:
        vert = cafHeight - row
        rowMinus = row + dim - cafHeight

    else:
        vert = dim
        rowMinus = 0

    for x in range(row - rowMinus, row + vert):

        if col + dim >= cafWidth:
            horz = cafWidth - col
            colMinus = col + dim - cafWidth

        else:
            horz = dim
            colMinus = 0

        for y in range(col - colMinus, col + horz):
            caf[x][y] = table


mapTables(1, 6, 1, 4)
mapTables(9, 18, 2, 4)
mapTables(1, 13, 3, 4)
mapTables(16, 9, 4, 5)
mapTables(9, 1, 5, 4)
mapTables(8, 9, 6, 5)

print(caf)

directions = []

def nav(tableNum):

    suggestedTable = []
    otherTables = []

    startX = 0
    startY = 0

    for x in range(0, cafHeight):
        for y in range(0, cafWidth):
            caf[x][y] = int(caf[x][y])
            if caf[x][y] == tableNum:
                suggestedTable.append((x, y))
            if (caf[x][y] > 0) & (caf[x][y] != tableNum):
                otherTables.append(caf[x][y])

    minY = cafWidth - 1
    minX = cafHeight - 1

    for point in suggestedTable:
        if point[0] < minX:
            minX = point[0]
        if point[1] < minY:
            minY = point[1]

    print(minX)
    print(minY)

    x = startX
    y = startY

    while caf[x][y] != tableNum:
        while (caf[x][y] == 0) & (x < minX):
            directions.append("straight")
            x = x + 1

        while (caf[x][y] == 0) & (y < minY):
            directions.append("left")
            y = y + 1


        while (caf[x][y+1] != 0) & (x > 0):
            x = x - 1
            directions.append("back")

        while (caf[x][y] == 0) & (y < minY):
            directions.append("left")
            y = y + 1


        while (caf[x][y] == 0) & (y < minY):
            directions.append("left")
            y = y + 1

        while (caf[x][y] == 0) & (x < minX):
            directions.append("straight")
            x = x + 1




    print(caf[x][y])
    print(directions)


nav(3)

