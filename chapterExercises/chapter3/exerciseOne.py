 
passes = 0 
failures = 0 

for student in range(10):

    result = int(input('Enter result (1=pass, 2=fail): '))

    if result == 1:
       passes = passes + 1
    elif result == 2:
       failures = 10 - passes
    if result != 1 or result != 2:
       print("Wrong input. Please enter 1 for pass or 2 for fail")
    else:
       break

print(f"Passes:{passes}")
print(f"Failures:{failures}")
 
 
 
