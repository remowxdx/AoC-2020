#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 4
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def to_list(data):
    passports = []
    current_passport = {}
    # print(data)
    for line in data:
        if line.strip() == '':
            passports.append(current_passport)
            current_passport = {}
        # print(line)
        for field in line.split():
            field, value = field.split(':')
            current_passport[field] = value
    passports.append(current_passport)
    return passports

def is_passport_valid(passport):
    
    required_fields = {
        'byr': 'Birth Year',
        'iyr': 'Issue Year',
        'eyr': 'Expiration Year',
        'hgt': 'Height',
        'hcl': 'Hair Color',
        'ecl': 'Eye Color',
        'pid': 'Passport ID',
        # 'cid': 'Country ID', Help self
    }

    for field in required_fields:
        # print(field)
        if field not in passport:
            return False
    return True


def test1(data):
    c = 0
    for p in data:
        if is_passport_valid(p):
            c += 1
    return c

def test2(data):
    return 0

def part1(data):
    c = 0
    for p in data:
        print(p)
        if is_passport_valid(p):
            c += 1
    return c

def part2(data):
    return None

if __name__ == '__main__':

    test_input_raw = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''
    test_input_1 = to_list(test_input_raw.splitlines())
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 2, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 42, test_input_2)
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
