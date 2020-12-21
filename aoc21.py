#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 21
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def parse(data):
    ingredients = {}
    allergens = {}
    foods = []
    for line in data:
        ingr, allerg = line.split(' (contains ')
        for i in ingr.split(' '):
            if i not in ingredients:
                ingredients[i] = set()
        for a in allerg[:-1].split(', '):
            if a not in allergens:
                allergens[a] = set()
            for i in [i for i in ingr.split(' ')]:
                allergens[a].add(i)
        foods.append([[i for i in ingr.split(' ')], [a for a in allerg[:-1].split(', ')], []])

    # print()
    # print(ingredients)
    # print(allergens)
    # print(foods)
    return ingredients, allergens, foods

def eliminate_non_allergic(ingredients, allergens, foods):
    for food in foods:
        for i in ingredients:
            if i not in food[0]:
                food[2].append(i)
        for inv_food in food[2]:
            for a in food[1]:
                if inv_food in allergens[a]:
                    allergens[a].remove(inv_food)

    # for a in allergens:
        # print(a, allergens[a])

def eliminate_duplicates(allergens):
    definitive = {}
    complete = False
    while not complete:
        complete = True
        to_remove = []
        for a in allergens:
            for d in definitive:
                if d in allergens[a]:
                    allergens[a].remove(d)
            if len(allergens[a]) == 1:
                definitive[allergens[a].pop()] = a
                to_remove.append(a)
            elif len(allergens) > 1:
                complete = False
        for r in to_remove:
            allergens.pop(r)
    return definitive

def count_ingredient_in_foods(ingredient, foods):
    s = 0
    for f in foods:
        if ingredient in f[0]:
            s += 1
    return s

def canonical_dangerous_ingredient_list(allergens):
    i_a = dict([(allergens[a], a) for a in allergens])
    return ','.join([i_a[k] for k in sorted(i_a)])

def test1(data):
    ingredients, allergens, foods = parse(data)
    eliminate_non_allergic(ingredients, allergens, foods)
    r = eliminate_duplicates(allergens)
    # print('-' * 20)
    # for i in r:
        # print(i, r[i])

    s = 0
    for i in ingredients:
        if i not in r:
            s += count_ingredient_in_foods(i, foods)
            # print(i)
    return s

def test2(data):
    ingredients, allergens, foods = parse(data)
    eliminate_non_allergic(ingredients, allergens, foods)
    r = eliminate_duplicates(allergens)
    return canonical_dangerous_ingredient_list(r)

def part1(data):
    ingredients, allergens, foods = parse(data)
    eliminate_non_allergic(ingredients, allergens, foods)
    r = eliminate_duplicates(allergens)

    s = 0
    for i in ingredients:
        if i not in r:
            s += count_ingredient_in_foods(i, foods)
    return s

def part2(data):
    ingredients, allergens, foods = parse(data)
    eliminate_non_allergic(ingredients, allergens, foods)
    r = eliminate_duplicates(allergens)
    return canonical_dangerous_ingredient_list(r)

if __name__ == '__main__':

    test_input_1 = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 5, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 'mxmxvkd,sqjhc,fvjkl', test_input_1)
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
