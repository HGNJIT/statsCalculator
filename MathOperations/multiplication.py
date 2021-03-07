class  Multiplication:
    @staticmethod
    def product(multiplier,multiplicand=None):
        if (isinstance(multiplier,list)):
            return Multiplication.productList(multiplier)
        return multiplier * multiplicand

    @staticmethod
    def productList (valueList):
        result = 1
        for element in valueList:
            result = Multiplication.product(result, element)
        return result