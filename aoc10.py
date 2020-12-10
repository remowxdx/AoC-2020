#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 10
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def test1(data):
    cur_jolt = 0
    ndata = [int(j) for j in data]
    ndata.sort()
    r = [0, 0, 0]
    for j in ndata:
        # print('j:', j)
        jolt_diff = int(j) - cur_jolt
        # print('diff: ', jolt_diff)
        r[jolt_diff - 1] += 1
        cur_jolt += jolt_diff
    r[2] += 1
    return r

def test2(data):
    return 0

def part1(data):
    cur_jolt = 0
    ndata = [int(j) for j in data]
    ndata.sort()
    r = [0, 0, 0]
    for j in ndata:
        jolt_diff = int(j) - cur_jolt
        r[jolt_diff - 1] += 1
        cur_jolt += jolt_diff
    r[2] += 1
    return r[0] * r[2]
    return None

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''16
10
15
5
1
11
7
19
6
12
4
'''.splitlines()
    test_input_2 = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, [7, 0, 5], test_input_1)
    test_eq('Test 1.2', test1, [22, 0, 10], test_input_2)
    print()

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
