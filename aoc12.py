#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 12
SOLVED_1 = False
SOLVED_2 = False


class Ship:
    def __init__(self):
        self.pos = (0, 0)
        self.dir = (1, 0)

        self.char_to_dir = {
            'E': (1, 0),
            'W': (-1, 0),
            'S': (0, -1),
            'N': (0, 1),
        }

    def turn_left(self):
        self.dir = (-self.dir[1], self.dir[0])

    def turn_right(self):
        self.dir = (self.dir[1], -self.dir[0])

    def step(self, action, value):
        if action in self.char_to_dir:
            d = self.char_to_dir[action]
            self.pos = (self.pos[0] + d[0] * value, self.pos[1] + d[1] * value)
        elif action == 'L':
            while value > 0:
                self.turn_left()
                value -= 90
        elif action == 'R':
            while value > 0:
                self.turn_right()
                value -= 90
        elif action == 'F':
            d = self.dir
            self.pos = (self.pos[0] + d[0] * value, self.pos[1] + d[1] * value)
        else:
            raise Exception('Unknown action')

    def parse_command(self, command):
        action = command[0]
        value = int(command[1:])
        return action, value

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def test1(data):
    s = Ship()
    for command in data:
        s.step(*s.parse_command(command))
    return abs(s.pos[0]) + abs(s.pos[1])

def test2(data):
    return 0

def part1(data):
    s = Ship()
    for command in data:
        s.step(*s.parse_command(command))
    return abs(s.pos[0]) + abs(s.pos[1])

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''F10
N3
F7
R90
F11
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 25, test_input_1)
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
