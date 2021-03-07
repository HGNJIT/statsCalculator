from StatisticsOperations.Covariance import Covariance
from StatisticsOperations.StandardDeviation import StandardDeviation
from RandomOperations.SelectSeed import SelectSeed


class SampleCorrelation():
    @staticmethod
    def correlation(sd, a, b):
        sampleA = SelectSeed.pickItem(sd, a, 10)
        sampleB = SelectSeed.pickItem(sd, b, 10)

        cov = Covariance.covariance(sampleA, sampleB)
        stdDevA = StandardDeviation.standardDeviation(sampleA)
        stdDevB = StandardDeviation.standardDeviation(sampleB)
        return cov/(stdDevA*stdDevB)