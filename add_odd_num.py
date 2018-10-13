# This program adds odd numbers upto the number specified by the user

# description
n = int(input("Enter the nth term: "))

sum = 0
i=1
while i<=n:
   sum = sum + i
   i=i+2
print("Sum is",sum)
