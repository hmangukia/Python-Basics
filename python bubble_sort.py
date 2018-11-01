"""
This is pure python implementation of bubble sort algorithm
For doctests run following command:
python -m doctest -v bubble_sort.py
or
python3 -m doctest -v bubble_sort.py
For manual testing run:
python bubble_sort.py
"""

from __future__ import print_function


def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([])
    []
    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection) # len() returns the number of items in the array
    for i in range(length): # range() returns an array with the numbers from 0 to the specified number
        swapped = False
        for j in range(length-1):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped: break  # Stop iteration if the collection is sorted.
    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip() # strip() returns a copy of the string in which all chars have been stripped from the beginning and the end of the string
    unsorted = [int(item) for item in user_input.split(',')] # split() splits a string into a list. In this case split by ,
    print(bubble_sort(unsorted))
