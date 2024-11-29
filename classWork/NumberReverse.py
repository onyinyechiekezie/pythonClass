number = int(input("Enter number between 100 to 999:"))
first_digit = (number // 100)
second_digit = (number // 10) % 10
third_digit = (number % 10)
even_counter = 0
odd_counter = 0
print(third_digit,second_digit,first_digit)
if(third_digit % 2 == 0): even_counter+=1
else: odd_counter+=1
if(second_digit % 2 == 0): even_counter+=1
else: odd_counter+=1
if(first_digit % 2 == 0): even_counter+=1
else: odd_counter+=1
print("Number of even numbers:", even_counter)
print("Number of odd numbers:", odd_counter)
 