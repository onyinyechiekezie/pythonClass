rows = 6
for number in range(1, rows + 1):
	for space in range(1, (rows + 1) - number):
		print('*', end=' ')
	print()