from numpy.random import seed
from RandomOperations.SelectItemList import SelectItemList

class PickSeedList():
    @staticmethod

    def pickSeed(sd, lst):
        seed(sd)

        return SelectItemList.pickItem(lst)