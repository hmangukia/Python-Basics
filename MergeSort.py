__author__ = 'Sanjay'

# merge sort (also commonly spelled mergesort) is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output. Merge sort is a divide and conquer algorithm

def mergeSort(alist):
    '''
    @param: alist(list)
    @desc: splits the list into multiple halfs, and finds the small one comparing 2 elements
    '''
    if len(alist)>1:
        mid = len(alist)//2 #python 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i,j,k=0,0,0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

if __name__ == '__main__':

    input_string = input("Enter list elements separated by space ")
    inputElements = [int(i) for i in input_string.split(" ")]
    mergeSort(inputElements)
