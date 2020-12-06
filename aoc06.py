#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 6
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def to_list(data):
    groups = []
    current_group = []
    print(data)
    for line in data:
        if line.strip() == '':
            groups.append(current_group)
            current_group = []
            continue
        print(line)
        for c in line.strip():
            if c not in current_group:
                current_group.append(c)
    groups.append(current_group)
    print(groups)
    return groups

def test1(data):
    s = 0
    for group in data:
        s += len(group)
    return s

def test2(data):
    return 0

def part1(data):
    s = 0
    for group in data:
        s += len(group)
    return s

def part2(data):
    return None

if __name__ == '__main__':

    test_input_raw = '''abc

a
b
c

ab
ac

a
a
a
a

b
'''.splitlines()
    test_input_1 = to_list(test_input_raw)
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 11, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 42, test_input_2)
    print()

    data_raw = get_input(f'input{DAY}')
    data = to_list(data_raw)

    r = part1(data)
    if r is not None:
        print('Part 1:', r)
        if SOLVED_1:
            check_solution(DAY, 1, r)
        else:
            save_solution(DAY, 1, r)

    r = part2(data)
    if r is not None:
        print('Part 2:', r)
        if SOLVED_2:
            check_solution(DAY, 2, r)
        else:
            save_solution(DAY, 2, r)
