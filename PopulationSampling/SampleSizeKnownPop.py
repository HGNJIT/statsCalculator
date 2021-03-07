from PopulationSampling.MarginError import MarginError
from StatisticsOperations.StandardDeviation import StandardDeviation
from MathOperations.exponentiation import Exponentiation

class SampleSizeKnownPop():
    @staticmethod

    def sampleSize(sd, data):

        e = MarginError.marginError(sd, data)
        stdDev = StandardDeviation.standardDeviation(data)
        val = (1.96 * stdDev) / e
        sample = Exponentiation.power(val, 2)

        return sample