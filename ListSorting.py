__author__ = 'Sanjay'


def sortingList(firstList):
    '''
    @param: firstList(list) as parameter
    @desc: give me a integers in a list, I will give you sorted list.
    '''
    if (len(firstList)) != 0:
        return firstList.sort()
    else:
        print("There's no elements to sort")

if __name__ == '__main__':
    # For your practise..
    # Get list input from user
    
    input_string = input("Enter list elements separated by space ")
    inputElements = [int(i) for i in input_string.split(" ")]
    
    output = sortingList(inputElements)
    print ("After soring, the output is.." , output)
