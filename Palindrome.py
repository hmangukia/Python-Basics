Input = input('Enter a string (quoted String) : ')
Reverse = Input[::-1]
if(Input.lower() == Reverse.lower()):
    print('String is Palindrome')
else:
    print('String is not Palindrome')
