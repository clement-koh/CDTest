import unittest

class Calculator():
	# Empty Constructor
	def __init__(self):
		pass

	def sum(self, x, y):
		return x + y

	def multiplication(self, x, y):
		return x * y


class testCalculator(unittest.TestCase):
	def setUp(self):
		self.calculator = Calculator()

	def testSum(self):
		result = self.calculator.sum(10, 5)
		self.assertEqual(result, 15, 'Adding two positive numbers')

	def testAddNegativeNumbers(self):
		result = self.calculator.sum(-10, -15)
		self.assertEqual(result, -25, 'Adding two negative numbers')

	def testAddNegativePositiveNumbers(self):
		result = self.calculator.sum(10, -19)
		self.assertEqual(result, -9, 'Adding a postive and negative number')

	def testMultiplicationPositiveNumber(self):
		result = self.calculator.multiplication(5, 5)
		self.assertEqual(result, 25, 'Multiplication of two positive numbers')

	def testMultiplicationNegativeNumber(self):
		result = self.calculator.multiplication(-5, -10)
		self.assertEqual(result, 50, 'Multiplication of two negative numbers')

	def testMultiplicationPositiveNegativeNumber(self):
		result = self.calculator.multiplication(5, -8)
		self.assertEqual(result, -40, 'Multiplication of a positive and a negative numbers')

	def testMultiplicationZero(self):
		result = self.calculator.multiplication(5, 0)
		self.assertEqual(result, 0, 'Multiplication by zero')

	def testMultiplicationOne(self):
		result = self.calculator.multiplication(5, 1)
		self.assertEqual(result, 5, 'Multiplication by one')

if __name__ == "__main__":
	unittest.main()