largest1=0
largest2 = 0
for i in range(10):
	numbers=int(input(f'Enter number {i+ 1}: '))
if numbers > largest1:
	largest1 = numbers
if largest2 < largest1 and largest2 > numbers:
	numbers = largest2
print(f'Two largest numbers are {largest1} and {largest2}')