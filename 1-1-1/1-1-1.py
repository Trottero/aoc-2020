import numpy as np

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
            rows = select_rows(matrix, i, j)

            if seat == 'L' and count_seats_occupied(rows) == 0: #Empty seat
                stable = False
                matrix_new[i][j] = '#' # Mark with person

            # Check whether the seats around it have 4 or more aorund it
            elif seat == '#' and count_seats_occupied(rows) - 1 >= 4: # Occupied seat -1 because your own seat is occupied
                stable = False
                matrix_new[i][j] = 'L' # go sit somewhere else

    # Return matrix and result
    # print('Resulting matrix: ')
    # for l in matrix_new:
    #     print(l)
    return matrix_new, stable

def count_seats_occupied(matrix):
    return np.sum([row.count('#') for row in matrix])

def select_rows(matrix, i, j):
    rows = []
    if i == 0: # First row
        rows = matrix[0: i + 2]
    elif i == len(matrix) - 1: # Last row
        rows = matrix[i -1:]
    else:
        rows = matrix[i-1: i + 2]
    
    # For every row splice the columns
    for index, row in enumerate(rows):
        if j == 0: # First column
            rows[index] = row[0: j + 2]
        elif j == len(row) - 1: # Last column
            rows[index] = row[j - 1:]
        else:
            rows[index] = row[j - 1: j + 2]
    return rows


n_matrix, stable = step(matrix)
while not stable:
    n_matrix, stable = step(n_matrix)

print(count_seats_occupied(n_matrix))