#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 8
SOLVED_1 = True
SOLVED_2 = False

class Console:
    def __init__(self, code):
        self.decode(code)
        self.instruction = 0
        self.accumulator = 0
        self.executed = []

    def execute(self, instruction, argument):
        if instruction == 'acc':
            self.accumulator += argument
            self.instruction += 1
        elif instruction == 'jmp':
            self.instruction += argument
        elif instruction == 'nop':
            self.instruction += 1
        else:
            raise "Unknown instruction."

    def step(self):
        if self.instruction >= len(self.code):
            raise "Executing instruction out of range."
        if self.instruction < 0:
            raise "Executing non existing instruction."
        print(f'{self.instruction}: {self.code[self.instruction][0]} {self.code[self.instruction][1]}')
        self.executed.append(self.instruction);
        self.execute(self.code[self.instruction][0], self.code[self.instruction][1])

    def run(self):
        while True:
            if self.instruction in self.executed:
                return self.accumulator
            self.step()
        return None

    def decode(self, lines):
        self.code = []
        for line in lines:
            instruction, argument = line.split()
            self.code.append((instruction, int(argument)))
        print(self.code)


def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def test1(data):
    c = Console(data)
    return c.run()

def test2(data):
    return 0

def part1(data):
    c = Console(data)
    return c.run()

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 5, test_input_1)
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
