#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 17
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

class Pocket:
    def __init__(self, dimensions, data):

        if dimensions < 2:
            raise ValueError("Dimension is too small.")

        self.active = set()
        self.dimensions = dimensions

        self.parse(data)
        self.create_dirs()

    def is_origin(self, coords):
        for coord in coords:
            if coord != 0:
                return False
        return True

    def create_dirs(self):
        self.dirs = [[]]
        for dim in range(self.dimensions):
            new_d = []
            for d in self.dirs:
                for c in range(2):
                    n = d[:]
                    n.append(c)
                    if dim != self.dimensions - 1 or not self.is_origin(n):
                        new_d.append(n)
                d.append(-1)
            self.dirs.extend(new_d)

    def parse(self, data):
        coord = [0] * self.dimensions
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '#':
                    coord[0] = x
                    coord[1] = y
                    self.active.add(tuple(coord))

    def activate(self, pos):
        self.active.add(pos)

    def deactivate(self, pos):
        if pos in self.active:
            self.active.remove(pos)

    def is_active(self, pos):
        return pos in self.active

    def bounding_box(self):
        min_max = [[0, 0]] * self.dimensions
        for pos in self.active:
            for coord in range(self.dimensions):
                if pos[coord] < min_max[coord][0]:
                    min_max[coord][0] = pos[coord]
                if pos[coord] > min_max[coord][1]:
                    min_max[coord][1] = pos[coord]
        return min_max

    def cycle(self):
        # min_max = self.bounding_box()
        # print('min max:', min_max)

        to_check = set()

        for cube in self.active:
            to_check.add(cube)
            for dir in self.dirs:
                neighbor = []
                for dim, coord in enumerate(cube):
                    neighbor.append(coord + dir[dim])
                to_check.add(tuple(neighbor))

        activate = []
        deactivate = []

        for cube in to_check:
            n = self.count_neighbors(cube)
            if self.is_active(cube):
                if n != 2 and n != 3:
                    deactivate.append(cube)
            else:
                if n == 3:
                    activate.append(cube)

        for cube in activate:
            self.activate(cube)

        for cube in deactivate:
            self.deactivate(cube)

    def count_active(self):
        return len(self.active)

    def count_neighbors(self, pos):
        count = 0
        for dpos in self.dirs:
            neighbor = []
            for dim, coord in enumerate(pos):
                neighbor.append(coord + dpos[dim])
            if self.is_active(tuple(neighbor)):
                count += 1
        return count

    def __str__(self):
        return 'TODO'
        r = []
        min_max = self.bounding_box()
        for z in range(min_max[2], min_max[5] + 1):
            r.append(f'\nz = {z}\n')
            for y in range(min_max[1], min_max[4] + 1):
                for x in range(min_max[0], min_max[3] + 1):
                    if self.is_active(x, y, z):
                        r.append('#')
                    else:
                        r.append('.')
                r.append('\n')
        return ''.join(r)


def test1(data):
    p = Pocket(3, data)
    # print(p)
    for c in range(6):
        p.cycle()
        # print(p)
    return p.count_active()

def test2(data):
    p = Pocket(4, data)
    # print(p)
    for c in range(6):
        p.cycle()
        # print(p)
    return p.count_active()

def part1(data):
    p = Pocket(3, data)
    # print(p)
    for c in range(6):
        p.cycle()
    return p.count_active()

def part2(data):
    p = Pocket(4, data)
    # print(p)
    for c in range(6):
        p.cycle()
        # print(p)
    return p.count_active()


if __name__ == '__main__':

    test_input_1 = '''.#.
..#
###
'''.splitlines()

    print('Test Part 1:')
    test_eq('Test 1.1', test1, 112, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 848, test_input_1)
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
