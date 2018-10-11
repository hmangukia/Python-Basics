#Diamond Pattern
n=int(input("Enter max length of pattern"))

for i in range(1,n+1):
    print((n-i)*" ",end="")
    print(i*"*")
for i in range(n-1,0,-1):
    print((n-i)*" ",end="")
    print(i*"*")

#Checking if No. is a Perfect Square
n=int(input("Enter any Number"))
if(n&(n-1)!=0 and n>0 or n==0):
    print("Not a perfect square")
else:
    print("Perfect Square")
