#__author__ = "Sanjay"

def validateEvenOrOddInput(num):  #Defining a function to check odd or even
	'''
	@param : num (int)
	@desc: returns given input is odd or even
	'''
	
	if(num % 2==0):          #checking if num is divisible by 2
		print('{} is an even number'.format(num))
	else:
		print('{} is an odd number'.format(num))	

if __name__ == '__main__':
	userInput = int(input('Input your number: ')) 
	if (type(num) == 'int'):    #checking if num is an integer
		validateEvenOrOddInput(userInput)  
	else:
		print ("Given input is not valid.")