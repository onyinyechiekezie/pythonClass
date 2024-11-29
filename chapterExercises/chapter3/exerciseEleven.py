gallons=0
miles=0
sentinel=-1
totalGallons=0
totalMiles=0
while gallons != sentinel or miles != sentinel: 
	gallons=float(input('Enter the gallons used (-1 to end): '))
	if gallons == sentinel:
		break
	if gallons < 0:
		print('Invalid input')
	miles=float(input('Enter miles driven (-1 to end): '))
	if miles == sentinel:
		break
	if miles < 0:
		print('Invalid input')

	milesPerGallon=miles/gallons
	print('The miles/gallon for this tank was', milesPerGallon)
totalGallons=totalGallons + gallons   
totalMiles=totalMiles + miles
total = totalMiles / totalGallons
print('The overall average miles per gallon was', total)   

