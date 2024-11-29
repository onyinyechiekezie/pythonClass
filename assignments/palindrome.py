

three_digit_integer = int(input('Enter a three digit integer: '))
   


digit1 = three_digit_integer // 100

digit3 = three_digit_integer % 10
   
if digit1 == digit3: 
	print(f'{three_digit_integer} is a palindrome')
else:
	print(f'{three_digit_integer} is not a palindrome' )
