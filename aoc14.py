#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 14
SOLVED_1 = True
SOLVED_2 = True

class Memory:
    def __init__(self):
        self.m = {}
        self.mask = {}

    def set_mask(self, mask):
        self.mask = {}
        bit = 35
        for mask_bit in mask:
            if mask_bit == '1':
                self.mask[bit] = 1
            elif mask_bit == '0':
                self.mask[bit] = 0
            bit -= 1

    def set_mem(self, address, value):
        max_int = (1 << 36) - 1
        for index in self.mask:
            bit = self.mask[index]
            n = 1 << index
            if bit == 1:
                value = value | n
            if bit == 0:
                value = value & (n ^ max_int)
        self.m[address] = value

    def exec(self, line):
        if line.startswith('mask'):
            s = line.split(' ')
            self.set_mask(s[2])
        elif line.startswith('mem'):
            s = line.split(' ')
            t = s[0].split('[')
            address = int(t[1][:-1])
            value = int(s[2])
            self.set_mem(address, value)
        else:
            raise Exception('Unknown command.')

class Memory2:
    def __init__(self):
        self.m = {}
        self.mask = {'0': [], '1': [], 'X': []}

    def set_mask(self, mask):
        self.mask = {'0': [], '1': [], 'X': []}
        bit = 35
        for mask_bit in mask:
            self.mask[mask_bit].append(bit)
            bit -= 1

    def next_floating(self, address, value, floating):
        if len(floating) == 0:
            self.m[address] = value
            return None

        max_int = (1 << 36) - 1
        n = 1 << floating[0]
        address = address | n
        self.next_floating(address, value, floating[1:])
        address = address & (n ^ max_int)
        self.next_floating(address, value, floating[1:])

    def set_mem(self, address, value):
        max_int = (1 << 36) - 1
        for index in self.mask['1']:
            n = 1 << index
            address = address | n
        self.next_floating(address, value, self.mask['X'])

    def exec(self, line):
        if line.startswith('mask'):
            s = line.split(' ')
            self.set_mask(s[2])
        elif line.startswith('mem'):
            s = line.split(' ')
            t = s[0].split('[')
            address = int(t[1][:-1])
            value = int(s[2])
            self.set_mem(address, value)
        else:
            raise Exception('Unknown command.')


        
def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def test1(data):
    m = Memory()
    for line in data:
        m.exec(line)

    s = 0
    for address in m.m:
        s += m.m[address]

    return s

def test2(data):
    m = Memory2()
    for line in data:
        m.exec(line)

    s = 0
    for address in m.m:
        s += m.m[address]

    return s

def part1(data):
    m = Memory()
    for line in data:
        m.exec(line)

    s = 0
    for address in m.m:
        s += m.m[address]

    return s

def part2(data):
    m = Memory2()
    for line in data:
        m.exec(line)

    s = 0
    for address in m.m:
        s += m.m[address]

    return s

if __name__ == '__main__':

    test_input_1 = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 165, test_input_1)
    print()

    test_input_2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''.splitlines()
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 208, test_input_2)
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
