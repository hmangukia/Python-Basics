def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j >= 1 and a[j-1] > a[j]:  
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
        print("i = {}, {}".format(i, a))
    return(v)
