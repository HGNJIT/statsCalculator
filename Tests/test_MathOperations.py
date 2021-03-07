import unittest

from Calculator.calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_sumList(self):
        numlist = [1, 3, 5, 2]
        result = self.calculator.Sum(numlist)
        self.assertEqual(11, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(4, 1)
        self.assertEqual(3, result)

    def test_MathOperation_Product(self):
        self.assertEqual(10, self.calculator.Product(2, 5))

    def test_MathOperations_Product_list(self):
        numlist = [1, 3, 5]
        self.assertEqual(15, self.calculator.Product(numlist))

    def test_MathOperations_Power(self):
        self.assertEqual(8, self.calculator.Power(2, 3))

    def test_MathOperations_Power_list(self):
        numlist = [1, 2, 3]
        self.assertEqual(9, self.calculator.Power(numlist, 2))

    def test_Root(self):
        self.assertEqual(3, self.calculator.Root(2,9))