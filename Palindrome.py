Input = input('Enter a string (quoted String) : ')
Reverse = Input[::-1] # [::-1] makes a copy of the same list in reverse order
if(Input.lower() == Reverse.lower()): # lower() returns a copy of the string with all lowercase
    print('String is Palindrome')
else:
    print('String is not Palindrome')
