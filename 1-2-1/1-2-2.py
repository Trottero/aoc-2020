import numpy as np

file = open('C:/Users/sava/source/repos/aoc-2020/1-2-1/input.txt').readlines()
file = [l.strip() for l in file]

instructions = [(l[0], int(l[1:])) for l in file]

def execute_instruction(a, i, x, y, sx, sy):
    if a == 'N':
        y += i
    elif a == 'S':
        y -= i
    elif a == 'E':
        x += i
    elif a == 'W':
        x -= i
    elif a == 'F':
        # Move the ship and move the waypoint with it
        sx += i * x
        sy += i * y
    elif a == 'R':
        # Rotate coordinate system clockwise with i degrees
        for rep in range(int(i / 90)):
            # Swap x,y
            t = x
            x = y
            y = t

            # Invert y
            y = -y

    elif a =='L':
        for rep in range(int(i / 90)):
            # Swap x,y
            t = x
            x = y
            y = t
            # Invert x
            x = -x

    return x, y, sx, sy

sx = 0
sy = 0

x = 10
y = 1

for instruction in instructions:
    a, i = instruction
    # print(a, i)
    x, y, sx, sy = execute_instruction(a, i, x, y, sx, sy)

print(abs(sx) + abs(sy))