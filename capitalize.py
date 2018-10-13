"""This file contains a simple way to capitalize in python"""

# Simpe string that you want to capitalize
str_to_cap = "what a wonderfull hacking day!"

# there is a list comprehension iterating over the splitted string to capitalize it
capitalized_str = " ".join([w.capitalize() for w in str_to_cap.split(' ')])

# An alternative to line above for a better understand:
cap_words = []
for word in str_to_cap.split(' '):
    cap_words.append(word.capitalize())

capitalized_str_alt = " ".join(cap_words)

print('Using list comprehension: {}'.format(capitalized_str))
print('Using simple for iteration: {}'.format(capitalized_str_alt))
