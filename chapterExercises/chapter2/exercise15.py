number1=float(input('Enter a decimal number: '))
number2=float(input('Enter a decimal number: '))
number3=float(input('Enter a decimal number: '))

small=number1
if number2<small:
	small=number2

if number3<small:
	small=number3
 
secondLargest=number2

if number1<secondLargest:
	secondLargest=number2

if number3>secondLargest:
	secondLargest=number3

largest=number3

if number2>largest:
	largest=number2

if number1>largest:
	largest=number1

print(small, secondLargest, largest) 








