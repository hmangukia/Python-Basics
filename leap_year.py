def enterYear():
	year = input("Enter the year: ")
	errorOrNot(year)
def errorOrNot(year):
	try:
		year = int(year)
	except Exception as e:
		print("You entered an invalid year.")
		print(e)
	else:
		leapOrNot(year)
def leapOrNot(year):
	if (year % 4 == 0):
		print("This year is a leap year.")
	else:
		print("This year is not a leap year")
enterYear()

