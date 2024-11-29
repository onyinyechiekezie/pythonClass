number = int(input('Enter a number: '))
for rows in range(1, number + 1):
	for column in range(1, rows + 1):
		print(column, end=' ')
	print()
for rows in range(1, number + 1):
	for column in range(1, (number + 1) - rows):
		print(column, end=' ')
	print()






