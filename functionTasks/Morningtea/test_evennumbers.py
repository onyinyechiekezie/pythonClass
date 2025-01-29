import unittest
import evennumbers

class TestEvenNumberFunction(unittest.TestCase):
	def test_that_get_even_numbers_exists(self):
		string = "73H2ADSdf439dm"
		evennumbers.get_even_numbers(string)
	def test_that_even_function_gives_the_correct_value(self):
		string = "73H2Adsdf439dm"
		actual = evennumbers.get_even_numbers(string)
		expected = [2, 4]
		self.assertEqual(actual, expected)


	def test_that_get_list_exists(self):
		numbers = [12, 15, 19, 21, 50, 70]
		evennumbers.get_list(numbers)
	"""def test_that_list_function_gives_the_correct_value(self):
		numbers = [12, 15, 19, 21, 50, 70]
		actual = evennumbers.get_list(numbers)
		expected = [21, 50]
		self.assertEqual(actual, expected)"""


	def test_that_get__exists(self):
		numbers = [12, 15, 19, 21, 50, 70]
		evennumbers.get_list(numbers)