#ALGORITHMS IS LIFE
first_number, second_number = map(int, raw_input().split())

#used (a *(a +1)/2) - (b *(b + 1)/2)
sum_total = (second_number*(second_number + 1))/2 - ((first_number-1)*(first_number ))/2

print sum_total
