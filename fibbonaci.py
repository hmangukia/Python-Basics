#This program prints fibbonaci series 
#fibbonaci series is a series in which next term is sum of previous 2 terms
num = int(input("Enter the number to which you want the fibbonaci series to be calculated upto: "))

temp1 = 0
temp2 = 1
answer = 0
print(temp1)
print(temp2)
for i in range(num):
	answer = temp1 + temp2
	print(answer)
	temp1 = temp2
	temp2 = answer
