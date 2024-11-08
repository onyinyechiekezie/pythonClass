number = input("Enter number: ")
counter=0
for count in number:
	if int(count) >= 5:
		counter = counter + 1  
print(counter)