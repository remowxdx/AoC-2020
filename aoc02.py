#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 2
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def process_input(raw_data):
    r = []
    for line in raw_data:
        policy, password = line.strip().split(':')
        r.append((password, policy))
    return r

def check_password(policy, password):
    repetitions, letter = policy.split(' ')
    min_rep, max_rep = repetitions.split('-')
    letter_count = 0
    for l in password:
        if l == letter:
            letter_count += 1
    if letter_count < int(min_rep) or letter_count > int(max_rep):
        return False
    return True

def count_valid_passwords(data):
    c = 0
    for password, policy in data:
        if check_password(policy, password):
            c += 1
    return c

def test1(data):
    return count_valid_passwords(data)

def test2(data):
    return 0

def part1(data):
    return count_valid_passwords(data)

def part2(data):
    return None

if __name__ == '__main__':

    raw_test_input = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
'''.splitlines()
    test_input_1 = process_input(raw_test_input)
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 2, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 42, test_input_2)
    print()

    raw_data = get_input(f'input{DAY}')
    data = process_input(raw_data)

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
