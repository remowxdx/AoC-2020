#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 19
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def parse_input(data):
    rules = {}
    messages = []
    state = 'rules'
    for line in data:
        if line == '':
            state = 'messages'
            continue
        if state == 'rules':
            rule_num, rule_desc = line.split(': ')
            if rule_desc.startswith('"'):
                rules[rule_num] = ('char', rule_desc[1])
                continue
            alt = rule_desc.split(' | ')
            if len(alt) == 1:
                rules[rule_num] = ('and', *alt[0].split(' '))
                continue
            if len(alt) == 2:
                first = ('and', *alt[0].split(' '))
                second = ('and', *alt[1].split(' '))
                rules[rule_num] = ('or', first, second)
                continue
        if state == 'messages':
            messages.append(line)
            continue
        raise ValueError('???')
    return rules, messages

def check(message, rule, rules):
    if len(message) == 0:
        return []
    if type(rule) != tuple:
        return check(message, rules[rule], rules)
    # print('Check', message, rule)
    if rule[0] == 'char':
        if message[0] == rule[1]:
            return [1]
        return []
    if rule[0] == 'and':
        s = []
        r1 = check(message, rule[1], rules)
        if len(rule) > 2:
            subrule = ('and', *list(rule[2:]))
            # print(subrule)
            for l1 in r1:
                rn = check(message[l1:], subrule, rules)
                for ln in rn:
                    s.append(l1 + ln)
        else:
            s = r1
        return s
    if rule[0] == 'or':
        r = []
        for i in range(1, len(rule)):
            r.extend(check(message, rule[i], rules))
        return r

def update_rules(rules):
    rules['8'] = ('or', '42', ('and', '42', '8'))
    rules['11'] = ('or', ('and', '42', '31'), ('and', '42', '11', '31'))

def test1(data):
    rules, messages = parse_input(data)
    valid = []
    count = 0
    # print(rules)
    for m in messages:
        r = check(m, '0', rules)
        if len(r) == 0:
            continue
        if len(r) == 1 and r[0] == len(m):
            count += 1
            valid.append(m)
            continue
    # print(valid)
    return count

def test2(data):
    rules, messages = parse_input(data)
    update_rules(rules)
    valid = []
    count = 0
    # print(rules)
    for m in messages:
        r = check(m, '0', rules)
        if len(r) == 0:
            continue
        else:
            for l in r:
                if l == len(m):
                    count += 1
                    valid.append(m)
                    break
            continue
        # print(m)
        # print(r, len(m))
        raise ValueError('???')
    # print(valid)
    return count

def part1(data):
    rules, messages = parse_input(data)
    valid = []
    count = 0
    # print(rules)
    for m in messages:
        r = check(m, '0', rules)
        if len(r) == 1 and r[0] == len(m):
            count += 1
            valid.append(m)
    # print(valid)
    return count

def part2(data):
    rules, messages = parse_input(data)
    update_rules(rules)
    valid = []
    count = 0
    # print(rules)
    for m in messages:
        r = check(m, '0', rules)
        if len(r) == 0:
            continue
        else:
            for l in r:
                if l == len(m):
                    count += 1
                    valid.append(m)
                    break
            continue
        # print(m)
        # print(r, len(m))
        raise ValueError('???')
    # print(valid)
    return count

if __name__ == '__main__':

    test_input_1 = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 2, test_input_1)
    print()

    test_input_2 = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
'''.splitlines()
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 12, test_input_2)
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
