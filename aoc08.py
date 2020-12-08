#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 8
SOLVED_1 = True
SOLVED_2 = True

class ConsoleException(Exception):
    pass

class ConsoleError(ConsoleException):
    def __init__(self, console, message):
        self.console = console
        self.message = message

    def __str__(self):
        return f'Console: {self.message} on instruction {self.console.instruction} with accumulator {self.console.accumulator}.'

class ConsoleInfiniteLoop(ConsoleException):
    def __init__(self, console):
        self.console = console

    def __str__(self):
        return f'Console: entered infinite loop on instruction {self.console.instruction} with accumulator {self.console.accumulator}.'

class ConsoleTerminated(ConsoleException):
    def __init__(self, console):
        self.console = console

    def __str__(self):
        return f'Console: program terminated on instruction {self.console.instruction} with accumulator {self.console.accumulator}.'

class Console:
    def __init__(self, code):
        self.load(code)
        self.restart()

    def restart(self):
        self.instruction = 0
        self.accumulator = 0
        self.executed = []

    def modify(self, instruction):
        if self.code[instruction][0] == 'nop':
            self.code[instruction] = ('jmp', self.code[instruction][1])
            return True
        elif self.code[instruction][0] == 'jmp':
            self.code[instruction] = ('nop', self.code[instruction][1])
            return True
        else:
            return False

    def execute(self, instruction, argument):
        if instruction == 'acc':
            self.accumulator += argument
            self.instruction += 1
        elif instruction == 'jmp':
            self.instruction += argument
        elif instruction == 'nop':
            self.instruction += 1
        else:
            raise ConsoleError(self, "unknown instruction")

    def step(self):
        if self.instruction in self.executed:
            raise ConsoleInfiniteLoop(self)
        if self.instruction == len(self.code):
            raise ConsoleTerminated(self)
        if self.instruction > len(self.code):
            raise ConsoleError(self, "executing instruction out of range")
        if self.instruction < 0:
            raise ConsoleError(self, "executing non existing instruction")
        # print(f'{self.instruction}: {self.code[self.instruction][0]} {self.code[self.instruction][1]}')
        self.executed.append(self.instruction);
        self.execute(self.code[self.instruction][0], self.code[self.instruction][1])

    def run(self):
        while True:
            self.step()

    def load(self, lines):
        self.code = []
        for line in lines:
            instruction, argument = line.split()
            self.code.append((instruction, int(argument)))
        # print(self.code)


def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def test1(data):
    c = Console(data)
    try:
        c.run()
    except ConsoleInfiniteLoop as e:
        return c.accumulator

def test2(data):
    i = len(data) - 1
    while i >= 0:
        c = Console(data)
        if c.modify(i):
            try:
                c.run()
            except ConsoleTerminated as e:
                # print(e)
                # print(c.accumulator)
                return c.accumulator
            except ConsoleInfiniteLoop as e:
                c.modify(i)
        i -= 1
    return None

def part1(data):
    c = Console(data)
    try:
        c.run()
    except ConsoleInfiniteLoop as e:
        return c.accumulator

def part2(data):
    i = len(data) - 1
    c = Console(data)
    while i >= 0:
        c.restart()
        if c.modify(i):
            try:
                c.run()
            except ConsoleTerminated as e:
                # print(e)
                # print(c.accumulator)
                return c.accumulator
            except ConsoleInfiniteLoop as e:
                c.modify(i)
        i -= 1
    print()
    print('Modified all instructions.')
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

    # test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 8, test_input_1)
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
