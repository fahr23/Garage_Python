import unittest

from main.Codefights.PythonCodefightlevel_5 import level5


class MyTestCase(unittest.TestCase):
    "sample test"

    def setUp(self):
        "setting up the test"
        # print('testing begin')

    def tearDown(self):
        "ss"
        # print("test end")

    def test_calternatingSumst(self):
        level5instance = level5()
        yr = 10
        fr = 10
        yl = 15
        fl = 15
        self.assertEqual(level5instance.areEquallyStrong(yl, yr, fl, fr), True)

    def arrayMaxTest(self):
        level5instance = level5()
        inputArray = [2, 4, 1, 0]
        self.assertEqual(level5instance.arrayMaximalAdjacentDifference(inputArray), 3)

    def isIPV4Adress(self):
        level5instance = level5()
        input = ".254.255.0"
        self.assertEqual(level5instance.isIPv4Address(input), False)
