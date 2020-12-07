#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 7
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def to_list(data):
    rules = {}
    for line in data:
        words = line.split()
        bag_type = ' '.join(words[:2])
        i = 4
        rules[bag_type] = {}
        while i < len(words):
            if not words[i].isdigit():
                # No other bags
                break
            num = int(words[i])
            inner_bag = ' '.join(words[i+1:i+3])
            rules[bag_type][inner_bag] = num
            i += 4
    return rules

def find_bag(rules, outer, current, target):
    if current == target:
        return set([outer])

    r = set()
    for inner_bag in rules[current]:

        r.update(find_bag(rules, outer, inner_bag, target))

    return r
    
def count_bags(rules, bag):
    count = 1
    for inner_bag in rules[bag]:
        count += rules[bag][inner_bag] * count_bags(rules, inner_bag) 
    return count

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
    return count_bags(data, 'shiny gold') - 1

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
    return count_bags(data, 'shiny gold') - 1

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

    test_input_raw = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''.splitlines()

    test_input_2 = to_list(test_input_raw)
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 32, test_input_1)
    test_eq('Test 2.2', test2, 126, test_input_2)
    print()

    data_raw = get_input(f'input{DAY}')
    data = to_list(data_raw)

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
