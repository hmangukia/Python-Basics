__author__ = 'Sanjay'

# Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

def insertionSort(alist):
    '''
    @param: alist(list) as parameter
    @desc : will return sorted list of integers.
    '''
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

if __name__ == '__ main__':

    alist = [54,26,93,17,77,31,44,55,20]
    insertionSort(alist)
    print(alist)
