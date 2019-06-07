# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()

#
# int centuryFromYear(int year) {
#     int kalan = (year % 100);
# if(kalan != 0){
# return  (year - kalan) / 100 + 1;
# }
# return (year-kalan)/100;

class level1_2_3:
    def __init__(self):
        self.message = 'Hello World'

    def centuryFromYear(self, year):
        kalan = year % 100;
        if kalan != 0:
            return (year - kalan) / 100 + 1
        return (year - kalan) / 100

    def checkPaindrome(self, input_string):
        lenStr = len(input_string)
        if (lenStr == 1):
            return True
        for x in range(0, lenStr):
            if (input_string[x] != input_string[lenStr - x - 1]):
                return False
        return True

    def adjacentElemensProduct(self, inputArray):
        max = inputArray[0] * inputArray[1]
        for x in range(0, len(inputArray) - 1):
            if (inputArray[x] * inputArray[x + 1] > max):
                max = inputArray[x] * inputArray[x + 1]
        return max

    def shapeArea(self, n):
        maxHight = 2 * n - 1
        shapeArea = 0
        for x in range(0, n):
            shapeArea += 2 * x + 1
        return 2 * shapeArea - maxHight

    def makeArrayConsecutive2(self, inputArray):
        minelement = min(inputArray)
        maxelement = max(inputArray)
        s = 0;
        for x in range(minelement, maxelement):
            if x not in inputArray:
                s = s + 1
        return s

    def almostIncreasingSequence(self, s):
        output = None
        for i in range(1, len(s)):
            if s[i] == s[i - 2] and output == False:
                return False
            elif s[i] <= s[i - 1]:
                if output == False:
                    return output
                elif i != len(s) - 1 and i != 1 and s[i] < s[i - 2]:
                    if s[i] == s[i - 2] or s[i + 1] < s[i - 2]:
                        return False
                output = False
        return True

    def matrixElementsSum(self, inputArray):
        r = len(inputArray)
        c = len(inputArray[0])
        total = 0
        for j in range(c):
            for i in range(r):
                if inputArray[i][j] != 0:
                    total += inputArray[i][j]
                else:
                    break
        return total

    def allLongestString(self, inputArray):
        result = []
        l = len(inputArray[0])
        for x in range(0, len(inputArray)):

            if len(inputArray[x]) > l:
                result.clear()
                l = len(inputArray[x])

            if len(inputArray[x]) == l:
                result.append(inputArray[x])
        return result

    def commonCharacterCount(self, s1, s2):
        d = {}
        for c in s1:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        s = 0
        for c in s2:
            if c in d and d[c] > 0:
                s += 1
                d[c] -= 1
        return s

    def isLucky(self, n):
        s = str(n)
        half = int(len(s) / 2)
        first, second = [s[:half], s[half:]]
        return sum([int(i) for i in first]) == sum([int(i) for i in second])

        # s = str(n)
        # pivot = len(s)//2
        # left, right = s[:pivot], s[pivot:]
        # return sum(map(int, left)) == sum(map(int, right))

    def sortByHeight(self, n):
        index = []
        result = []
        for x in range(0, len(n)):
            if (n[x] == -1):
                index.append(x);
        ff = sorted(n)
        ss = list(filter(lambda a: a != -1, ff))
        i = 0;
        for y in range(0, len(n)):
            if y in index:
                result.append(-1)
            else:
                result.append(ss[i])
                i = i + 1
        return result

    def reverseParentheses(self, s):
        l = list(s)
        while l.count(")"):
            a = l.index(")")
            b = list(reversed(l[:a])).index("(")
            l = l[:a - b - 1] + list(reversed(l[a - b:a])) + l[a + 1:]
        return ''.join(l)
