def check_prime(number):
	if number > 1:
	   # check for factors
	   for i in range(2,number):
	       if (number % i) == 0: # % (modulo) returns the remainder after number divided by i
	           print(number,"is not a prime number")
	           print(i,"times",number//i,"is",number)
	           break
	   else:
	       print(number,"is a prime number")
	       
	# if input number is less than
	# or equal to 1, it is not prime
	else:
	   print(number,"is not a prime number")


if __name__ == "__main__":
	number = int(input("Enter a number to check:"))
	check_prime(number)