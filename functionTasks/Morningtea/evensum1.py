def get_evensum1(number):

	sum = 0
	for count in number:
		if count % 2 == 0:
			sum = sum + count
	return sum


def get_primenumbers(number):
	numbers = []
	for count in range(2, number):
		if number % count == 0:
			numbers.append(count)
			return numbers


"""def get_list(number):
	numbers = []
	for i in number:
		numbers.append(i)
	return numbers
number = 5
print(get_list(number))"""



"""def get_list():
	return[i for i in range(1, 6)]
print(get_list())"""


"""def get_list():
	return(sum([i for i in range(1, 6)]))
print(get_list())"""


"""def get_total(list:):
	total = 0
	for i in list:
		total = total + i
	return total
list = [1, 2, 3, 4, 5]
print(get_total(list))"""


"""def get_evencount(numbers):
	even = 0
	for count in numbers:
		if count % 2 == 0:
			even+=1
	return even"""


def get_evencount(value):
	return len([x for x in value if x % 2 == 0])


"""def get_boolean_value(numbers):
	boolean_result = []
	for count in numbers:
		if count % 2 == 0:
			boolean_result.append(True)
			return boolean_result
		else:
			boolean_result.append(False) 
			return boolean result(doesn't exactly work)"""


def get_boolean_value(numbers):
	return[True if x % 2 == 0 else False for x in numbers]


"""def get_firstlettercapitalized(strings):
	capitalized = []
	for i in strings:
		capitalized.append(i.capitalize())
	return capitalized"""

def get_firstlettercapitalized(strings):
	return[word.title() for word in strings]


def get_multiples_of_3(numbers):
	multiples = []
	for count in range(3, 31, 3):
			multiples.append(count)
	return multiples

"""def get_multiples_of_3(numbers):
	return[x for x in range(3, 31, 3)]"""


"""def get_odd_squared(numbers):
	odd_square = []
	for i in numbers:
		if i % 2 != 0:
					
				odd_square.append(i)
	return odd_square"""


"""def get_odd_squared(numbers):
	return[i*i for i in numbers if i % 2 != 0]"""


def get_square(value):
	return[i * i for i in range(1, value + 1)]


def get_greaterthan10(values):
	return[i for i in values if i > 10]



def is_palindrome(strings):
	return[word == word[::-1] for word in strings]


def get_numbers_only(string_values):
	return[int(i) for i in string_values if i.isdigit()]


def get_double(value):
	return[i * 2 for i in value]


def get_five_words(strings):
	return[i for i in strings if len(i) >= 5]


def get_digit_addition(value):
	return(sum(int(i) for i in str(value)))	


def get_vowels(strings):
	return[i for i in len(strings) ]


"""Not working yet as a function def get_evensquared(value):
	squared = {x:x**2 for x in range(1,10) if x % 2 == 0}
print(get_evensquared(value))"""



def get_zip_list(keys, values):
	my_dict = {}
	for key,values in zip(keys,values):
		my_dict[key] = values
	return my_dict

 


			

	


		
		
	
	
	
	
	
		
		
 
