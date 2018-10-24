#__author__ = "Sanjay"

def validateEvenOrOddInput(num):
    '''
    @param : num (int)
    @desc: returns given input is odd or even
    '''

    if isinstance(num, int):
        if(num % 2==0):
            print('{} is an even number'.format(num))
        else:
            print('{} is an odd number'.format(num))

if __name__ == '__main__':
    userInput = int(input('Input your number: '))

    if isinstance(userInput, int):
        validateEvenOrOddInput(userInput)
    else:
        print ("Given input is not valid.")
