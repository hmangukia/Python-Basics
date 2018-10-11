n = int(input('Enter the number of terms:'))

total_terms = 0
number = 0
while total_terms <= n:
    if number % 2 == 0:
        print(number)
        total_terms += 1
    number += 1
    
