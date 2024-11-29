pounds = float(input('Enter weight in pounds: '))
inches = float(input('Enter height in inches: '))
kilograms = pounds * 0.45359237
meters = inches * 0.0254
bodyMassIndex = kilograms / (meters * meters)
print(bodyMassIndex)