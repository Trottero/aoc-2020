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

active_rules['8'] = ['42', '|', '42', '8']
active_rules['11'] = ['42', '31', '|', '42', '11', '31']

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

    # If the rules cant be expanded, break
    if to_remove == []:
        break
    # print(expanded_rules)

    # print(active_rules)

print(active_rules)

total = 0
for i in range(0, 20):
    for message in lines[line_start + 1:]:
        m = message[0]
        # Contrsutrct regex where any element of 42 can be repeated

        rule_42 = expanded_rules['42']
        rule_31 = expanded_rules['31']

        reg42 = f'{"|".join(rule_42)}'
        reg31 = f'{"|".join(rule_31)}'

        reg42_c = re.findall(reg42, m)
        if len(reg42_c) < 2:
            continue
        last_42 = reg42_c[-1]
        reg31_c = re.findall(reg31, m)
        if len(reg42_c) < len(reg31_c):
            continue

        regex = '^(' + reg42 + '){' + str(i+2) + ',}(' + reg31 + '){' + str(i+1) + '}$'
        if re.match(regex, m):
            total += 1

print(total)
