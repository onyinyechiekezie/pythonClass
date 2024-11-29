import random

def get_math_quiz():

	response = 0
	passed = 0
	failed = 0
	sign = ["+"]
	counter = 0
	correction=[]
	positive_count = 0
	negative_count = 0
	for counter in range(10):

		gen1 = random.randrange(1, 1000)
		gen2 = random.randrange(1, 1000)
		
		match counter:
			case 0:
				response =int(input(f"{gen1} + {gen2}: "))
				correct = gen1 + gen2
			case 1:
				response =int(input(f"{gen1} + {gen2}: "))
				correct = gen1 + gen2
			case 2:
				response =int(input(f"{gen1} + {gen2}: "))
				correct = gen1 + gen2
			case 3:
				response =int(input(f"{gen1} + {gen2}: "))
				correct = gen1 + gen2
			case 4:
				response =int(input(f"{gen1} + {gen2}: "))
				correct = gen1 + gen2
			case 5:
				response =int(input(f"{gen1} * {gen2}: "))
				correct = gen1 * gen2
			case 6:
				response =int(input(f"{gen1} * {gen2}: "))
				correct = gen1 * gen2
			case 7:
				response =int(input(f"{gen1} * {gen2}: "))
				correct = gen1 * gen2
			case 8:
				response =int(input(f"{gen1} - {gen2}: "))
				correct = gen1 - gen2
			case 9:
				response =int(input(f"{gen1} - {gen2}: "))
				correct = gen1 - gen2
			case _:
				print("Nothing")

		

	
		if correct == response:
			passed+=1
		else:
			failed+=1
			correction.append(f"The correct answer to question {counter + 1} is {correct}")
		counter+=1
		

	for i in correction:
		print(i)
	return (f" Your score is {passed} / 10")



print(get_math_quiz())






