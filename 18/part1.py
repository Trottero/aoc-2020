import re
from typing import List

with open('./18/input.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]


operators = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}

# Find locations of brackets followed by a number


def find_last_bracket_number(line):
    for i, val in enumerate(reversed(line)):
        if val == '(':
            if line[i+1].isnumeric():
                return i

    return None


def find_first_bracket_expression(line: List[str]):
    for i, val in enumerate(line):
        if val == '(':
            pass
            if all([line[x].isnumeric() or line[x] in operators for x in range(i + 1, line.index(')', i))]):
                return i, line.index(')', i)

    return None


def solve_line(line: List[str]):
    # flatten the line
    line = [item for sublist in line for item in sublist]

    # Use regex to find the first bracketed expression
    # and evaluate it
    matches = re.search(r'\([+*\d]+\)', "".join(line))
    while matches is not None:
        match_start, match_end = find_first_bracket_expression(line)
        match = line[match_start+1:match_end]
        result = int(match[0])
        for i in range(1, len(match), 2):
            result = operators[match[i]](result, int(match[i+1]))
        # Remove this match from the line
        del line[match_start:match_end + 1]
        # Insert the result
        line.insert(match_start, str(result))

        matches = re.search(r'\([+*\d]+\)', "".join(line))

    print(line)

    result = int(line[0])
    for i in range(1, len(line), 2):
        result = operators[line[i]](result, int(line[i+1]))

    return result


print(sum([solve_line(line) for line in lines]))
