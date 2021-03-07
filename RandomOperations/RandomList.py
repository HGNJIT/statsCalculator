from numpy.random import seed
from numpy.random import randint
from numpy.random import uniform


class RandomList():
    @staticmethod
    def listInt(a, b, length, sd):
        if isinstance(a, float):
            return listDec(a, b, length, sd)
        lst = []
        seed(sd)
        for each in range(length):
            num = randint(a, b)
            lst.append(num)
        return lst

    @staticmethod
    def listDec(a, b, length, sd):
        lst = []
        seed(sd)
        for each in range(length):
            num = uniform(a, b)
            lst.append(num)
        return lst