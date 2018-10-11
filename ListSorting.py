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
    sortingList([13,43431,54651,17676,37667886])
