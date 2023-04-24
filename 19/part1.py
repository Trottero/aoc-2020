import re
from typing import List

with open('./19/input.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

expanded_rules = {}
active_rules = {}

for line_start, line in enumerate(lines):
    if line == ['']:
        break
    rule_num = line[0][:-1]
    if line[1] == '"a"':
        expanded_rules[rule_num] = ['a']
    elif line[1] == '"b"':
        expanded_rules[rule_num] = ['b']
    else:
        active_rules[rule_num] = line[1:]

while active_rules:
    to_remove = []
    for rule_key, rule in active_rules.items():
        # Check if we know how to expand all of the rules
        pass
        if all(x in expanded_rules for x in rule if x.isnumeric()):
            oror = []

            current = []
            for x in rule:
                # If so, expand them
                if x == '|':
                    oror += current
                    current = []
                    continue

                if len(current) == 0:
                    current = expanded_rules[x]
                    continue

                current = [z + y for z in current for y in expanded_rules[x]]

            oror += current

            expanded_rules[rule_key] = oror
            to_remove.append(rule_key)

    for rule_key in to_remove:
        del active_rules[rule_key]

    # print(expanded_rules)

    # print(active_rules)

total = 0
for message in lines[line_start + 1:]:
    if message[0] in expanded_rules['0']:
        total += 1

print(total)
