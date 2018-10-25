#Prime numbers using the sieve of eratosthenes

for i in xrange(int(raw_input("Number of tests: "))):
	
	n = int(raw_input("Interger number: "))
	prime = True
	
	if n % 2 == 0 and n > 2:
		prime = False
	
	else:
		for i in xrange(3, int(n**0.5) + 1, 2):
			
			if n % i == 0:
				prime = False
				break
				
	
	if prime: print("Prime")
	else: print("Not Prime")

# author: Mateus Tranquilino - Brazil
