rows=12
columns=20
print({2}:>6, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20) 
for i in range(2, rows + 1):
	for j in range(2,columns + 1):
		square = i * j
		print(square, end=" ")
	print() 