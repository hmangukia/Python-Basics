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

def capitalizeAndGiveMe(userGivenInput):
    '''
    @param: userGivenInput(string)
    @desc: method will return capitalized string.
    '''
    splittedInput = userGivenInput.split(" ")
    output =  ''
    for i in splittedInput:
        output = output + i.capitalize()
    return output

if __name__ == '__main__':
    userInput = str(intput())
    if userInput != '':
        capitalizedString = capitalizeAndGiveMe(userInput)
        print (capitalizedString)
