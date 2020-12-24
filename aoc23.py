#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 23
SOLVED_1 = True
SOLVED_2 = True

class Cups2:
    def __init__(self, cups):
        self.cups = {cups[0]: None}
        self.current = cups[0]
        self.picks = {}
        p = cups[0]
        for c in cups[1:]:
            self.cups[p] = c
            p = c
        self.cups[p] = self.current

    def pick(self):
        self.picks = self.cups[self.current]
        self.cups[self.current] = self.cups[self.cups[self.cups[self.picks]]]
        self.cups[self.cups[self.cups[self.picks]]] = None

    def insert(self):
        destination_num = self.current
        while True:
            destination_num -= 1
            if destination_num <= 0:
                destination_num = len(self.cups)

            if destination_num == self.picks or destination_num == self.cups[self.picks] or destination_num == self.cups[self.cups[self.picks]]:
                continue

            else:
                break

        n = self.cups[destination_num]
        self.cups[destination_num] = self.picks
        self.cups[self.cups[self.cups[self.picks]]] = n
        self.picks = None
        self.current = self.cups[self.current]


    def move(self):
        self.pick()
        self.insert()

    def ret(self):
        r = ''
        c = self.cups[1]
        while c != 1:
            r += str(c)
            c = self.cups[c]
        return r

    def ret_2(self):
        n1 = self.cups[1]
        n2 = self.cups[n1]
        print(n1, n2)
        return n1 * n2


class Cup:
    def __init__(self, num):
        self.num = num
        self.next = None


class Cups:
    def __init__(self, cups):
        self.max = 0
        self.current = Cup(cups[0])
        c = self.current
        if c.num == 1:
            self.one = c
        self.picks = None
        if c.num == 6:
            self.six = c
        for n in cups[1:]:
            if n > self.max:
                self.max = n
            c.next = Cup(n)
            c = c.next
            if c.num == 1:
                self.one = c
            if c.num == 6:
                self.six = c
            if c.num == self.current.num - 1:
                self.prev = c
        c.next = self.current
        print('Starting...')
        print(self)

    def pick(self):
        self.picks = self.current.next
        self.current.next = self.picks.next.next.next
        self.picks.next.next.next = None
        # print(self)

    def insert(self):
        destination_num = self.current.num
        if self.six == self.picks or self.six == self.picks.next or self.six == self.picks.next.next:
            cursor = self.current
        else:
            cursor = self.six
        while True:
            destination_num -= 1
            if destination_num <= 0:
                destination_num = self.max

            if destination_num == self.picks.num or destination_num == self.picks.next.num or destination_num == self.picks.next.next.num:
                continue

            for r in range(self.max - 3):
                if cursor.num == destination_num:
                    n = cursor.next
                    cursor.next = self.picks
                    self.picks.next.next.next = n
                    self.picks = None
                    self.current = self.current.next
                    print(self.one.next.num, self.one.next.next.num)
                    return None
                cursor = cursor.next
            
    def move(self):
        self.pick()
        self.insert()

    def __str__(self):
        c = self.current
        cups = [str(c.num)]
        c = c.next
        count = 0
        while c != self.current:
            if count > 100:
                break
            cups.append(str(c.num))
            c = c.next
            count += 1
        str_cups = 'Cups: ' + ' '.join(cups)

        c = self.picks
        picks = []
        count = 0
        while c != None:
            if count > 100:
                break
            picks.append(str(c.num))
            c = c.next
            count += 1
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

    def ret_2(self):
        c = self.current
        while c.num != 1:
            c = c.next

        print(c.next.num * c.next.next.num)


def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()


def test1(data):
    cups_list = [int(n) for n in data[0]]
    cups = Cups2(cups_list)
    for i in range(10):
        # print(cups)
        cups.move()
    # print(cups)
    return cups.ret()

def test2(data):
    cups_list = [int(n) for n in data[0]]
    cups_list.extend(list(range(10, 1_000_001)))
    cups = Cups2(cups_list)
    for i in range(10_000_000):
        # print(cups)
        cups.move()
        if i % 1_000_000 == 0:
            print(i)
    print(cups)
    return cups.ret_2()

def part1(data):
    cups_list = [int(n) for n in data[0]]
    cups = Cups2(cups_list)
    for i in range(100):
        # print(cups)
        cups.move()
    # print(cups)
    return cups.ret()

def part2(data):
    cups_list = [int(n) for n in data[0]]
    cups_list.extend(list(range(10, 1_000_001)))
    cups = Cups2(cups_list)
    for i in range(10_000_000):
        # print(cups)
        cups.move()
        if i % 1_000_000 == 0:
            print(i)
    print(cups)
    return cups.ret_2()

if __name__ == '__main__':

    test_input_1 = ['32415']
    test_input_1 = ['389125467']
    print('Test Part 1:')
    test_eq('Test 1.1', test1, '92658374', test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 149245887792, test_input_1)
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
