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
    
def count_trees(data, slopes):
    width = len(data[0])
    height = len(data)
    cs = [0] * len(slopes)
    xs = [0] * len(slopes)
    for y, line in enumerate(data):
        # print(x, y)
        for index, slope in enumerate(slopes):
            if y % slope[1] != 0:
                continue
            if data[y][xs[index] % width] == '#':
                cs[index] += 1
            xs[index] += slope[0]
    return cs

def test1(data):
    return count_trees(data, [(3, 1)])[0]

def test2(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = count_trees(data, slopes)
    m = 1
    for n in trees:
        m *= n
    return m

def part1(data):
    return count_trees(data, [(3, 1)])[0]

def part2(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = count_trees(data, slopes)
    m = 1
    for n in trees:
        m *= n
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
