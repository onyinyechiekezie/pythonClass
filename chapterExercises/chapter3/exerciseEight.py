sum=0
average=0
product=1
largest=0
smallest=0

for i in range(4):
	integer=int(input(f'Enter an integer{i+1}: '))
	sum=sum + integer
	average=sum/4
	product=product * integer
	if integer > largest:
		largest = integer
	else:
		smallest = integer
print('Sum is:', sum)
print('Average is:', average)
print('Product is:', product)
print('Smallest is:', smallest)
print('Largest is:', largest)
	
	 