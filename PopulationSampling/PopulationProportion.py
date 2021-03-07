from RandomOperations.SelectSeed import SelectSeed


class PopulationProportion():
    @staticmethod

    def proportion(sd, data, rnge):
        data2 = SelectSeed.pickItem(sd, data, rnge)
        proportion = len(data2)/len(data)
        return proportion