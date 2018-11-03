import sys

def binary_search(array, element, first, last):
    
    if (first>last):
        return -1
    
    mid = (first+last)//2

    if(element == array[mid]):
        return mid
    elif(element<array[mid]):
        last = mid - 1
    elif(element>array[mid]):
        first = mid + 1
    else:
        return -1
    
    return binary_search(array, element, first, last)

n, array, index, element = 0, [], -1, None

print("Enter the number of elements: ")
n = int(input())

if(n==0):
    print("Empty Array !!!!!")
    sys.exit(0)
if(n==1):
    print("Only one element in the array")
    sys.exit(0)
    
print("Enter the elements of the array: ")
array = input().split(' ')

if(len(array)!=n):
    print("Size of the array and the number of elements entered do not match")
    sys.exit(0)

for i in range(len(array)):
    array[i] = int(array[i])

print("Enter the element to be searched: ")
element = int(input())

index = binary_search(array, element, 0, n)
    
if(index>=0):
    print("Element found at index: "+str(index))
else:
    print("Element not found")
