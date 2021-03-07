from MathOperations.MathOperations import *


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b=0):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Product(self, a, b=1):
        self.Result = Multiplication.product(a, b)
        return self.Result

    def Quotient(self, a, b):
        self.Result = Division.quotient(a, b)
        return self.Result

    def Power(self, a, b):
        self.Result = Exponentiation.power(a, b)
        return self.Result

    def Root(self, a, b):
        self.Result = NthRoot.root(a, b)
        return self.Result