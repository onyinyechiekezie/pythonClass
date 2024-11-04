integer = int(input('Enter five digit integer: '))
length = len(str(integer))

if length != 5:
	print('Invalid input')
digit1=integer//10000
digit2=(integer//1000)%10
digit3=(integer//100)%10
digit4=(integer//10)%10
digit5=integer%10
	
if digit1==digit5 and digit2==digit4:
	print('Integer is a palindrome')
else:
	print('Integer is not a palindrome')
	



	
