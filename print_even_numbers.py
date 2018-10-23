n = int(input('Enter the number of terms:'))

total_terms = 0
number = 0
while total_terms <= n:
    if number % 2 == 0: # % (modulo) returns the remainder after number divided by 2
        print(number)
        total_terms += 1 # x += y is shorthand for x = x + y
    number += 1
    
