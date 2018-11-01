print("Enter number of elements")
N=int(input())
print("Enter array")
A=input().split(' ')
for i in range(0,N):
	mini=A[i]
	ind=i
	for j in range(i,N):
		if A[j]<mini:
			mini=A[j]
			ind=j
	tmp=A[i]
	A[i]=A[ind]
	A[ind]=tmp
print(A)
