#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 13
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def get_lines_in_service(lines):
    service = []
    for line in lines.split(','):
        if line == 'x':
            continue
        service.append(int(line))
    return service

def test1(data):
    after = int(data[0])
    lines = get_lines_in_service(data[1])
    next_departure = {}
    earliest_line = -1
    earliest_departure = after + lines[0]
    for line in lines:
        departure = ((after // line) + 1) * line
        next_departure[line] = departure
        if departure < earliest_departure:
            earliest_departure = departure
            earliest_line = line

    return (earliest_departure - after) * earliest_line

def test2(data):
    return 0

def part1(data):
    after = int(data[0])
    lines = get_lines_in_service(data[1])
    next_departure = {}
    earliest_line = -1
    earliest_departure = after + lines[0]
    for line in lines:
        departure = ((after // line) + 1) * line
        next_departure[line] = departure
        if departure < earliest_departure:
            earliest_departure = departure
            earliest_line = line

    return (earliest_departure - after) * earliest_line

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''939
7,13,x,x,59,x,31,19
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 295, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 42, test_input_2)
    print()

    data = get_input(f'input{DAY}')

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
