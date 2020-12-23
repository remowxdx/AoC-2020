#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 23
SOLVED_1 = True
SOLVED_2 = False

class Cup:
    def __init__(self, num, next):
        self.num = num
        self.next = next


class Cups:
    def __init__(self, cups):
        self.cups = []
        self.picks = None
        for n in list(cups[0].strip()):
            self.cups.append(Cup(int(n), None))
        for i, cup in enumerate(self.cups):
            cup.next = self.cups[(i + 1) % len(self.cups)]
        self.current = self.cups[0]

    def pick(self):
        self.picks = self.current.next
        self.current.next = self.picks.next.next.next
        self.picks.next.next.next = None
        print(self)

    def insert(self):
        destination_num = self.current.num - 1
        cursor = self.current
        while True:
            for r in range(7):
                if cursor.num == destination_num:
                    n = cursor.next
                    cursor.next = self.picks
                    self.picks.next.next.next = n
                    self.picks = None
                    self.current = self.current.next
                    return None
                cursor = cursor.next
            destination_num = (destination_num - 1) % 10
            
    def move(self):
        self.pick()
        self.insert()

    def __str__(self):
        c = self.current
        cups = [str(c.num)]
        c = c.next
        while c != self.current:
            cups.append(str(c.num))
            c = c.next
        str_cups = 'Cups: ' + ' '.join(cups)

        c = self.picks
        picks = []
        while c != None:
            picks.append(str(c.num))
            c = c.next
        str_picks = 'Picks: ' + ' '.join(picks)

        return str_cups + '\n' + str_picks

    def ret(self):
        c = self.current
        while c.num != 1:
            c = c.next
        r = ''
        c = c.next
        while c.num != 1:
            r += str(c.num)
            c = c.next
        return r


def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()


def test1(data):
    cups = Cups(data)
    for i in range(10):
        print(cups)
        cups.move()
    print(cups)
    return cups.ret()

def test2(data):
    return 0

def part1(data):
    cups = Cups(data)
    for i in range(100):
        print(cups)
        cups.move()
    print(cups)
    return cups.ret()

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = ['32415']
    test_input_1 = ['389125467']
    print('Test Part 1:')
    test_eq('Test 1.1', test1, '92658374', test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 42, test_input_1)
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
