import math
sides = float(input('Enter the number of sides on polygon: '))
length = float(input('Enter the length of one of the sides: '))
area = (sides * length ** 2) / (4 * math.tan(3.14 / sides))
print(area)