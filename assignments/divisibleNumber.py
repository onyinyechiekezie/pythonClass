range = int(input('Enter start of range (): '))
rangeEnd = int(input('Enter end of range (): '))
divisor = int(input('Enter divisor (): '))

if rangeStart <= rangeEnd and divisor != 0:

count = 0
for i in range(rangeStart, rangeEnd + 1):
if i % divisor != 0
	count +=1
print(f"Count of numbers between {rangeStart} and {rangeEnd} divisible by {divisor}: {count}
print("Invalid input 