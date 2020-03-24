def main():
	listOf100 = [0,0,0,0,0,0,0,0,0,0]
	listOf50 = [0,0,0,0,0,0,0,0,0,0]
	listOf10 = [0,0,0,0,0,0,0,0,0,0]
	count10 = 0
	count50 = 0
	count100 = 0
	for i in range(5):
		try:
			newNote = int(input("Enter your currency: "))
			if (newNote != 10 ):
				if (newNote != 50):
					if (newNote != 100):
						raise exception
		except:
			print("Invalid Input. Enter Again.")
			continue
		else:
			action = input("Do you want to take or place money: (T/P)?").lower()
			if (action == "t"):
				if ( newNote == 10):
					listOf10, count10 = myPop(listOf10, count10)
					print(listOf10)
				if ( newNote == 50):
					listOf50, count50 = myPop(listOf50, count50)
					print(listOf50)
				if ( newNote == 100):
					listOf100, count100 = myPop(listOf100, count100)
					print(listOf100)
			if (action == "p"):
				if ( newNote == 10):
					listOf10, count10 = myPush(listOf10, count10, newNote)
					print(listOf10)
				if ( newNote == 50):
					listOf50, count50 = myPush(listOf50, count50, newNote)
					print(listOf50)
				if ( newNote == 100):
					listOf100, count100 = myPush(listOf100, count100, newNote)
					print(listOf100)
def myPop(list, count):
	for i in range(len(list) - 1):
		if (list[0] == 0):
			print("Stack is empty.")
			break
		else:
			list[i] = list[i + 1]
			count -= 1
	list[-1] = 0
	
	return list, count

def myPush(list, count, newNote):
	for i in range(len(list)):
		if(count == len(list)):
			print("The stack is full.")
			break
		if( list[i] == 0):
			list[i] = newNote
			count += 1
			break
		else:
			continue
	return list, count
main()
	
