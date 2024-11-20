def get_divide_or_square(number):
	import math
	if number % 5 == 0:
		result = math.sqrt(number)
		result = round(result, 2)
		return result
	elif number % 5 != 0:
		remainder = number % 5
		return remainder
	if number < 0:
		return(TypeError)
	
	if number == 0:
		return(TypeError)
	if number == " ":
		return(TypeError)


def get_futureinvestment(futureinvestment):
	import math
	futureinvestment = investment_amount * (1 * monthly_interest)**12
	return futureinvestment
	



	



