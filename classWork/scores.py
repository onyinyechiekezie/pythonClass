
passes = 0
failures = 0
counter = 1


for i in range(15):
	scores = int(input(f'Enter student score {i + 1}: '))
	if scores >= 45:
		passes = passes + counter
		 
	else:
		failures = 15 - passes
counter+=1
print(passes, 'students passed')
print(failures, 'students failed')		 