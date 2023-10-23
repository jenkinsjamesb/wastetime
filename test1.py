#!/usr/bin/env python3
import waste
import unittest

class TestSum(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(waste.waste(2), 0)

if __name__ == '__main__':
    unittest.main()