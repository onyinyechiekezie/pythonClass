negativeCounter = 0
positiveCounter = 0
zeroCounter = 0
numberCounter = 0

while(numberCounter <= 4):
  number= int(input("Enter five numbers:"))
 
  if(number < 0):
    negativeCounter += 1

  elif(number > 0):
    positiveCounter +=1

  elif(number == 0):
    zeroCounter += 1
 

  numberCounter += 1	

print('Negative numbers are', negativeCounter)
print('Positive numbers are', positiveCounter)
print('Zero numbers are', zeroCounter)

 

