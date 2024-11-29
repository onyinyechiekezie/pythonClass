negativeCounter = 0
positiveCounter = 0
zeroCounter = 0
numberCounter = 1

while(numberCounter <=4):
	print('Enter five numbers: ')
 
	if(number < 0): 
 		negativeCounter +=1

	elif(number > 0):
 		positiveCounter +=1

	else:
 		zeroCounter +=1

 	numberCounter +=1

print('Negative numbers are', negativeCounter)
print('Positive numbers are %d%n', positiveCounter)
print('Zero numbers are', zeroCounter)


