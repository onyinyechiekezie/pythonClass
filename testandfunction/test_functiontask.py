import unittest
import functiontask

class TestSquareRootFunction(unittest.TestCase):
	def test_that_get_divide_or_square_function_exists(self):
		functiontask.get_divide_or_square(5)


	def test_that_number_gives_the_correct_square_root_value(self):
		actual = functiontask.get_divide_or_square(10)
		expected = 3.16
		self.assertEqual(actual, expected)
		actual = functiontask.get_divide_or_square(7)
		expected = 2
		self.assertEqual(actual, expected)

	def test_divide_or_square_function_raise_exception_with_negative_value(self):
		self.assertRaises(TypeError, functiontask.get_divide_or_square(-7))

	def test_divide_or_square_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, functiontask.get_divide_or_square, "onyii")

	def test_that_divide_or_square_function_return_correct_value_with_float(self):
		actual = functiontask.get_divide_or_square(10.5)
		expected = 0.5 
		self.assertEqual(actual, expected)

	def test_divide_or_square_function_raise_exception_with_zero_input(self):
		self.assertRaises(TypeError, functiontask.get_divide_or_square(0))



	#Question2

	def test_that_get_futureinvestment_function_exists(self):
		functiontask.get_futureinvestment(100










