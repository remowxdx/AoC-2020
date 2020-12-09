#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 9
SOLVED_1 = True
SOLVED_2 = False

class XMAS:
    def __init__(self, secret, preamble_len):
        self.secret = [int(n) for n in secret]
        self.preamble_len = preamble_len

    def is_number_valid(self, pos):
        if pos < self.preamble_len:
            raise Exception('Cannot check preamble')

        start = pos - self.preamble_len
        for i in range(self.preamble_len - 1):
            for j in range(i + 1, self.preamble_len):
                if self.secret[start + i] + self.secret[start + j] == self.secret[pos]:
                    return True
        return False

    def __len__(self):
        return len(self.secret)

    def __getitem__(self, n):
        return self.secret[n]

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def test1(data):
    x = XMAS(data, 5)
    for i in range(5, len(x)):
        if not x.is_number_valid(i):
            return x[i]
    return None

def test2(data):
    return 0

def part1(data):
    x = XMAS(data, 25)
    for i in range(25, len(x)):
        if not x.is_number_valid(i):
            return x[i]
    return None

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 127, test_input_1)
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
