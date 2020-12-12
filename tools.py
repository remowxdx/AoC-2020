#!/usr/bin/env python3

class Vector:

    directions = ['E', 'N', 'W', 'S']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
        
    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def rotate_left_90(self):
        t = self.x
        self.x = -self.y
        self.y = t
        
    def rotate_right_90(self):
        t = self.x
        self.x = self.y
        self.y = -t
        
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    @staticmethod
    def null():
        return Vector(0,0)

    @staticmethod
    def unit(direction):
        if direction == 'E':
            return Vector(1,0)
        elif direction == 'N':
            return Vector(0,1)
        elif direction == 'W':
            return Vector(-1,0)
        elif direction == 'S':
            return Vector(0,-1)
        else:
            raise Exception('Unknown direction')


def permutations(a):
    if len(a) == 1:
        return [a]

    perms = []
    for i in range(len(a)):
        sp = permutations(a[:i] + a[i+1:])
        for p in sp:
            perms.append([a[i]] + p)
    return perms

