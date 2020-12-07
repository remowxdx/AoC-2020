#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 7
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def to_list(data):
    rules = {}
    for line in data:
        bag, desc = line.split('contain')
        bag_type = bag.strip().replace('bags', '').strip()
        rules_desc = desc.strip().split(',')
        bag_rules = {}
        for rd in rules_desc:
            if rd.strip().startswith('no other'):
                continue
            print(line)
            words = rd.strip().split()
            num = int(words[0])
            inner_bag = f'{words[1]} {words[2]}'
            bag_rules[inner_bag] = num
        rules[bag_type] = bag_rules
    i = 0
    for bag in rules:
        print(bag, rules[bag])
        if i > 10:
            break
        i += 1
    return rules

def find_bag(rules, outer, current, target):
    if current == target:
        return set([outer])

    r = set()
    for inner_bag in rules[current]:

        r.update(find_bag(rules, outer, inner_bag, target))

    return r
    

def test1(data):
    r = set()
    for bag in data:
        r.update(find_bag(data, bag, bag, 'shiny gold'))
    print(r)

    if 'shiny gold' in r:
        return len(r) - 1
    else:
        return len(r)

def test2(data):
    return 0

def part1(data):
    r = set()
    for bag in data:
        r.update(find_bag(data, bag, bag, 'shiny gold'))
    print(r)

    if 'shiny gold' in r:
        return len(r) - 1
    else:
        return len(r)

def part2(data):
    return None

if __name__ == '__main__':

    test_input_raw = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''.splitlines()
    test_input_1 = to_list(test_input_raw)
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 4, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 42, test_input_2)
    print()

    data = get_input(f'input{DAY}')

    r = part1(to_list(data))
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
