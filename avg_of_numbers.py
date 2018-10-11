#The program takes the elements of the list one by one and displays the average of the elements of the list.

n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    element=int(input("Enter element: "))
    a.append(element) #append() method takes a single item and adds it to end of list
avg=sum(a)/n
print("Average of elements in the list : ",round(avg,2))
