'''
Requirement: Print all numbers smaller than 7, odd or even.
'''

# if / else inside while loop
a = 1
while a < 7:
    if a % 2 == 0:
        print(a, 'is even')
    else:
        print(a, 'is odd')
    a+=1