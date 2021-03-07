import numpy as np

class Covariance():
    @staticmethod
    def covariance(data1,data2):
        return np.cov(data1,data2)[0,1]