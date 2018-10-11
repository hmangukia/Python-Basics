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

def capitalizeAndGiveMe(userGiveInput):
    l = userInput.split(" ")

    for i in l:
        print (i.capitalize())

if __name__ == '__main__':
    userInput = str(intput())
    if userInput != '':
        capitalizeAndGiveMe(userInput)
