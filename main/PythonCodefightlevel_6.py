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

class level6:
    def __init__(self):
        self.message = 'Hello World'

    def elemReplace(self, inputArray, elemtoReplace, substituteElem):
        for i in range(len(inputArray)):
            if inputArray[i] == elemtoReplace:
                inputArray[i] = substituteElem
        return inputArray;

    def evenDigitsOnely(self, n):
        odd = (1, 3, 5, 7, 9)
        number_string = str(n)
        for ch in number_string:
            if int(ch) in odd:
                return False
        return True

    def variableName(self, name):
        return name.isidentifier()

    def alphabeticShift(self, s):
        return "".join(chr((ord(i) - 96) % 26 + 97) for i in s)
