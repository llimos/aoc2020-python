import input

directions = input.lines(12)

facing = 0 # degrees from east
pos = [0, 0] # east, north

for dir in directions:
    inst = dir[0]
    amount = int(dir[1:])
    if inst == 'N':
        pos[1] += amount
    elif inst == 'S':
        pos[1] -= amount
    elif inst == 'E':
        pos[0] += amount
    elif inst == 'W':
        pos[0] -= amount
    elif inst == 'F':
        if facing == 0:
            pos[0] += amount
        elif facing == 90:
            pos[1] -= amount
        elif facing == 180:
            pos[0] -= amount
        elif facing == 270:
            pos[1] += amount
    elif inst == 'R':
        facing = (facing + amount) % 360
    elif inst == 'L':
        facing = (360 + facing - amount) % 360


print(abs(pos[0])+abs(pos[1]))


waypoint = [10, 1]
pos = [0, 0] # east, north
for dir in directions:
    inst = dir[0]
    amount = int(dir[1:])
    if inst == 'N':
        waypoint[1] += amount
    elif inst == 'S':
        waypoint[1] -= amount
    elif inst == 'E':
        waypoint[0] += amount
    elif inst == 'W':
        waypoint[0] -= amount
    elif inst == 'F':
        pos[0] += waypoint[0] * amount
        pos[1] += waypoint[1] * amount
    elif inst in ['L','R'] and amount == 180:
        waypoint[0] *= -1
        waypoint[1] *= -1
    elif (inst == 'R' and amount == 90) or (inst == 'L' and amount == 270):
        waypoint = [
            waypoint[1],
            -waypoint[0]
        ]
    elif (inst == 'R' and amount == 270) or (inst == 'L' and amount == 90):
        waypoint = [
            -waypoint[1],
            waypoint[0]
        ]
    
print(abs(pos[0])+abs(pos[1]))


"""
R90
N | E | N' | E'
+   +   -    +
-   +   -    -
-   -   +    -
+   -   +    +

N' = reverse of E
E' = N

L90
N | E | N' | E'
+   +   +    -
+   -   -    -
-   -   -    +
-   +   +    +

N' = E
E' = reverse of N
"""