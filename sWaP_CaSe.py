#This program will convert uppercase letters of a string to lowercase and vice versa.
def swap():
    string1 = input("Enter a string with a random sequence of small and capital letters : ")
    print(" ")   #To leave a blank line.
    string2 = ""
    
    if(string1.isalpha() == True):  #To check if given string contains alphabets only.
        for i in string1:
            k = i
            l = i.upper()
            if (k != l):
                string2 = string2 + str(l)
            else:
                string2 = string2 + str(k.lower())
        print("After swapping: " ,string2)
    else:
        print("Enter alphabets only.")
        swap()
    print("")
    z = input("Enter Y to run again and any key to quit.")
    if (z.upper() == 'Y'):
        print("")
        swap()
    else:
        pass
swap()
