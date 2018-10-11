def main():
	list1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	orders = 0
	while(True):
		receiveOrOrder = input("Do you want to receive or give your order (R/G):").upper()
		if (receiveOrOrder == "R"):
			if (list1[0] == 0):
				print("You haven't placed your order yet.")
			else:
				print("Here's your order.", list1[0]," Thanks for visiting")
				list1, orders = myPop(list1, orders)
		else:
			orderNo = input("Enter your order: ")
			list1, orders = myPush(list1, orders, orderNo)
		print(list1)
def myPush(list1, orders, orderNo):
	for i in range(len(list1)):
		if(orders == len(list1)):
			print("The pending orders are full.")
			break
		if( list1[i] == 0):
			list1[i] = orderNo
			orders += 1
			break
		else:
			continue
	return list1, orders
def myPop(list1, orders):
	for i in range(len(list1) - 1):
		list1[i] = list1[i + 1]
	list1[-1] = 0
	orders -= 1
	return list1, orders
main()