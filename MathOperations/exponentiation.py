import math;

class Exponentiation:
    @staticmethod
    def power(base, exponent=None):
        if (isinstance(base, list)):
            return Exponentiation.powerList(base,exponent)
        return math.pow(base,exponent)

    @staticmethod
    def powerList(valueList,exp):
        result = 1
        for element in valueList:
            result = Exponentiation.power(element, exp)
        return result