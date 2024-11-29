def is_Even(integer):
	for value in range(2, integer):
		if integer % 2 == 0:
			return True
		else:
			return False
	if integer == 0:
		return(TypeError)


def is_prime(number):
	for value in range(3, number):
		if number % value == 0:
			return False
		else:
			return True



def get_difference(integer1, integer2):
	if integer1 > integer2:
		difference = integer1 - integer2
	else:
		difference = integer2 -integer1
	return difference



def get_quotient(integer1, integer2):
	if integer2 > 0:
		quotient = integer1 / integer2
	elif integer2 == 0:
		quotient == 0
	return quotient