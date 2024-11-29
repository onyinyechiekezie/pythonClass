rows = int(input("Give me number of rows: "))
for i in range(0, rows):
	for j in range(0, rows -i):
		print(" ", end=" ")
	for j in range(0, i ):
		print("ABC", end=" ")
	print()
for i in range(0, rows):
	for j in range(0, rows -2):
		print(" ",end=" ")
	for j in range(0, i):
		print("ABC", end=" ")
	print()	  