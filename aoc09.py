#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 9
SOLVED_1 = True
SOLVED_2 = True

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

    def find_contiguous_set_fast(self, target):
        for start in range(len(self.secret) - 1):
            rs = self.secret[start]
            for end in range(start + 1, len(self.secret)):
                rs += self.secret[end]
                if rs == target:
                    return self.secret[start:end+1]
                if rs > target:
                    break
        return None

    def find_contiguous_set(self, target):
        for start in range(len(self.secret) - 1):
            for end in range(start + 2, len(self.secret)):
                r = self.secret[start:end]
                s = sum(r)
                if s == target:
                    return r
                if s > target:
                    break
        return None

    def find_contiguous_set_slow(self, target):
        for start in range(len(self.secret) - 1):
            for end in range(start + 2, len(self.secret)):
                r = self.secret[start:end]
                if sum(r) == target:
                    return r
        return None

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
    x = XMAS(data, 5)
    for i in range(5, len(x)):
        if not x.is_number_valid(i):
            # print(x[i])
            r = x.find_contiguous_set(x[i])
            # print(r)
            return min(r) + max(r)
    return None

def part1(data):
    x = XMAS(data, 25)
    for i in range(25, len(x)):
        if not x.is_number_valid(i):
            return x[i]
    return None

def part2(data):
    x = XMAS(data, 25)
    for i in range(25, len(x)):
        if not x.is_number_valid(i):
            # print(x[i])
            r = x.find_contiguous_set_fast(x[i])
            # print(r)
            return min(r) + max(r)
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

    print('Test Part 2:')
    test_eq('Test 2.1', test2, 62, test_input_1)
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
