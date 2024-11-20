import unittest
import listsumtask

class TestListSumFunction(unittest.TestCase):
	def test_that_get_sum_exists(self):
		numbers = [1,3,5,7]
		listsumtask.get_sum(numbers)

	def test_that_sum_function_gives_the_correct_addition_value(self):
		numbers = [1, 2, 3, 5]
		actual = listsumtask.get_sum(numbers)
		expected = 11
		self.assertEqual(actual, expected)

	def test_sum_function_raise_exception_with_invalid_input(self):
		numbers = ["onyii","ab"]
		self.assertRaises(TypeError, listsumtask.get_sum(numbers), "onyii")


