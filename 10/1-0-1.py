import numpy as np
import re
import string
import pprint

file = open('C:/Users/Niels/source/repos/aoc-2020/1-0-1/input.txt').readlines()
file = [int(l.strip()) for l in file]

file.sort()
# All adapters have a -3 aswell
device_jolts = np.max(file) + 3
file.append(device_jolts)

jumps = []

prev = 0
# Always pick lowest out of the adapters available for a step
for adapter in file:
    jumps.append(adapter - prev)
    prev = adapter

print(jumps.count(3) * jumps.count(1))

