import numpy as np

file = open('C:/Users/niels/source/repos/aoc-2020/1-4/input.txt').readlines()
file = [l.strip() for l in file]

memory = {}
mask = file[0].replace('mask = ', '')

def bit36(number):
    return format(number, '036b')

def mask_n(number):
    n36 = apply_mask(bit36(number), mask)
    
    # Count number of X's
    n_x = n36.count('X')
    if n_x == 0:
        return [int(n36, 2)]
    
    # Handle floating bits
    xmasks = [bit36(i) for i in range(0, 2**n_x)]
    return [int(apply_mask(n36, ms, x=True), 2) for ms in xmasks]

def apply_mask(number_36, mask_a, x=False):
    n36 = list(number_36)
    if not x:
        for i, m in enumerate(mask_a):
            if m == '0':
                continue
            n36[i] = m
    else: # This only replaces x's in the number
        c = 1
        for i, e in reversed(list(enumerate(n36))):
            if n36[i] == 'X':
                n36[i] = mask_a[-c]
                c += 1
    return "".join(n36)


for instruction in file:
    spl = instruction.split('=')
    l = spl[0].strip('mem[] ')
    r = spl[1].strip()
    if l == 'ask':
        mask = r
    else:
        adresses = mask_n(int(l))
        for adress in adresses:
            memory[adress] = int(r)

sum = sum([memory[key] for key in memory])
print(sum)