def get_largest(numbers:list):
	largest = numbers[0]
	for number in numbers:
		if number > largest:
			largest = number
	return largest
	


def get_reverse(numbers:list):
	for number in numbers:
		reverse = numbers[: : -1]
	if reverse != numbers:
		return reverse


def get_numberexistence(numbers:list, number:int):
	value = number
	for index in numbers:
		if value == number: 
			return True
		
		return False


def get_oddpositions(numbers:list):
	list = []
	for index in range (len(numbers)):
		if index % 2 != 0:
			list.append(numbers[index])
	return list




def get_evenpositions(numbers:list):
	list = []
	for index in range (2, len(numbers)):
		if index % 2 == 0:
			list.append(numbers[index])
	return list


def get_total(numbers:list):
	total = 0
	for count in numbers:
		total = total + count
	return total


def is_palindrome(words):
	words = words.upper()
	count = 0
	for letter in words:
		if letter == words:
			return True
		else:
			return False


