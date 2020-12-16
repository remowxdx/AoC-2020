#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 16
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def parse_input(data):
    state = 'field rules'
    rules = {}
    tickets = []
    for line in data:
        if len(line) == 0:
            continue
        if line.startswith('your ticket'):
            state = 'my ticket'
            continue
        elif line.startswith('nearby ticket'):
            state = 'nearby tickets'
            continue
        if state == 'field rules':
            name, intervals = line.split(': ')
            rules[name] = []
            for interval in intervals.split(' or '):
                start, end = interval.split('-')
                rules[name].append((int(start), int(end)))
        if state == 'my ticket':
            my_ticket = [int(n) for n in line.split(',')]
        if state == 'nearby tickets':
            tickets.append([int(n) for n in line.split(',')])
    return {'rules': rules, 'my ticket': my_ticket, 'nearby tickets': tickets}


def in_interval(value, interval):
    r = value >= interval[0] and value <= interval[1]
    # print(f'Is {value} in {interval[0]}-{interval[1]}? {r}')
    return r


def in_one_interval(value, intervals):
    for interval in intervals:
        if in_interval(value, interval):
            return True
    return False


def validates_one_rule(value, rules):
    for rule in rules:
        if in_one_interval(value, rules[rule]):
            return True
    return False
            

def get_invalid_values(ticket, rules):
    invalid = []
    for value in ticket:
        if not validates_one_rule(value, rules):
            invalid.append(value)
    return invalid


def test1(data):
    i = parse_input(data)
    invalid = []
    for ticket in i['nearby tickets']:
        invalid.extend(get_invalid_values(ticket, i['rules']))
    return sum(invalid)

def test2(data):
    return 0

def part1(data):
    i = parse_input(data)
    invalid = []
    for ticket in i['nearby tickets']:
        invalid.extend(get_invalid_values(ticket, i['rules']))
    return sum(invalid)

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 71, test_input_1)
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
