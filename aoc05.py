#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 5
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()


def seat_ID(code):
    id = 0
    for c in code:
        id *= 2
        if c == 'B' or c =='R':
            id += 1
    return id

def test1(data):
    r = []
    for code in data:
        r.append(seat_ID(code))
    return r

def test2(data):
    return 0

def part1(data):
    highest = 0
    for code in data:
        id = seat_ID(code)
        if id > highest :
            highest = id
    return highest

def part2(data):
    # r = []
    s = [False] * 128 * 8
    for code in data:
        id = seat_ID(code)
        s[id] = True
        # r.append(id)

    print(s)

    started = False
    for id, seat in enumerate(s):
        if started == False and seat == True:
            started = True
        if started == True and seat == False:
            return id

    return None

if __name__ == '__main__':

    test_input_1 = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
    print('Test Part 1:')
    test_eq('Test 1.1', test1, [567, 119, 820], test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 0, test_input_2)
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
