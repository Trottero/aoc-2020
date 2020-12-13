import numpy as np

file = open('C:/Users/niels/source/repos/aoc-2020/1-3-1/input.txt').readlines()
file = [l.strip() for l in file]

epoch = int(file[0])


busses_total = [bus for bus in file[1].split(',')]

offsets = [i for i, bus in enumerate(busses_total) if bus != 'x']
busses = np.array([int(bus) for bus in file[1].split(',') if bus != 'x'])

print(busses)
print(offsets)

timestep = 1
time = 1
for i, t in enumerate(zip(busses, offsets)):
    bus, offset = t
    while True:
        if (time + offset) % bus == 0:
            timestep = np.lcm(timestep, bus, dtype=np.uint64)
            break
        time += timestep
print(time)