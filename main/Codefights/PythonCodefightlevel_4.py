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

class level4:
    def __init__(self):
        self.message = 'Hello World'

    def alternatingSums(self, a):
        return [sum(a[::2]), sum(a[1::2])]

    def addBorder(self, picture):
        width = len(picture[0]) + 2
        result = ['*' * width]
        for i in picture:
            result.append('*' + i + '*')
        result.append('*' * width)
        return result

    def areSimilar(self, A, B):
        s = 0
        m = 0
        diff1 = [0, 0, 0]
        diff2 = [0, 0, 0]
        for i in range(len(A)):

            if m > 2:
                return False

            if A[i] != B[i]:
                s = s + 1
                diff1[m] = A[i]
                diff2[m] = B[i]
                m = m + 1

        if (s > 2):
            return False
        if (diff2[0] != diff1[1]) | (diff1[0] != diff2[1]):
            return False
        return True

    def arrayChange(self, inputArray):
        s = 0
        for i in range(1, len(inputArray)):
            k = inputArray[i - 1] - inputArray[i] + 1
            if k > 0:
                s += k
                inputArray[i] += k
        return s

    def palindromeRearranging(self, inputString):
        odds = 0
        for ch in set(inputString):
            if inputString.count(ch) % 2:
                odds += 1
                if odds > 1:
                    return False
        return True
