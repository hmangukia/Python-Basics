
# The program takes the elements of the list one by one and displays the average
# of the elements of the list.

# Problem Statment : User will give list of numbers as input, we will calcuate the Sum and Average

def giveMeSum(listOfNumbers):
    '''
    @method : giveMeSum
    @param : listOfNumbers(list)
    @desc : sum() is a predefined method in python, returns sum of integers
    '''
    return sum(listOfNumbers)

def giveMeAverage(listOfNumbers):
    '''
    @method : giveMeSum
    @param : listOfNumbers(list)
    @desc : sum() and len() is a predefined method in python, returns sum of
            integers and returns array length
    '''
    return (sum(listOfNumbers)/len(listOfNumbers))

if __name__ : '__main__':
    totalInputs=int(input("How many number inputs you wanna average?"))
    listOfIntegers = []
    for item in range(0, totalInputs):
        element=int(input("Enter element: "))
        listOfIntegers.append(element)

    calculatedSum = giveMeSum(listOfIntegers) #calling above Methods
    calcaulatedAverage = giveMeAverage(listOfIntegers) #calling above Methods

    print ("Total number of given inputs: ", totalInputs)
    print ("Sum of all given numbers is ", calculatedSum )
    print ("Therefore the average is ", calcaulatedAverage)
