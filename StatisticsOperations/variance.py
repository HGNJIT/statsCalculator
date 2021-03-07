from numpy import var

class Variance:
    @staticmethod
    def variance(data):
        res = var(data)
        return res