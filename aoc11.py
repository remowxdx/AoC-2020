#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 11
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

class WaitingArea:
    def __init__(self, floor):
        self.floor = floor
        self.width = len(self.floor[0])
        self.height = len(floor)

    def seat(self, x, y):
        return self.floor[y][x]

    def occupied_neighbors(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                ox = x + dx
                oy = y + dy
                if ox >= 0 and oy >= 0 and ox < self.width and oy < self.height:
                    if self.seat(ox, oy) == '#':
                        count += 1
        return count

    def step(self):
        next_step = []
        changed = False
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                s = self.seat(x, y)
                if s == '.':
                    row += '.'
                else:
                    o = self.occupied_neighbors(x, y)
                    if o == 0:
                        row += '#'
                        if s != '#':
                            changed = True
                    elif o >= 4:
                        row += 'L'
                        if s != 'L':
                            changed = True
                    else:
                        row += s
            next_step.append(row)
        self.floor = next_step
        return changed

    def count_occupied(self):
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                s = self.seat(x, y)
                if s == '#':
                    count += 1
        return count

def test1(data):
    w = WaitingArea(data)
    c = True
    turns = 0
    # print('------', turns)
    # print('\n'.join(w.floor))
    while c:
        c = w.step()
        # print('------', turns)
        # print('\n'.join(w.floor))
        turns += 1
    return w.count_occupied()

def test2(data):
    return 0

def part1(data):
    w = WaitingArea(data)
    c = True
    turns = 0
    print('------', turns)
    print('\n'.join(w.floor))
    turns += 1
    while c:
        c = w.step()
        turns += 1
    print('------', turns)
    print('\n'.join(w.floor))
    return w.count_occupied()

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 37, test_input_1)
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
