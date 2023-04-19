

with open('./16/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

rules = {}


def is_valid_for_rule(value, rule):
    lower1, upper1 = rule['1']
    lower2, upper2 = rule['2']
    return (lower1 <= value <= upper1) or (lower2 <= value <= upper2)


def is_valid_ticket(ticket, rules):
    return all([any([is_valid_for_rule(x, rule) for rule in rules.values()]) for x in ticket])


print(lines)
for i, val in enumerate(lines):
    if val == '':
        break

    t, remainder = val.split(':')
    lower, upper = remainder.split(' or ')
    rules[t] = {'1': [int(x) for x in lower.split('-')], '2': [int(x) for x in upper.split('-')]}

lines = lines[i+1:]
your_ticket = [int(x) for x in lines[1].split(',')]
print(your_ticket)
lines = lines[4:]
tickets = [[int(x) for x in line.split(',')] for line in lines]

print(tickets)


# Remove invalid tickets
tickets = [ticket for ticket in tickets if is_valid_ticket(ticket, rules)]
tickets.append(your_ticket)

# get a list of all rule names
rule_names = list(rules.keys())
# Create an index for each rule name with all of the poisslbile indexes
rule_indexes = {rule_name: set(range(len(rules))) for rule_name in rule_names}

for key, value in rule_indexes.items():
    print(key, value)
    to_remove = set()
    for column in value:
        if not all([is_valid_for_rule(ticket[column], rules[key]) for ticket in tickets]):
            to_remove.add(column)

    rule_indexes[key] = value - to_remove

while any([len(x) > 1 for x in rule_indexes.values()]):
    for key, value in rule_indexes.items():
        if len(value) == 1:
            for key2, value2 in rule_indexes.items():
                if key != key2:
                    rule_indexes[key2] = value2 - value

print(rule_indexes)

# Only take the keys that start with departure
departure_indexes = [x for x in rule_indexes.keys() if x.startswith('departure')]

mult = 1
for index in departure_indexes:
    mult *= your_ticket[list(rule_indexes[index])[0]]

print(mult)
