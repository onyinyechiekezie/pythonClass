def is_odd(numbers):
	return numbers % 2 != 0
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
list(filter(is_odd, numbers))