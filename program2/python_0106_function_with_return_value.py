# define a function
def square(x):
    '''
    This function will calculate the square number of the passed-in parameter x
    :param x:
    :return: the square number of x
    '''
    return x ** 2 # You use keyword 'return' to return x square back to the function caller

# call a function
result1 = square(1)
result2 = square(2)
print(result1, result2)

result = []
for i in range(101):
    result.append(square(i))
print(result)

# define a function
def volume_of_cuboid(long, width, height):
    return long * width * height

l = 5
w = 4
h = 3
print("long =", l, "width =", w, "height =", h, "volume =", volume_of_cuboid(l, w, h))

'''
Requirement:
This function returns the nth_root of number x.
For example:
print(nth_root(4,2)) # This should print the square root of 4, so it should print 2
print(nth_root(27,3)) # This should print the cube root of 27, so it should print 3
print(nth_root(625,4)) # This should print the 4th root of 625, so it should print 5
'''
def nth_root(x, n):
    return x ** (1/n)

print(nth_root(4, 2))
print(nth_root(27, 3))
print(nth_root(625, 4))