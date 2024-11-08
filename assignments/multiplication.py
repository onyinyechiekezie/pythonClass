rows=12
columns=20 
for i in range(2, rows + 1):
	for j in range(1,columns + 1):
		square = i * j
		print(f'{square}', end=" ")
	print() 