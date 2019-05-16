import unittest

from main.PythonCodefightlevel_1_2_3 import level1_2_3


class MyTestCase(unittest.TestCase):
    "sample test"

    def setUp(self):
        "setting up the test"
        print('testing begin')

    def tearDown(self):
        print("test end")

    @unittest.skip("test ignore 1")
    def test_centuryFromYear_set(self):
        level1_2_3instance = level1_2_3()
        self.assertEqual(level1_2_3instance.centuryFromYear(1905), 20)
        self.assertEqual(level1_2_3instance.centuryFromYear(1700), 17)

    @unittest.skip('test ignore 2')
    def test_paindrome(self):
        level1_2_3instance = level1_2_3();
        self.assertEqual(level1_2_3instance.checkPaindrome("aabaa"), True)
        self.assertEqual(level1_2_3instance.checkPaindrome("abac"), False)
        self.assertEqual(level1_2_3instance.checkPaindrome("a"), True)

    @unittest.skip('test ignore')
    def test_adjacent(self):
        level1_2_3instance = level1_2_3()
        item = [3, 6, -2, -5, 7, 3]
        self.assertEqual(level1_2_3instance.adjacentElemensProduct(item), 21)

    @unittest.skip('test ignore')
    def test_shapeArea(self):
        level1_2_3instance = level1_2_3()
        self.assertEqual(level1_2_3instance.shapeArea(2), 5)
        self.assertEqual(level1_2_3instance.shapeArea(3), 13)

    @unittest.skip('test ignore')
    def test_makeArrayConsecutive2(self):
        status = [6, 2, 3, 8]
        level1_2_3instance = level1_2_3()

        self.assertEqual(level1_2_3instance.makeArrayConsecutive2(status), 3)

    @unittest.skip('test ignore')
    def test_almostIncreasingSequence(self):
        list1 = [1, 3, 2, 1]
        list2 = [1, 2, 1, 2]
        list3 = [1, 1, 1, 2, 3]
        list4 = [1, 3, 2]
        list5 = [1, 2, 3, 4, 5, 3, 5, 6]
        list6 = [1, 1]
        list7 = [1, 2, 3, 4, 3, 6]

        level1_2_3instance = level1_2_3()
        self.assertEqual(level1_2_3instance.almostIncreasingSequence(list1), False)
        self.assertEqual(level1_2_3instance.almostIncreasingSequence(list2), False)
        self.assertEqual(level1_2_3instance.almostIncreasingSequence(list3), False)
        self.assertEqual(level1_2_3instance.almostIncreasingSequence(list4), True)
        self.assertEqual(level1_2_3instance.almostIncreasingSequence(list5), False)
        self.assertEqual(level1_2_3instance.almostIncreasingSequence(list6), True)
        self.assertEqual(level1_2_3instance.almostIncreasingSequence(list7), True)

    @unittest.skip('test ignore')
    def test_matrixElement(self):
        list1 = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]];

        level1_2_3instance = level1_2_3();
        self.assertEqual(level1_2_3instance.matrixElementsSum(list1), 9)

    @unittest.skip('test ignore')
    def testallLongest(self):
        list1 = ["aba", "aa", "ad", "vcd", "aba"];
        result = ["aba", "vcd", "aba"];

        level1_2_3instance = level1_2_3();
        self.assertEqual(level1_2_3instance.allLongest(list1), result)

    @unittest.skip('test ignore')
    def testcommonCharacterCount(self):
        level1_2_3instance = level1_2_3();
        s1 = "aabcc";
        s2 = "adcaa";
        self.assertEqual(level1_2_3instance.commonCharacterCount(s1, s2), 3)

        s3 = "zzzz";
        s4 = "zzzzzzz";
        self.assertEqual(level1_2_3instance.commonCharacterCount(s3, s4), 4)

    @unittest.skip('test ignore')
    def testisLucky(self):
        level1_2_3instance = level1_2_3()
        n = 1230
        self.assertEqual(level1_2_3instance.isLucky(n), True)
        m = 239017
        self.assertEqual(level1_2_3instance.isLucky(m), False)

    @unittest.skip('test ignore')
    def testsortByHeight(self):
        level1_2_3instance = level1_2_3()
        a = [-1, 150, 190, 170, -1, -1, 160, 180]
        result = [-1, 150, 160, 170, -1, -1, 180, 190]
        self.assertEqual(level1_2_3instance.sortByHeight(a), result)

    def testreverseParantes(self):
        level1_2_3instance = level1_2_3()
        s = "a(bc)de";
        result = "acbde";
        self.assertEqual(level1_2_3instance.reverseParentheses(s), result);

        s1 = "a(bcdefghijkl(mno)p)q";
        result1 = "apmnolkjihgfedcbq";
        self.assertEqual(level1_2_3instance.reverseParentheses(s1), result1);

        s2 = "co(de(fight)s)";
        result2 = "cosfighted";
        self.assertEqual(level1_2_3instance.reverseParentheses(s2), result2);

        s3 = "Code(Cha(lle)nge)";
        result3 = "CodeegnlleahC";
        self.assertEqual(level1_2_3instance.reverseParentheses(s3), result3);

        s4 = "Where are the parentheses?";
        result4 = "Where are the parentheses?";
        self.assertEqual(level1_2_3instance.reverseParentheses(s4), result4);

        s5 = "abc(cba)ab(bac)c";
        result5 = "abcabcabcabc";
        self.assertEqual(level1_2_3instance.reverseParentheses(s5), result5);

        s6 = "The ((quick (brown) (fox) jumps over the lazy) dog)";
        result6 = "The god quick nworb xof jumps over the lazy";
        self.assertEqual(level1_2_3instance.reverseParentheses(s6), result6);
