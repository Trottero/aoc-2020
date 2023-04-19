import numpy as np
import re
import string
import pprint

file = open('C:/Users/Niels/source/repos/aoc-2020/0-9-1/input.txt').readlines()
file = [int(l.strip()) for l in file]

def combination_exists(number, amble):
    for i, num in enumerate(amble):
        # print(number, i, num, amble)
        if i + 1 != len(amble) and number - num in amble[i + 1:]:
            return True
    return False

preamble_n = 25
seq_index = 0

invalid_num = 0
# Start forloop but we can skip the first couple
for num in file[preamble_n:]:
    preamble = file[seq_index:seq_index + preamble_n]
    if not combination_exists(num, preamble):
        invalid_num = num
        break
    seq_index += 1

print('p1 solution:', invalid_num)

for idx, num in enumerate(file):
    numbers = []
    for numi in file[idx:]:
        numbers.append(numi)
        sum = np.sum(numbers)
        if sum > invalid_num:
            break
        if sum == invalid_num:
            print(np.max(numbers) + np.min(numbers))
            exit()
