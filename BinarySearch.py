def binary_search(l, low, high, item):
    # check the base case
    if high >= low:
        mid = (high + low) // 2
        # if element present at middle
        if l[mid] == item:
            return mid
        # if element is smaller than mid
        elif l[mid]>item:
            return binary_search(l,low,mid-1, item)
        # if element is larger than mid
        else:
            return binary_search(l, mid+1, high, item)
    else:
        # element is not preset in list
        return -1


# take a list
n = int(input('enter no of element: '))
print('enter elements: ')
l = []
for i in range(0, n):
    ele = int(input())
    l.append(ele)
item = int(input('enter element to be search: '))
result = binary_search(l, 0, len(l)-1, item)
if result!= -1:
    print('Element is preset at index', str(result))
else:
    print('Element is not present in the list')