from StatisticsOperations.StandardDeviation import StandardDeviation
from StatisticsOperations.Zscore import Zscore
from MathOperations.nthRoot import NthRoot


class MarginError():
    @staticmethod
    def marginError(sd, data):
        zscore = Zscore.zscore(sd, data)
        standardDeviation = StandardDeviation.standardDeviation(data)
        MoE = zscore * (standardDeviation / (NthRoot.root(sd, 2)))
        return MoE