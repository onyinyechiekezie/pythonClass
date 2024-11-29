import math
number1=float(input("Enter first floating point number: "))
number2=float(input("Enter second floating point number: "))

floatingPoint1 = number1 * 1000
floatingPoint2 = number2 * 1000
floatingPoint_1 = math.round(floatingPoint1)
floatingPoint_2 = math.round(floatingPoint2)

if floatingPoint_1 == floatingPoint_2:
	print("Numbers are the same")
else:
	print("Numbers are different")
 


