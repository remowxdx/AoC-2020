#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 24
SOLVED_1 = True
SOLVED_2 = True

def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines.splitlines()

def coords(tile):
    e = 0
    n = 0
    state = 'first'
    for d in tile:
        if state == 'first':
            if d == 'e':
                e += 2
            elif d == 'w':
                e -= 2
            elif d == 'n':
                n += 1
                state = 'second'
            elif d == 's':
                n -= 1
                state = 'second'
            else:
                raise ValueError('Unknown direction')
        elif state == 'second':
            if d == 'e':
                e += 1
            elif d == 'w':
                e -= 1
            else:
                raise ValueError('Unknown direction')
            state = 'first'
        else:
            raise ValueError('Unknown state')
    return e, n

def flip(tiles, tile):
    if tile in tiles:
        tiles.remove(tile)
    else:
        tiles.add(tile)


def day(tiles):
    to_flip = set()
    white_tiles = set()
    for tile in tiles:
        count_black = 0
        x, y = tile
        for neighbor in [(x + 2, y), (x + 1, y + 1), (x - 1, y + 1), (x - 2, y), (x - 1, y - 1), (x + 1, y - 1)]:
            if neighbor in tiles:
                count_black += 1
            else:
                if neighbor not in white_tiles:
                    white_tiles.add(neighbor)
        if count_black == 0 or count_black > 2:
            to_flip.add(tile)

    for tile in white_tiles:
        count_black = 0
        x, y = tile
        for neighbor in [(x + 2, y), (x + 1, y + 1), (x - 1, y + 1), (x - 2, y), (x - 1, y - 1), (x + 1, y - 1)]:
            if neighbor in tiles:
                count_black += 1
        if count_black == 2:
            to_flip.add(tile)

    for tile in to_flip:
        flip(tiles, tile)

def test1(data):
    tiles = set()
    for line in data:
        c = coords(line)
        flip(tiles, c)
    return len(tiles)


def test2(data):
    tiles = set()
    for line in data:
        c = coords(line)
        flip(tiles, c)
    for d in range(100):
        day(tiles)
        # print(d, len(tiles))
    return len(tiles)

def part1(data):
    tiles = set()
    for line in data:
        c = coords(line)
        flip(tiles, c)
    return len(tiles)


def part2(data):
    tiles = set()
    for line in data:
        c = coords(line)
        flip(tiles, c)
    for d in range(100):
        day(tiles)
        # print(d, len(tiles))
    return len(tiles)


if __name__ == '__main__':

    test_input_1 = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
'''.splitlines()
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 10, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 2208, test_input_1)
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
