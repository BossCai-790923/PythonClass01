'''

IMPORTANCE!!! -------------------------------------------------
for loop / while loop can have an 'else' clause at the end.
---------------------------------------------------------------

if 'break' is triggered inside the loop body, then 'else' clause won't be triggered.
if 'break' is NOT triggered inside the loop body, then 'else' clause WILL be triggered.

'else' clause is your reward code to run, if you never break out of the loop.

'''

# example 1 - there is no break inside the for loop, so 'break' can not be triggered. (It doesn't even exist!)
# 'break' is not triggered -> 'else' clause will be triggered.

for i in range(5):
    print(i)
else:
    print("For loop finished all iterations, no break happens!")



# example 2 - 'break' will be triggered when i = 3
# 'break' is triggered -> 'else' clause will NOT be triggered.
for i in range(5):
    print(i)
    if i > 2:
        print('i is greater than 2 now!')
        break
else:
    print("For loop finished all iterations, no break happens!")