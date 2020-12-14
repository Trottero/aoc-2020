import numpy as np

file = open('C:/Users/niels/source/repos/aoc-2020/1-4/input.txt').readlines()
file = [l.strip() for l in file]

mask = file[0].replace('mask = ', '')

memory = {}

def bit36(number):
    return format(number, '036b')

def mask_n(number):
    n36 = list(bit36(number))
    for i, m in enumerate(mask):
        if m == 'X':
            continue
        n36[i] = m
    return int("".join(n36), 2)

for instruction in file:
    spl = instruction.split('=')
    l = spl[0].strip('mem[] ')
    r = spl[1].strip()
    if l == 'ask':
        mask = r
    else:
        memory[l] = mask_n(int(r))

sum = np.sum([memory[key] for key in memory])
print(sum)