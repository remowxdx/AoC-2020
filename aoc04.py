#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 4
SOLVED_1 = True
SOLVED_2 = True

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
    
def is_passport_really_valid(passport):
    
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
        if not is_field_valid(field, passport[field]):
            print(field, passport[field])
            return False
    return True

def is_field_valid(field, value):
    if field == 'byr':
        if value.isdigit():
            i = int(value)
            if i >= 1920 and i <= 2002:
                return True
        return False

    if field == 'iyr':
        if value.isdigit():
            i = int(value)
            if i >= 2010 and i <= 2020:
                return True
        return False

    if field == 'eyr':
        if value.isdigit():
            i = int(value)
            if i >= 2020 and i <= 2030:
                return True
        return False

    if field == 'hgt':
        if value.endswith('cm'):
            height = value[:-2]
            if height.isdigit():
                i = int(height)
                if i >= 150 and i <= 193:
                    return True
        if value.endswith('in'):
            height = value[:-2]
            i = int(height)
            if i >= 59 and i <= 76:
                return True
        return False

    if field == 'hcl':
        if value.startswith('#') and len(value) == 7:
            color = value[1:]
            for l in color:
                if l not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    return False
            return True
        return False

    if field == 'ecl':
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
        return False

    if field == 'pid':
        if value.isdigit() and len(value) == 9:
            return True
        return False

    raise Exception('Should never raise')

def test1(data):
    c = 0
    for p in data:
        if is_passport_valid(p):
            c += 1
    return c

def test2(data):
    c = 0
    for p in data:
        if is_passport_really_valid(p):
            c += 1
    return c

def part1(data):
    c = 0
    for p in data:
        print(p)
        if is_passport_valid(p):
            c += 1
    return c

def part2(data):
    c = 0
    for p in data:
        # print(p)
        if is_passport_really_valid(p):
            c += 1
    return c

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

    test_input_raw = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''

    test_input_2 = to_list(test_input_raw.splitlines())
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 4, test_input_2)
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
