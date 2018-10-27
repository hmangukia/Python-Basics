# Prime numbers Python 3 implemantation

for i in range(int(input("Number of tests: "))):
	
	n = int(input("Insert a positive interger number: "))
	prime = True
	
	# Any even number diferrent of 2, is not prime 
	if n % 2 == 0 and n != 2:
		prime = False
	
	# 1 is not prime
	elif n < 2:
		prime = False
		
	else:
		for i in range(3, int(n**0.5) + 1, 2):
			
			if n % i == 0:
				prime = False
				break
				
	
	if prime: print("%d is Prime" % n)
	else: print("%d is not Prime" % n)
	
	# Breakline
	print()

# author: Mateus Tranquilino - Brazil
