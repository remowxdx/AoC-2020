#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 16
SOLVED_1 = True
SOLVED_2 = True

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
            

def is_valid(ticket, rules):
    for value in ticket:
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
    inp = parse_input(data)
    valid_tickets = []

# Get only valid tickets
    for ticket in inp['nearby tickets']:
        if is_valid(ticket, inp['rules']):
            valid_tickets.append(ticket)
    print()
    print('Valid:', len(valid_tickets), 'All:', len(inp['nearby tickets']))

    fields = list(inp['rules'].keys())
    possible_fields = [fields[:] for f in fields]
    print(fields)


    for field_index in range(len(fields)):
        for rule in fields:
            for ticket in valid_tickets:
                if not in_one_interval(ticket[field_index], inp['rules'][rule]):
                    possible_fields[field_index].remove(rule)
                    break
    print(possible_fields)

    not_ok = True
    while not_ok:
        not_ok = False
        for i, fields in enumerate(possible_fields):
            if len(fields) == 1:
                for j, f in enumerate(possible_fields):
                    if i != j and fields[0] in f:
                        f.remove(fields[0])
            else:
                not_ok = True
    print(possible_fields)
    return [f[0] for f in possible_fields]

def part1(data):
    i = parse_input(data)
    invalid = []
    for ticket in i['nearby tickets']:
        invalid.extend(get_invalid_values(ticket, i['rules']))
    return sum(invalid)

def part2(data):
    inp = parse_input(data)
    invalid_values = []

    for ticket in inp['nearby tickets']:
        invalid_values.extend(get_invalid_values(ticket, inp['rules']))

# Get only valid tickets
    valid_tickets = []
    for ticket in inp['nearby tickets']:
        valid = True
        for value in ticket:
            if value in invalid_values:
                valid = False
        if valid:
            valid_tickets.append(ticket)

    print()
    print('Valid:', len(valid_tickets), 'All:', len(inp['nearby tickets']))

    fields = list(inp['rules'].keys())
    possible_fields = [fields[:] for f in fields]
    print(fields)


    for field_index in range(len(fields)):
        for rule in fields:
            for ticket in valid_tickets:
                if not in_one_interval(ticket[field_index], inp['rules'][rule]):
                    possible_fields[field_index].remove(rule)
                    break
    print(possible_fields)

    not_ok = True
    while not_ok:
        not_ok = False
        for i, fields in enumerate(possible_fields):
            if len(fields) == 1:
                for j, f in enumerate(possible_fields):
                    if i != j and fields[0] in f:
                        f.remove(fields[0])
            else:
                not_ok = True
    print(possible_fields)
    m = 1
    for i, field in enumerate([f[0] for f in possible_fields]):
        if field.startswith('departure'):
            m *= inp['my ticket'][i]
    return m


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

    test_input_2 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
'''.splitlines()
    print('Test Part 2:')
    test_eq('Test 2.1', test2, ['row', 'class', 'seat'], test_input_2)
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
