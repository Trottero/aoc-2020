import numpy as np

file = open('C:/Users/sava/source/repos/aoc-2020/1-0-1/input.txt').readlines()
file = [int(l.strip()) for l in file]

# Add in and outlets
file.append(0)
file.append(np.max(file) + 3)
file.sort()


# Start out jump list with the first # of options
jumps = [1]

for index, adapter in enumerate(file):
    if index == 0:
        continue
    
    chain_sum = 0
    print('adapter:', adapter, file[max(0, index - 3):index])
    for jndex, potadapter in enumerate(file[max(0, index - 3):index]): # Iterate through the previous 3 adapters
        # check whether the current adapter connects to the previous adaptars
        if potadapter + 3 >= adapter:
            # Add the current known total to the current chain
            chain_sum += jumps[max(0, index - 3) + jndex]
    # Now that we know the total chain cost, we add it to the jump list
    jumps.append(chain_sum)

print(jumps)