import unittest

from main.PythonCodefightlevel_4 import level4


class MyTestCase(unittest.TestCase):
    "sample test"

    def setUp(self):
        "setting up the test"
        # print('testing begin')

    def tearDown(self):
        "ss"
        # print("test end")

    @unittest.skip("test ignore 1")
    def test_calternatingSumst(self):
        level4instance = level4()
        list1 = [50, 60, 60, 45, 70]
        result = [180, 105]
        self.assertEqual(level4instance.alternatingSums(list1), result)

    @unittest.skip("test ignore 1")
    def test_addBorder(self):
        level4instance = level4()
        list = ["abc", "ded"]
        result = ["*****", "*abc*", "*ded*", "*****"]
        self.assertEqual(level4instance.addBorder(list), result)

    @unittest.skip("test ignore 1")
    def test_areSimilar(self):
        level4instance = level4()
        A = [1, 2, 3]
        B = [1, 2, 3]
        self.assertEqual(level4instance.areSimilar(A, B), True)

        C = [1, 2, 3]
        D = [2, 1, 3]
        self.assertEqual(level4instance.areSimilar(C, D), True)

        F = [1, 2, 2]
        G = [2, 1, 1]
        self.assertEqual(level4instance.areSimilar(F, G), False)

    def test_arrayChange(self):
        level4instance = level4()
        A = [1, 1, 1]
        self.assertEqual(level4instance.arrayChange(A), 3)

    def test_palindromeRearring(self):
        level4instance = level4()
        input = "aabb"
        self.assertEqual(level4instance.palindromeRearranging(input), True)
