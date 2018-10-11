__author__ = 'Sanjay'

def compareTwoList(firstList,secondList):
    '''
    @param : firstList, secondList (list) as paramters
    @desc : compares two list and prints whether it's equal or not.
    '''
    if len(firstList) == len(secondList):
        if (firstList == secondList):
            print ("Both list are identical to each other!")
        else:
            print("Not equal")
    else:
        print ("Both list are sufficient to compare.")

if __name__ == '__main__':
    # For your practise..
    # Get list input from user and store in two variables
    # pass those two variables as parameters to compareTwoList method.
    compareTwoList([1,1,1,1,3], [1,1,1,1,3]) # Both list are identical to each other!
    compareTwoList([11,1,1], [11,1,5]) #Both list are identical to each other!
    compareTwoList([1,2,3],[1,2])
