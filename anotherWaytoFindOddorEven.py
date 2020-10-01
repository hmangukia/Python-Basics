def validateEvenOrOddInput(num):  
	if(num & 1 == 0): # & (logical and) returns the 0 if num is even
		print('{} is an even number'.format(num))
	else:
		print('{} is an odd number'.format(num))	


if __name__ == '__main__':
	num = int(input('Input your number: ')) 
	validateEvenOrOddInput(num) 
