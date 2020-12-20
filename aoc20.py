#!/usr/bin/env python3

from aoc import *

pd = Debug(True)
DAY = 20
SOLVED_1 = True
SOLVED_2 = True

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
    if num == rnum:
        raise Exception('Argh! Palindromic border!')
    return num , rnum
        

def get_tiles(data):
    tiles = {}
    tile_num = 0
    for line in data:
        if line.startswith('Tile'):
            tile_num = int(line[5:-1])
            tiles[tile_num] = {'raw': [], 'img': []}
            line_num = 0
            continue
        if line == '':
            tiles[tile_num]['img'].pop()
            continue
        if line_num != 0:
            tiles[tile_num]['img'].append(line[1:-1])
        tiles[tile_num]['raw'].append(line)
        line_num += 1
    return tiles


def get_borders(tiles):
    borders = {}
    for tile in tiles:
        cur = tiles[tile]['raw']
        top = pixels_to_num(cur[0])
        tiles[tile]['top'] = top
        bottom = pixels_to_num(cur[-1])
        tiles[tile]['bottom'] = bottom
        left = pixels_to_num([line[0] for line in cur])
        tiles[tile]['left'] = left
        right = pixels_to_num([line[-1] for line in cur])
        tiles[tile]['right'] = right
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

def rotate_image(img, angle):
    rot_img = []
    if angle == 90:
        h = len(img)
        for y in range(h):
            w = len(img[y])
            line = []
            for x in range(w):
                line.append(img[x][h - 1 - y])
            rot_img.append(''.join(line))

    elif angle == 180:
        h = len(img)
        for y in range(h):
            w = len(img[y])
            line = []
            for x in range(w):
                line.append(img[h - 1 - y][w - 1 - x])
            rot_img.append(''.join(line))

    elif angle == -90 or angle == 270:
        h = len(img)
        for y in range(h):
            w = len(img[y])
            line = []
            for x in range(w):
                line.append(img[w - 1 - x][y])
            rot_img.append(''.join(line))

    return rot_img


def rotate_borders(tile, angle):
    if angle == 90:
        t = tile['top']
        tile['top'] = tile['right']
        tile['right'] = tile['bottom']
        tile['bottom'] = tile['left']
        tile['left'] = t
        tile['left'] = (tile['left'][1], tile['left'][0])
        tile['right'] = (tile['right'][1], tile['right'][0])

    elif angle == 180:
        t = tile['top']
        tile['top'] = tile['bottom']
        tile['bottom'] = t
        t = tile['left']
        tile['left'] = tile['right']
        tile['right'] = t
        tile['top'] = (tile['top'][1], tile['top'][0])
        tile['bottom'] = (tile['bottom'][1], tile['bottom'][0])
        tile['left'] = (tile['left'][1], tile['left'][0])
        tile['right'] = (tile['right'][1], tile['right'][0])

    elif angle == -90 or angle == 270:
        t = tile['top']
        tile['top'] = tile['left']
        tile['left'] = tile['bottom']
        tile['bottom'] = tile['right']
        tile['right'] = t
        tile['top'] = (tile['top'][1], tile['top'][0])
        tile['bottom'] = (tile['bottom'][1], tile['bottom'][0])


def flip_image(img, axis):
    flip_img = []

    if axis == 'V':
        h = len(img)
        for y in range(h):
            w = len(img[y])
            line = []
            for x in range(w):
                line.append(img[y][w - 1 - x])
            flip_img.append(''.join(line))

    elif axis == 'H':
        h = len(img)
        for y in range(h):
            w = len(img[y])
            line = []
            for x in range(w):
                line.append(img[h - 1 - y][x])
            flip_img.append(''.join(line))

    return flip_img

def flip_borders(tile, axis):

    if axis == 'V':
        t = tile['left']
        tile['left'] = tile['right']
        tile['right'] = t
        tile['top'] = (tile['top'][1], tile['top'][0])
        tile['bottom'] = (tile['bottom'][1], tile['bottom'][0])

    elif axis == 'H':
        t = tile['top']
        tile['top'] = tile['bottom']
        tile['bottom'] = t
        tile['left'] = (tile['left'][1], tile['left'][0])
        tile['right'] = (tile['right'][1], tile['right'][0])


def rotate_tile(tile, angle):
    rot_img = rotate_image(tile['img'], angle)
    rotate_borders(tile, angle)
    tile['img'] = rot_img


def flip_tile(tile, axis):
    flip_img = flip_image(tile['img'], axis)
    flip_borders(tile, axis)
    tile['img'] = flip_img


def build_image(corner, tiles, borders):
    border_names = ['top', 'left', 'bottom', 'right']
    tiling = []
    image = []
    c = corner
    # print(tiles[c])
    cb = []
    for b in border_names:
        if len(borders[min(tiles[c][b])]) == 1:
            # print(b)
            cb.append(b)

    if 'top' not in cb:
        flip_tile(tiles[c], 'H')
    if 'left' not in cb:
        flip_tile(tiles[c], 'V')

    at_bottom_border = False
    while not at_bottom_border:
        cur_tile_name = c
        tiling_row = []
        at_right_border = False
        while not at_right_border:
            tiling_row.append(cur_tile_name)
            cur_right_border = min(tiles[cur_tile_name]['right'])
            matching_tile_names = borders[cur_right_border]
            # print('---', matching_tile_names)
            if len(matching_tile_names) == 1:
                at_right_border = True
                break
            next_tile_name = matching_tile_names[0]
            if next_tile_name == cur_tile_name:
                next_tile_name = matching_tile_names[1]

            # find which border matches
            for bn in border_names:
                if min(tiles[next_tile_name][bn]) == cur_right_border:
                    break

            if bn == 'top':
                rotate_tile(tiles[next_tile_name], 90)
            elif bn == 'right':
                rotate_tile(tiles[next_tile_name], 180)
            elif bn == 'bottom':
                rotate_tile(tiles[next_tile_name], -90)

            if tiles[cur_tile_name]['right'] != tiles[next_tile_name]['left']:
                flip_tile(tiles[next_tile_name], 'H')

            if tiles[cur_tile_name]['right'] != tiles[next_tile_name]['left']:
                raise Exception('Right and left borders should be equal now!')

            cur_tile_name = next_tile_name
        tiling.append(tiling_row)

        cur_bottom_border = min(tiles[c]['bottom'])
        matching_tile_names = borders[cur_bottom_border]
        # print('-', matching_tile_names)
        if len(matching_tile_names) == 1:
            at_bottom_border = True
            break
        next_tile_name = matching_tile_names[0]
        if next_tile_name == c:
            next_tile_name = matching_tile_names[1]

        # find which border matches
        for bn in border_names:
            if min(tiles[next_tile_name][bn]) == cur_bottom_border:
                break

        if bn == 'right':
            rotate_tile(tiles[next_tile_name], 90)
        elif bn == 'bottom':
            rotate_tile(tiles[next_tile_name], 180)
        elif bn == 'left':
            rotate_tile(tiles[next_tile_name], -90)

        if tiles[c]['bottom'] != tiles[next_tile_name]['top']:
            flip_tile(tiles[next_tile_name], 'V')

        if tiles[c]['bottom'] != tiles[next_tile_name]['top']:
            raise Exception('Bottom and top borders should be equal now!')

        c = next_tile_name
        
    for y, img_row in enumerate(tiling):
        for x, tile in enumerate(img_row):
            img = tiles[tile]['img']
            # print_img(img)
            th = len(img)
            if th != 8:
                # print(tiles[tile])
                raise Exception(f'{tile} height {th} should be 8!')
            if x == 0:
                image.extend(['' for i in range(th)])
            for j, tile_row in enumerate(img):
                image[y * th + j] += tile_row
        if len(image[y * th + 7]) != 8 * len(tiling[0]):
            raise Exception(f'Image row length not good at {x} {y}.')
    
    # print_img(image)
    # print(tiling)
    return image

def find_monsters(image, monster):
    found_monsters = False
    for y in range(len(image)):
        for x in range(len(image[y])):
            found = True
            for dx, dy in monster:
                if x + dx >= len(image[y]):
                    found = False
                    break
                if y + dy >= len(image):
                    found = False
                    break
                if image[y + dy][x + dx] != '#':
                    found = False
                    break
            if found:
                found_monsters = True
                for dx, dy in monster:
                    line = list(image[y + dy])
                    line[x + dx] = 'O'
                    image[y + dy] = ''.join(line)
    # print('Monsters')
    # print_img(image)
    return found_monsters

def count_rough_water(image):
    count = 0
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == '#':
                count += 1
    return count

def print_img(img):
    print()
    for row in img:
        print(row)

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
    # print()
    tiles = get_tiles(data)
    borders = get_borders(tiles)
    # print(borders)
    image_borders = find_image_borders(borders)
    # print(sorted(image_borders))
    image_corners = find_image_corners(image_borders)
    # print(image_corners)
    image = build_image(image_corners.pop(), tiles, borders )

    monster_str = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
 '''.splitlines()
    monster = []
    for y, line in enumerate(monster_str):
        for x, char in enumerate(line):
            if char == '#':
                monster.append((x, y))

    image = flip_image(image, 'H')
    for f in range(2):
        for r in range(4):
            found = find_monsters(image, monster)
            if found:
                return count_rough_water(image)
            image = rotate_image(image, 90)
        image = flip_image(image, 'H')


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
    tiles = get_tiles(data)
    borders = get_borders(tiles)
    image_borders = find_image_borders(borders)
    image_corners = find_image_corners(image_borders)
    image = build_image(image_corners.pop(), tiles, borders )

    monster_str = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
 '''.splitlines()
    monster = []
    for y, line in enumerate(monster_str):
        for x, char in enumerate(line):
            if char == '#':
                monster.append((x, y))

    image = flip_image(image, 'H')
    for f in range(2):
        for r in range(4):
            found = find_monsters(image, monster)
            if found:
                return count_rough_water(image)
            image = rotate_image(image, 90)
        image = flip_image(image, 'H')

    return None

if __name__ == '__main__':

    test_input_1 = get_input('test_input_20')
    print('Test Part 1:')
    test_eq('Test 1.1', test1, 20899048083289, test_input_1)
    print()

    test_input_2 = [4,5,6]
    print('Test Part 2:')
    test_eq('Test 2.1', test2, 273, test_input_1)
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
