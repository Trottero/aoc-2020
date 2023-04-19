import numpy as np

file = open('C:/Users/sava/source/repos/aoc-2020/1-2-1/input.txt').readlines()
file = [l.strip() for l in file]

instructions = [(l[0], int(l[1:])) for l in file]

rotation_map = {
    270: 'N',
    0: 'E',
    90: 'S',
    180: 'W'
}

def execute_instruction(a, i, x, y, rotation):
    if a == 'N':
        y += i
    elif a == 'S':
        y -= i
    elif a == 'E':
        x += i
    elif a == 'W':
        x -= i
    elif a == 'F':
        return execute_instruction(rotation_map[rotation], i, x, y, rotation)
    elif a == 'R':
        rotation = (rotation + i) % 360
    elif a =='L':
        rotation = (rotation + 360 - i) % 360
    return x, y, rotation

# East = 0
rotation = 0
x = 0
y = 0

for instruction in instructions:
    a, i = instruction
    # print(a, i)
    x, y, rotation = execute_instruction(a, i, x, y, rotation)

print(abs(x) + abs(y))