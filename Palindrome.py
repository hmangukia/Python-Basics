

def checkPalindrome(userGivenInput):
    '''
    @param: userGivenInput(string)
    @desc: converting userGivenInput as lowercase and compares with reverse of that string.
    '''
    if(userGivenInput.lower() == userGivenInput[::-1].lower()):
        print('String is Palindrome')
    else:
        print('String is not Palindrome')

if __name__ = '__main__':
    userInput = str(input('Enter a string :' ))
    if userInput !='':
        checkPalindrome(userInput);
    else:
        print("There's nothing to reverse and check Palindrome here.")
