__author__ = 'Sanjay'
# /*
# You are given two integers. Store them into two variables and then exchange them. Rather than using any fancy logic, make sure to use a tuple to do the task. Print the two numbers.

# Sample Input

# 2
# 1
# Sample Output

# 1
# 2
# Here's the implementation..

a = int(raw_input())
b = int(raw_input())

print(a, "is assinged to variable A and ", b, " is assigned to variable B" )
a, b = b, a
print ("After swappting the variable values, the result is")
print ("Variable A contains ", a)
print ("Variable B contains ", b)
