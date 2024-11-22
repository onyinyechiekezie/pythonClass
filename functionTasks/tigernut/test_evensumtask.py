import unittest
import evensumtask

class TestEvenSumFunction(unittest.TestCase):
	def test_that_get_evensum_exists(self):
		number = [2, 3, 4, 5, 8]
		evensumtask.get_evensum(number)
	def test_that_evensum_function_gives_the_correct_value(self):
		number = [2, 3, 4, 5, 8]
		actual = evensumtask.get_evensum(number)
		expected = 14
		self.assertEqual(actual, expected)


	def test_that_get_vowel_exists(self):
		letters = ("Python is sweet")
		evensumtask.get_vowel(letters)
	def test_that_vowel_function_gives_the_correct_value(self):
		letters = ("Python is sweet")
		actual = evensumtask.get_vowel(letters)
		expected = 4
		self.assertEqual(actual, expected)


	def test_that_is_palindrome_exists(self):
		words = "madam"
		evensumtask.is_palindrome(words)
	def test_that_palindrome_function_gives_the_correct_value(self):
		words = ("madam")
		actual = evensumtask.is_palindrome(words)
		expected = True
		self.assertEqual(actual, expected)


	def test_that_get_anagram_exists(self):
		word_one = "listen"
		word_two = "silent"
		evensumtask.get_anagram(word_one, word_two)
	def test_that_anagram_function_gives_the_correct_value(self):
		word_one = "listen"
		word_two = "silent"
		actual = evensumtask.get_anagram(word_one, word_two)
		expected = True
		self.assertEqual(actual, expected)



	def test_that_is_prime_exists(self):
		number = 7
		evensumtask.is_prime(number)
	def test_that_prime_function_gives_the_correct_value(self):
		number = 10
		actual = evensumtask.is_prime(number)
		expected =True 
		self.assertEqual(actual, expected)


	def test_that_get_average_exists(self):
		numbers = [10, 20, 30, 40]
		evensumtask.get_average(numbers)
	def test_that_get_average_function_gives_the_correct_value(self):
		numbers = [10, 20, 30, 40]
		actual = evensumtask.get_average(numbers)
		expected = 25
		self.assertEqual(actual, expected)


	def test_that_get_reverse_exists(self):
		word = "hello"
		evensumtask.get_reverse(word)
	def test_that_get_reverse_function_gives_the_correct_value(self):
		word = "hello"
		actual = evensumtask.get_reverse(word)
		expected = "olleh"
		self.assertEqual(actual, expected)



	def test_that_get_summation_exists(self):
		numbers = [1, 2, 3, 4]
		evensumtask.get_summation(numbers)
	def test_that_get_summation_function_gives_the_correct_value(self):
		numbers = [1, 2, 3, 4,5]
		actual = evensumtask.get_summation(numbers)
		expected = 60
		self.assertEqual(actual, expected)



	def test_that_get_sort_numbers_exists(self):
		list_one = [3, 4, 9, 10]
		list_two = [1, 5, 7, 8]
		evensumtask.get_sort_numbers(list_one, list_two)
	def test_that_get_sort_numbers_function_gives_the_correct_value(self):
		list_one = [3, 4, 9, 10,90]
		list_two = [1, 5, 7, 8,-5]
		actual = evensumtask.get_sort_numbers(list_one, list_two)
		expected = [-5,1, 3, 4, 5, 7, 8, 9, 10,90]
		self.assertEqual(actual, expected)


	def test_that_get_firstlettercapital_exists(self):
		strings = ["apple", "banana", "cherry"]
		evensumtask.get_firstlettercapital(strings)
	def test_that_get_firstlettercapital_function_gives_the_correct_value(self):
		strings = ["apple", "banana", "cherry"]
		actual = evensumtask.get_firstlettercapital(strings)
		expected = ["Apple", "Banana", "Cherry"]
		self.assertEqual(actual, expected)



	def test_that_get_sumdigits_exists(self):
		number = 15324
		evensumtask.get_sumdigits(number)
	def test_that_get_sumdigits_function_gives_the_correct_value(self):
		number = 15324
		actual = evensumtask.get_sumdigits(number)
		expected = 15
		self.assertEqual(actual, expected)



	def test_that_get_sumodddigits_exists(self):
		number = 12345
		evensumtask.get_sumodddigits(number)
	def test_that_get_sumodddigits_function_gives_the_correct_value(self):
		number = 12345
		actual = evensumtask.get_sumodddigits(number)
		expected = 9
		self.assertEqual(actual, expected)
		


	def test_that_get_acronym_exists(self):
		word = "Portable Network Graphics"
		evensumtask.get_acronym(word)
	def test_that_get_acronym_function_gives_the_correct_value(self):
		word = "Portable Network Graphics"
		actual = evensumtask.get_acronym(word)
		expected = " PNG"
		self.assertEqual(actual, expected)



	def test_that_get_factorial_exists(self):
		number = 5
		evensumtask.get_factorial(number)
	def test_that_get_factorial_function_gives_the_correct_value(self):
		number = 5
		actual = evensumtask.get_factorial(number)
		expected = 120
		self.assertEqual(actual, expected)


