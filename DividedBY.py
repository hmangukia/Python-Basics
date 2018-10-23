#In this code lines, you can insert a number and know what numbers are divided by him
number = int(input("Write a number "))
div = []
for i in range(1,number+1):
    
    if ((number % i) == 0): # % (modulo) returns the remainder after number divided by i
        div.append(i) # append() appends an element to the end of the list