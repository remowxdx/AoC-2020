#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 18
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def evaluate(line):
    stack = []
    ops = []
    value = None
    prev_value = None
    for c in line:
        if c == ' ':
            continue
        elif c.isdigit():
            value = int(c)
        elif c == '+' or c == '*':
            prev_value = value
            value = None
            ops.append(c)
        elif c == '(':
            stack.append(prev_value)
            prev_value = None
        elif c == ')':
            prev_value = stack.pop()

        if len(ops) > 0 and prev_value is not None and value is not None:
            op = ops.pop()
            if op == '+':
                value = value + prev_value
            if op == '*':
                value = value * prev_value
            prev_value = None
        # print(stack, ops, prev_value, value)
    return value


def evaluate_w(line):
    stack = [[]]
    cur_stack = 0
    ops = []
    for c in line:
        if c == ' ':
            continue
        elif c.isdigit():
            stack[cur_stack].append(int(c))
        elif c == '+' or c == '*':
            ops.append(c)
        elif c == '(':
            stack.append([])
            cur_stack += 1
        elif c == ')':
            v = stack[cur_stack].pop()
            stack.pop()
            cur_stack -= 1
            stack[cur_stack].append(v)

        if len(ops) > 0 and len(stack[cur_stack]) > 1:
            right = stack[cur_stack].pop()
            left = stack[cur_stack].pop()
            op = ops.pop()
            if op == '+':
                stack[cur_stack].append(left + right)
            if op == '*':
                stack[cur_stack].append(left * right)
        # print(stack, ops)
    return stack[0][0]


def test1(data):
    return evaluate(data)

def test2(data):
    return 0

def part1(data):
    s = 0
    for line in data:
        s += evaluate(line)
    return s

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = '1 + 2 * 3 + 4 * 5 + 6'
    test_input_2 = '1 + (2 * 3) + (4 * (5 + 6))'
    test_input_3 = '2 * 3 + (4 * 5)'
    test_input_4 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    test_input_5 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    test_input_6 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 71, test_input_1)
    test_eq('Test 1.2', test1, 51, test_input_2)
    test_eq('Test 1.3', test1, 26, test_input_3)
    test_eq('Test 1.4', test1, 437, test_input_4)
    test_eq('Test 1.5', test1, 12240, test_input_5)
    test_eq('Test 1.6', test1, 13632, test_input_6)
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
