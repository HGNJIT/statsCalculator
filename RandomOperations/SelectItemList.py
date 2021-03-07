from numpy.random import randint

class SelectItemList():
    @staticmethod
    def pickItem(lst):
        length = len(lst)
        position = randint(0, length-1)

        return lst[position]