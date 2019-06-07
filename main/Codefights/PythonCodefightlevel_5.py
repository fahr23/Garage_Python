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

class level5:
    def __init__(self):
        self.message = 'Hello World'

    def areEquallyStrong(self, yourleft, yourRigh, friendLeft, friendRigh):
        return sorted([yourleft, yourRigh]) == sorted([friendLeft, friendRigh])

    def arrayMaximalAdjacentDifference(inputArray):
        return max(map(lambda x: abs(x[0] - x[1]), zip(inputArray, inputArray[1:])))

    def isIPv4Address(s):
        p = s.split('.')
        return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)
