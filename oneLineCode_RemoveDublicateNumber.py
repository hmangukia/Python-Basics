# This program is used to remove duplicated values from a list passed by parameter
l = [11,10,8,9,9,9,9,8,8,11]  #given list

def compare(list):           #function to remove duplicates
    ans = list(set(list))    # In this line first we convert list into set which contains unique element and then again we convert it into list
    return ans

x = compare(l)
print(x)
