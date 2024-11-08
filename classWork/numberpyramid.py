number = int(input('Enter a number: '))

for row in range(1, number, 1):
	for column in range(number, 0, -1):
		print(*list(range(column , number)))














