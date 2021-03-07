from scipy.stats import sem, t
from StatisticsOperations.Mean import Mean


class ConfidenceIntervalPop():
    @staticmethod

    def confidenceIntervalPop(conf, data):

        lngth = len(data)
        mean = Mean.mean(data)
        std_err = sem(data)
        high = std_err * t.ppf((1 + conf) / 2, lngth - 1)

        start = mean - high
        end = mean + high

        return start, end