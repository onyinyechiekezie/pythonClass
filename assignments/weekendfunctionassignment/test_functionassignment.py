import unittest
import functionassignment

class TestFunctions(unittest.TestCase):
	def test_that_get_largest_exists(self):
		numbers = [2, 3, 4, 5, 8]
		functionassignment.get_largest(numbers)
	def test_that_largest_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8]
		actual= functionassignment.get_largest(numbers)
		expected = 8
		self.assertEqual(actual, expected)
	def test_that_largest_function_return_correct_value_with_float(self):
		numbers = [0.6, 7.5, 8.9, 4.5, 3.1]
		actual = functionassignment.get_largest(numbers)
		expected = 8.9 
		self.assertEqual(actual, expected)


	def test_that_get_reverse_exists(self):
		numbers = [2, 3, 4, 5, 8]
		functionassignment.get_reverse(numbers)
	def test_that_reverse_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8]
		actual= functionassignment.get_reverse(numbers)
		expected = [8, 5, 4, 3, 2]
		self.assertEqual(actual, expected)
	def test_that_reverse_function_return_correct_value_with_float(self):
		numbers = [0.6, 7.5, 8.9, 4.5, 3.1]
		actual = functionassignment.get_reverse(numbers)
		expected = [3.1, 4.5, 8.9, 7.5, 0.6] 
		self.assertEqual(actual, expected)


	def test_that_get_numberexistence_exists(self):
		numbers = [2, 3, 4, 5, 8]
		number = 2
		functionassignment.get_numberexistence(numbers, number)
	def test_that_numberexistence_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8]
		number = 2
		actual= functionassignment.get_numberexistence(numbers, number)
		expected = True
		self.assertEqual(actual, expected)
	def test_that_numberexistence_function_return_correct_value_with_float(self):
		numbers = [0.6, 7.5, 8.9, 4.5, 3.1]
		number = 0.6
		actual = functionassignment.get_numberexistence(numbers, number)
		expected = True 
		self.assertEqual(actual, expected)


	def test_that_get_oddpositions_exists(self):
		numbers = [2, 3, 4, 5, 8]
		functionassignment.get_oddpositions(numbers)
	def test_that_oddpositions_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8]
		actual= functionassignment.get_oddpositions(numbers)
		expected = [3, 5]
		self.assertEqual(actual, expected)
	def test_that_oddpositions_function_return_correct_value_with_float(self):
		numbers = [0.6, 7.5, 8.9, 4.5, 3.1]
		actual = functionassignment.get_oddpositions(numbers)
		expected =[7.5, 4.5]  
		self.assertEqual(actual, expected)



	def test_that_get_evenpositions_exists(self):
		numbers = [2, 3, 4, 5, 8]
		functionassignment.get_evenpositions(numbers)
	def test_that_evenpositions_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8]
		actual= functionassignment.get_evenpositions(numbers)
		expected = [4, 8]
		self.assertEqual(actual, expected)
	def test_that_evenpositions_function_return_correct_value_with_float(self):
		numbers = [0.6, 7.5, 8.9, 4.5, 3.1]
		actual = functionassignment.get_evenpositions(numbers)
		expected =[8.9, 3.1]  
		self.assertEqual(actual, expected)



	def test_that_get_total_exists(self):
		numbers = [2, 3, 4, 5, 8]
		functionassignment.get_total(numbers)
	def test_that_total_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8]
		actual= functionassignment.get_total(numbers)
		expected = 22
		self.assertEqual(actual, expected)
	def test_that_odd_function_return_correct_value_with_float(self):
		numbers = [0.6, 7.5, 8.9, 4.5, 3.1]
		actual = functionassignment.get_total(numbers)
		expected =  24.6
		self.assertEqual(actual, expected)



	def test_that_is_palindrome_exists(self):
		words = "flip"
		functionassignment.is_palindrome(words)
	def test_that_is_palindrome_function_gives_the_correct_value(self):
		words = "flip"
		actual= functionassignment.is_palindrome(words)
		expected = False
		self.assertEqual(actual, expected)








