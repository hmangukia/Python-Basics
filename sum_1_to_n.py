#ALGORITHMS IS LIFE
print ("pls, please give two numbers separated by a space, a, b (a <= b)")
first_number, second_number = map(int, input().split())

#used (a *(a +1)/2) - (b *(b + 1)/2)
sum_total = (second_number*(second_number + 1))/2 - ((first_number-1)*(first_number ))/2

print (int(sum_total))
