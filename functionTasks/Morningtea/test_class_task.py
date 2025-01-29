import unittest
import class_task

class TestEvenOddFunction(unittest.TestCase):
	def test_that_get_evenodd_exists(self):
		numbers = [2, 3, 4, 5, 8]
		class_task.get_even_odd(numbers)
	def test_that_even_odd_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8,10]
		actual = class_task.get_even_odd(numbers)
		expected = [2, 4]
		self.assertEqual(actual, expected)