def get_even_odd(numbers):
	list = []
	odd = 0
	even = 0
	for number in numbers:
		if number % 2 != 0:
			odd+=1
			list.append(odd)
		if number % 2 == 0:
			even+=1
			list.append(even)
	return list

def get_even_odd(numbers):
	return[

def check():
	number = [1,2,3,6,8,10,1]
	odd = [val for val in number if val % 2 != 0 ]
	even = [get for get in number if get % 2 == 0]
	print(f"[{len(odd)},{len(even)}]")

	input = [5,3,7,9,2,8]
	odd_number = [num for num in input if num % 2 !=0 ]
	even_number = [value for value in input if value % 2 == 0 ]
	print(f"[{len(odd_number)},{len(even_number)}]")

check()