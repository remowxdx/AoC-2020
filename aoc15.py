#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 15
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def test1(data):
    n = 2020

    print(data)
    start = [int(n) for n in data[0].split(',')]
    print(start)

    numbers = {}
    for i, num in enumerate(start):
        if num in numbers:
            is_new = False
        else:
            is_new = True
        prev = (num, i + 1)
        numbers[num] = i + 1
    print(numbers, is_new)

    for i in range(len(start)+1, n+1):
        if is_new:
            prev = (0, numbers[0])
            numbers[0] = i
            is_new = False
        else:
            next_num = i - prev[1] - 1
            # print(i, prev, numbers[prev[0]], next_num)
            if next_num in numbers:
                is_new = False
                prev = (next_num, numbers[next_num])
            else:
                is_new = True
                prev = (next_num, i)
            numbers[next_num] = i
        print(f'{i}: {prev}', is_new)
    return prev[0]

def test2(data):
    return 0

def part1(data):
    n = 2020

    print(data)
    start = [int(n) for n in data[0].split(',')]
    print(start)

    numbers = {}
    for i, num in enumerate(start):
        if num in numbers:
            is_new = False
        else:
            is_new = True
        prev = (num, i + 1)
        numbers[num] = i + 1
    print(numbers, is_new)

    for i in range(len(start)+1, n+1):
        if is_new:
            prev = (0, numbers[0])
            numbers[0] = i
            is_new = False
        else:
            next_num = i - prev[1] - 1
            # print(i, prev, numbers[prev[0]], next_num)
            if next_num in numbers:
                is_new = False
                prev = (next_num, numbers[next_num])
            else:
                is_new = True
                prev = (next_num, i)
            numbers[next_num] = i
        print(f'{i}: {prev}', is_new)
    return prev[0]

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '0,3,6'.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 436, test_input_1)
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
