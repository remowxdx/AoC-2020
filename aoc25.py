#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 25
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()


def loop_size(subject_number, mod, pk):
    value = 1
    ls = 0
    while value != pk:
        value = (value * subject_number) % mod
        ls += 1
    print(f'Loop size of {pk}: {ls}')
    return ls

def encryption_key(subject_number, loop_size, mod):
    value = 1
    i = 0
    for i in range(loop_size):
        value = (value * subject_number) % mod

    return value

def test1(data):
    subject_number = 7
    mod = 20201227
    card_pk = int(data[0])
    door_pk = int(data[1])
    card_ls = loop_size(subject_number, mod, card_pk)
    # door_ls = loop_size(subject_number, mod, door_pk)
    r = encryption_key(door_pk, card_ls, mod)
    return r

def test2(data):
    return 0

def part1(data):
    subject_number = 7
    mod = 20201227
    card_pk = int(data[0])
    door_pk = int(data[1])
    card_ls = loop_size(subject_number, mod, card_pk)
    # door_ls = loop_size(subject_number, mod, door_pk)
    r = encryption_key(door_pk, card_ls, mod)
    return r


def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = ['5764801', '17807724']
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 14897079, test_input_1)
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
