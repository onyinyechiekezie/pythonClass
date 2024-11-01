date = int(input("Enter a date to return book: "))
if date <=5:
	print("Fine is 50 paise")
elif date <=10:
	print("Fine is one rupee")
elif date <=30:
	print("Fine is 5 rupees")
elif date >30:
	print("Your membership has been cancelled")

