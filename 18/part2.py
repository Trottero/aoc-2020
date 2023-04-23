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


def solve_sub_expression(subline: List[str]):
    # Solves a subexpression
    # Sub expressions are line, without the brackets

    # First solve all of the additions
    while '+' in subline:
        for i, val in enumerate(subline):
            if val == '+':
                result = str(operators[val](int(subline[i-1]), int(subline[i+1])))
                del subline[i - 1:i+2]
                subline.insert(i - 1, result)
                break

    # Now solve all of the multiplications
    while '*' in subline:
        for i, val in enumerate(subline):
            if val == '*':
                result = str(operators[val](int(subline[i-1]), int(subline[i+1])))
                del subline[i - 1:i+2]
                subline.insert(i - 1, result)
                break

    return int(subline[0])


def solve_line(line: List[str]):
    # flatten the line
    line = [item for sublist in line for item in sublist]

    # Use regex to find the first bracketed expression
    # and evaluate it
    matches = re.search(r'\([+*\d]+\)', "".join(line))
    while matches is not None:
        match_start, match_end = find_first_bracket_expression(line)
        match = line[match_start+1:match_end]
        result = solve_sub_expression(match)
        # Remove this match from the line
        del line[match_start:match_end + 1]
        # Insert the result
        line.insert(match_start, str(result))

        matches = re.search(r'\([+*\d]+\)', "".join(line))

    print(line)

    return solve_sub_expression(line)


print(sum([solve_line(line) for line in lines]))
