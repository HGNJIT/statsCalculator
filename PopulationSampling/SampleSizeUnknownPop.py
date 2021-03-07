from StatisticsOperations.Zscore import Zscore
from PopulationSampling.MarginError import MarginError
from MathOperations.exponentiation import Exponentiation

class SampleSizeUnkownPop():

    @staticmethod
    def sampleSize(sd, data, percentage):
        z = Zscore.zscore(sd, data)
        e = MarginError.marginError(sd, data)
        p = percentage
        q = 1 - p
        val = z/e
        sample = Exponentiation.power(val, 2) * p * q

        return sample