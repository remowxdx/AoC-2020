#!/usr/bin/env python3

from aoc import *
from tools import Vector

pd = Debug(True)
DAY = 12
SOLVED_1 = True
SOLVED_2 = True

class Ship:
    def __init__(self):
        self.pos = Vector.null()
        self.dir = Vector.unit('E')
        self.waypoint = Vector(10, 1)

    def step(self, action, value):
        if action in Vector.directions:
            d = Vector.unit(action)
            self.pos += d * value
        elif action == 'L':
            while value > 0:
                self.dir.rotate_left_90()
                value -= 90
        elif action == 'R':
            while value > 0:
                self.dir.rotate_right_90()
                value -= 90
        elif action == 'F':
            d = self.dir
            self.pos += d * value
        else:
            raise Exception('Unknown action')

    def waypoint_step(self, action, value):
        if action in Vector.directions:
            d = Vector.unit(action)
            self.waypoint += d * value
        elif action == 'L':
            while value > 0:
                self.waypoint.rotate_left_90()
                value -= 90
        elif action == 'R':
            while value > 0:
                self.waypoint.rotate_right_90()
                value -= 90
        elif action == 'F':
            d = self.waypoint
            self.pos += d * value
        else:
            raise Exception('Unknown action')

    def parse_command(self, command):
        action = command[0]
        value = int(command[1:])
        return action, value

    def manhattan(self):
        return self.pos.manhattan()

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def test1(data):
    s = Ship()
    for command in data:
        s.step(*s.parse_command(command))
    return s.manhattan()

def test2(data):
    s = Ship()
    for command in data:
        s.waypoint_step(*s.parse_command(command))
    return s.manhattan()

def part1(data):
    s = Ship()
    for command in data:
        s.step(*s.parse_command(command))
    return s.manhattan()

def part2(data):
    s = Ship()
    for command in data:
        s.waypoint_step(*s.parse_command(command))
    return s.manhattan()

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
    test_eq('Test 2.1', test2, 286, test_input_1)
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
