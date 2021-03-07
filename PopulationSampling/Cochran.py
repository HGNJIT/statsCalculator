from StatisticsOperations.Zscore import Zscore
from MathOperations.exponentiation import Exponentiation
from PopulationSampling.MarginError import MarginError
from PopulationSampling.PopulationProportion import PopulationProportion

class Cochran():
    @staticmethod
    def cochran(sd, data, rnge):
        z = Zscore.zscore(sd, data)
        p = PopulationProportion.proportion(sd, data, rnge)
        e = MarginError.marginError(sd, data)
        q = 1 - p

        cochran = (Exponentiation.power(z, 2) * p * q) / Exponentiation.power(e, 2)

        return cochran