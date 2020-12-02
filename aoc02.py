#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 2
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def extract_policy_and_password(line):
    return line.strip().split(': ')

def check_password(policy, password):
    repetitions, letter = policy.split(' ')
    min_rep, max_rep = repetitions.split('-')
    letter_count = 0
    for l in password:
        if l == letter:
            letter_count += 1
    if letter_count < int(min_rep) or letter_count > int(max_rep):
        return 0
    return 1

def real_check_password(policy, password):
    positions, letter = policy.split(' ')
    first_pos, second_pos = positions.split('-')
    c = 0
    if password[int(first_pos) - 1] == letter:
        c += 1
    if password[int(second_pos) - 1] == letter:
        c += 1
    if c == 1:
        return 1
    return 0

def test1(data):
    return sum([check_password(*extract_policy_and_password(line)) for line in data])

def test2(data):
    return sum([real_check_password(*extract_policy_and_password(line)) for line in data])

def part1(data):
    return sum([check_password(*extract_policy_and_password(line)) for line in data])

def part2(data):
    return sum([real_check_password(*extract_policy_and_password(line)) for line in data])

if __name__ == '__main__':

    test_input_1 = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 2, test_input_1)
    print()

    test_input_2 = test_input_1
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 1, test_input_2)
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
