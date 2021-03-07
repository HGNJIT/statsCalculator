from numpy.random import randint
from numpy.random import uniform


class RandomNoSeed():
    @staticmethod
    def randomInt(a, b):
        if isinstance(a, float):
            return RandomNoSeed.randomDec(a, b)
        return randint(a, b)

    @staticmethod
    def randomDec(a, b):
        return uniform(a, b)