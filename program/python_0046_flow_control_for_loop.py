
# IMPORTANT!! -------------------------------------------
# This is how you define a for loop:
#
# 1) You are defining a variable i.
#
# 2) range() is a python built-in function.
#    range() allows you to generate a series of numbers within a given range.
#    range(5) generates number 0, 1, 2, 3, 4.
#
# 3) So the for loop will loop 5 times. In these 5 times, looping variable i equals 0, 1, 2, 3, 4.
#
# [range style 1]
# range(stop) generates number in range [0, stop)
# -------------------------------------------------------

print('range(5) generates number from 0 to 4, no 5!')
for i in range(5):
    print(i)

print("-------------------------------------------")

# IMPORTANT!! -------------------------------------------
# [range style 2]
# range(start, stop) generates number in range[start, stop)
# -------------------------------------------------------
print('range(5, 10) generates number from 5 to 9, no 10!')
for i in range(5, 10):
    print(i)


print("range(100, 100) doesn't generate any number. So it prints nothing.")
for i in range(100, 100):
    print(i)


print("-------------------------------------------")

# IMPORTANT!! -------------------------------------------
# [range style 3]
# range(start, stop, step) generates number in range[start, stop), with step
# -------------------------------------------------------

print("range(10,-10,-2) generates number 10,8,6,4,2,0,-2,-4,-6,-8")
for i in range(10, -10, -2):
    print(i)

print("-------------------------------------------")
