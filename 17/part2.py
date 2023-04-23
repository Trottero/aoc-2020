

with open('./17/input.txt', 'r') as f:
    lines = [[c for c in line.strip()] for line in f.readlines()]

active_nodes = set()

for i, row in enumerate(lines):
    for j, val in enumerate(row):
        if val == '#':
            active_nodes.add((j, i, 0, 0))


print(active_nodes)


def get_neighbours(x, y, z, w):
    neighbours = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    neighbours.add((x + i, y + j, z + k, w + l))

    neighbours.remove((x, y, z, w))
    return neighbours


cycles = 6
for cycle in range(cycles):
    new_active_nodes = set()

    neighbour_counts = {}
    for node in active_nodes:
        neighbours = get_neighbours(*node)
        active_neighbours = neighbours.intersection(active_nodes)
        if len(active_neighbours) in [2, 3]:
            new_active_nodes.add(node)

        non_active_neighbours = neighbours.difference(active_nodes)
        for non_active_neighbour in non_active_neighbours:
            neighbour_counts[non_active_neighbour] = neighbour_counts.get(non_active_neighbour, 0) + 1

    new_active_nodes.update(k for k, v in neighbour_counts.items() if v == 3)

    active_nodes = new_active_nodes

print(len(active_nodes))
