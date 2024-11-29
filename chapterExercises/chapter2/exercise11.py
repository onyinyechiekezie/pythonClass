number=int(input('Enter a five digit number: '))
fiveDigits=int(number/10000)%10, int(number/1000)%10, int(number/100)%10, int(number/10)%10, number%10
print(fiveDigits,end="   ") 