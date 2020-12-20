#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 20
SOLVED_1 = True
SOLVED_2 = False

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def pixels_to_num(pixels):
    num = 0
    rnum = 0
    start = 1 << (len(pixels) - 1)
    for i, p in enumerate(pixels):
        if p == '#':
            bit = 1
        else:
            bit = 0
        num = (num << 1) + bit
        rnum = (rnum >> 1) + start * bit
    # Return only one of the to possibilities
    # print(num, rnum)
    return num , rnum
        

def get_tiles(data):
    tiles = {}
    tile_num = 0
    for line in data:
        if line.startswith('Tile'):
            tile_num = int(line[5:-1])
            tiles[tile_num] = {'raw': [], 'img': []}
            continue
        if line == '':
            continue
        tiles[tile_num].append(line)
    return tiles


def get_borders(tiles):
    borders = {}
    for tile in tiles:
        top = pixels_to_num(tiles[tile][0])
        bottom = pixels_to_num(tiles[tile][-1])
        left = pixels_to_num([line[0] for line in tiles[tile]])
        right = pixels_to_num([line[-1] for line in tiles[tile]])
        for bd in [top, left, bottom, right]:
            b = min(bd)
            if b not in borders:
                borders[b] = []
            borders[b].append(tile)
    return borders

def find_image_borders(borders):
    image_borders = []
    for b in borders:
        if len(borders[b]) == 1:
            image_borders.append(borders[b][0])
    return image_borders

def find_image_corners(image_borders):
    visited = set()
    corners = set()
    for b in image_borders:
        if b not in visited:
            visited.add(b)
        else:
            corners.add(b)
    return corners
    

def test1(data):
    tiles = get_tiles(data)
    borders = get_borders(tiles)
    # print(borders)
    image_borders = find_image_borders(borders)
    # print(sorted(image_borders))
    image_corners = find_image_corners(image_borders)
    # print(sorted(image_corners))
    m = 1
    for c in image_corners:
        m *= c
    return m

def test2(data):
    return 0

def part1(data):
    tiles = get_tiles(data)
    borders = get_borders(tiles)
    # print(borders)
    image_borders = find_image_borders(borders)
    # print(sorted(image_borders))
    image_corners = find_image_corners(image_borders)
    # print(sorted(image_corners))
    m = 1
    for c in image_corners:
        m *= c
    return m

def part2(data):
    return None

if __name__ == '__main__':

    test_input_1 = get_input('test_input_20')
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 20899048083289, test_input_1)
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
