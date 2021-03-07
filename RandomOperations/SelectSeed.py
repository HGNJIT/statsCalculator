from numpy.random import seed
from RandomOperations.SelectNoSeed import SelectNoSeed

class SelectSeed():
    @staticmethod
    def pickItem(sd, lst, rnge):
        seed(sd)
        lst2 = SelectNoSeed.pickItem(lst, rnge)
        return lst2