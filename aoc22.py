#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 22
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def build_decks(data):
    decks = []
    player = None
    for line in data:
        if line.startswith('Player '):
            player = int(line[7:-1]) - 1
            decks.append([])
        elif line == '':
            continue
        elif line.isdigit():
            decks[player].append(int(line))
        else:
            raise Exception(f'Unknown line: {line}.')

    return decks

def play_round(decks):
    c1 = decks[0][0]
    decks[0] = decks[0][1:]
    c2 = decks[1][0]
    decks[1] = decks[1][1:]

    if c1 > c2:
        decks[0].extend([c1, c2])
    if c2 > c1:
        decks[1].extend([c2, c1])
    
def evaluate_deck(deck):
    s = 0
    l = len(deck)
    for i, c in enumerate(deck):
        s += c * (l - i)
    return s

def test1(data):
    decks = build_decks(data)
    while True:
        if len(decks[0]) == 0:
            return evaluate_deck(decks[1])
        if len(decks[1]) == 0:
            return evaluate_deck(decks[0])
        play_round(decks)

    return 0

def test2(data):
    return 0

def part1(data):
    decks = build_decks(data)
    while True:
        if len(decks[0]) == 0:
            return evaluate_deck(decks[1])
        if len(decks[1]) == 0:
            return evaluate_deck(decks[0])
        play_round(decks)

    return 0
    return None

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 306, test_input_1)
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
