# from Statistics import statistics
#
# class zscore:
#
#     @staticmethod
#     def zscore(data):
#         mean = statistics.mean(data)
#         stD = statistics.standardDeviation(data)
#         for i in data:
#             zscore = (i - mean) / stD
#             return zscore

from StatisticsOperations.Mean import Mean
from StatisticsOperations.StandardDeviation import StandardDeviation
from RandomOperations.PickSeedList import PickSeedList

class Zscore():

    @staticmethod
    def zscore(seed, data):
        X = PickSeedList.pickSeed(seed, data)
        meanData = Mean.mean(data)
        sd = StandardDeviation.standardDeviation(data)
        z = (X-meanData) / sd
        return z