import numpy

class Quartile:
    @staticmethod
    def quartile(data):
        q1 = numpy.quantile(data,0.25)
        q2 = numpy.quantile(data, 0.5)
        q3 = numpy.quantile(data, 0.75)
        return [q1,q2,q3]