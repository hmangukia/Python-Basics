# This program is used to remove duplicated values from a list passed by parameter

my_list = [11,10,8,9,9,9,9,8,8,11]


def remove_duplicated(list):
    return set(list)


no_duplicates = remove_duplicated(my_list)
print(no_duplicates)
