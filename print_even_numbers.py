#A program to print n number of even numbers, taking input to n

n = int(input('Enter the number of terms:')) #taking input

total_terms = 0                     #to check the no. of even numbers printed
number = 0

while total_terms <= n:             #checking if no. of printed numbers is still less than n
    if number % 2 == 0: # % (modulo) returns the remainder after number divided by 2
        print(number)
        total_terms += 1 # x += y is shorthand for x = x + y
    number += 1
    
