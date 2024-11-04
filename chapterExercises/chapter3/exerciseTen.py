principal=1000
annualRate=7/100

for i in range(0,30,10):
	years=int(input(f'Enter amount invested up to year{i+10}: '))

year10= principal*(1+0.07)**10
year20= principal*(1+0.07)**20
year30= principal*(1+0.07)**30

print('Investment return after 10 years is ', year10)
print('Investment return after 20 years is ', year20)
print('Investment return after 30 years is ', year30)

