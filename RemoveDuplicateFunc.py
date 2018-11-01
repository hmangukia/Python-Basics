# This program is used to remove duplicated values from a list passed by parameter
l = [11,10,8,9,9,9,9,8,8,11]  #given list

def compare(list):           #function to remove duplicates
    newList = []             #created new list
    for x in list:
        if x not in newList:
            newList.append(x) # append() appends an element to the end of the list
    return newList

x = compare(l)
print(x)