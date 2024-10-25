import math
latitudex1 = float(input('Enter latitude of first coordinate: '))
longitudey1 = float(input('Enter longitude of first coordinate: '))
latitudex2 = float(input('Enter latitude of second coordinate: '))
longitudey2 = float(input('Enter longitude of second coordinate: '))
radius = 6371.01
distance = radius * math.acos(math.sin(1) * math.sin(2) + math.cos(1) * math.cos(2) * math.cos(longitudey1 - longitudey2))
print(distance)

