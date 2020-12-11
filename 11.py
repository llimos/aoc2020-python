import input

grid = [x for x in input.lines(11)]

def occupied(x, y):
    return y < len(grid) and x < len(grid[y]) and grid[y][x] == '#'

def process():
    toToggle = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            surroundingOccupied = 0
            for testX in range(x-1, x+2):
                for testY in range(y-1, y+2):
                    if (testX != x or testY != y) and occupied(testX, testY):
                        surroundingOccupied += 1
            
