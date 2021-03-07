import unittest
from random import randint, seed, sample

from PopulationSampling.Cochran import Cochran
from PopulationSampling.MarginError import MarginError
from PopulationSampling.RandomSampling import SimpleSampling
from PopulationSampling.SampleSizeKnownPop import SampleSizeKnownPop
from PopulationSampling.SampleSizeUnknownPop import SampleSizeUnkownPop


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(4)
        self.testData = sample(range(0, 50), 10)
        self.testData2 = randint(0, 50)


    def test_Cochran(self):
        result = Cochran.cochran(3, self.testData, 4)
        self.assertEqual(result, 0.37809484249342223)

    def test_Margin_Error(self):
        result = MarginError.marginError(3, self.testData)
        self.assertEqual(result, -9.524406311809198)

    def test_generate_sample(self):
        result = SimpleSampling.generateSampling(3, self.testData, 5)
        self.assertEqual(result, [4, 46, 4, 4, 15])

    def test_SampleSizeKnownPop(self):
        result = SampleSizeKnownPop.sampleSize(3, self.testData)
        self.assertEqual(result, 0.04267106345907859)

    def test_SampleSizeUnKnownPop(self):
        result = SampleSizeUnkownPop.sampleSize(3, self.testData, .5)
        self.assertEqual(result, 0.39384879426398156)

if __name__ == '__main__':
    unittest.main()