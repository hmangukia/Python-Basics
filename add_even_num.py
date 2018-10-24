# __author__ = 'Sanjay'

# ProblemStatement : Add even numbers till given limit from the user.


# function: addEvenNumbers
# param : limit(int)
def addEvenNumbers(limit):
    """
    Get's a list of even numbers up to passed limit and returns a sum
    """

    even_nums = filter(lambda num: num % 2 == 0, range(limit))
    sum = sum(even_nums)

    return sum


if __name__ == '__main__':
    userGivenInput = int(input("Enter the nth term: "))
    result = addEvenNumbers(userGivenInput)
    print(result)
