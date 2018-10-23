# __author__ = 'Sanjay'

# ProblemStatement : Add even numbers till given limit from the user.


# method: addEvenNumbers
# param : limit(int)
# desc : iterate the limit, for each iteration check conditiom, if true, then add with sum.
def addEvenNumbers(limit):
    sum = 0
    for item in range(limit):
      if item%2 == 0:
        sum = sum + item

    print("Sum is",sum)


if __name__ == '__main__':
    userGivenInput = int(input("Enter the nth term: "))
    addEvenNumbers(userGivenInput)
