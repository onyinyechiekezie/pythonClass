number1 = int(input("Give me a number: "))
number2 = int(input("Give me a number: "))
number3 = int(input("Give me a number: "))

if(number1 < number2 and number2 < number3): 
	print("Numbers are in ascending order") 

elif(number3 < number2 and number2 < number1):
	print("Numbers are in descending order")

else:
	print("Numbers are not in order")