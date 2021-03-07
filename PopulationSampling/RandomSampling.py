from RandomOperations.SelectSeed import SelectSeed

from numpy.random import seed


class SimpleSampling(SelectSeed):
    @staticmethod

    def generateSampling(sd, lst, rnge):
        seed(sd)
        return SelectSeed.pickItem(sd, lst, rnge)