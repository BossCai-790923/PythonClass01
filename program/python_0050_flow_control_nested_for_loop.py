'''
Requirement:
There are 4 numbers: 1/2/3/4.
List out all 3 digits numbers using these 4 numbers.
You cannot use the same number twice in the 3 digits numbers.
'''

#Step 1) How to generate 1 digit number?
for i in range(1,5):
    print(i, end=' ')

print('\n-------------------------------------')

#Step 2) How to generate 2 digits number?
# Nested loop: for/while loop inside another for/while loop.
for i in range(1,5):
    for j in range(1, 5):
        num = i * 10 + j
        print(num, end=' ')

print('\n-------------------------------------')

#Step 3) How to generate 3 digits number?
# Nested loop: for/while loop inside another for/while loop, inside another for/while loop.
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            num = i * 100 + j * 10 + k
            print(num, end=' ')

print('\n-------------------------------------')

#Step 4) It has another condition - the 3 numbers should be different.

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                num = i * 100 + j * 10 + k
                print(num, end=' ')
