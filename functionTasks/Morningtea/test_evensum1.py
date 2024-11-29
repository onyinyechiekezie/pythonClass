import unittest
import evensum1

class TestEvenSumFunction(unittest.TestCase):
	def test_that_get_evensum1_exists(self):
		number = [2, 3, 4, 5, 8]
		evensum1.get_evensum1(number)
	def test_that_evensum_function_gives_the_correct_value(self):
		number = [2, 3, 4, 5, 8,10]
		actual = evensum1.get_evensum1(number)
		expected = 24
		self.assertEqual(actual, expected)


	"""def test_that_get_primenumbers_exists(self):
		number = 20
		evensum1.get_primenumbers(number)

	def test_that_get_primenumbers_function_gives_the_correct_value(self):
		number = 20
		actual = evensum1.get_primenumbers(number)
		expected = [2, 3, 5, 7, 11, 13, 17, 19]
		self.assertEqual(actual, expected)"""

	def test_that_get_evencount_exists(self):
		numbers = [2, 3, 4, 5, 8]
		evensum1.get_evencount(numbers)
	def test_that_evencount_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8,10]
		actual = evensum1.get_evencount(numbers)
		expected = 4
		self.assertEqual(actual, expected)



	def test_that_get_boolean_value_exists(self):
		numbers = [2, 3, 4, 5, 8]
		evensum1.get_boolean_value(numbers)
	def test_that_get_boolean_value_function_gives_the_correct_value(self):
		numbers = [2, 3, 4, 5, 8,10]
		actual = evensum1.get_boolean_value(numbers)
		expected = [True, False, True, False, True, True]
		self.assertEqual(actual, expected)


	def test_that_get_firstlettercapitalized_exists(self):
		strings = ['red', 'orange', 'yellow', 'green', 'blue']
		evensum1.get_firstlettercapitalized(strings)
	def test_that_get_firstlettercapitalized_function_gives_the_correct_value(self):
		strings = ['red', 'orange', 'yellow', 'green', 'blue']
		actual = evensum1.get_firstlettercapitalized(strings)
		expected = ['Red', 'Orange', 'Yellow', 'Green', 'Blue']
		self.assertEqual(actual, expected)


	def test_that_get_multiples_of_3_exists(self):
		numbers = (3, 31, 3)
		evensum1.get_multiples_of_3(numbers)
	def test_that_get_multiples_of_3_function_gives_the_correct_value(self):
		numbers = (3, 31, 3)
		actual = evensum1.get_multiples_of_3(numbers)
		expected = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
		self.assertEqual(actual, expected)

	
	"""def test_that_get_odd_squared_exists(self):
		numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
		evensum1.get_odd_squared(numbers)"""


	def test_that_get_square_exists(self):
		value = (4)
		evensum1.get_square(value)
	def test_that_get_square_function_gives_the_correct_value(self):
		value = (4)
		actual = evensum1.get_square(value)
		expected = [1, 4, 9, 16]
		self.assertEqual(actual, expected)


	def test_that_get_greaterthan10_exists(self):
		values = [1, 5, 12, 15, 8]
		evensum1.get_greaterthan10(values)
	def test_that_get_greaterthan10_function_gives_the_correct_value(self):
		values = [1, 5, 12, 15, 8]
		actual = evensum1.get_greaterthan10(values)
		expected = [12, 15]
		self.assertEqual(actual, expected)


	def test_that_is_palindrome_exists(self):
		strings = ['madam', 'apple', 'racecar']
		evensum1.is_palindrome(strings)
	def test_that_is_palindrome_function_gives_the_correct_value(self):
		strings = ['madam', 'apple', 'racecar']
		actual = evensum1.is_palindrome(strings)
		expected = [True, False, True]
		self.assertEqual(actual, expected)



	def test_that_get_numbers_only_exists(self):
		string_values = 'abc123def456'
		evensum1.get_numbers_only(string_values)
	def test_that_get_numbers_only_function_gives_the_correct_value(self):
		string_values = 'abc123def456'
		actual = evensum1.get_numbers_only(string_values)
		expected = [1, 2, 3, 4, 5, 6]
		self.assertEqual(actual, expected)



	def test_that_get_double_exists(self):
		value = [1,2, 3]
		evensum1.get_double(value)
	def test_that_get_double_function_gives_the_correct_value(self):
		value = [1,2,3]
		actual = evensum1.get_double(value)
		expected = [2, 4, 6]
		self.assertEqual(actual, expected)



	def test_that_get_five_words_exists(self):
		strings = ["Apple", "Fish", "Orange", "Ice", "Lime"]
		evensum1.get_five_words(strings)
	def test_that_get_five_words_function_gives_the_correct_value(self):
		strings = ["Apple", "Fish", "Orange", "Ice", "Lime"]
		actual = evensum1.get_five_words(strings)
		expected = ["Apple", "Orange"]
		self.assertEqual(actual, expected)


	def test_that_get_digit_addition_exists(self):
		value = 192374
		evensum1.get_digit_addition(value)
	def test_that_get_digit_addition_function_gives_the_correct_value(self):
		value = 192374
		actual = evensum1.get_digit_addition(value)
		expected = 26
		self.assertEqual(actual, expected)


	"""def test_that_get_vowels_exists(self):
		strings = ["Orange","Apple","ice","Beans","Rice"]
		evensum1.get_vowels(strings)
	def test_that_get_vowels_function_gives_the_correct_value(self):
		strings = ["Orange","Apple","ice","Beans","Rice"]
		actual = evensum1.get_vowels(strings)
		expected = ["rng","ppl","c","Bns","Rc"]
		self.assertEqual(actual, expected)"""


	"""def test_that_get_evensquared_exists(self):
		value = (10)
		evensum1.get_evensquared(value)"""


	def test_that_get_zip_list_exists(self):
		keys = ["name", "age", "city"]
		values = ["Alice", 25, "New York"]
		evensum1.get_zip_list(keys, values)
	def test_that_get_zip_list_function_gives_the_correct_value(self):
		keys = ["name", "age", "city"]
		values = ["Alice", 25, "New York"]
		actual = evensum1.get_zip_list(keys, values)
		expected = {"name":"Alice", "age":25, "city":"New York"}
		self.assertEqual(actual, expected)









		


