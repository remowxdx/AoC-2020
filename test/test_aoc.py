#!/usr/bin/env python3

import unittest

import aoc
import io
import sys

class DebugTest(unittest.TestCase):

    def setUp(self):
        self.debug = aoc.Debug()

    def test_debug_is_enabled(self):
        self.assertTrue(self.debug.enabled)

    def test_debug_disable(self):
        self.debug.disable()
        self.assertFalse(self.debug.enabled)

    def test_debug_enabled(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.debug('test')
        sys.stdout = sys.__stdout__
        self.assertEqual('test\n', capturedOutput.getvalue())

    def test_debug_disabled(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.debug.disable()
        self.debug('test')
        sys.stdout = sys.__stdout__
        self.assertEqual('', capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()
