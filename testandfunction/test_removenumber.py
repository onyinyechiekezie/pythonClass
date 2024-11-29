import unittest
import removenumber

class TestNumberRemoval(unittest.TestCase):
	def test_that_remove_number_exists(self):
		numbers = [1, 3, 4, 5]
		removenumber.get_remove_number(numbers)

	def test_that_remove_function_gives_the_correct_addition_value(self):
		numbers = [1, 2, 3, 5]
		actual = removenumber.get_remove_number(numbers)
		expected = [1, 2, 5] 
		self.assertEqual(actual, expected)

