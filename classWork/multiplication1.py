
userInput=int(input('Enter a number: '))

for i in range(1,13,1):
	product = userInput * i
	print(f'{userInput} * {i} = {product}')
