from StatisticsOperations.Covariance import Covariance
from StatisticsOperations.StandardDeviation import StandardDeviation


class populationCorrelation():
    @staticmethod

    def populationcorrelation(a, b):
        cov = Covariance.covariance(a, b)
        stdDevA = StandardDeviation.standardDeviation(a)
        stdDevB = StandardDeviation.standardDeviation(b)
        return cov/(stdDevA*stdDevB)