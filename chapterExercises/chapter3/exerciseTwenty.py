decimal = 0
power = 0
binary = int(input("Enter a binary integer: "))
while binary > 0:

	digit = binary % 10
	power = power + 1
	decimal = decimal + digit *(2 ** power)
	binary = binary // 10
	finalDecimal = decimal / 4
	print(f"{decimal}")
