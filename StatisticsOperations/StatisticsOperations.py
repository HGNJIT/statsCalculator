from StatisticsOperations.Mean import Mean
from StatisticsOperations.Median import Median
from StatisticsOperations.mode import Mode
from StatisticsOperations.skew import Skew
from StatisticsOperations.variance import Variance
from StatisticsOperations.StandardDeviation import StandardDeviation
from StatisticsOperations.Covariance import Covariance
from StatisticsOperations.samplecorrelation import SampleCorrelation
from StatisticsOperations.Zscore import Zscore
from StatisticsOperations.Quartile import Quartile
from StatisticsOperations.MeanDeviation import MeanDeviation
from StatisticsOperations.PopulationCorrelation import populationCorrelation

def mean(data):
    return Mean.mean(data)

def median(data):
    return Median.median(data)
  
def mode(data):
    return Mode.mode(data)

def skew(data, axis, bias):
    return Skew.skew(data, axis, bias)

def variance(data):
    return Variance.variance(data)

def standardDeviation(data):
    return StandardDeviation.standardDeviation(data)

def covariance(data1, data2):
    return Covariance.covariance(data1,data2)

def samplecorrelation(number,data1,data2):
    return SampleCorrelation.correlation(number,data1,data2)

def zscore(sd, data):
    return Zscore.zscore(sd, data)

def quartile(data):
    return Quartile.quartile(data)

def meandeviation(data):
    return MeanDeviation.meanDeviation(data)

def populationcorrelation(data,data2):
    return populationCorrelation.populationcorrelation(data, data2)