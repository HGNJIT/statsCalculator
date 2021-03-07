class Subtraction:

    @staticmethod
    def difference(minuend, subtraend=None):
        if isinstance(minuend, list):
            return Subtraction.diffList(minuend)
        return minuend - subtraend

    @staticmethod
    def diffList(sublist):
        result = 0
        for value in sublist:
            result = Subtraction.difference(value, result)

        return value