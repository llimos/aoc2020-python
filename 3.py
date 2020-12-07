import input

grid = [[x == '#' for x in row] for row in input.lines(3)]
width = len(grid[0])

def trees(xstep, ystep):
    x = 0
    y = 0
    trees = 0
    while y < len(grid):
        if grid[y][x % width]:
            trees += 1
        x += xstep
        y += ystep
    return trees

print(trees(3,1))
print(trees(1,1)*trees(3,1)*trees(5,1)*trees(7,1)*trees(1,2))