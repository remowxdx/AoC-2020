#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 3
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def to_array(data):
    return data.splitlines()
    
def count_trees(data, dx, dy):
    c = 0
    x = 0
    y = 0
    width = len(data[0])
    height = len(data)
    while y < height:
        # print(x, y)
        if data[y][x % width] == '#':
            c += 1
        x += dx
        y += dy
    return c

def test1(data):
    return count_trees(data, 3, 1)

def test2(data):
    m = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        m *= count_trees(data, *slope)
    return m

def part1(data):
    return count_trees(data, 3, 1)

def part2(data):
    m = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        m *= count_trees(data, *slope)
    return m

if __name__ == '__main__':

    test_input_raw = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''
    test_input_1 = to_array(test_input_raw)
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 7, test_input_1)
    print()

    test_input_2 = test_input_1
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 336, test_input_2)
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
