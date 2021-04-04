'''
None is a Python value
None means "Nothing here".
None means "We haven't put any value here yet".
'''


# Initialize a list with size 10, but there is nothing in it
list1 = [None] * 10
print(list1)

def func1():
    print("A function returns nothing")

var1 = func1()
print(var1)

if var1 == None:
    print("There is nothing inside variable var1")
else:
    print("There is something inside variable var1")