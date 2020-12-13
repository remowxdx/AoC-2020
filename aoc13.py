#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 13
SOLVED_1 = True
SOLVED_2 = True

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

def get_diff_lines(lines):
    service = []
    for diff, line in enumerate(lines.split(',')):
        if line == 'x':
            continue
        service.append((int(line), diff))
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

def combine(l1, l2):
    b1, o1 = l1
    b2, o2 = l2

    d1 = b1 - o1
    d2 = b2 - o2

    n1 = 1
    while True:
        t = n1 * b1 + d1
        if (t + d2) % b2 == 0:
            b3 = b1 * b2
            n3 = t // b3 + 1
            o3 = b3 * n3 - t
            return b3, o3
        n1 += 1

def test2(data):
    diff = get_diff_lines(data[1])
    cur = (1,0)
    for i, l in enumerate(diff):
        cur = combine(cur, l)
    return cur[1]

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
    diff = get_diff_lines(data[1])
    cur = (1,0)
    for i, l in enumerate(diff):
        cur = combine(cur, l)
    return cur[1]

if __name__ == '__main__':

    test_input_1 = '''939
7,13,x,x,59,x,31,19
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 295, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 1068781, test_input_1)
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
