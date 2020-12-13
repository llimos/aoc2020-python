import input

grid = [list(row) for row in input.lines(11)]

def occupied(x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]) and grid[y][x] == '#'

def empty(x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]) and grid[y][x] == 'L'

def process(testFn, limit):
    toYes = []
    toNo = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] != '.':
                surroundingOccupied = 0
                for testX in [-1, 0, 1]:
                    for testY in [-1, 0, 1]:
                        if (testX != 0 or testY != 0) and testFn(x, y, testX, testY):
                            surroundingOccupied += 1
                if surroundingOccupied == 0 and not occupied(x, y):
                    toYes.append([x,y])
                elif surroundingOccupied >= limit and occupied(x, y):
                    toNo.append([x, y])
    for [x, y] in toYes:
        grid[y][x] = '#'
    for [x, y] in toNo:
        grid[y][x] = 'L'
    return len(toNo) + len(toYes)

changes = 1
while changes:
    changes = process(lambda x, y, dX, dY: occupied(x + dX, y + dY), 4)

print(sum([len([x for x in row if x == '#']) for row in grid]))
del grid

# Part 2


def canSee(x, y, dX, dY):
    testX = x + dX
    testY = y + dY
    while testY >= 0 and testY < len(grid) and testX >= 0 and testX < len(grid[testY]):
        if occupied(testX, testY):
            return True
        elif empty(testX, testY):
            return False
        testX += dX
        testY += dY
    return False


grid = [list(row) for row in input.lines(11)]
# grid = [list(row) for row in """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL""".splitlines()]
changes = 1
while changes:
    changes = process(canSee, 5)
    # print('\n'.join([''.join(x) for x in grid]), '\n\n')

print(sum([len([x for x in row if x == '#']) for row in grid]))
