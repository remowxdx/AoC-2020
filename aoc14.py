#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 14
SOLVED_1 = True
SOLVED_2 = False

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
        if address not in self.m:
            self.m[address] = 0
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
    return 0

def part1(data):
    m = Memory()
    for line in data:
        m.exec(line)

    s = 0
    for address in m.m:
        s += m.m[address]

    return s

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 165, test_input_1)
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
