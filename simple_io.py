"""This file contains a simple IO Script for Python"""

import os

# A nice way to reach files is using the path pattern that will adapt for any OS
current_folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_folder, 'README.md')
output_file = os.path.join(current_folder, 'OUTPUT.txt')

# Use with open to open and close automaticaly and avoid some IO errors.
# 'r' tag will allow you to read from file, 
with open(input_file, 'r') as input_stream:
    plain_text = input_stream.read()
    lines = input_stream.readlines()
    first_line = input_stream.readline()

# Use with open to open and close automaticaly and avoid some IO errors.
# 'w' tag will allow you to write to file, but with a '+' it will create a file if it doesn't exist.
with open(output_file, 'w+') as output_stream:
    output_stream.write('Data to write to file!')

