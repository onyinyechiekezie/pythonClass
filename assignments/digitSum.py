integer=int(input('Enter integer between 0 and 1000: '))

firstDigit = (integer / 100) 
secondDigit = (integer / 10) % 10
thirdDigit = (integer % 10)
    
sum = firstDigit + secondDigit + thirdDigit

print('Sum of each digits are: ', sum)


