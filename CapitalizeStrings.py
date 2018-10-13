__author__ = 'Sanjay'

# You are given a string SS. Your task is to capitalize each word of SS.
#
# Input Format
#
# A single line of input containing the string, SS.
# Output Format
#
# Print the capitalized string, SS.
#
# Sample Input
#
# hello world
# Sample Output
#
# Hello World

def capitalizeStrings(userGivenInput):
    '''
    @param: userGivenInput(string)
    @desc: method will return capitalized string.
    '''
    userInputList = userGivenInput.split(" ")
    output =  ''
    for i in userInputList:
        output = output + i.capitalize()
    return output

if __name__ == '__main__':
    userInput = str(intput())
    if userInput != '':
        capitalizedString = capitalizeStrings(userInput)
        print (capitalizedString)
