from numpy.random import randint

class SelectNoSeed():
    @staticmethod

    def pickItem(lst, rnge):
        lst2 =[]
        size = len(lst)

        for each in range(rnge):
            position = randint(0, size-1)
            lst2.append(lst[position])

        return lst2