factorial=1
integer=int(input('Enter an integer: '))
if integer < 0:
	print('Invalid input. Integer must be positive')
if integer == 0 or integer == 1:
	factorial = 1
	print('Factorial of', integer, 'is', factorial)
if integer > 0 or integer > 1:
	for i in range(2, integer + 1):
		factorial= factorial * i
	print('Factorial of', integer, 'is', factorial)
	

