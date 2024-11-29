principalAmount=float(input('Enter principal amount:'))
annualInterestRate=float(input('Enter annual interest rate:'))
duration=float(input('Enter duration of mortgage in years:'))

monthlyInterest=(annualInterestRate/100)/12
numberOfPayments=duration*12
monthlyPayment=principalAmount*monthlyInterest*(1+monthlyInterest)**numberOfPayments/((1+monthlyInterest)**numberOfPayments-1)

print('Your monthly payment is', monthlyPayment)

