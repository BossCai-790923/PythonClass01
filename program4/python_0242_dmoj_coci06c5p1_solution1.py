'''
https://dmoj.ca/problem/coci06c5p1
'''

import sys

# Step 1) Read data from question
everything_from_input = sys.stdin.read()
all_lines = everything_from_input.split('\n')
first_line = all_lines[0]

# Step 2) define 3 variables
a, b, c = 1, 0, 0

# Step 3) Mimic the process
for switch_type in first_line:
    if switch_type == 'A':
        a, b = b, a
    if switch_type == 'B':
        b, c = c, b
    if switch_type == 'C':
        a, c = c, a

# Step 4) print the result
if a == 1:
    print('1')
if b == 1:
    print('2')
if c == 1:
    print('3')

