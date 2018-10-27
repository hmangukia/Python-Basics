#A program to print n number of even numbers, taking input to n

n = int(input('Enter the number of terms:')) #taking input

total_terms = 0                     #to check the no. of even numbers printed
number = 0
while total_terms <= n:             #checking if no. of printed numbers is still less than n
    if number % 2 == 0:             #checking if the number is an even number
        print(number)
        total_terms += 1
    number += 1
    
