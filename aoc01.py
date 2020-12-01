#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 1
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [int(n) for n in lines]

def test1(data):
    for first in data:
        for second in data:
            if first + second == 2020:
                return first * second
    return 0

def test2(data):
    for first in data:
        for second in data:
            for third in data:
                if first + second + third == 2020:
                    return first * second * third
    return 0

def part1(data):
    for first in data:
        for second in data:
            if first + second == 2020:
                return first * second
    return None

def part2(data):
    for first in data:
        for second in data:
            for third in data:
                if first + second + third == 2020:
                    return first * second * third
    return None

if __name__ == '__main__':

    test_input_1 = [1721, 979, 366, 299, 675, 1456]
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 514579, test_input_1)
    print()

    test_input_2 = test_input_1
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 241861950, test_input_2)
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
