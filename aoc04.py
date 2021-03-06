#!/usr/bin/env python3

from aoc import *

import re

pd = Debug(False)
DAY = 4
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

class PassportInvalid(Exception):
    pass

class PassportFieldMissing(PassportInvalid):
    def __init__(self, passport, field):
        self.passport = passport
        self.field = field

    def __str__(self):
        return f'Passport invalid because missing field "{self.field}".'


class PassportFieldFormatIvalid(PassportInvalid):
    def __init__(self, passport, field, value):
        self.passport = passport
        self.field = field
        self.value = value

    def __str__(self):
        return f'Passport invalid because the format of field "{self.field}" is not valid. {self.field} is "{self.value}".'

class PassportFieldValueOutOfRange(PassportInvalid):
    def __init__(self, passport, field, value, min_value, max_value):
        self.passport = passport
        self.field = field
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f'Passport invalid because "{self.field}" is out of range. "{self.field}" is "{self.value}" but should be between "{self.min_value}" and "{self.max_value}".'

def get_passports(data, validate_passport):

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

    passports = []
    current_passport = {}
    # print(data)
    for line in data:
        if line.strip() == '':
            try:
                validate_passport(current_passport)
                current_passport['valid'] = True
            except PassportInvalid as r:
                current_passport['valid'] = False
                current_passport['reason'] = str(r)
            passports.append(current_passport)
            current_passport = {}
        # print(line)
        for field in line.split():
            field, value = field.split(':')
            current_passport[field] = value
    try:
        validate_passport(current_passport)
        current_passport['valid'] = True
    except PassportInvalid as r:
        current_passport['valid'] = False
        current_passport['reason'] = str(r)
    passports.append(current_passport)
    return passports

def validate_passport(passport):
    
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
            raise PassportFieldMissing(passport, field)
    
def real_validate_passport(passport):
    
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
            raise PassportFieldMissing(passport, field)
        validate_field(passport, field)

def validate_field(passport, field):
    required_fields = {
        'byr': ('Birth Year', '^([0-9]{4})$', (1920, 2002)),
        'iyr': ('Issue Year', '^([0-9]{4})$', (2010, 2020)),
        'eyr': ('Expiration Year', '^([0-9]{4})$', (2020, 2030)),
        'hgt': ('Height', '^(\d{2,3})(cm|in)$', (150, 193, 59, 76)),
        'hcl': ('Hair Color', '^#([0-9a-f]{6})$', None),
        'ecl': ('Eye Color', '^amb|blu|brn|gry|grn|hzl|oth$', None),
        'pid': ('Passport ID', '^\d{9}$', None),
        # 'cid': 'Country ID', Help self
    }

    value = passport[field]

    m = re.match(required_fields[field][1], value)
    if m is None:
        # RegExp doesn't match
        raise PassportFieldFormatIvalid(passport, field, value)

    else:
        if required_fields[field][2] is None:
            pass
        else:
            if len(required_fields[field][2]) == 2:
                # RegExp does match but we need to check the range
                num = int(m[1])
                if num >= required_fields[field][2][0] and num <= required_fields[field][2][1]:
                    # Range is OK
                    pass
                else:
                    # Range is not OK
                    raise PassportFieldValueOutOfRange(passport, field, value, required_fields[field][2][0], required_fields[field][2][1])

            elif len(required_fields[field][2]) == 4:
                # RegExp does match but we need to check on of 2 ranges
                num = int(m[1])
                if m[2] == 'cm':
                    # We have to check the range for "cm"
                    if num >= required_fields[field][2][0] and num <= required_fields[field][2][1]:
                        # Range is OK
                        pass
                    else:
                        # Range is not OK
                        raise PassportFieldValueOutOfRange(passport, field, value, required_fields[field][2][0], required_fields[field][2][1])
                elif m[2] == 'in':
                    # We have to check the range for "in"
                    if num >= required_fields[field][2][2] and num <= required_fields[field][2][3]:
                        # Range is OK
                        pass
                    else:
                        # Range is not OK
                        raise PassportFieldValueOutOfRange(passport, field, value, required_fields[field][2][2], required_fields[field][2][3])

def test1(data):
    c = 0
    for p in data:
        if p['valid']:
            c += 1
    return c

def test2(data):
    c = 0
    for p in data:
        if p['valid']:
            c += 1
    return c

def part1(data):
    c = 0
    for p in data:
        if p['valid']:
            c += 1
    return c

def part2(data):
    c = 0
    for p in data:
        if p['valid']:
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
    test_input_1 = get_passports(test_input_raw.splitlines(), validate_passport)
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

    test_input_2 = get_passports(test_input_raw.splitlines(), real_validate_passport)
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 4, test_input_2)
    print()

    data_raw = get_input(f'input{DAY}')
    data = get_passports(data_raw, validate_passport)

    r = part1(data)
    if r is not None:
        print('Part 1:', r)
        if SOLVED_1:
            check_solution(DAY, 1, r)
        else:
            save_solution(DAY, 1, r)

    data = get_passports(data_raw, real_validate_passport)
    print(data)
    r = part2(data)
    if r is not None:
        print('Part 2:', r)
        if SOLVED_2:
            check_solution(DAY, 2, r)
        else:
            save_solution(DAY, 2, r)
