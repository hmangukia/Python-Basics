__author__ = 'Sanjay'
# Description: compare two strings, get results true or false.


def compareTwoStrings(firstValue,secondValue):
        '''
        @param : firstValue, secondValie (string) as paramters
        @desc : compares two strings and prints whether it's equal or not.
        '''
        if firstValue == secondValue:
            print("both strings are equal")
        else:
            print("not equal")

if __name__ == '__main__':

    # For your practise..
    # Get list input from user and store in two variables
    # pass those two variables as parameters to compareTwoList method.

    compareTwoStrings("abcde","edcba") # not equal

    compareTwoStrings("abcde","edcba") # both strings are equal
