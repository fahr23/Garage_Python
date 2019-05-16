import unittest

from main.PythonCodefightlevel_6 import level6


class MyTestCase(unittest.TestCase):
    "sample test"

    def setUp(self):
        "setting up the test"
        # print('testing begin')

    def tearDown(self):
        "ss"
        # print("test end")

    @unittest.skip("test ignore ")
    def test_elemReplace(self):
        level6instance = level6()
        inputArray = [1, 2, 1]
        elemtoReplace = 1
        substituteElem = 3
        result = [3, 2, 3]
        self.assertEqual(level6instance.elemReplace(inputArray, elemtoReplace, substituteElem), result)

    @unittest.skip("test ignore ")
    def test_eventDigisOnly(self):
        n = 642386
        level6instance = level6()
        self.assertEqual(level6instance.evenDigitsOnely(n), False)

    @unittest.skip("test ignore ")
    def test_variableName(self):
        input = 'var_1__Int'
        level6instance = level6()
        self.assertEqual(level6instance.variableName(input), True)

    def test_alphabeticShift(self):
        input = 'crazy'
        level6instance = level6()
        self.assertEqual(level6instance.alphabeticShift(input) == "dsbaz", True)
