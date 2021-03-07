from numpy.random import seed
from numpy.random import randint


def getRandomNumbers(seedNum, min, max, num):
    seed(seedNum)
    randomData = []
    i = 1
    while i < num + 1:
        randomData.append(randint(min, max))
        i += 1
    return randomData