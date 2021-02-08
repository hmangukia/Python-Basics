def descending(l):
    if len(l) <= 1 or (len(l) == 2 and l[0] >= l[1]):
        return True
    else:
        if l[0] >= l[1]:
            return descending(l[1::])
        else:
            return False
print(descending([]))
print(descending([4,4,3]))
print(descending([19,17,18,7]))