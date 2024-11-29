def get_evensum(number):

	sum = 0
	for count in number:
		if count % 2 == 0:
			sum = sum + count
	return sum


def get_vowel(letters:str):
	count = 0
	vowels = ("A", "E", "I", "O", "U")
	for vowel in vowels:
		for char in letters:
			if vowel == char.upper():
				count = count + 1
	return count


def is_palindrome(words):
	words = words.upper()
	count = 0
	for letter in words:
		if letter == words[count]:
			return True
		else:
			return False


def get_anagram(word_one, word_two):
	for char in word_one:
		if char in word_two:
			return True


def is_prime(number):
	for value in range(3, number):
		if number % value == 0:
			return False
		else:
			return True
 
	
		
def get_average(numbers):
	sum = 0
	for count in numbers:
		sum = sum + count
		average = sum / len(numbers)
	return average


def get_reverse(word:str):
	word = word.lower()
	reverse = word[: : -1]
	if reverse != word:
		return reverse



def get_summation(numbers):
	sum = 0
	for i in range(len(numbers)):
		for count in numbers:
			sum = sum + count
		sum = sum - numbers[i]
	return sum




def get_sort_numbers(list_one, list_two):
	sum = list_one + list_two
	sum.sort()
	return sum


def get_firstlettercapital(strings):
	capitalized = []
	for i in strings:
		capitalized.append(i.capitalize())
	return capitalized


def get_sumdigits(number):
	remainder = 0
	sum = 0
	while number > 0:
		remainder = number % 10
		sum = sum + remainder
		number = number // 10
	return sum


def get_sumodddigits(number):
	total = 0
	remainder = 0
	while number > 0:
		if number % 2 != 0:
			remainder = number % 10
			total = total + remainder
		number = number // 10
	return total


def get_acronym(word):
	acronym = " "
	letters = word.split()
	for count in letters:
		acronym = acronym + count[0]
	return acronym



def get_factorial(number):
	factorial = 1
	if number < 0:
		print("Number must be positive")
	elif number == 0:
		print("The factorial of 0 is 1")
	for count in range(1, number + 1):
		factorial = factorial * count				
	return factorial																														
			
	





	
	







