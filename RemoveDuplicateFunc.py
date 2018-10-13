# This program is used to remove duplicated values from a list passed by parameter

def compare(list):
    newList = []
    for x in list:
        if x not in newList:
            newList.append(x)
    return newList

#Another Simple Solution
def removeDuplicates(inputHasDuplicates):
    uniqueOutput = list(set(inputHasDuplicates))
    return uniqueOutput


if __name__ = '__main__':
    userInput = [11,10,8,9,9,9,9,8,8,11]

    veryGoodSolution = removeDuplicates(userInput)
    print ("After removing duplicates, the output is ", veryGoodSolution)
