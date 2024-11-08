userInput = int(input("Enter a number: "))
remainder = 0
userInput = 0

while userInput > 0:
	remainder = userInput % 10
	sum = sum + remainder
	userInput = userInput // 10
	print(sum)
