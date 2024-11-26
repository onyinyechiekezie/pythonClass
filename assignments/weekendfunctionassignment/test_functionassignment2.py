import unittest
import functionassignment2

class TestFunctions2(unittest.TestCase):
	def test_that_is_Even_exists(self):
		integer = 4
		functionassignment2.is_Even(integer)
	def test_that_is_Even_function_gives_the_correct_value(self):
		integer = 6
		actual= functionassignment2.is_Even(integer)
		expected = True
		self.assertEqual(actual, expected)



	def test_that_is_prime_exists(self):
		number = 4
		functionassignment2.is_prime(number)
	def test_that_is_prime_function_gives_the_correct_value(self):
		number = 6
		actual= functionassignment2.is_prime(number)
		expected = False
		self.assertEqual(actual, expected)



	def test_that_get_difference_exists(self):
		integer1 = 4
		integer2 = 1
		functionassignment2.get_difference(integer1, integer2)
	def test_that_get_difference_function_gives_the_correct_value(self):
		integer1 = 6
		integer2 = 8
		actual= functionassignment2.get_difference(integer1, integer2)
		expected = 2
		self.assertEqual(actual, expected)


	def test_that_get_quotient_exists(self):
		integer1 = 4
		integer2 = 1
		functionassignment2.get_quotient(integer1, integer2)
	def test_that_get_quotient_function_gives_the_correct_value(self):
		integer1 = 6
		integer2 = 2
		actual= functionassignment2.get_quotient(integer1, integer2)
		expected = 3
		self.assertEqual(actual, expected)


