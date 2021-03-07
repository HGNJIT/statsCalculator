class  Addition:
    @staticmethod
    def sum(augend,addend=None):
        if isinstance(augend,list):
            return Addition.sumList(augend)
        return augend + addend

    @staticmethod
    def sumList (valueList):
        result = 0
        for element in valueList:
            result = Addition.sum(result, element)
        return result