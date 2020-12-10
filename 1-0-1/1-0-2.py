import numpy as np

file = open('C:/Users/Niels/source/repos/aoc-2020/1-0-1/input.txt').readlines()
file = [int(l.strip()) for l in file]

# Add in and outlets
file.append(0)
device_jolts = np.max(file) + 3
file.append(device_jolts)

file.sort()
# All adapters have a -3 aswell

jumps = []
# Key: adapter from, value: amount of options
adapter_dict = {}

prev = 0


def options(adapter, adapter_options):
    r = []
    for ad in adapter_options:
        # for all of the options
        if ad > adapter and ad <= adapter + 3:
            r.append(ad)
    return r


for index, adapter in enumerate(file[:-1]):
    opts = options(adapter, file[index + 1:index + 4])
    print('index:', index, 'adapter:', adapter, 'opts: ', opts, 'from: ', file[index + 1:index + 4])
    adapter_dict[adapter] = len(opts)

total = 1
for opt_n in adapter_dict:
    total *= adapter_dict[opt_n]

print(total)