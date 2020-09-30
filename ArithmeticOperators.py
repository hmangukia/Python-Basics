__author__ = 'Sanjay'
# Let's learn about Python's arithmetic operators.
#
# First, let's read two integers:
#
# a = int(raw_input())
# b = int(raw_input())
# The three basic arithmetic operators are the following:
#
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division
# Integer Division
# Modulo Division
# Exponent

# Task
# Read two integers from STDIN and print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# The fourt line contains the division of the two numbers.
# The fifth line contains the integer divisio of the two numbers.
# The sixth line contains the modulo sivision of the two numbers.
# The seventh line contains the first to the power of second numbers.
# Input Format
# The first line contains the first integer, numberA. The second line contains the second integer, numberB.
#
#
# Output Format
# Print the three lines as explained above.
#
# Sample Input
#
# 3
# 2
# Sample Output
#
# 5
# 1
# 6
# 1.5
# 1
# 1
# 9
# Explanation
# 3+2
# 3-2
# 3*2
# 3/2
# 3//2
# 3%2
# 3^2 or 3**2

# Enter your code here. Read input from STDIN. Print output to STDOUT
numberA = int(raw_input())
numberB = int(raw_input())

print (numberA+numberB)
print (numberA-numberB)
print (numberA*numberB)
print (numberA/numberB)
print (numberA//numberB)
print (numberA%numberB)
print (numberA**numberB)
