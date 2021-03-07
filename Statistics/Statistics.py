from Calculator.calculator import Calculator
from StatisticsOperations.StatisticsOperations import *


class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean.mean(data)
        return self.Result

    def median(self, data):
        self.Result = Median.median(data)
        return self.Result

    def mode(self, data):
        self.Result = Mode.mode(data)
        return self.Result

    def skew(self, data, axis, bias):
        self.Result = Skew.skew(data, axis, bias)
        return self.Result

    def variance(self, data):
        self.Result = Variance.variance(data)
        return self.Result

    def standardDeviation(self, data):
        self.Result = StandardDeviation.standardDeviation(data)
        return self.Result

    def covariance(self, data1, data2):
        self.Result = Covariance.covariance(data1, data2)
        return self.Result

    def samplecorrelation(self, number, data1, data2):
        self.Result = SampleCorrelation.correlation(number, data1, data2)
        return self.Result

    def zscore(self, sd, data):
        self.Result = Zscore.zscore(sd, data)
        return self.Result

    def quartile(self, data):
        self.Result = Quartile.quartile(data)
        return self.Result

    def meandeviation(self, data):
        self.Result = MeanDeviation.meanDeviation(data)
        return self.Result

    def populationCorrelation(self, data, data2):
        self.Result = populationCorrelation.populationcorrelation(data, data2)
        return self.Result