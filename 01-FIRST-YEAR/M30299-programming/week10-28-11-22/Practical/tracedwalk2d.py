import random

def initialiseGrid():
    # grid initialised as 9x9, grid[] is x coord and grid[][] is y coord
    # top left is [0][0]
    grid = []
    for x in range(0,9):
        grid.append([])
        for i in range(0,9):
            grid[x].append(0)
    return grid

def walkOver(x, y):
    if x >=9:
        return True
    elif x < 0:
        return True
    elif y>= 9:
        return True
    elif y < 0:
        return True
    else:
        return False

def printGrid(grid):
    for each in grid:
        printString = ""
        for innerEach in each:
            printString += str(innerEach) + " "
        print(printString)

def goForWalk(grid):
    x = 5
    y = 5
    while not walkOver(x, y):
        grid[x][y] += 1
        direction = random.randint(1, 4)
        if direction == 1:
            # up (x-1)
            x -= 1
        elif direction == 2:
            # down (x+1)
            x += 1
        elif direction == 3:
            # left (y-1)
            y -= 1
        elif direction == 4:
            # right (y+1)
            y += 1
    printGrid(grid)



def main():
    grid = initialiseGrid()
    goForWalk(grid)


main()