#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 10
SOLVED_1 = True
SOLVED_2 = True

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
        jolt_diff = j - cur_jolt
        # print('diff: ', jolt_diff)
        r[jolt_diff - 1] += 1
        cur_jolt += jolt_diff
    r[2] += 1
    return r

def test2(data):
    a = [1, 1, 2, 4, 7, 13, 28]
    cur_jolt = 0
    ndata = [int(j) for j in data]
    ndata.append(0)
    ndata.sort()
    diff_run = [0]
    for i, jolt in enumerate(ndata):
        if jolt == 0:
            continue
        jolt_diff = jolt - cur_jolt
        cur_jolt += jolt_diff
        if jolt_diff == 1:
            diff_run[-1] += 1
        elif jolt_diff == 3:
            diff_run.append(0)
        else:
            raise Exception(f'Help! {i}, {jolt}')
    arrangements = 1
    for d in diff_run:
        arrangements *= a[d]

    print(diff_run)
    print(arrangements)
    return arrangements

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
    a = [1, 1, 2, 4, 7, 13]
    cur_jolt = 0
    ndata = [int(j) for j in data]
    ndata.append(0)
    ndata.sort()
    diff_run = [0]
    for i, jolt in enumerate(ndata):
        if jolt == 0:
            continue
        jolt_diff = jolt - cur_jolt
        cur_jolt += jolt_diff
        if jolt_diff == 1:
            diff_run[-1] += 1
        elif jolt_diff == 3:
            diff_run.append(0)
        else:
            raise Exception(f'Help! {i}, {jolt}')
    arrangements = 1
    for d in diff_run:
        arrangements *= a[d]

    print(diff_run)
    print(arrangements)
    return arrangements
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
    test_eq('Test 2.1', test2, 8, test_input_1)
    test_eq('Test 2.2', test2, 19208, test_input_2)
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
