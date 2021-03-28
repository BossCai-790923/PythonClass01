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


def nth_root(x, n):
    pass

print(nth_root(4, 2))
print(nth_root(27, 3))
print(nth_root(625, 4))