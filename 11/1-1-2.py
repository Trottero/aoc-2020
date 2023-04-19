import numpy as np
from numpy.lib.function_base import kaiser

file = open('C:/Users/sava/source/repos/aoc-2020/1-1-1/input.txt').readlines()
file = [l.strip() for l in file]

# States:

# . floor
# L empty seat
# # occupied
matrix = []
for line in file:
    t = []
    for c in line:
        t.append(c)
    matrix.append(t)

# print(matrix)

def step(matrix):
    matrix_new = [l.copy() for l in matrix]
    stable = True
    for i, row in enumerate(matrix):
        # print('row: ', row)
        for j, seat in enumerate(row):
             # Select submatrix

            if seat == 'L' and get_visisble_seats(matrix, i, j) == 0: #Empty seat
                stable = False
                matrix_new[i][j] = '#' # Mark with person

            # Check whether the seats around it have 4 or more aorund it
            elif seat == '#' and get_visisble_seats(matrix, i, j) >= 5:
                stable = False
                matrix_new[i][j] = 'L' # go sit somewhere else

    # Return matrix and result
    # print('Resulting matrix: ')
    # for l in matrix_new:
    #     print(l)
    return matrix_new, stable

def count_seats_occupied(matrix):
    return np.sum([row.count('#') for row in matrix])

def get_visisble_seats(matrix, i, j):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    c = 0
    for stepx, stepy in directions:
        x = j
        y = i
        seat_hit = False
        # Primary direction
        while not seat_hit:
            # Safeguards:
            if x + stepx >= 0 and x + stepx < len(matrix[0]) and y + stepy >= 0 and y + stepy < len(matrix):
                # Increment
                x += stepx
                y += stepy
                seat = matrix[y][x]
                if seat == '.':
                    continue
                if seat == 'L':
                    break
                if seat == '#':
                    c += 1
                    break
            else:
                break
        # Invert and reset x, y
        x = j
        y = i
        stepx = -stepx
        stepy = -stepy
        while not seat_hit:
            # Safeguards:
            if x + stepx >= 0 and x + stepx < len(matrix[0]) and y + stepy >= 0 and y + stepy < len(matrix):
                # Increment
                x += stepx
                y += stepy
                seat = matrix[y][x]
                if seat == '.':
                    continue
                if seat == 'L':
                    break
                if seat == '#':
                    c += 1
                    break
            else:
                break
    return c




n_matrix, stable = step(matrix)
while not stable:
    n_matrix, stable = step(n_matrix)

print(count_seats_occupied(n_matrix))