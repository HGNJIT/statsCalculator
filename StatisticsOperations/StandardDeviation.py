from MathOperations.nthRoot import NthRoot
from StatisticsOperations.variance import Variance

class StandardDeviation:
   @staticmethod
   def standardDeviation(data):
      return NthRoot.root(Variance.variance(data), 2)