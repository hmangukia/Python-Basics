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
    
print("Enter the elements of the array: ")
array = input().split(' ')

for i in range(len(array)):
    array[i] = int(array[i])

print("Enter the element to be searched: ")
element = int(input())

index = binary_search(array, element, 0, n)
    
if(index>=0):
    print("Element found at index: "+str(index))
else:
    print("Element not found")
