__author__ = 'Sanjay'

def compareTwoList(firstList,secondList):
    if (len(firstList)) != 0:
        return firstList.sort()
    else:
        print("There's no elements to sort")

if __name__ == '__main__':
    # For your practise..
    # Get list input from user
    compareTwoList([13,43431,54651,17676,37667886])
