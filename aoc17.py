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
    def __init__(self, data):
        self.active = set()
        self.parse(data)
        self.dirs = []
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if x == 0 and y == 0 and z == 0:
                        continue
                    self.dirs.append((x, y, z))

    def parse(self, data):
        z = 0
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '#':
                    self.active.add((x, y, z))

    def activate(self, x, y, z):
        self.active.add((x, y, z))

    def deactivate(self, x, y, z):
        if (x, y, z) in self.active:
            self.active.remove((x, y, z))

    def is_active(self, x, y, z):
        return (x, y, z) in self.active

    def find_limits(self):
        min_max = [0, 0, 0, 0, 0, 0]
        for x, y, z in self.active:
            if x < min_max[0]:
                min_max[0] = x
            if x > min_max[3]:
                min_max[3] = x
            if y < min_max[1]:
                min_max[1] = y
            if y > min_max[4]:
                min_max[4] = y
            if z < min_max[2]:
                min_max[2] = z
            if z > min_max[5]:
                min_max[5] = z
        return min_max

    def cycle(self):
        min_max = self.find_limits()
        print('min max:', min_max)

        activate = []
        deactivate = []

        for z in range(min_max[2] - 1, min_max[5] + 2):
            for y in range(min_max[1] - 1, min_max[4] + 2):
                for x in range(min_max[0] - 1, min_max[3] + 2):
                    n = self.count_neighbors(x, y, z)
                    if self.is_active(x, y, z):
                        if n != 2 and n != 3:
                            deactivate.append((x, y, z))
                    else:
                        if n == 3:
                            activate.append((x, y, z))

        for p in activate:
            self.activate(*p)

        for p in deactivate:
            self.deactivate(*p)

    def count_active(self):
        return len(self.active)

    def count_neighbors(self, x, y, z):
        count = 0
        for dx, dy, dz in self.dirs:
            if self.is_active(x + dx, y + dy, z + dz):
                count += 1
        return count

    def __str__(self):
        r = []
        min_max = self.find_limits()
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


class HyperPocket:
    def __init__(self, data):
        self.active = set()
        self.parse(data)
        self.dirs = []
        for w in range(-1, 2):
            for z in range(-1, 2):
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        if x == 0 and y == 0 and z == 0 and w == 0:
                            continue
                        self.dirs.append((x, y, z, w))

    def parse(self, data):
        z = 0
        w = 0
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '#':
                    self.active.add((x, y, z, w))

    def activate(self, x, y, z, w):
        self.active.add((x, y, z, w))

    def deactivate(self, x, y, z, w):
        if (x, y, z, w) in self.active:
            self.active.remove((x, y, z, w))

    def is_active(self, x, y, z, w):
        return (x, y, z, w) in self.active

    def find_limits(self):
        min_max = [0, 0, 0, 0, 0, 0, 0, 0]
        for x, y, z, w in self.active:
            if x < min_max[0]:
                min_max[0] = x
            if x > min_max[4]:
                min_max[4] = x
            if y < min_max[1]:
                min_max[1] = y
            if y > min_max[5]:
                min_max[5] = y
            if z < min_max[2]:
                min_max[2] = z
            if z > min_max[6]:
                min_max[6] = z
            if w < min_max[3]:
                min_max[3] = w
            if w > min_max[7]:
                min_max[7] = w
        return min_max

    def cycle(self):
        min_max = self.find_limits()
        print('min max:', min_max)

        activate = []
        deactivate = []

        for w in range(min_max[3] - 1, min_max[7] + 2):
            for z in range(min_max[2] - 1, min_max[6] + 2):
                for y in range(min_max[1] - 1, min_max[5] + 2):
                    for x in range(min_max[0] - 1, min_max[4] + 2):
                        n = self.count_neighbors(x, y, z, w)
                        if self.is_active(x, y, z, w):
                            if n != 2 and n != 3:
                                deactivate.append((x, y, z, w))
                        else:
                            if n == 3:
                                activate.append((x, y, z, w))

        for p in activate:
            self.activate(*p)

        for p in deactivate:
            self.deactivate(*p)

    def count_active(self):
        return len(self.active)

    def count_neighbors(self, x, y, z, w):
        count = 0
        for dx, dy, dz, dw in self.dirs:
            if self.is_active(x + dx, y + dy, z + dz, w + dw):
                count += 1
        return count

    def __str__(self):
        r = []
        min_max = self.find_limits()
        for w in range(min_max[3], min_max[7] + 1):
            for z in range(min_max[2], min_max[6] + 1):
                r.append(f'\nz = {z}, w = {w}\n')
                for y in range(min_max[1], min_max[5] + 1):
                    for x in range(min_max[0], min_max[4] + 1):
                        if self.is_active(x, y, z, w):
                            r.append('#')
                        else:
                            r.append('.')
                    r.append('\n')
        return ''.join(r)


def test1(data):
    p = Pocket(data)
    print(p)
    for c in range(6):
        p.cycle()
        # print(p)
    return p.count_active()

def test2(data):
    p = HyperPocket(data)
    print(p)
    for c in range(6):
        p.cycle()
        # print(p)
    return p.count_active()

def part1(data):
    p = Pocket(data)
    print(p)
    for c in range(6):
        p.cycle()
    return p.count_active()

def part2(data):
    p = HyperPocket(data)
    print(p)
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
