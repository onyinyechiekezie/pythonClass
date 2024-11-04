factorial = 1
eApproximate = 0
terms = int(input('Enter number of terms: '))
if terms == 0 or terms == 1:
	factorial = 1
for i in range(terms):
	eApproximate+=1/(i)factorial
print(f'Estimated value of e is {eApproximate}') 
 
