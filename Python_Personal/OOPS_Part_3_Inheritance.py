class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print("am inside init instance")

    def getData(self):
        print("am inside getData")

    def summation(self):
        return self.firstNum + self.secondNum + Calculator.num


obj = Calculator(2, 3)
print(obj.firstNum)
obj.getData()
print(obj.summation())


class ChildCalc(Calculator):
    num2 = 200

    def __init__(self, childA, childB):
        Calculator.__init__(self, childA, childB)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


childObj = ChildCalc(5, 10)
print(childObj.getCompleteData())
