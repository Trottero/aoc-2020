

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

print(lines)

tickets = [ticket for ticket in tickets if not is_valid_ticket(ticket, rules)]

# flatten the array
tickets = [item for sublist in tickets for item in sublist]

print(sum([x for x in tickets if not any([is_valid_for_rule(x, rule) for rule in rules.values()])]))
