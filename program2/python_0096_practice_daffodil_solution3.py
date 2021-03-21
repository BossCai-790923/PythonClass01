'''
Logic:
If it is so difficult to find the unit / tens / hundreds number of the 3 digits number
Then we can use nested loop to find the answer
'''

for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            i = 100 * a + 10 * b + c
            if a ** 3 + b ** 3 + c ** 3 == i:
                print(i)