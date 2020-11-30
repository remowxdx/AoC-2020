#!/usr/bin/env python3

import unittest

import tools

class ToolsTest(unittest.TestCase):

    def test_permutations_1_el(self):
        a = [1,]
        r = tools.permutations(a)
        self.assertEqual(r, [[1, ], ])

    def test_permutations_2_el(self):
        a = [1,2]
        r = tools.permutations(a)
        self.assertEqual(r, [[1,2], [2,1]])

    def test_permutations_3_el(self):
        a = [1,2,3]
        r = tools.permutations(a)
        self.assertEqual(r, [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]])

if __name__ == '__main__':
    unittest.main()
