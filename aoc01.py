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

def find_sum_eq(data, target, num):
    if num == 0:
        if target == 0:
            return []
        else:
            return False

    for n in data:
        r = find_sum_eq(data, target - n, num - 1)
        if r is False:
            continue
        else:
            r.append(n)
            return r
    return False

def list_mult(data):
    r = 1
    for n in data:
        r *= n
    return r

def test1(data):
    r = find_sum_eq(data, 2020, 2)
    return list_mult(r)

def test2(data):
    r = find_sum_eq(data, 2020, 3)
    return list_mult(r)

def part1(data):
    r = find_sum_eq(data, 2020, 2)
    return list_mult(r)

def part2(data):
    r = find_sum_eq(data, 2020, 3)
    return list_mult(r)

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
