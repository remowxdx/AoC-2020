#!/usr/bin/env python3

def permutations(a):
    if len(a) == 1:
        return [a]

    perms = []
    for i in range(len(a)):
        sp = permutations(a[:i] + a[i+1:])
        for p in sp:
            perms.append([a[i]] + p)
    return perms

