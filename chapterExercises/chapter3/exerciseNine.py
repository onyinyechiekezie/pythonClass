integer = int(input('Enter a five digit integer: '))
while integer > 0:
	digit=integer % 10
	integer=integer//10
	print(digit, end="")
		
	 
